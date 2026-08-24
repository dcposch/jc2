# Hostile different-model review — AS gauge growth at p=3 through depth four

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a`, with frozen uncommitted
artifacts on top. Read in full:

- `xmodel/as-gauge-growth-p3-depth4-gate-20260824.md`;
- every payload named in
  `cases/as_gauge_growth_p3_depth4_20260824/FREEZE.sha256`;
- the frozen bounded-polar-conductor producer/review named as inputs.

Frozen hashes:

- producer report:
  `bfacd9a475f8e2aa7da9d26e43785b80ff3eadd53615e4823dfe6d52fc6fd660`;
- preregistration:
  `65a36738032e003185f48539b1c571b754bbbec2868629893c840cfae3eceefd`;
- producer replay/stdout:
  `db6ffc06efcdcc1f3a3619ff73e5d2c243f662ada9a5371394346c9922e93ed7` /
  `088cb5546e36968c2e1fb0cd6917b948a45f50b7fefe837a1dbc978873462b7e`;
- same-model negative-control checker/stdout:
  `2fc1e60f827237d37b91b164a653de5b294aa97d0a48ec5d3aa9d4a3da166d6d` /
  `10717a107b69ae9b961b86af520a3cc8467ed81780e7271e39d73897639ecc26`;
- manifest:
  `b57bfe29136fe334fef3a53fa53efa4d7ff03607036a0357c71f2b0328d6a380`;
- freeze file:
  `7805a82e0c8113953cbc203ec7be134fd4aaed83cc81a095f313b86dd3b79fbb`.

Verify the freeze and rerun both registered programs. Then independently
attack every load-bearing statement:

1. **Gauge elimination and finite-system equivalence.** Starting from
   `C_p=(T-T^p,y/(1-pT^(p-1)))` and `C_p o Phi_F=F`, derive
   `A-A^p=P` and `B=Q(1-pA^(p-1))`. Check Hensel uniqueness on the identity
   branch and the determinant identity. At finite depth, verify that the
   F-only formulation retains both map and canonical-gauge degree caps, so
   no bounded condition is lost by elimination.
2. **Universal depth-four carries.** Independently expand
   `A=x+3a+9c+27e`, `B=y+3b+9d+27f` modulo 81. Recompute both coordinate
   formulas and
   `det J(A,B)=1+3L1+9L2+27L3`, including all `a^2,a^3,ab`, mixed-bracket,
   and divided-divergence carries. Use a separate exact implementation or
   hand-derived coefficient extraction, not just the producer assertions.
3. **Depths two and three.** Verify the positive cotangent controls and the
   exact lower bound at depth two. Rebuild the full depth-three affine
   systems at D=3,4,5 or give independent exact certificates. Check ranks
   `15/16`, `21/22`, and `28/28`, and independently derive the small unit row
   `[x^4y]=[x^2y]b-[x^3]a+1` after the cap/divergence constraints.
4. **Depth-four forced degrees.** Audit the Frobenius/top-degree argument
   forcing `deg a<=2`, the second-coordinate argument forcing
   `deg b<=3` at D=5 and `<=4` at D=6, and the rows forcing
   `c_[x5]=a_[x3]=b_[x2y]=0`. Look for cancellations from c,d,e,f or an
   omitted same-degree monomial before accepting any bound.
5. **Unit certificate.** Independently derive
   `U=[x5y](ab)`, `K=[x4]{a,b}`, and `K=-U` over F3, treating the absent top
   b-slots at D=5 explicitly. Recompute the exact determinant carry at x4
   and the second-coordinate x6y row. Verify that
   `(Q row)-(det row)-b_[x2y]=1` is a true ideal certificate at both D=5
   and D=6, with no illegal division or representative-dependent carry.
   Independently exhaust the relevant finite top assignments as a negative
   control.
6. **Positive depth-four control.** Verify that the truncated cotangent map
   at D=7 has determinant one modulo 81, exact second-coordinate degree
   seven, and satisfies the same canonical gauge cap. Decide whether the
   three exact minima are therefore 3,5,7.
7. **Scope and successor.** Attack every inference from this finite result
   to depth n>=5, the formula `(n-1)(p-1)+1`, p=109, nonexistence of an
   unbounded polynomial lift, identification of A_infinity, a counterexample,
   or JC2. State whether an inductive highest-carry/unit-certificate lemma or
   an exact n=5 discriminator is the smallest honest successor.

Use exact arithmetic throughout. The included `independent_check.py` is a
same-model control and is not itself the required independent review. Do not
edit producer, case, canonical, or erratum files and do not launch AWS. Write
exactly one report:

`xmodel/as-gauge-growth-p3-depth4-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, independent derivations, the smallest failing identity if any,
precise promotion scope, and quarantine language at both ends.
