# Input custody — f10-all-r-late-unit-composition-gate-fable5-20260910

First action 2026-09-10 22:05:22 UTC: both owned targets absent (ls errors on the report path and the box directory). Lane input directory /tmp/jc2-lane.DXalaj/inputs holds exactly eight files (read-only filesystem; expected list fed to sha256sum -c over stdin). Result at 22:05 UTC: 8 OK, exit 0, before any body read.

| sha256 | file | lines | bytes | read |
|---|---|---|---|---|
| bc39ffde5bc2e5bdd6c52dc513189dca40c599e63688383a42e034a16f4ef5a6 | ROOT-CARD.md | 14 | 3442 | WHOLE to EOF |
| 8158a7b54c441b4649f9e005a8d5e8a6f976364f8cc9154482ca167359b48123 | f10-all-r-late-unit-composition-astra-20260910.md | 187 | 16362 | WHOLE to Seal |
| 9b80a8cf5fc9708dabee6a5c7eeead399873c83a15e884b40699833ba50521a0 | f10-contact-gram-execution-relative-gate-fable5-20260910.md | 87 | 27884 | WHOLE to marker |
| 7041a28bfa457f97e428a6fab166b10ebf42dfa455b4b2a71f884b3691626517 | f10-contact-gram-execution-root-20260910.md | 50 | 12534 | WHOLE to Seal |
| 7d87064e27a949b22da85afc47fdc658d57c5c24e25c70524867dd3da590b70b | f10-all-r-late-contact-astra-20260909.md | 134 | 11716 | WHOLE to Seal |
| 03b2fe315c048598e57c6409b26bb7a3d6e797ff0f1c2a2f2040ab5a2dbc69de | f10-all-r-late-contact-gate-fable5-20260909.md | 77 | 15940 | WHOLE to marker |
| 4bbecd357077b422fbe636de61c9feefc5b304d88eea0a872b476456b1fbdf30 | f10-two-exponent-contact-discriminator-astra-20260909.md | 303 | 18506 | WHOLE to Seal |
| 4a46e7f605759016829fcfb8ad92586fa9ebe875c4b5a62835b603c8b0ab1e90 | f10-two-exponent-contact-gate-fable5-20260909.md | 83 | 12680 | WHOLE to marker |

Every read was one bounded cat -n of the entire file followed by an EOF echo; no clipping occurred (the two largest, 27884 B and 18506 B, were read in their own calls). No coefficient, fixture, candidate or baseline body exists among these inputs. Tools: date, ls, mkdir (box directory only), sha256sum, cat, wc, grep/sed for own-report metadata; apply_patch for every authored byte. ZERO CAS/subprocess mathematics, ZERO network/AWS/SSH/Git/agents.
