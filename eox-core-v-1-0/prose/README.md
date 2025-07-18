# The EOX-CORE v1.0 Prose Folder

This place offers access to the editable sources of the v1.0 EOX-CORE specification (to be).

In the `share` folder, there are the user facing delivery items that offer layout and navigation
optimized for online viewing per

- a typical web interface of a version control server (like Codeberg, GitHub, GitLab, or SourceHut) - the Markdown file
- any typical browser (like Brave, Chrome, Edge, Firefox, or Safari) - the HTML file

Inside the `edit` folder we build these delivery items from the source files (also in Markdown format, but
split by concerns, verifiable per syntax, and offering clean structural constructs for definition lists etc.
instead of the specific idioms mixed in for ease of use in specific reading tools).

The `share/eox-core-v1.0-draft.md` file is generated from the source files below `edit/src/` as collected per `edit/etc/bind.txt` through
the `edit/bin/volatile.py` script.

To generate the Markdown version and the HTML user facing delivery item simply call `make` inside the edit folder.

To generate the PDF (experimental) file, call `make render-pdf` in the edit folder.
