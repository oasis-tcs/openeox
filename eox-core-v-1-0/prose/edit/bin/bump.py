#! /usr/bin/env python
"""Given a target date, bump the version in all relevant places for the next editor revision."""
import calendar as cal
import datetime as dti
import difflib
import json
import locale
import pathlib
import os
import sys

# Types
Job = dict[str, bool | str | int]
Messages = list[str]

# General constants
ENCODING = 'utf-8'
ENC_ERRS = 'ignore'
NL = '\n'
CB_END = '}'
COLON = ':'
COMMA = ','
DASH = '-'
DOT = '.'
FULL_STOP = '.'
HASH = '#'
PARA = '§'
SEMI = ';'
SPACE = ' '
CSEP = COMMA + SPACE
TM = '™'
LANG_CODE = 'en_US'

# Generate tuple with English month names in title case
locale.setlocale(locale.LC_ALL, LANG_CODE)
MONTHS_EN = tuple(name for name in cal.month_name[1:])

# Harden the key based job user data interface
COMMIT = 'commit'
DEBUG = 'debug'
DATE_SPEC = 'date-spec'

# Harden the key based job derived data interface
PUB_DAY_STR = 'pub-day-str'
PUB_MONTH_NAME_EN = 'pub-month-name-en'
PUB_YEAR_STR = 'pub-year-str'

PUB_DAY_INT = 'pub-day-int'
PUB_MONTH_STR = 'pub-month-en-str'
PUB_MONTH_INT = 'pub-month-int'
PUB_YEAR_INT = 'pub-year-int'

PUB_DATE = 'pub-date'
PUB_ISO_COMPACT = 'pub-iso-compact'
PUB_ISO_DASH = 'pub-iso-dash'

# Nicer usage info
here = pathlib.Path().absolute()
tool = pathlib.Path(__file__)
path = tool.relative_to(here)
USAGE = f'usage: {path} [--{COMMIT}] [--{DEBUG}] "DD Month YYYY"'


def parse_date(job: Job, month_names: tuple[str, ...] = MONTHS_EN) -> tuple[int, Job, Messages]:
    """Parse (and validate) the given date-spec in the job into a multi format structure.

    Note: Expected is format DD B YYYY, where B is the format-code for a title cased
          English month name like January.
    """
    messages: Messages = []
    try:
        day_str, month_name_en, year_str = job[DATE_SPEC].split(SPACE)
        job[PUB_DAY_STR] = day_str
        month_name_en = month_name_en.title()
        job[PUB_MONTH_NAME_EN] = month_name_en
        job[PUB_YEAR_STR] = year_str
    except ValueError:
        messages.append(f'ERROR: Parsing date value ({job[DATE_SPEC]})')
        return 2, messages
    except IndexError:
        messages.append(f'ERROR: Not enough arguments for date-spec in ({job[DATE_SPEC]})')
        return 2, messages

    if len(job[PUB_DAY_STR]) != 2:
        print('ERROR: Day part must be two-digits (zero-padded)')
        return 2, messages

    try:
        job[PUB_DAY_INT] = int(job[PUB_DAY_STR])
        if not 1 <= job[PUB_DAY_INT] <= 31:
            raise ValueError
    except ValueError:
        print('ERROR: Day part must be an integral number in [1, 31]')
        return 2, messages

    if job[PUB_MONTH_NAME_EN] not in MONTHS_EN:
        print(f'ERROR: English month part must be in ({CSEP.join(MONTHS_EN)})')
        return 2, messages

    job[PUB_MONTH_STR] = '00'
    for number, name in enumerate(MONTHS_EN, start=1):
        if month_name_en == name:
            job[PUB_MONTH_STR] = f'{number :02d}'

    if job[PUB_MONTH_STR] == '00':
        print('ERROR: English month part to %m mapping failed')
        return 1, messages

    if len(year_str) != 4:
        print('ERROR: Year part must be four-digits')
        return 2, messages

    now = dti.datetime.now(dti.UTC)
    this_year = now.year
    try:
        job[PUB_YEAR_INT] = int(job[PUB_YEAR_STR])
        if job[PUB_YEAR_INT] < this_year - 1:
            raise ValueError
    except ValueError:
        print(f'ERROR: Year part must be an integral number >= {this_year - 1}')
        return 2, messages

    try:
        job[PUB_MONTH_INT] = int(job[PUB_MONTH_STR])
        if not 1 <= job[PUB_MONTH_INT] <= 12:
            raise ValueError
    except ValueError:
        print('ERROR: Month part must map to an integral number in [1, 12]')
        return 1, messages

    _, max_days_of_month = cal.monthrange(job[PUB_YEAR_INT], job[PUB_MONTH_INT])
    if job[PUB_DAY_INT] > max_days_of_month:
        print(f'ERROR: Day part must be inside days of month [1, {max_days_of_month}]')
        return 2, messages

    job[PUB_DATE] = f'{job[PUB_DAY_STR]}{SPACE}{job[PUB_MONTH_NAME_EN]}{SPACE}{job[PUB_YEAR_STR]}'
    job[PUB_ISO_DASH] = f'{job[PUB_YEAR_STR]}{DASH}{job[PUB_MONTH_STR]}{DASH}{job[PUB_DAY_STR]}'
    job[PUB_ISO_COMPACT] = job[PUB_ISO_DASH].replace(DASH, '')

    return 0, messages


