# Coordinator integration — Sigray Propositions 6.7/6.8

Date: 2026-08-28  
Verdict: **PROPOSITION 6.7 PROMOTED WITH REPAIR; PROPOSITION 6.8
PROVISIONALLY REPAIRED, LEMMA 6.1 REVIEW OWED**

## Frozen evidence

```text
c3d6ff9239fb136cc35b815de6e229755f7d27b640481e7751d03d63291d1ebd  producer source audit
eb37373b3bf84c83b0f4774968690f650fb3a62635baa66e35e81096f8f30db4  Opus5 hostile review (REPAIR)
050ccddddeabfddbb97ffcf3d7ef6abdcac024a56f6db1df0f6d88ef87474fc2  Opus5 correction addendum
581219e095123642eb32018bad1d52ee1ba06bba6573279f4c135831a96e8590  Statement 6.2 consumer sweep r2
651231a80274de4d684076c4b238be38b98e3a4ad704e750a06fa23c43ef6e5f  Lemma 6.1 repair producer
```

The correction addendum is mandatory: the review initially reversed
Notation 2.4.  The primary source defines `alpha/beta=k_f/k_g`, so the
producer's `d_(g,F)/d_F=beta/alpha` is correct.  The addendum also withdraws
the review's mistaken conflation of finite thresholds with `T_a^0` critical-
value vertices.  Neither correction changes the review's core `REPAIR`
verdict.

## Proposition 6.7

The conclusion is true after adding the typing rider
`kappa*pi(F) in N`.  The promoted repair has four essential parts.

1. Every residual `p_(H,F)` at a vertex is semi-invariant under the exact
   `mu_(nu_F)` stabilizer.  The map on the group is an automorphism because
   `gcd(beta_j/e_j,nu_F)=1`, so the strict multiplicity inequality survives
   the unique root rotation in corrected Statement 3.18.
2. Exact Statement 3.9 remains licensed for `f,g`, but not for the derived
   terminal `h_F`.  Corrected Statement 3.11 gives
   `r<=n` and `e_G>=e-n/kappa`, hence

   ```text
   m*e_G-n*d_G >= m(e-n/kappa)-n(d-m/kappa)=me-nd>0.
   ```

3. Proposition 6.3 gives only a matching tower prefix, not the source's
   asserted `h=h_G`.  If the child tower stops at that prefix, Proposition
   6.4 contradicts the strict ratio.  If it extends, the zero leading bracket
   forces equality of the same order/degree ratios, again contradicting the
   strict ratio.  This closes the producer's remaining load-bearing gap.
4. In the `h=g` branch, integrality and the corrected pole ratio exclude
   `kappa*d_F=1`; in the `h!=g` branch, the reviewed no-first-corner theorem
   licenses positive first exponents and Proposition 4.1 excludes `d_G=0`.

Thus every defined one-grid-step child of a down vertex with `deg p_F>1` is
positive, and some such child is down.

## Lemma 6.1 and Proposition 6.8

The printed proof of Lemma 6.1 ends with an invalid bare inference from
`deg p_(g,F)=0` to a nonzero leading Jacobian.  The short replacement
`651231a8...` proves the lemma without that grid argument: if `m_F>0`, the
first positive-tree relation is `q^alpha=s*p^beta`; `deg p=1` forces
`alpha|beta`, contradicting coprimality and `alpha>=2`.  Hence `m_F=0`, and
the terminal clause of corrected Proposition 4.2 gives the desired nonzero
multiple of `xi^(-pi(F))`.  A Fable5 review launch was attempted but blocked
by its account usage cap; this proof therefore remains explicitly
different-model-review-owed.

Conditional only on that short lemma, Proposition 6.8 is repaired as follows:

- use one fixed common-suitable grid;
- exclude degree-one intermediate points with Lemma 6.1;
- replace the false printed bound `d_(F_n)<=u-n/kappa` by
  `d_(F_n)<=d_F-n/kappa`, which forces finite termination; and
- use Notation 3.8/Statement 3.5 to show that the terminal pole and every
  intermediate flag lie on one branch.

## Statement 6.2 bridge and firewall

`G*_(kappa)c` is a one-grid-step point; `H=G+c` is the next vertex.  They
need not coincide.  Under Statement 6.2's raw strict inequality, Proposition
6.7 first supplies positivity of the microstep, making it down.  A genuine
next vertex has transported degree `mult(p_G,c)>=2`; repaired Proposition 6.8
then supplies a same-direction pole branch through `H`, and monotonicity makes
`H` positive.  The verified iff in Statement 6.2 makes `H` down.

Therefore Proposition 6.8, not Proposition 6.7 alone, is load-bearing for
every next-vertex regularity consumer in AF2, III, A2P, MULTIPOLE and the
Statements 9.6--9.11 template.  No current conclusion rolls back, but those
consumers remain provisionally dependent on different-model review of the
new Lemma 6.1 proof.  Nothing here audits Sections 7--9, Proposition 5.8,
landing, a degree ceiling, or JC2.
