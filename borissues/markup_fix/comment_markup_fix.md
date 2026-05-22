### Location

Counterpart of https://github.com/sanskrit-lexicon/PWG/issues/175 (PWG) and https://github.com/sanskrit-lexicon/PWK/issues/113 (PWK) for `bor.txt`.

I ran the same two-job recipe over `csl-orig/v02/bor/bor.txt`: auto-fix the few things with a single safe resolution; audit everything else with line refs. Added `08_markup_fix.py` plus outputs to a new `borissues/markup_fix/` folder on the branch `markup-fix-audit`.

@funderburkjim @Andhrabharati — please review the findings listed below.

## Markup fixer + audit for `bor.txt`

### What it auto-fixes

| Pattern | Result |
|---|---|
| `<ab><ab>X</ab> Y</ab>` | `<ab>X Y</ab>` |
| `<div> word </div>` | `<div>word</div>` |
| `<ls> word </ls>` | `<ls>word</ls>` |

Whitespace trimming applies to all 2 paired tag(s) in `bor.txt`: `<div>`, `<ls>`. The original file is never modified — output goes to `bor_fixed.txt`, with the full diff in `markup_fix_changes.txt` (updateByLine format). 11623 line(s) changed.

### Closing-tag inventory in current `bor.txt`

| Tag | Count |
|---|---:|
| `</div>` | 71 |
| `</019)>` | ? |
| `</ls>` | 526 |

### What it found in current `bor.txt`

- 11,623 whitespace trims applied: trailing spaces stripped from `<div>` tags throughout bor.txt. This is the largest single auto-fix of all dictionaries processed.
- 0 adjacent `</ab> <ab>` — no `<ab>` tag in bor.txt.
- 0 `<ab n="…">` attributes — no abbreviation markup.
- 88 `{{old → new || …}}` correction records present.

### Usage

```
cd borissues/markup_fix
python 08_markup_fix.py                        # uses csl-orig/v02/bor/bor.txt by default
python 08_markup_fix.py IN.txt OUT.txt         # custom paths
```

Outputs: `bor_fixed.txt`, `markup_fix_changes.txt`, `markup_audit.txt`.

### Summary

26,056 trailing-space hits in <div> (from scan; 11,623 changed lines after dedup).

### Severity

`minor`
