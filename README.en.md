<div align="center">

# One-Page LaTeX Résumé Template

**One content source, three scenarios**: visual (tech) · formal (state-owned) · plain ATS
Bilingual (CN / EN) · XeLaTeX · one-switch theme color & photo

<br>

[简体中文](README.md) · **English**

</div>

---

## Three versions

A single content source (`content/en.tex` / `content/zh.tex`) drives all three layouts via `\usepackage` options — no conflicts:

| Version | File | Best for | Traits |
|---|---|---|---|
| **Tech / internet** | `main-internet.tex` | algorithm / AI / dev / data roles | blue, single-column, no photo, plain-text skills; basic text-extraction friendly |
| **Formal / SOE** | `main-soe.tex` | state-owned enterprises, print / human review | navy, portrait photo, formal; keeps hierarchy in B/W print |
| **Pure ATS** | `main-ats.tex` | strict online application systems | single text flow: no tables, no photo, no colored tags — maximal extraction & reading order |

Chinese version: `main-en.tex` → for Chinese use `content/zh.tex` (see the CN README).

<div align="center">
<table>
<tr>
<td align="center"><b>Tech</b></td>
<td align="center"><b>SOE / Formal</b></td>
<td align="center"><b>Pure ATS</b></td>
</tr>
<tr>
<td><img src="assets/preview-internet.png" width="250"></td>
<td><img src="assets/preview-soe.png" width="250"></td>
<td><img src="assets/preview-ats.png" width="250"></td>
</tr>
</table>
<sub>All previews are compiled from the current <code>main-*.tex</code>.</sub>
</div>

---

## Section order

Optimised for job applications, with internship as its own module (no longer buried inside projects):

```
Education  →  Internship  →  Projects  →  Research / Open Source  →  Skills
```

---

## Quickstart

**Overleaf**: upload the whole repo → open any `main-*.tex` → set compiler to **XeLaTeX** → compile.

**Local** (TeX Live / MacTeX):

```bash
xelatex main-internet.tex     # or main-soe / main-ats / main-en
# or build all four at once:
bash build.sh
```

> Compile twice to generate PDF bookmarks. For the SOE version's photo, drop `photo.jpg` in the repo root; if missing, a placeholder box is shown.

---

## How to edit

**Edit one file**: `content/en.tex` (Chinese: `content/zh.tex`). All three scenario versions update together.

- **Header fields**: name, target role, contacts (phone · email · city · GitHub — a single text line).
- **PDF keywords**: driven by the `\ResumeKeywords` variable — a generic default; edit it for your target role and don't keep terms unrelated to the job.
- **SOE extra fields**: uncomment `\ResumeExtraLine` in the content file to add formal fields (target role / location / etc.); off by default to avoid over-sharing personal info.

Switch theme color / photo from the options at the top of `main-*.tex`:

```latex
\usepackage[blue]{resume}          % tech blue, no photo
\usepackage[navy,photo]{resume}    % SOE navy, with photo
\usepackage[ats,mono]{resume}      % near-black plain text, max ATS compatibility
```

Options: `blue` / `navy` / `mono` (theme), `photo` (show photo), `ats` (plain text flow).

---

## About ATS compatibility (please read)

This template makes several parser-friendly choices: **contacts on a single text line** (no nested tables), **visible link text** (not icon-only), **skills as categorised plain text** (no colored tag boxes), PDF bookmarks, and variable keyword metadata.

`main-ats.tex` goes further — no tables, no photo, no color or icons — and is the **safest** version to parse. The repo ships `check-ats.py` to verify text-extraction order:

```bash
bash build.sh && python3 check-ats.py
# prints: name → role → contact line → sections, in the correct order
```

> **Honest note**: ATS parsers vary a lot. The visual versions pass basic text extraction, but if a target company uses a strict online application system, prefer the PDF from `main-ats.tex`. This template aims for **text-selectable / basic ATS compatibility**, not a guarantee of "100% ATS pass".

---

## Layout

```
resume.sty            shared style: theme colors, page geometry, all layout macros (scenario logic)
content/zh.tex        Chinese content (sample data — edit here)
content/en.tex        English content
main-internet.tex     tech / internet version
main-soe.tex          SOE / formal version
main-ats.tex          pure ATS version
main-en.tex           English version
build.sh              build all versions
check-ats.py          ATS text-extraction self-test
assets/               previews (compiled from the current main-*.tex)
```

---

## License

MIT — free to use, modify and use commercially, no attribution required. Sample content is fictional; replace it with your own.
