# Selected-Q8 breadth contact forces a mod-127 projection component

Date: 2026-08-25  
Status: **PRODUCER-EXACT MOD-127 COMPONENT THEOREM; hostile review required**

## Result

In the selected nonparity Q8 chart over `F_127`, the localized six-row source
has an irreducible one-dimensional component whose cycle-theoretic projection
to `(w,v)` has image equal to the geometrically irreducible candidate plane
curve `H(w,v)=0`.

This is an existence theorem for a projected source component modulo 127.  It
is not yet a degree-one graph theorem, an all-contact grouping theorem, a
characteristic-zero no-merger theorem, or a trajectory exclusion.

## Exact breadth endpoint

Eighty deterministic good fibres completed on AWS:

```text
Box02: w=1..42 excluding 25,39       40 PASS, 0 FAIL
Box03: w=43..83 excluding 56         40 PASS, 0 FAIL
```

Every lane independently checked:

```text
fixed-fibre lex-shape custody                         present
all original fixed-fibre source remainders            zero (pinned audit)
candidate H specialization                            exact (pinned audit)
deg_v H(w_i,v)                                        190
gcd(H,H_v)                                            1
gcd(H,det J_6x6)                                      1
moving algebra dimension / length                     0 / 1520
six divided source rows through s^8                   zero
ratio v*x5-x3+2*x5 through s^8                        zero
localizer through s^8                                 zero
final_fail                                             0
```

The 80 lane peak resident set size was only 48,008 KiB.  Exact per-lane input,
stdout, stderr, metadata hashes and the selected fibre lists are in

```text
cases/max12_912_order3_nu_q8_p127_breadth_order8_aws_20260825/breadth_summary.json.
```

## Component inequality

The frozen sparse contact-to-component lemma gives

```text
deg(pi_*Z) <= 658
```

and says that normalized contact sum `S>658` forces an `H`-supported projected
component.  Its immutable report is

```text
xmodel/max12-912-order3-nu-q8-sparse-contact-component-lemma-20260825.md
SHA256 78fb3e1b08556498d79ed180f9b64e243f88dd80780936bc47e15b3749b5ce77.
```

All 123 exact squarefree fixed fibres contribute baseline order one.  The
separately frozen `w=25` order-64 lift replaces one baseline contribution by
64.  Take the lexicographically first 68 passing order-8 fibres,

```text
w=1..71 excluding 25,39,56.
```

They are distinct from `w=25` and from one another.  Therefore

```text
S = 123 + (64-1) + 68*(8-1)
  = 662
  > 658.
```

At each selected fibre, squarefreeness splits the degree-190 moving algebra
over the algebraic closure into 190 distinct length-eight jets.  The unit
source Jacobian makes each base point a unique reduced local branch and `w-w_i`
a uniformizer.  Thus the jets contribute at least `190*662` to the finite
intersection with `H`.  If no projected source component were `H`, the frozen
lemma and projective Bezout would bound the same intersection by
`190*658`, a contradiction.  Hence the stated component exists.

The twelve remaining passing fibres are unused margin; the proof subset is
fixed independently of runtimes or output values.

## Scope firewall

What is now exact, conditional only on the cited frozen inputs, is:

> at least one mod-127 relevant source component has projected image `H`.

Still charged:

1. The source-to-`H` map may have degree greater than one.  A smooth/etale
   sampled point proves local degree one there, not global degree one.
2. The theorem does not place every one of the 190 branches, nor the eight Q8
   boundary contacts, on a single source component.
3. A mod-127 component can in principle be the merger of distinct horizontal
   characteristic-zero components.  The integral full-contact/no-merger
   checklist remains necessary.
4. Taylor realization, polynomial boundary data, the terminal differential
   row, rationality, and Keller/trajectory conclusions are untouched.

No msolve output is used.  Every substantive calculation ran on AWS under
pure Singular 4.3.2; the contact-to-degree calculation is exact Normaliz
support arithmetic.

## Principal custody

```text
breadth_summary.json  7cfeb94ca1f6c36bbdaf6fd32e163f4b3a764383a45b6f1c7f1c2ad919f91d74
generate_breadth.py   6b33f1c6ca57422fc229441059402b3f1908420023aeb6a2095eb3aa1545b2af
run_one.sh            0318b213599d158588a12947bdaf69ab89b7a5a5b473c432ba349d3bd67683b2
summarize.py           fb911fbaf2831784d73f27a0510af7482cb662861474a64a7bb89d12c5d860a3
```
