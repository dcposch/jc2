# Review lane: TB-GERM-HOSTILE-REVIEW — different-model gate on THEOREM TB-GERM

You are the hostile reviewer gating promotion of the charged
TB-G2-FINISH report's THEOREM TB-GERM (its §3): for the (8,6) row
mixed triple covers at g=2, the discriminant of the cubic family
is a perfect cube (t^2 + 108*alpha_3^2*disc(eta') = 16h^3,
h = alpha_2^2 - 3*alpha_1*alpha_3), whence
27*alpha_3^2*U*f = P^2 - 4*sigma^2*h^3 with
P = 27*rho*alpha_3^2 - sigma*t/2, and via h(0,0)=0, smoothness and
L_inf-tangency of {P=0}, and a Weierstrass count:
beta_1 = 8 + 3*kappa with kappa = ord_{P_inf}(h|_{P=0}) odd —
so beta_1 == 2 (mod 3) is necessary.

Review tasks, hostile standard:
(1) §3.1 identities: verify both displayed identities by direct
    computation (sympy available in your sandbox — do the algebra,
    do not eyeball). Check every coefficient.
(2) §3.2 lemmas and §3.3 proof: replay the Weierstrass count and
    the parity claim kappa odd. Hunt specifically for: division by
    quantities not shown nonzero (alpha_3, sigma, U); the
    h(0,0)=0-else-reducible step; whether {P=0} smoothness is
    proved or assumed; whether ord is well-defined if h|_{P=0}
    vanishes identically.
(3) §5 independence claim: the report says TB-GERM reproduces the
    prebuild's TUBE-2 gate E = 3(2-kappa) sharing ONLY SK-5. Audit
    the dependency lists of both chains against the prebuild
    (charged) — if any other shared load-bearing input exists, the
    "two independent chains" corroboration downgrades to one.
(4) §4 witnesses: verify the explicit Phi realizes the A_22 and
    A_28 germs with m=4 as claimed (compute the germ data), since
    the no-local-kill conclusion for (8,6,9)/(8,6,3) rests on it.
(5) §§6-7: check the L_inf crossing constraints and that the
    verdict table follows; check §7.2's claim that (8,6,3) has no
    TB backstop.

Verdict: PROMOTE / PROMOTE-WITH-REPAIRS (list them) / BLOCKED
(name the defect). Cite by section and displayed formula.
Report: `xmodel/tb-germ-hostile-review-gpt55-20260901.md`.
Seal-at-completion contract: skeleton without the marker, bounded
per-section writes, seal at completion. Target 15-25KB.
charged_input=xmodel/tb-g2-finish-opus5-20260901.md
charged_input=xmodel/row-86-prebuild-opus5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
4f464f9c7321501cf0adaacc6ad573212911d41e4589ccf47e834be709b59d6c  {{LANE_INPUTS}}/tb-g2-finish-opus5-20260901.md
7247cef3961576b9919a2ca6e67c484f9f84e6e0af5bca4ceaa353d900bbd4ed  {{LANE_INPUTS}}/row-86-prebuild-opus5-20260901.md
```