def parse_args(args: list[str]) -> tuple[int, Job, Messages]:
    """Parse the given arguments returning an error code, the expected job structure, and messages."""
    job: Job = {}
    messages: Messages = []
    if not args:
        return 0, job, messages

    job[DEBUG] = bool(os.getenv('BUMP_DEBUG', ''))
    for slot, arg in enumerate(args):
        if arg.lower() == f'--{DEBUG}':
            job[DEBUG] = True
            del args[slot]

    job[COMMIT] = False
    for slot, arg in enumerate(args):
        if arg.lower() == f'--{COMMIT}':
            job[COMMIT] = True
            del args[slot]

    job[DATE_SPEC] = ''
    try:
        slot = 0
        job[DATE_SPEC] = args[slot].strip(SPACE)
        del args[slot]
    except IndexError:
        messages.append('ERROR: Not enough arguments')
        return 2, job, messages

    if args:
        messages.append('ERROR: Too many arguments')
        return 2, job, messages

    return 0, job, messages


def main(args: list[str]) -> int:
    """Drive the transform to bump the dates based on the given argument."""
    err, job, messages = parse_args(args)

    if not err and not job:
        print(USAGE)
        return 0

    if err:
        print(USAGE)
        for message in messages:
            print(message)
        return 2

    err, messages = parse_date(job)

    if err:
        print(USAGE)
        for message in messages:
            print(message)
        return 2

    commit = job[COMMIT]
    debug = job[DEBUG]
    if debug:
        print('DEBUG: The job was parsed as follows:')
        print(json.dumps(job, indent=2))

    if not commit:
        print('INFO: Dry-run only - only diffs are shown and no files changed.')
        print()
    else:
        print('INFO: Commit mode - the magical five files will be bumped.')
        print()

    # Configuration and runtime parameter candidates:
    PDF_BOOKMATTER_IN = pathlib.Path('etc/liitos/bookmatter.tex.in')
    PDF_META_YAML = pathlib.Path('etc/liitos/meta.yml')
    PDF_SETUP_IN = pathlib.Path('etc/liitos/setup.tex.in')
    SRC_FRONTMATTER = pathlib.Path('src/frontmatter.md')
    SRC_HISTORY = pathlib.Path('src/revision-history.md')

    any_changes = False

    with open(PDF_BOOKMATTER_IN, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        lines = [line.rstrip(NL) for line in source.readlines()]

    bumped = []
    debug and print('#  -  -  -  -  -  -  -  -  - ')
    for line in lines:
        prefix = r'\subsection*{'
        postfix = r'}\label{pub-date}'
        # \subsection*{21 January 2026}\label{pub-date}
        if line.startswith(prefix) and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_DATE] + postfix)
            debug and print(f'DEBUG: Bumped to ({job[PUB_DATE]})')
            continue

        prefix = 'Hagen, and Thomas Schmidt. '
        postfix = '. OASIS Committee Specification'
        # Hagen, and Thomas Schmidt. 21 January 2026. OASIS Committee Specification
        if line.startswith(prefix) and line.endswith('. OASIS Committee Specification'):
            pub_date = line.replace(prefix, '').replace('. OASIS Committee Specification', '')
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_DATE] + '. OASIS Committee Specification')
            debug and print(f'DEBUG: Bumped to ({job[PUB_DATE]})')
            continue

        bumped.append(line)

    if lines != bumped:
        if not any_changes:
            any_changes = True
        print(f'# - - - 8< - -(( {PDF_BOOKMATTER_IN} )) - - - - - - - - - - - - - - >')
        print()
        sys.stdout.writelines(difflib.unified_diff(
            tuple(line + NL for line in lines),
            tuple(line + NL for line in bumped),
            fromfile='bookmatter.tex.in',
            tofile='bookmatter-bumped.tex.in',
        ))
        if commit:
            with open(PDF_BOOKMATTER_IN, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
                target.write(NL.join(bumped) + NL)
    else:
        print(f'INFO: No changes to {PDF_BOOKMATTER_IN}')

    with open(PDF_META_YAML, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        lines = [line.rstrip(NL) for line in source.readlines()]

    bumped = []
    debug and print('#  -  -  -  -  -  -  -  -  - ')
    for line in lines:
        #     footer_outer_field_normal_pages: 21 January 2026 - \theMetaPageNumPrefix { } \thepage { } of \pageref{LastPage}
        prefix = '    footer_outer_field_normal_pages: '
        postfix = r' - \theMetaPageNumPrefix { } \thepage { } of \pageref{LastPage}'
        if line.startswith(prefix) and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_DATE] + postfix)
            debug and print(f'DEBUG: Bumped to ({job[PUB_DATE]})')
            continue

        bumped.append(line)

    if lines != bumped:
        if not any_changes:
            any_changes = True
        print()
        print(f'# - - - 8< - -(( {PDF_META_YAML} )) - - - - - - - - - - - - - - - - - - >')
        print()
        sys.stdout.writelines(difflib.unified_diff(
            tuple(line + NL for line in lines),
            tuple(line + NL for line in bumped),
            fromfile='meta.yml',
            tofile='meta-bumped.yml',
        ))
        if commit:
            with open(PDF_META_YAML, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
                target.write(NL.join(bumped) + NL)
    else:
        print(f'INFO: No changes to {PDF_META_YAML}')

    with open(PDF_SETUP_IN, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        lines = [line.rstrip(NL) for line in source.readlines()]

    bumped = []
    debug and print('#  -  -  -  -  -  -  -  -  - ')
    for line in lines:
        prefix = r'  \cfoot*{\upshape{\scriptsize Copyright © OASIS Open '
        postfix = r'. All Rights Reserved.}}'
        #   \cfoot*{\upshape{\scriptsize Copyright © OASIS Open 2026. All Rights Reserved.}}
        if line.startswith(prefix) and line.endswith(postfix):
            copyright_year = line.replace(prefix, '').replace(postfix, '')
            debug and print(f'DEBUG: Found prior copyright-year ({copyright_year})')
            bumped.append(prefix + job[PUB_YEAR_STR] + postfix)
            debug and print(f'DEBUG: Bumped to ({job[PUB_YEAR_STR]})')
            continue

        bumped.append(line)

    if lines != bumped:
        if not any_changes:
            any_changes = True
        print()
        print(f'# - - - 8< - -(( {PDF_SETUP_IN} )) - - - - - - - - - - - - - - >')
        print()
        sys.stdout.writelines(difflib.unified_diff(
            tuple(line + NL for line in lines),
            tuple(line + NL for line in bumped),
            fromfile='setup.tex.in',
            tofile='setup-bumped.tex.in',
        ))
        if commit:
            with open(PDF_SETUP_IN, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
                target.write(NL.join(bumped) + NL)
    else:
        print(f'INFO: No changes to {PDF_SETUP_IN}')


    with open(SRC_FRONTMATTER, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        lines = [line.rstrip(NL) for line in source.readlines()]

    bumped = []
    debug and print('#  -  -  -  -  -  -  -  -  - ')
    for line in lines:
        # ## 21 January 2026
        prefix = '## '
        postfix = ''
        if line.startswith(prefix):
            try:
                day = line.replace(prefix, '').replace(postfix, '').split(SPACE)[0]
                int(day)
                pub_date = line.replace(prefix, '').replace(postfix, '')
                debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
                bumped.append(prefix + job[PUB_DATE] + postfix)
                debug and print(f'DEBUG: Bumped to ({job[PUB_DATE]})')
                continue
            except ValueError:
                pass

        # 21 January 2026.
        prefix = ''
        postfix = '.'
        if 11 < len(line) < 19 and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            try:
                a_day, a_month_name, a_year = pub_date.split(SPACE)  # noqa
            except (ValueError, IndexError):
                bumped.append(line)
                continue
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_DATE] + postfix)
            debug and print(f'DEBUG: Bumped to ({job[PUB_DATE]})')
            continue

        # Copyright &copy; OASIS Open 2026. All Rights Reserved.
        prefix = 'Copyright &copy; OASIS Open '
        postfix = '. All Rights Reserved.'
        if line.startswith(prefix) and line.endswith(postfix):
            pub_date = line.replace(prefix, '').replace(postfix, '')
            debug and print(f'DEBUG: Found prior pub-date ({pub_date})')
            bumped.append(prefix + job[PUB_YEAR_STR] + postfix)
            debug and print(f'DEBUG: Bumped to ({job[PUB_DATE]})')
            continue

        bumped.append(line)

    if lines != bumped:
        if not any_changes:
            any_changes = True
        print()
        print(f'# - - - 8< - -(( {SRC_FRONTMATTER} )) - - - - - - - - - - - - - - - - - - >')
        print()
        sys.stdout.writelines(difflib.unified_diff(
            tuple(line + NL for line in lines),
            tuple(line + NL for line in bumped),
            fromfile='frontmatter.md',
            tofile='frontmatter-bumped.md',
        ))
        if commit:
            with open(SRC_FRONTMATTER, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
                target.write(NL.join(bumped) + NL)
    else:
        print(f'INFO: No changes to {SRC_FRONTMATTER}')

    with open(SRC_HISTORY, 'rt', encoding=ENCODING, errors=ENC_ERRS) as source:
        lines = [line.rstrip(NL) for line in source.readlines()]

    bumped = []
    do_amend = True
    past_table = None  # State machine: None -> False -> True -> None
    trigger_prefix = '|:-----------------------------'
    prefix = '| eox-core-v1.0-wd'
    in_between = f'{job[PUB_ISO_COMPACT]}-dev | {job[PUB_ISO_DASH]}'
    stop_token = prefix + in_between
    postfix = ' | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision for TC review     |'
    debug and print('#  -  -  -  -  -  -  -  -  - ')
    for line in lines:
        # | eox-core-v1.0-wd20260121-dev | 2026-01-21 | Jautau White, Stefan Hagen, and Thomas Schmidt | Editor Revision for TC review     |
        # <-- append here when past_table is True
        if line.startswith(trigger_prefix) and past_table is None:
            past_table = False
            bumped.append(line)
            continue

        if line.startswith(prefix) and past_table is False:
            bumped.append(line)
            if line.startswith(stop_token):
                do_amend = False
            continue

        if not line.strip(SPACE + DASH) and past_table is False:
            debug and print('DEBUG: Found empty line following revision history table')
            if do_amend:
                bumped.append(prefix + in_between + postfix)
                debug and print(f'DEBUG: Appended with in_between ({in_between})')
                do_amend = False
            else:
                debug and print(f'DEBUG: Did NOT append duplicate ({in_between})')
            bumped.append(line)
            continue

        bumped.append(line)

    if lines != bumped:
        if not any_changes:
            any_changes = True
        print()
        print(f'# - - - 8< - -(( {SRC_HISTORY} )) - - - - - - - - - - - - - - - - - - >')
        print()
        sys.stdout.writelines(difflib.unified_diff(
            tuple(line + NL for line in lines),
            tuple(line + NL for line in bumped),
            fromfile='revision-history.md',
            tofile='revision-history-bumped.md',
        ))
        if commit:
            with open(SRC_HISTORY, 'wt', encoding=ENCODING, errors=ENC_ERRS) as target:
                target.write(NL.join(bumped) + NL)
            print()
    else:
        print(f'INFO: No changes to {SRC_HISTORY}')

    print()
    if any_changes:
        print('INFO: Bumped - OK') if commit else print('INFO: Dry-Bumped - OK')
    else:
        print('INFO: No changes - no commit - OK') if commit else print('INFO: No dry-changes - nothing would be committed - OK')

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
