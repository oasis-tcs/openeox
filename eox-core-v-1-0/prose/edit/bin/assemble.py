#! /usr/bin/env python
"""Assemble prose sources along the html and pdf channels (html is default).

Select output format with -t (html is default):

  html -> build/tmp.md  + build/toc-mint.json  (input for pandoc -> toccata.py) - - > html delivery item
                +-> (is gfm-plus delivery item)
  pdf  -> build/pdf.md                         (input for liitos) - - > pdf delivery item

"""
import json
import pathlib
import re
import os
import sys
from typing import Union

import yaml

ENCODING = 'utf-8'
NL = '\n'
CB_END = '}'
COLON = ':'
DASH = '-'
DOT = '.'
FULL_STOP = '.'
HASH = '#'
PARA = '§'
SEMI = ';'
SPACE = ' '
TM = '™'

DEBUG = bool(os.getenv('ASSEMBLE_DEBUG', ''))
TARGETS = (
    TARGET_HTML := 'html',
    TARGET_PDF := 'pdf',
)

# Optionally dump look-up tables back to etc/ as a cross-check against sections.py output:
DUMP_LUT = bool(os.getenv('DUMP_LUT', ''))

# Paths:
SLUG_NOT = (' ', '.', ',', ';', '?', '!', '_', '(', ')', '[', ']', '{', '}', '<', '>', '\\', '/', '$', ':', '+')
BINDER_AT = pathlib.Path('etc') / 'bind.txt'
SOURCE_AT = pathlib.Path('src')
BUILD_AT = pathlib.Path('build')
CONFIG_AT = pathlib.Path('etc') / 'sections-config.yaml'
SECTION_DISPLAY_TO_LABEL_AT = pathlib.Path('etc') / 'section-display-to-label.json'
SECTION_LABEL_TO_DISPLAY_AT = pathlib.Path('etc') / 'section-label-to-display.json'
SECTION_DISPLAY_TO_TEXT_AT = pathlib.Path('etc') / 'section-display-to-text.json'
EG_GLOBAL_TO_LABEL_AT = pathlib.Path('etc') / 'example-global-to-local.json'
EG_LABEL_TO_GLOBAL_AT = pathlib.Path('etc') / 'example-local-to-global.json'

# Parsers:
IS_CITE_REF = 'cite'
CITE_REF_DETECT = re.compile(r'\[(?P<text>cite)\]\(#(?P<label>[^)]+)\)')
IS_EG_REF = 'eg'
EG_REF_DETECT = re.compile(r'\[(?P<text>eg)\]\(#(?P<label>[^)]+)\)')
IS_SEC_REF = 'sec'
SEC_REF_DETECT = re.compile(r'\[(?P<text>sec)\]\(#(?P<label>[^)]+)\)')
MD_REF_DETECT = re.compile(r'\[(?P<text>[^]]+)\]\(#(?P<target>[^)]+)\)')

# Code block label reference patterns (label values inside inline comments):
SEC_LABEL_BRACKET_CB_DETECT = re.compile(r'\ +#\ +[^(]+\((?P<label>\(#(?P<value>[0-9a-z-]+)\))\)\.')
SEC_LABEL_FREE_CB_DETECT = re.compile(r'\ +#\ +[^(]+(?P<label>\(#(?P<value>[0-9a-z-]+)\))\.')

SEC_OVER = '[sec]('
CIT_OVER = '[cite]('
CIT_TOO_DIRECT = '[cite](http'

HC_BEG = '<!--'
HC_END = '-->'
YAML_SEP = '---'
TOK_TOC = '(#$thing$)'
TOK_SEC = "<a id='$thing$'></a>"
TOK_LAB = '{#'
H = '#'
YAML_X_SEP = DASH * 7
TOC_HEADER = f"""{YAML_X_SEP}

# Table of Contents
"""

LOGO_URL = 'https://docs.oasis-open.org/templates/OASISLogo-v3.0.png'
LOGO_LOCAL_PATH = 'images/OASISLogo-v3.0.png'
TOP_LOGO_LINE = f'![OASIS Logo]({LOGO_URL})'

FENCED_BLOCK_FLIP_FLOP = '```'

SEC_NO_TOC_POSTFIX = '{.unnumbered .unlisted}'

# Matches top-level annex/appendix headings: "Annex A ...", "Appendix 1 ..."
ANNEX_TOP_PATTERN = re.compile(r'^(?P<prefix>(?:Annex [A-Z]|Appendix [0-9]+))(?:\s+(?P<rest>.+))?$')
# Matches inner annex sub-headings with explicit letter-number prefix: "A.1.", "B.2"
APPENDIX_INNER_PATTERN = re.compile(r'^(?P<display>[A-Z][.0-9]+\.?)\s+(?P<rest>.+)$')

SECTION_DISPLAY_TO_LABEL: dict[str, str] = {}
SEC_LABEL_TEXT: dict[str, str] = {}

TOC_TEMPLATE = {
    1: '$sec_cnt_disp$ [$text$](#$label$)  ',
    2: '\t$sec_cnt_disp$ [$text$](#$label$)  ',
    3: '\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
    4: '\t\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
    5: '\t\t\t\t$sec_cnt_disp$ [$text$](#$label$)  ',
}

