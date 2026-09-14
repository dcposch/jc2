
## 10. What this changes (for the synthesis), in three lines

1. **17(tttttt) is confirmed and strengthened**: `Γ_t ∩ {b4 ≠ 0}` is one orbit with full symmetric Galois group
   at t = 3..6; the "one scalar per simple point" of the rank lane is "one scalar per t" at these indices.
2. **The instrument is real**: clause (ii) at fixed t costs one modular `std` + one `finduni` + one evaluation
   (t = 6: 3 min).  At t = 8 the wall is the 52140-point elimination (msolve F4/FGLM), not a number-field std; a
   fleet-hour with ≥ 16 threads should land it — the CI formulation (7 forms in q_2..q_7, b3) is the right one.
3. **The all-t residual is problem (II), not (I)**: Prop. 7.1 makes irreducibility logically unnecessary for
   clause (ii); no uniform point of `Γ_t` is known, and the `S_n` Galois data say it cannot come from a symmetry —
   it must come from the Abel/formal-solution side (Astra's non-truncating (F3) solutions).  Disposition: STOP
   fixed-t (V0) work below t = 8; finish the t = 8 one-point test as a fleet job; route the uniform effort to (II).
