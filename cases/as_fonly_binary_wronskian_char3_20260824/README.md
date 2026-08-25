# Binary-Wronskian compression in characteristic three

This tiny package replays the algebraic compression used for the `N12` and
`N11` rows of the AS F-only `D=7` successor.  It is independent of the large
finite-state enumeration.

Run:

```bash
./replay_all.sh
```

The replay takes about two seconds and less than 20 MB RSS on the producer
machine.  It contains no large CAS, Lean, or finite-state search.

The theorem and exact scope are stated in
`../../xmodel/as-fonly-binary-wronskian-char3-20260824.md`.
