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
