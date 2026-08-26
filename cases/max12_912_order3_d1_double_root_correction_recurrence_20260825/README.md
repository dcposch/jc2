# D1 double-root correction-aware recurrence wave

The Box02 exact replay consumed all eight independently reconstructed ordinary
tails and confirmed both correction negative controls with rc zero and empty
stderr.

- In the non-target control, every tail vanishes through `t^48`; deleting the
  forced `U/9` correction makes weight `t^48` nonzero.
- In the target control, every tail below `t^60` vanishes and the complete
  `t^60` vector is `(0,0,2/3,0,0,0,0,0)`; deleting the `-1/2` correction
  changes it.

These are exact finite Newton successors, not formal lifts.  `DESIGN.md`
specifies the correction-aware coefficient recurrence and the mandatory
finite-slope firewall.  Whole-fan coverage requires a certified tropical /
Groebner-fan traversal; bounded slope runs remain screening.