TOK_EG = "<a id='$thing$'></a>"
TOC_VERTICAL_SPACER = ''

CITE_COSMETICS_TEMPLATE = '**\\[**<span id="$label$" class="anchor"></span>**$code$\\]** $text$'

# Type declarations:
META_TOC_TYPE = dict[str, dict[str, Union[bool, str, list[dict[str, str]]]]]

# Post-loop HTML heading remaps: strip legacy numeric prefixes added during the section counter pass.
# Keys are heading lines as they appear after section-counter processing.
APPENDIX_HEAD_REMAP_HTML: dict[str, dict[str, object]] = {
    '## Appendix 1 Leadership': {'replace': ['## Appendix 1 ', '## '], 'attrs': ''},
    '## 9.2 Special Thanks': {'replace': ['## 9.2 ', '## '], 'attrs': ''},
    '## 9.3 Participants': {'replace': ['## 9.3 ', '## '], 'attrs': ''},
    '# Changes From Previous Version': {'replace': ['# ', '# Appendix 2 '], 'attrs': ''},
    '## Appendix 2.1. Revision History': {'replace': ['## Appendix 2.1. ', '##  '], 'attrs': ''},
}

# Inline PDF heading remaps: applied during the heading scan.  Keys match heading lines as
# reconstructed from tag + text + link_attributes (before section-counter injection, which
# is omitted for PDF).  The transform adds pandoc {.unnumbered #label} attributes and
# LaTeX \newpage / \columns= commands where needed.
APPENDIX_HEAD_REMAP_PDF: dict[str, dict[str, object]] = {
    '# Annex A License, Document Status and Notices{#annex-a}{#annex-a}': {
        'replace': [
            '# Annex A License, Document Status and Notices{#annex-a}{#annex-a}',
            '# Annex A License, Document Status and Notices',
        ],
        'attrs': '{.unnumbered #annex-a}',
    },
    '## Document Status': {'replace': ['## ', '## A.1 '], 'attrs': '{.unnumbered #document-status}'},
    '## License and Notices': {'replace': ['## ', '## A.2 '], 'attrs': '{.unnumbered #license-and-notices}'},
    '# References': {'replace': ['# ', '\\newpage\n\n# Annex B '], 'attrs': '{.unnumbered #references}'},
    '## Normative References': {'replace': ['## ', '## B.1 '], 'attrs': '{.unnumbered #normative-references}'},
    '## Informative References': {'replace': ['## ', '## B.2 '], 'attrs': '{.unnumbered #informative-references}'},
    '# Acknowledgments': {'replace': ['# ', '\\newpage\n\n# Appendix 1 '], 'attrs': '{.unnumbered #acknowledgments}'},
    '## Leadership': {'replace': ['## . ', '## '], 'attrs': '{.unnumbered #leadership}'},
    '## Special Thanks': {'replace': ['## .. ', '## '], 'attrs': '{.unnumbered #special-thanks}'},
    '## Participants': {'replace': ['## ... ', '## '], 'attrs': '{.unnumbered #participants}'},
    '# Changes From Previous Version': {
        'replace': ['# ', '\\newpage\n\n# Appendix 2 '],
        'attrs': '{.unnumbered #changes-from-previous-version}',
    },
    '## Revision History': {
        'replace': ['## .... Revision History', '## Revision History'],
        'attrs': '{.unnumbered #revision-history}',
    },
}

# Data interface keys:
CHILDREN = 'children'
ENUMERATE = 'enumerate'
LABEL = 'label'
TOC = 'toc'


def highlight_in_context(text_lines: list[str], pos: int, span: int = 15) -> None:
    """Show error line in context to help authors find the root cause of a problem."""
    for n in range(max(0, pos - span), min(pos + span, len(text_lines))):
        if n != pos:
            print(f'        {n:4} | {text_lines[n].rstrip(NL)}')
        else:
            print(f'HERE>>> {n:4} | {text_lines[n].rstrip(NL)} <<<HERE')
    print(DASH * 69)


def load_binder(binder_at: Union[str, pathlib.Path], ignores: Union[list[str], None] = None) -> list[pathlib.Path]:
    """Load the linear binder text file into a list of file paths."""
    with open(binder_at, 'rt', encoding=ENCODING) as resource:
        collation = [pathlib.Path(entry.strip()) for entry in resource.readlines() if entry.strip()]
    return [path for path in collation if str(path) not in ignores] if ignores else collation


def end_of_toc_in(text: str, marker: str) -> bool:
    """Detect the end of the table of contents placeholder.

    marker is the clean-md-start value (e.g. '# Introduction').
    By the time this runs, headings have been numbered (e.g. '# 1 Introduction'),
    so we match by presence of the heading word as a substring, not by prefix.
    """
    marker_text = marker.lstrip('#').strip()
    return text.startswith(HASH) and f' {marker_text}' in text


