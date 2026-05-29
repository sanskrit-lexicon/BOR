# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**BOR** is the corrections repository for the Cologne digitization of Borooah's *English-Sanskrit Dictionary* (1877). The canonical source lives in `csl-orig/v02/bor/bor.txt`.

## Architecture

| Directory | Purpose |
|---|---|
| `csl_orig_issue_606/` | Batch correction for csl-orig issue #606: Devanagari punctuation handling |

### `csl_orig_issue_606/`

Scripts for fixing punctuation placement in Devanagari transliteration:
- `bor_corrected.txt` — corrected output
- `error_deva.txt` — entries with Devanagari encoding errors
- `punctuation_in_devanagari.sh` — identifies punctuation-in-Devanagari issues
- `shift_punctuation.py` — moves punctuation to correct position relative to Devanagari clusters

Issues and corrections are tracked via the [GitHub issue tracker](https://github.com/sanskrit-lexicon/BOR/issues).

## Common Commands

### Apply line-level corrections (standard pattern)
```bash
python updateByLine.py <input_file> <changein_file> <output_file>
```

### Rebuild and validate XML (from `csl-pywork/v02/`)
```bash
sh generate_dict.sh bor ../../BORScan/2020
sh xmlchk_xampp.sh bor
```

## Dependencies

- **Python 3**
- **bor.txt** — in `$BASE/cologne/csl-orig/v02/bor/bor.txt`

## Data format

BOR is an **English→Sanskrit** dictionary: English headwords with Sanskrit glosses.

| Tag | Role | Example |
|---|---|---|
| `<L>NNNN` | Entry begin, with `<pc>` print page ref | `<L>1<pc>001` |
| `<k1>`, `<k2>` | Primary / secondary headword | `<k1>a<k2>a` |
| `<LEND>` | Entry end | |
| `{@…@}` | English headword (bold) | `{@A@}` |
| `{%…%}` | Italic display | `{%or%}` |
| `<div n="…">` | Sense / sub-entry structure | `<div n="I">` |

Annotated example — the first entry of `bor.txt`:
```
<L>1<pc>001<k1>a<k2>a              # entry 1; English headword "A"
{@A@}¦ {%or%} (before vowels) AN: <div n="I">I This article ...   # bold headword ¦ gloss + sense
<LEND>                             # entry end
```

## GitHub Issue Conventions

This repository uses the Cologne dictionary-repo issue taxonomy. Every issue has exactly one **type**, one **severity**, and one **milestone**:

- **Type** (9): link-target, link-splitting, markup, text-correction, content-enhancement, encoding, scan-quality, bug, question
- **Severity** (3): minor, medium, hard
- **Milestone** (4): Dictionary to Book, Digitization Quality, Structured Data, Major Enhancements

See the [Cologne issue runbook](https://github.com/sanskrit-lexicon/csl-observatory/blob/main/runbook/cologne-issue-runbook.md) for label definitions and the type→milestone mapping.
