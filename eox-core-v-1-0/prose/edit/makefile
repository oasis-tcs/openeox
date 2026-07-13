.POSIX:
.SILENT:
.DEFAULT_GOAL = build

pyversion = py312
linelength = 120
black = black -S -l $(linelength) --target-version $(pyversion) --quiet bin
lint = ruff check bin
types = mypy bin
build_root = build/
build_pdf = $(build_root)render/pdf/
liitos_templates = etc/liitos/
optimize_pdf = qpdf --linearize --replace-input

target_gfm_plus = gfm-plus
target_pdf = pdf

out_html = ../share/eox-core-v1.0-draft.html
out_gfm_plus = ../share/eox-core-v1.0-draft.md
out_pdf = ../share/eox-core-v1.0-draft.pdf

.PHONY: all
all: lint types build

.PHONY: format
format:
	command -v ruff >/dev/null 2>&1 || { echo >&2 "make format requires ruff but it's not installed - you can install with: 'pip install ruff'.  Aborting."; exit 1; }
	$(lint) --fix
	command -v black >/dev/null 2>&1 || { echo >&2 "make format requires black but it's not installed - you can install with: 'pip install black'.  Aborting."; exit 1; }
	$(black)

.PHONY: lint
lint:
	$(lint) --diff
	$(black) --check --diff
	command -v unmake >/dev/null 2>&1 || { echo >&2 "make lint requires unmake but it's not installed - you can install with: 'cargo install unmake'.  Aborting."; exit 1; }
	unmake makefile

.PHONY: types
types:
	command -v mypy >/dev/null 2>&1 || { echo >&2 "make types requires mypy but it's not installed - you can install with: 'pip install mypy'.  Aborting."; exit 1; }
	$(types)

.PHONY: render
render: render-html

.PHONY: sections
sections:
	python -m nide harvest

.PHONY: gfm-plus
gfm-plus: sections
	python -m nide assemble -t $(target_gfm_plus) && \
	  cp -a build/tmp.md $(out_gfm_plus) && \
	  printf "Rendered user facing delivery item in markdown format:\n" && \
	  ls -l $(out_gfm_plus)

.PHONY: html
html: gfm-plus
	command -v pandoc >/dev/null 2>&1 || { echo >&2 "make render-html requires pandoc but it's not installed - you can get help on installing at https://pandoc.org.  Aborting."; exit 1; }
	command -v tidy >/dev/null 2>&1 || { echo >&2 "make render-html requires tidy but it's not installed - you can get help on installing by searching for it on the wild internets.  Aborting."; exit 1; }
	python -m nide assemble -t html && \
	  pandoc -f gfm+definition_lists -t html build/tmp.md --columns=345 \
	    --css style/base.css --css style/skin.css --standalone -o build/tmp.html && \
	  python -m nide inject && \
	  timeout 2 tidy -config etc/tidy-config.txt build/injected.html -ashtml 2>/dev/null | \
	    sed 's/<!\[CDATA\[//g; s/\]\]>//g;' > $(out_html) && \
	  printf "Rendered user facing delivery item in html format:\n" && \
	  ls -l $(out_html)

.PHONY: deprecated-pdf
deprecated-pdf:
	command -v liitos >/dev/null 2>&1 || { echo >&2 "make render-pdf requires liitos but it's not installed - you can install per pip install liitos.  Aborting."; exit 1; }
	command -v etiketti >/dev/null 2>&1 || { echo >&2 "make render-pdf requires etiketti but it's not installed - you can install per pip install etiketti.  Aborting."; exit 1; }
	command -v qpdf >/dev/null 2>&1 || { echo >&2 "make render-pdf requires qpdf but it's not installed - you can search the internets on how to install qpdf.  Aborting."; exit 1; }
	python -m nide assemble -t $(target_pdf) && \
		mkdir -p $(build_pdf)images $(build_root)images && \
		printf "pdf.md\n" > $(build_root)bind.txt && \
		cp -a ../media/OASISLogo-v3.0.png $(build_root)images/ && \
		cp -a ../media/OASISLogo-v3.0.png $(build_pdf)images/ && \
		cp -a $(liitos_templates)approvals.yml $(build_root) && \
		cp -a $(liitos_templates)bookmatter.tex.in $(build_root) && \
		cp -a $(liitos_templates)changes.yml $(build_root) && \
		cp -a $(liitos_templates)driver.tex.in $(build_pdf) && \
		cp -a $(liitos_templates)meta.yml $(build_root) && \
		cp -a $(liitos_templates)metadata.tex.in $(build_pdf) && \
		cp -a $(liitos_templates)patch.yml $(build_root) && \
		cp -a $(liitos_templates)publisher.tex.in $(build_root) && \
		cp -a $(liitos_templates)setup.tex.in $(build_pdf) && \
		cp -a $(liitos_templates)structure.yml $(build_root) && \
		cp -a $(liitos_templates)structure.yml $(build_pdf) && \
		cp -a etc/etiketti/etiketti.yml $(build_pdf) && \
		cd $(build_pdf) && \
		max_print_line=10000 liitos render ../../ --target eox-core --facet pdf --patch-tables --filters ' ' --label "etiketti --config etiketti.yml --enforce" && \
		$(optimize_pdf) -- this.pdf && \
		cp -a this.pdf ../../../$(out_pdf)

.PHONY: typst
typst:
	command -v typst >/dev/null 2>&1 || { echo >&2 "make typst requires typst but it's not installed - you can install per brew install typst.  Aborting."; exit 1; }
	# Pass 1+2: assemble IR and render typst channel
	nide assemble
	nide render -t typst
	# Prepare logo (pandoc/typst resolves image paths relative to the .typ file)
	mkdir -p build/images
	cp ../media/OASISLogo-v3.0.png build/images/
	# Convert to typst source
	pandoc -f markdown+definition_lists -t typst --standalone --template etc/openeox.typ --lua-filter build/nide-columns.lua build/typst.md -o build/typst.typ
	# Compile to PDF
	typst compile --root . build/typst.typ build/typst.pdf && \
	  $(optimize_pdf) -- build/typst.pdf && cp -a build/typst.pdf $(out_pdf) && open $(out_pdf)

.PHONY: pdf
pdf: typst

.PHONY: render-pdf  # Deprecated - backwards compatibility target
render-pdf: typst

.PHONY: render-html # Deprecated - backwards compatibility target
render-html: html

.PHONY: render-markdown # Deprecated - backwards compatibility target
render-markdown: gfm-plus

.PHONY: build
build: render status

.PHONY: status
status:
	printf "Current version control status:\n"; \
	git status

.PHONY: diff-pdf
diff-pdf:
	printf "Current PDF version control diff:\n"; \
	command -v iconv >/dev/null 2>&1 || { echo >&2 "make diff-pdf requires iconv but it's not installed - you can search the internets on how to install iconf.  Aborting."; exit 1; }
	git diff -a $(out_pdf) | iconv --from-code=UTF-8 -c

.PHONY: clean
clean:
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]' `
	rm -f `find . -type f -name '*~' `
	rm -f `find . -type f -name '.*~' `
	rm -rf .cache .*_cache
	rm -f .DS_Store
	rm -fr $(build_root)
	mkdir -p $(build_root)

.PHONY: distclean
distclean: clean
	rm -fr $(build_root)