def detect_meta(text_lines: list[str]) -> tuple[META_TOC_TYPE, list[str]]:
    """Extract YAML data from top of file, remove those lines, return (meta, remaining)."""
    meta_lines = []
    if text_lines[0].startswith(HC_BEG) and text_lines[1].startswith(YAML_SEP):
        for line in text_lines[2:]:
            if line.startswith(YAML_SEP):
                break
            meta_lines.append(line)

    from_here = len(meta_lines) + 4
    if from_here > 4:
        text_lines = text_lines[from_here:]

    return yaml.safe_load(''.join(meta_lines)) if meta_lines else {}, text_lines


def load_document(path: Union[str, pathlib.Path]) -> tuple[META_TOC_TYPE, list[str]]:
    """Load text file into list of strings, harvesting any YAML meta."""
    with open(path, 'rt', encoding=ENCODING) as resource:
        return detect_meta(resource.readlines())


def dump_assembly(text_lines: list[str], to_path: Union[str, pathlib.Path]) -> None:
    """Write lines of text to file at path."""
    with open(to_path, 'wt', encoding=ENCODING) as resource:
        resource.write(''.join(text_lines))


def label_derive_from(text: str) -> str:
    """Transform text to kebab-style label (no newlines assumed)."""
    slug = text.strip()
    for bad in SLUG_NOT:
        slug = slug.replace(bad, DASH)
    parts = slug.split(DASH)
    slug = DASH.join(s for s in parts if s and s != DASH)
    return slug.lower()


def label_in(text: str) -> bool:
    """Detect if the line contains a label reference."""
    return '](#' in text


def example_local_number(text: str) -> int:
    """Return local example number from *Example N: line, or 0."""
    ls_text = text.lstrip()
    if ls_text.startswith('*Example ') or ls_text.startswith('*Examples '):
        rest = ls_text.split(SPACE, 1)[1]
        de_colon = rest.split(COLON, 1)[0]
        number = de_colon.split(SPACE, 1)[0] if SPACE in de_colon else de_colon
        try:
            return int(number)
        except ValueError:
            pass
    return 0


def example_in(text: str) -> bool:
    """Detect if the line contains a magic example token."""
    return example_local_number(text) > 0


def code_block_label_in(text: str) -> bool:
    """Detect if the line contains a code block section label."""
    return '(#' in text and ' # ' in text


def load_config(path: Union[str, pathlib.Path] = CONFIG_AT) -> dict:  # type: ignore[type-arg]
    """Load per-spec sections configuration."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return yaml.safe_load(handle) or {}


def load_label_to_display_lut(path: Union[str, pathlib.Path] = SECTION_LABEL_TO_DISPLAY_AT) -> dict[str, str]:
    """Load section label → display LUT."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return json.load(handle)


def load_display_to_label_lut(path: Union[str, pathlib.Path] = SECTION_DISPLAY_TO_LABEL_AT) -> dict[str, str]:
    """Load section display → label LUT."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return json.load(handle)


def load_display_to_text_lut(path: Union[str, pathlib.Path] = SECTION_DISPLAY_TO_TEXT_AT) -> dict[str, str]:
    """Load section display → heading text LUT."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return json.load(handle)


