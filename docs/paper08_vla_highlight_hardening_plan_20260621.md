# Paper08 VLA Highlight Hardening Plan

Date: 2026-06-21

## Objective

Make `C:/Users/wangz/Downloads/08.pdf` explicitly match the visible VLA-v4
role model's boxed-link behavior while preserving the final 26-page active
constraint signatures paper:

- citation links use green one-point boxes;
- internal figure/table/equation/section links use red one-point boxes;
- URL links use green one-point boxes;
- the final PDF is rebuilt, copied to Downloads, visually checked, and leaves
  no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/08.pdf`
- Pages: 26
- Size: 327,986 bytes
- SHA256: `396716A90BA2B59C6F281C31F44FA536B9D4FAB24DB8801A20810D980F454A89`
- Local `paper/main.pdf`: absent
- Repository branch: `master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[]`
- Annotation colors: green = 0, red = 0, cyan = 0
- Border widths: none

Source finding:

- `paper/main.tex` is the active manuscript source.
- The active manuscript preamble does not currently load `hyperref`, so the
  baseline PDF has no boxed citation or internal-reference links.
- The target is to install `hyperref` plus the VLA role-model border policy so
  citation/URL links become green boxed links and internal references become red
  boxed links.
- Use the documented manual LaTeX flow from `paper/`: `pdflatex`, `bibtex`,
  and repeated `pdflatex` passes before export.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add `\usepackage{hyperref}` and the VLA `\hypersetup` block in the active
   `paper/main.tex` preamble.
2. Rebuild manually from `paper/` with `pdflatex`, `bibtex`, and repeated
   `pdflatex` passes.
3. If the log asks for another pass for cross-references, run the final
   canonical pass before recording metadata.
4. Copy the rebuilt `paper/main.pdf` to `C:/Users/wangz/Downloads/08.pdf`.
5. Remove local `paper/main.pdf` after export.
6. Recompute page count, byte size, SHA256, annotation colors, border widths,
   and link pages from the final Downloads PDF.
7. Render every page that contains final link annotations into
   `tmp/pdfs/paper08_after`.
8. Visually inspect rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
9. Update README/status/audit/version/validation metadata with the new hash and
   VLA-style boxed-link inventory.
10. Validate build logs, diff hygiene, final PDF hash, and absence of local
    `paper/main.pdf`.
11. Remove Paper08 temp renders, leaving only the shared role-model render
    directory.
12. Stage only Paper08 source and metadata files, commit, push, and verify a
    clean repository before moving to Paper07.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations, references, URLs, or template examples merely
  to change link counts.
- Do not create an additional `8.pdf`; keep the repository's canonical
  Downloads target as `08.pdf`.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Added `\usepackage{hyperref}` and the explicit VLA `\hypersetup` block in
  active `paper/main.tex`.
- Rebuilt from `paper/` with `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`.
- Exported canonical PDF: `C:/Users/wangz/Downloads/08.pdf`
- Pages: 26
- Size: 397,753 bytes
- SHA256: `962CE3D8110DEE1A30DB3ABD31211CA3497048BDEB33415972E2EEB6CC717DB2`
- Link inventory: 63 annotations on pages `[(1, 13), (2, 35), (3, 6), (7, 2), (9, 4), (10, 2), (11, 1)]`; green = 54, red = 9, cyan = 0; all borders `(0, 0, 1)`.
- Visual audit: rendered pages 1, 2, 3, 7, 9, 10, and 11; green citation/URL boxes and red internal-reference boxes are crisp and aligned.
- Local `paper/main.pdf`: removed after export.
- Duplicate `C:/Users/wangz/Downloads/8.pdf`: not created.
