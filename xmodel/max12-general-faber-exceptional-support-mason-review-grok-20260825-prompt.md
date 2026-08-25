# Hostile-review charge: general Faber exceptional-support theorem

Act as an adversarial algebraic referee. Inspect, but do not modify or
execute, these two artifacts:

- `xmodel/max12-general-faber-exceptional-support-mason-20260825.md`
- `xmodel/max12-general-faber-exceptional-support-mason-review-20260825.md`

The producer target has SHA-256
`7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919`.
Treat the independent review and its `CONFIRMED` string as non-authoritative.

Audit the following points from first principles.

1. For monic depressed `f` of degree `m`, positive Faber index `n`, and
   `g=F_n(f)`, verify that vanishing of tails `r_1,...,r_(m-1)` gives
   `deg(g^a-f^b)<=N-m-n`, including why substitution through
   `z(w)=w+O(w^-1)` cannot hide a larger polynomial degree.
2. Check the Mason--Stothers application after division by
   `gcd(g^a,f^b)`: pairwise coprimality, radical-degree bound, signs,
   constant-`W` case, `D<0`, `a=1`, `b=1`, and the apparent `e=N` edge.
3. Check that `g^a=f^b` over an arbitrary characteristic-zero field forces
   a unique monic degree-`d` polynomial `K` over that same field, with
   `f=K^a`, `g=K^b`, and that depression descends to `K`.
4. Check the converse using the Faber definition, not an unstated analytic
   hypothesis.
5. Check the scheme-language boundary exactly: equality of geometric zero
   sets, radical contraction to the base field, closed prime triangular
   power locus `A^(d-1)`, and weighted projectivization
   `P(2,3,...,d)`. Reject any accidental claim that the tail ideal itself is
   reduced. Check the `d=1` edge.
6. Verify the `(9,12)` common-cubic and `(8,12)` common-quartic clients and
   the firewall requiring each Rees client independently to prove that its
   exceptional rows are the ordinary unloaded first tails.

Return numbered findings with severity, the strongest theorem you can
confirm, every required repair, and one final standalone verdict line:

`CONFIRMED`

`CONFIRMED_WITH_REPAIRS`

`NOT_CONFIRMED`
