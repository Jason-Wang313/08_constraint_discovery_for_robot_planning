# Child Status

Stage: VLA-style boxed-link hardening complete; final artifact exported and verified.

Latest actions:
- Downloaded official ICLR 2026 template from the ICLR author guide / Master-Template zip.
- Wrote `paper/main.tex` and `paper/references.bib`.
- Built with direct `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied final PDF to `C:\Users\wangz\Downloads\08.pdf`.
- Confirmed visible Desktop PDF exists at `C:\Users\wangz\OneDrive\Desktop\08.pdf`.
- Wrote `docs/final_audit.md`.
- Committed reproducible repo contents.
- Created and pushed public GitHub repo: `https://github.com/Jason-Wang313/08_constraint_discovery_for_robot_planning`.

Exact commands:
- `Invoke-WebRequest -Uri 'https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip' -OutFile paper\iclr2026.zip`
- `Expand-Archive -LiteralPath paper\iclr2026.zip -DestinationPath paper\iclr2026_template -Force`
- `pdflatex -interaction=nonstopmode -halt-on-error main.tex; bibtex main; pdflatex -interaction=nonstopmode -halt-on-error main.tex; pdflatex -interaction=nonstopmode -halt-on-error main.tex`
- `Copy-Item -LiteralPath paper\main.pdf -Destination 'C:\Users\wangz\Downloads\08.pdf' -Force`
- `gh auth status`
- `git add -A`
- `git commit -m "Add active constraint signature paper"`
- `gh repo create 08_constraint_discovery_for_robot_planning --public --source . --remote origin --push`

Failures:
- Initial template file read used the parent folder instead of the extracted `iclr2026/` subfolder; recovered by listing and using the correct path.
- `gh repo view` reported the target repository did not exist before creation, which was expected.

Recovery steps:
- Copied style files from `paper\iclr2026_template\iclr2026\`.
- Created the missing GitHub repository successfully.

Next:
- none

Exit code: 0
End time: 2026-06-11 09:57:59 +01:00
PDF exists: True

## Submission Hardening v2

- Completed: 2026-06-12 21:42:25 +01:00
- Terminal decision: workshop-only
- Canonical PDF target: `C:/Users/wangz/Downloads/08.pdf` (161983 bytes)
- Key experiment change: added signature-noise stress with false-negative and false-positive diagnostic corruption.
- Key result: at active probability 0.35, valid-plan rate drops from 1.000 exact to 0.887 at 5% active-family misses, 0.766 at 10%, and 0.584 at 20%.
- Claim narrowed: ACS requires reliable low-false-negative family diagnostics and remains a proof-of-mechanism abstraction.

## VLA-Style Link Hardening

- Completed: 2026-06-21
- Added explicit `hyperref` plus VLA-style boxed-link policy to `paper/main.tex`; the baseline final PDF had no link annotations.
- Rebuilt with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Copied final verified PDF to `C:/Users/wangz/Downloads/08.pdf` (26 pages, 397,753 bytes, SHA256 `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`).
- Final link inventory: 63 annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; colors green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Rendered and visually inspected pages 1, 2, 3, 7, 9, 10, and 11; highlighted boxes are crisp and aligned.
- Local `paper/main.pdf` removed after canonical copy.
- No duplicate `C:/Users/wangz/Downloads/8.pdf` was created.
