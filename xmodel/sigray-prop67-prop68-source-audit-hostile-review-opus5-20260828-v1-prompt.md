You are Opus 5 acting as a genuinely different-model hostile mathematical
reviewer in the plane Jacobian conjecture campaign. Work in
`/Users/dc/code/math/jc2`.

Hostile-review this frozen producer audit:

`xmodel/sigray-prop67-prop68-source-audit-sol-ultra-20260828.md`

Frozen SHA-256:

`c3d6ff9239fb136cc35b815de6e229755f7d27b640481e7751d03d63291d1ebd`.

Recompute that hash before reading. Read the primary source directly at
`refs/sigray_full.pdf`, especially printed pp. 12--18, 23--35 and Propositions
6.7--6.8. Also read the producer's pinned corrected dependencies named in its
Section 1. Do not treat any report verdict or checker banner as evidence.

Independently reconstruct and attack every part of the repair, concentrating
on these possible failure points:

1. **Auxiliary `h=h_F` denominator.** Verify the printed exact use of
   Statement 3.9 is unlicensed when `kappa` is only common-suitable for `f,g`.
   Check the proposed replacement from corrected Statement 3.11 with the
   correct inequality directions:
   `deg p_(h,G)<=n`, `d_(h,G)>=e-n/kappa`, and
   `m(e-n/kappa)-n(d-m/kappa)=me-nd>0`. Decide whether this alone really
   identifies `h=h_G` and forces the chosen child searrow, including any use
   of Propositions 6.3/6.4 and the corrected constant-corner trichotomy.
2. **Cyclic residual lemma.** Prove or refute that for an arbitrary polynomial
   `H` and vertex `F`, `p_(H,F)` is semi-invariant under the relevant
   `mu_(nu_F)` action, so `mult(p_(H,F),epsilon*c)` is constant on each
   nonzero orbit. Check that the group acting in corrected Statement 3.18 is
   exactly the group in this lemma, independent of an enlarged denominator.
   This must license preserving the strict `q`-multiplicity inequality after
   the unique rotation selecting an existing child. If it is not derivable
   from the source setup, mark a genuine gap.
3. **`h=g` branch.** Check the repaired sided-threshold argument, the use of
   `deg p_F>1` to force `F` to equal rather than strictly follow the pole
   threshold, corrected Proposition 5.3(ii)/(viii), integrality, and the
   conclusion `d_G>0`.
4. **`h!=g` and `d_G!=0`.** Verify the positive first exponents from the
   no-first-corner theorem, exact Statement 3.9 only for fixed `f,g`, the
   condition-(7) licence at `G`, and the equality-branch contradiction.
5. **Proposition 6.8.** Check Lemma 6.1 use, the exclusion of degree one,
   sequential licensing, the corrected bound `d_(F_n)<=d_F-n/kappa`, finite
   termination, and the exact same-branch ancestor conclusion. Confirm the
   printed `u-n/kappa` really is wrong rather than notation for `d_F`.
6. **Microstep versus next vertex.** Check Notation 3.8 and Proposition 3.2:
   `G*_(kappa)c` need not equal the vertex `H=G+c`. Verify or refute the
   producer's bridge. Under the raw Statement 6.2 inequality, does the first
   microstep lie searrow? If `H` is a genuine next vertex, must
   `m=mult(p_G,c)>1`? Does repaired Proposition 6.8 then put a pole on a final
   branch whose grid ancestors include `H`, proving `H` searrow? Explicitly
   test the apparent `m=1` edge case rather than assuming it away.
7. **Blast radius.** Decide whether Proposition 6.8 is therefore load-bearing
   for every Statement 6.2 next-vertex regularity consumer (AF2, III, A2P,
   MULTIPOLE, the Statements 9.6--9.11 template), not only explicit pole
   manufacture. Separate any actual rollback from documentary dependency
   repair.

Give a terminal verdict exactly one of `PASS`, `REPAIR`, or `REFUTE`. Separate
the truth of Propositions 6.7/6.8 from defects in the producer's proof and from
consumer blast radius. Keep the report under 3,000 words and your final CLI
response under 200 words. Do not create a checker unless a genuinely
nontrivial finite computation is indispensable; this should be a source proof
audit.

Write exactly:

`xmodel/sigray-prop67-prop68-source-audit-hostile-review-opus5-20260828-v1.md`

Do not edit the frozen producer, any canonical/top-level campaign file, or any
other existing artifact. Never enter, list, search, read, build, status, or
modify `jc2-lean`. Preserve the dirty shared worktree. Your only write may be
the required review; the lane wrapper owns its `.log` and `.run` files. No
AWS, web, or heavy local CAS.