def load_eg_label_to_global_lut(path: Union[str, pathlib.Path] = EG_LABEL_TO_GLOBAL_AT) -> dict[str, str]:
    """Load example label → global number LUT."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return json.load(handle)


def load_eg_global_to_label_lut(path: Union[str, pathlib.Path] = EG_GLOBAL_TO_LABEL_AT) -> dict[str, str]:
    """Load example global number → label LUT."""
    with pathlib.Path(path).open('rt', encoding=ENCODING) as handle:
        return json.load(handle)


def detect_leftovers(records: list[str], marker: str = 'Found') -> list[tuple[int, str]]:
    """Detect unresolved citation and section references."""
    ref_defects = [(n, r) for n, r in enumerate(records) if CIT_OVER in r or SEC_OVER in r]
    if ref_defects:
        print(f'{marker} {len(ref_defects)} citation or section reference defects:')
        for slot, record in ref_defects:
            print(f'- "{record.strip()}" (slot {slot})')
            if CIT_TOO_DIRECT in record:
                print('  ! citation references should use indirect targets (reference section entries) not URLs')
    return ref_defects


def insert_any_citation(record: str) -> str:
    """Expand [cite](#label) placeholder or return record unchanged."""
    if label_in(record):
        for ref in CITE_REF_DETECT.finditer(record):
            if ref:
                found = ref.groupdict()
                trigger_text = found['text']
                if trigger_text != IS_CITE_REF:
                    raise RuntimeError(f'false positive cite ref in ({record.rstrip(NL)})')
                label = found['label']
                text = label.replace(';', ':')
                sem_ref = f'[cite](#{label})'
                evil_ref = f'\\[[{text}](#{label})\\]'
                record = record.replace(sem_ref, evil_ref)
    return record


def insert_any_section_reference(
    record: str,
    label_to_display: dict[str, str],
    display_to_text: dict[str, str],
    sec_ref_style: str,
) -> str:
    """Expand [sec](#label) placeholder or return record unchanged.

    Rendering depends on sec-ref-style from sections-config.yaml:
      number              → [1.2.3](#label)
      number-title        → [1.2.3 Heading Text](#label)
      section-sign-number → [§1.2.3](#label)
    """
    if not label_in(record):
        return record
    for ref in SEC_REF_DETECT.finditer(record):
        if ref:
            found = ref.groupdict()
            trigger_text = found['text']
            if trigger_text != IS_SEC_REF:
                raise RuntimeError(f'false positive sec ref in ({record.rstrip(NL)})')
            label = found['label']
            if label not in label_to_display:
                print(f'ERROR: in insert-any-section-reference ({record=})')
                print(f'ERROR-CONTEXT: {label=}')
                for skey in label_to_display:
                    if skey.startswith(label[: len(label) // 2]):
                        print(f'DEBUG: - similar {skey=} exists')
                print(f'DEBUG: You may want to execute grep -n {label} src/*.md')
                raise RuntimeError(f'missing register label for sec ref in ({record.rstrip(NL)})')
            display = label_to_display[label]
            sem_ref = f'[sec](#{label})'
            if sec_ref_style == 'number-title':
                heading_text = display_to_text.get(display, '')
                link_text = f'{display} {heading_text}'.strip()
            elif sec_ref_style == 'section-sign-number':
                link_text = f'{PARA}{display}'
            else:  # 'number' is the default
                link_text = display
            evil_ref = f'[{link_text}](#{label})'
            record = record.replace(sem_ref, evil_ref)
    return record


def main(argv: list[str]) -> int:
    """Drive the assembly."""
    debug = DEBUG
    bind_seq_path = BINDER_AT
    target = TARGET_HTML
    args = list(argv)
    for slot, arg in enumerate(args):
        if arg.lower() in ('-h', '--help', '/h', '-?'):
            print('USAGE: bin/assemble.py [-d|--debug] [-b path|--binder path] [-t format|--target format]')
            print(f'       known targets: [{", ".join(TARGETS)}], default: {TARGET_HTML}')
            return 0
    for slot, arg in enumerate(args):
        if arg in ('-d', '--debug'):
            debug = True
            del args[slot]
            break
    for slot, arg in enumerate(args):
        if arg in ('-b', '--binder'):
            bind_seq_path = pathlib.Path(args[slot + 1])
            del args[slot + 1]
            del args[slot]
            break
    for slot, arg in enumerate(args):
        if arg in ('-t', '--target'):
            target = args[slot + 1].lower()
            del args[slot + 1]
            del args[slot]
            if target not in TARGETS:
                print(f'ERROR: unknown {target=} (not in [{", ".join(TARGETS)}])')
                return 2
            break
    if args:
        print(f'WARNING: Unprocessed {args=}')

    # PDF path skips frontmatter.md — liitos provides its own title page via etc/liitos/ templates.
    binder_ignores = ['frontmatter.md'] if target == TARGET_PDF else None
    binder = load_binder(bind_seq_path, binder_ignores)
    for resource in binder:
        if not (SOURCE_AT / resource).is_file():
            print(f'Problem reading {resource}')
            return 1

    config = load_config()
    sec_ref_style: str = str(config.get('sec-ref-style', 'number'))
    clean_md_start: str = str(config.get('clean-md-start', '# Scope'))
    track_examples: bool = bool(config.get('track-examples', False))
    citation_sources: tuple[str, ...] = tuple(config.get('citation-sources', []))
    glossary_sources: tuple[str, ...] = tuple(config.get('glossary-sources', []))
    citation_skip_prefixes: tuple[str, ...] = tuple(config.get('citation-skip-prefixes', ['#']))

    display_from = load_label_to_display_lut()
    display_to_text = load_display_to_text_lut()
    eg_global_from = load_eg_label_to_global_lut() if track_examples else {}

    # Assemble source files into flat line list, expanding citations and glossary.
    lines: list[str] = []
    meta_hooks: dict[int, META_TOC_TYPE] = {}
    first_meta_slot = None
    for resource in binder:
        meta, part_lines = load_document(SOURCE_AT / resource)
        if part_lines[-1] != NL:
            part_lines.append(NL)
        if meta:
            meta_hooks[len(lines)] = meta
            meta_hooks[len(lines) + len(part_lines) - 1] = {}
            if first_meta_slot is None:
                first_meta_slot = len(lines) + len(part_lines) - 1

        if resource.name in citation_sources:  # TODO: citation management → class
            patched = []
            in_citation = False
            for line in part_lines:
                if line.startswith(citation_skip_prefixes):
                    patched.append(line)
                    continue
                if line.strip() and not line.startswith(COLON):
                    in_citation = True
                    code = line.strip()
                    label = code.replace(COLON, SEMI).rstrip(TM)
                    text = ''
                    continue
                if in_citation:
                    if line.startswith(COLON):
                        text += line.lstrip(COLON).strip()
                        continue
                    if line.strip():
                        text += SPACE + line.strip()
                        continue
                    if not line.strip():
                        citation = (
                            CITE_COSMETICS_TEMPLATE.replace('$label$', label)
                            .replace('$code$', code)
                            .replace('$text$', text)
                            + NL
                        )
                        in_citation = False
                        patched.append(citation)
                        patched.append(line)
                        continue
                else:
                    patched.append(line)
            part_lines = list(patched)

        # Glossary <dl> expansion: HTML needs raw HTML for rendering; PDF uses LaTeX definition lists.
        if target == TARGET_HTML and resource.name in glossary_sources:  # TODO: glossary management → class
            patched = ['<dl>' + NL]
            in_definition = False
            for line in part_lines:
                if not in_definition and line.strip() and not line.startswith(COLON):
                    in_definition = True
                    term = line.strip()
                    label = 'def;' + label_derive_from(term)
                    definition = ''
                    continue
                if in_definition:
                    if line.startswith(COLON):
                        definition += line.lstrip(COLON).strip()
                        definition = (
                            definition.replace('_Examples_', '<em>Examples</em>')
                            .replace('_Example_', '<em>Example</em>')
                            .replace('**Notes**', '<strong>Notes</strong>')
                            .replace('**Note**', '<strong>Note</strong>')
                        )
                        continue
                    if line.strip():
                        definition += NL + ' ' * 6 + line.strip()
                        definition = (
                            definition.replace('_Examples_', '<em>Examples</em>')
                            .replace('_Example_', '<em>Example</em>')
                            .replace('**Notes**', '<strong>Notes</strong>')
                            .replace('**Note**', '<strong>Note</strong>')
                        )
                        continue
                    if not line.strip():
                        for ref in MD_REF_DETECT.finditer(definition):
                            if ref:
                                found = ref.groupdict()
                                ref_text = found['text']
                                ref_anchor = found['target']
                                md_ref = f'[{ref_text}](#{ref_anchor})'
                                html_ref = f'<a href="#{ref_anchor}">{ref_text}</a>'
                                definition = definition.replace(md_ref, html_ref)
                        item = f'{" " * 2}<dt id="{label}">{term}</dt>\n{" " * 2}<dd>{definition}</dd>\n'
                        in_definition = False
                        patched.append(item)
                        continue
                else:
                    patched.append(line)
            patched.append('</dl>' + NL + NL)
            part_lines = list(patched)

        lines.extend(part_lines)

    # Heading scan: build TOC, track section context per line, rewrite heading lines.
    print(f'INFO: Manage section counters and build the table of contents (for {len(lines)} text records)')
    lvl_min, lvl_sup = 1, 7
    sec_cnt = {f'{H * level} ': 0 for level in range(lvl_min, lvl_sup)}
    sec_lvl = {f'{H * level} ': level for level in range(lvl_min, lvl_sup)}
    lvl_sec = {level: f'{H * level} ' for level in range(lvl_min, lvl_sup)}
    H1 = f'{H} '
    cur_lvl = sec_lvl[H1]
    meta_hook: META_TOC_TYPE = {}
    tic_toc = [TOC_HEADER]
    mint = []
    did_appendix_sep = False
    is_appendix = False
    clean_headings = False
    in_fenced_block = False
    current_cs = None
    cs_of_slot: list[Union[str, None]] = [None for _ in lines]

    for slot, line in enumerate(lines):
        # HTML: drop standalone \newpage commands — they are PDF/LaTeX pass-through only.
        # A standalone \newpage is a line whose stripped content is exactly '\newpage'.
        if target == TARGET_HTML and line.rstrip() == r'\newpage':
            lines[slot] = NL
            line = NL

        # PDF: replace remote logo URL with local copy for offline rendering
        if target == TARGET_PDF and line.rstrip() == TOP_LOGO_LINE:
            lines[slot] = line.replace(LOGO_URL, LOGO_LOCAL_PATH, 1)
            line = lines[slot]

        if line.startswith(FENCED_BLOCK_FLIP_FLOP):
            in_fenced_block = not in_fenced_block

        if meta_hooks.get(slot) is not None:
            meta_hook = meta_hooks[slot]
        if line.startswith(clean_md_start):
            clean_headings = True
        cs_of_slot[slot] = current_cs

        for tag in sec_cnt:
            if line.startswith(tag) and clean_headings and not in_fenced_block:
                nxt_lvl = sec_lvl[tag]  # set for all branches; needed for cur_lvl update
                app_lvl = 1  # default; overridden in meta_hook branch
                annex_top = None  # set in auto-counter branch if heading has Annex/Appendix prefix
                annex_inner = None  # set in auto-counter branch if heading has letter-number prefix
                if not meta_hook:
                    is_plain = True
                    # Peek at the text to decide counter strategy.
                    text_peek = line.split(tag, 1)[1].rstrip()
                    if TOK_LAB in text_peek:
                        text_peek = text_peek.split(TOK_LAB, 1)[0].rstrip(SPACE)
                    annex_top = ANNEX_TOP_PATTERN.match(text_peek)
                    annex_inner = APPENDIX_INNER_PATTERN.match(text_peek) if is_appendix else None
                    if annex_top:
                        # Top-level annex/appendix: display comes from the heading itself.
                        sec_cnt_disp = annex_top.group('prefix')
                        is_appendix = True
                    elif annex_inner:
                        # Inner heading with explicit letter-number prefix (e.g. "A.1.", "B.2").
                        sec_cnt_disp = annex_inner.group('display')
                        if not sec_cnt_disp.endswith(FULL_STOP):
                            sec_cnt_disp += FULL_STOP
                    elif is_appendix:
                        # Unnumbered sub-heading inside an appendix (e.g. "Leadership").
                        sec_cnt_disp = ''
                    else:
                        # Normal numeric auto-counter.
                        sec_cnt[tag] += 1
                        if nxt_lvl < cur_lvl:
                            for level in range(nxt_lvl + 1, lvl_sup):
                                sec_cnt[lvl_sec[level]] = 0
                        sec_cnt_disp_vec = []
                        for s_tag, cnt in sec_cnt.items():
                            if cnt == 0:
                                print(f'ERROR: counting is hard: {sec_cnt} at {tag} for {slot}:{line.rstrip(NL)}')
                                highlight_in_context(lines, slot)
                                return 1
                            sec_cnt_disp_vec.append(str(cnt))
                            if s_tag == tag:
                                break
                        sec_cnt_disp = FULL_STOP.join(sec_cnt_disp_vec)
                        if FULL_STOP not in sec_cnt_disp:
                            sec_cnt_disp += FULL_STOP
                else:
                    # pull in counters from meta (legacy YAML frontmatter appendix handling)
                    is_plain = False
                    text_tmp = line.split(tag, 1)[1].rstrip()
                    if TOK_LAB in text_tmp:
                        text_tmp = text_tmp.split(TOK_LAB, 1)[0]
                    if text_tmp == meta_hook[TOC][LABEL]:
                        sec_cnt_disp = meta_hook[TOC][ENUMERATE]  # type: ignore[assignment]
                        app_lvl = 1
                    elif meta_hook[TOC].get(CHILDREN):
                        for cand in meta_hook[TOC][CHILDREN]:  # type: ignore[union-attr]
                            if text_tmp == cand[LABEL]:
                                sec_cnt_disp = cand[ENUMERATE]  # type: ignore[assignment]
                                app_lvl = 2

                # manage label
                text = line.split(tag, 1)[1].rstrip()

                # PDF: capture any {#label} / {.class} attributes already present on the heading
                link_attributes = ''
                if target == TARGET_PDF and '{' in line:
                    link_attributes = '{' + line.split('{', 1)[1]

                if TOK_LAB in text:
                    label = text.split(TOK_LAB, 1)[1].rstrip(CB_END)
                    if target == TARGET_HTML:
                        # strip {#label} from visible text for HTML
                        text = text.split(TOK_LAB, 1)[0].rstrip(SPACE)
                else:
                    label = label_derive_from(text)

                # HTML only: strip the annex/appendix display prefix from the visible heading text
                # so that the sec_cnt_disp injection produces e.g. "# Annex A Foo" not "# Annex A Annex A Foo".
                # PDF keeps the full heading text: liitos/LaTeX must see it as-is, and
                # APPENDIX_HEAD_REMAP_PDF handles any structural transformation needed there.
                had_explicit_label = TOK_LAB in line.split(tag, 1)[1]
                if target == TARGET_HTML:
                    if annex_top and annex_top.group('rest'):
                        rest = annex_top.group('rest')
                        if TOK_LAB in rest:
                            rest = rest.split(TOK_LAB, 1)[0].rstrip(SPACE)
                        text = rest
                        if not had_explicit_label:
                            label = label_derive_from(text)
                    elif annex_inner:
                        text = annex_inner.group('rest')
                        if not had_explicit_label:
                            label = label_derive_from(text)

                clean_sec_cnt_disp = (f'{sec_cnt_disp}' if is_plain else sec_cnt_disp).rstrip(FULL_STOP)
                SEC_LABEL_TEXT[label] = clean_sec_cnt_disp
                SECTION_DISPLAY_TO_LABEL[clean_sec_cnt_disp] = label

                # Build heading line per target:
                # HTML: inject <a id> anchor + section number prefix on every heading.
                # PDF:  preserve existing {#label} attributes; apply APPENDIX_HEAD_REMAP inline;
                #       section numbers are NOT injected (LaTeX auto-numbers them).
                if target == TARGET_HTML:
                    line = tag + text + ' ' + TOK_SEC.replace('$thing$', label)
                    if sec_cnt_disp:
                        line = line.replace(tag, f'{tag}{sec_cnt_disp} ', 1) + NL
                    else:
                        line = line + NL
                else:  # TARGET_PDF
                    line = tag + text + link_attributes
                    terse_line = line.rstrip()
                    if terse_line in APPENDIX_HEAD_REMAP_PDF:
                        transform = APPENDIX_HEAD_REMAP_PDF[terse_line]
                        this, that = transform['replace']  # type: ignore[misc]
                        attributes = transform['attrs']
                        if 'history' in terse_line.lower():
                            attributes += NL + NL + r'\columns=27%,10%,,32%' + NL + NL
                        line = terse_line.replace(this, that) + attributes + NL  # type: ignore[operator]
                        debug and print(f'DEBUG: ... ({terse_line}) -- ({transform}) --> ({line.rstrip(NL)}) ...')
                    elif annex_top or annex_inner:
                        # Annex/appendix heading not covered by APPENDIX_HEAD_REMAP_PDF:
                        # add {.unnumbered} so LaTeX does not auto-number it.
                        # \newpage comes from the source file; no injection needed here.
                        line = terse_line + f'{{.unnumbered #{label}}}' + NL
                        debug and print(f'DEBUG: annex fallback ({terse_line}) --> ({line.rstrip(NL)})')

                lines[slot] = line
                cur_lvl = nxt_lvl

                if not did_appendix_sep and meta_hook and slot < first_meta_slot:  # type: ignore[operator]
                    tic_toc.append(TOC_VERTICAL_SPACER)
                    did_appendix_sep = True

                # TOC entry
                extended = 0
                if sec_cnt_disp.upper().isupper():
                    extended = 2 if set(sec_cnt_disp).intersection('0123456789') else 1
                    if extended == 2:
                        extended = sec_cnt_disp.count(DOT) + 1
                if label in (
                    'document-status',
                    'license-and-notices',
                    'leadership',
                    'special-thanks',
                    'participants',
                    'revision-history',
                ):
                    extended = 2
                toc_text = text
                if '{#' in toc_text and label in toc_text:
                    debug and print(f'{slot=}: Fixed ToC for {toc_text=}')
                    toc_text = toc_text.replace('{#' + label + '}', '')
                toc_template = TOC_TEMPLATE[cur_lvl if not meta_hook else app_lvl]
                tic_toc.append(
                    toc_template.replace('$sec_cnt_disp$', sec_cnt_disp)
                    .replace('$text$', toc_text)
                    .replace('$label$', label)
                )

                # PDF: deduplicate {#label}{#label} (caused by link_attributes doubling)
                if target == TARGET_PDF and line.startswith('#') and '{#' in line:
                    hack = '{#' + label + '}'
                    hackhack = f'{hack}{hack}'
                    if hackhack in line:
                        line = line.replace(hackhack, hack)
                        debug and print(f'{slot=}: Fixed {line=} in collector')
                        lines[slot] = line

                mint.append([list(sec_cnt.values()), extended, sec_cnt_disp, toc_text, label])
                current_cs = label
                cs_of_slot[slot] = current_cs  # type: ignore[index]

            # SEC_NO_TOC_POSTFIX: PDF only, pre-introduction headings.
            # Only meaningful for PDF/LaTeX; HTML TOC is built by toccata.py independently.
            if line.startswith(tag) and not clean_headings and target == TARGET_PDF:
                lines[slot] = line.rstrip() + SEC_NO_TOC_POSTFIX + NL

    # HTML only: post-loop heading remap to strip legacy numeric prefixes
    if target == TARGET_HTML:
        print(f'WARN: Post-process the text display of section labels (for {len(lines)} text records)')
        for slot, line in enumerate(lines):
            terse_line = line.rstrip()
            if terse_line.startswith(tuple(APPENDIX_HEAD_REMAP_HTML.keys())):
                for cand in APPENDIX_HEAD_REMAP_HTML:
                    if terse_line.startswith(cand):
                        transform = APPENDIX_HEAD_REMAP_HTML[cand]
                        this, that = transform['replace']  # type: ignore[misc]
                        attributes = transform['attrs']
                        line = terse_line.replace(this, that) + attributes + NL  # type: ignore[operator]
                        debug and print(f'DEBUG: ... ({terse_line}) -- ({transform}) --> ({line.rstrip(NL)}) ...')
                        lines[slot] = line
                        break

    # Process citation refs
    print(f'INFO: Process the text display of citation references (for {len(lines)} text records)')
    for slot, line in enumerate(lines):
        completed = insert_any_citation(line)
        if line != completed:
            lines[slot] = completed

    # Process example refs
    print(f'INFO: Process the text display of example references (for {len(lines)} text records)')
    for slot, line in enumerate(lines):
        if example_in(line):
            num = example_local_number(line)
            section = cs_of_slot[slot]
            magic_label = f'{section}-eg-{num}'
            pl_anchor = TOK_EG.replace('$thing$', magic_label)
            line = line.rstrip(NL) + pl_anchor + NL
            if not section or section not in display_from:
                print(f'ERROR: lines[{slot}]({line.rstrip(NL)}) has no registered section({section}) for example({num})')
                highlight_in_context(lines, slot)
                return 1
            sec_disp = 'sec-' + display_from[section].replace(FULL_STOP, '-')  # type: ignore[union-attr]
            sec_disp_num_label = f'{sec_disp}-eg-{num}'
            sec_disp_num_anchor = TOK_EG.replace('$thing$', sec_disp_num_label)
            line = line.rstrip(NL) + sec_disp_num_anchor + NL
            try:
                global_example_num = eg_global_from[magic_label]
            except KeyError as err:
                print(f'ERROR: {slot=} in example-refs-global-counter-lookup ({err})')
                print(f'ERROR-CONTEXT: {slot=} - {line=}')
                print(f'ERROR-CONTEXT: {slot=} - {magic_label=}')
                for ekey in eg_global_from:
                    if ekey.startswith(magic_label[: len(magic_label) // 2]):
                        print(f'DEBUG: - similar {ekey=} exists')
                return 1
            global_example_num_label = f'example-{global_example_num}'
            global_example_num_anchor = TOK_EG.replace('$thing$', global_example_num_label)
            line = line.rstrip(NL) + global_example_num_anchor + NL
            lines[slot] = line

        if label_in(line):
            for ref in EG_REF_DETECT.finditer(line):
                if ref:
                    found = ref.groupdict()
                    trigger_text = found['text']
                    if trigger_text != IS_EG_REF:
                        raise RuntimeError(f'false positive example ref in ({line.rstrip(NL)})')
                    label = found['label']
                    sem_ref = f'[eg](#{label})'
                    if '-eg-' not in label:
                        raise RuntimeError(f'bad label for example in ({line.rstrip(NL)})')
                    section, number = label.split('-eg-', 1)
                    if section == cs_of_slot[slot]:
                        debug and print(f'detected local reference for {label} in ({line.rstrip(NL)})')
                        evil_ref = f'\\[[{number}](#{label})\\]'
                    else:
                        debug and print(f'detected remote reference for {label} in ({line.rstrip(NL)})')
                        sec_disp = display_from[section]
                        evil_ref = f'\\[[{number} (of section {sec_disp})](#{label})\\]'
                    line = line.replace(sem_ref, evil_ref)
                    debug and print(line.rstrip(NL))
                    lines[slot] = line

    # Process section refs
    print(f'INFO: Process the text display of section references (for {len(lines)} text records)')
    for slot, line in enumerate(lines):
        completed = insert_any_section_reference(line, display_from, display_to_text, sec_ref_style)
        if line != completed:
            lines[slot] = completed

    # Process code block label references
    print(f'INFO: Process the code blocks for references to map from label to display value (for {len(lines)} text records)')
    for slot, line in enumerate(lines):
        if code_block_label_in(line):
            for ref in SEC_LABEL_BRACKET_CB_DETECT.finditer(line):
                if ref:
                    found = ref.groupdict()
                    value = found['value']
                    if not value or value not in display_from:
                        continue
                    label = found['label']
                    display = display_from[value]
                    line = line.replace(label, display)
                    lines[slot] = line
            for ref in SEC_LABEL_FREE_CB_DETECT.finditer(line):
                if ref:
                    found = ref.groupdict()
                    value = found['value']
                    if not value or value not in display_from:
                        continue
                    label = found['label']
                    display = display_from[value]
                    line = line.replace(label, display)
                    lines[slot] = line

    # HTML only: inject table of contents before the Scope heading
    if target == TARGET_HTML:
        tic_toc.append(YAML_X_SEP)
        tic_toc.append(NL)
        print(f'INFO: Inject the table of contents (for {len(lines)} text records)')
        for slot, line in enumerate(lines):
            if end_of_toc_in(line, clean_md_start):
                lines[slot] = NL.join(tic_toc) + line
                print(f'INFO: Inserted ToC in slot({slot}) before the text({line.rstrip(NL)})')
                break

    # Remove trailing blank lines
    print(f'INFO: Remove any trailing blank line (for {len(lines)} text records)')
    while lines[-1] == NL:
        del lines[-1]

    # Detect and attempt to fix leftover unresolved references
    print(f'INFO: Detect left over citation and section references (for {len(lines)} text records)')
    ref_defects = detect_leftovers(lines, marker='Found')
    if ref_defects:
        print(f'+ processing {len(ref_defects)} text lines for citation or section reference insertions ...')
        rem_defects = []
        for slot, record in ref_defects:
            completed = insert_any_citation(record)
            if record != completed:
                lines[slot] = completed
            else:
                rem_defects.append((slot, record))
        for slot, record in rem_defects:
            completed = insert_any_section_reference(record, display_from, display_to_text, sec_ref_style)
            if record != completed:
                lines[slot] = completed
        ref_defects = detect_leftovers(lines, marker='Still found')
        if ref_defects:
            pass  # return 1
    else:
        print(f'INFO: No reference defects identified (Good)')

    print(f'INFO: Dump the assembly (for {len(lines)} text records)')
    BUILD_AT.mkdir(parents=True, exist_ok=True)
    if target == TARGET_HTML:
        dump_assembly(lines, BUILD_AT / 'tmp.md')
        print(f'INFO: Dump the minted table of contents database (of {len(mint)} entries)')
        with open(BUILD_AT / 'toc-mint.json', 'wt', encoding=ENCODING) as handle:
            json.dump(mint, handle, indent=2)
    else:  # TARGET_PDF
        dump_assembly(lines, BUILD_AT / 'pdf.md')
        # toc-mint.json not written: liitos/LaTeX handles the TOC natively

    if DUMP_LUT:
        with SECTION_DISPLAY_TO_LABEL_AT.open('wt', encoding=ENCODING) as handle:
            json.dump(SECTION_DISPLAY_TO_LABEL, handle, indent=2)
        section_label_to_display = dict(sorted((label, disp) for disp, label in SECTION_DISPLAY_TO_LABEL.items()))
        with SECTION_LABEL_TO_DISPLAY_AT.open('wt', encoding=ENCODING) as handle:
            json.dump(section_label_to_display, handle, indent=2)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
