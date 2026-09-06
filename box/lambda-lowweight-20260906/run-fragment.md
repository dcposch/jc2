All **30 charge-zero target computations completed** at the listed B, with basis size 1 and `NF(s^B)=s^B`. The final replay took 19.193 seconds and peaked at 145.4 MiB; `chargezero-independent-audit.json` binds these target-component results.

Cells list N=1,2,3: **C** = completed truncated nonunit at the listed B; **D** = exact target bound below the c-row, not a full basis; **O** = OPEN, no completed weight; **—** = no executed UX probe.

| case | all-row baseline | with c-localizer | with c-localizer and UX |
|---|---|---|---|
| C70 | C,C,C | D,D,D | —,—,C |
| C109 | C,O,O | D,O,O | —,O,O |
| C127 | C,C,C | D,D,D | —,—,— |
| C171 | O,O,O | D,O,O | —,O,O |
| C341 | O,O,O | D,O,O | —,O,O |
| C455 | O,O,O | D,O,O | —,O,O |
| R001 | O,O,O | D,O,O | —,O,O |
| R002 | O,O,O | D,O,O | —,O,O |
| R003 | O,O,O | D,O,O | —,O,O |
| R004 | O,O,O | O,O,O | O,O,O |

R003 reuses the verified identical R002 presentation. `best-results.json` pins chosen receipts and their history; `run-summary.md` gives individual bounds, times, and memory. No class-unit certificate was obtained.
