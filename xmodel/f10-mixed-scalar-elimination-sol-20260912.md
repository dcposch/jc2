# F10 mixed-scalar uniform elimination source packet

Status: `SOURCE-COMPLETE / UNEXECUTED / INTERNAL-UNREVIEWED / DISABLED`.

I implemented one uniform-parameter experiment over `Q(nu)`, not an r/prime
farm. `eliminate.sing` derives `d5,d6,d7` and `B(nu,X,Y)` from the stipulated
truncated-power formula, computes a standard basis of
`(d6,d7,B,z*Y*d5-1)`, and, only if it is the unit ideal, retains a lifted
cofactor identity after multiplying by every coefficient denominator
`N(nu)`. `check-certificate.sing` independently reconstructs the polynomials,
checks the cleared identity, factors `N`, records its exact exceptional
parameters, and rejects any root arising from an integer `r>=2`.

The coefficient recurrence used in both sources is obtained by comparing the
`u^(k-1)` coefficient in `phi*T'=s*phi'*T`:

`k*t_k(s) = sum_{j=1..min(3,k)} (((s+1)j-k) phi_j t_{k-j}(s))`,

with `(phi_1,phi_2,phi_3)=(1,X,Y)` and `t_0=1`. Thus the emitted coefficients
are exact finite coefficients of the required truncations through 7, not an
assumed matrix. Formal inversion of `phi` through degree 14 then forms exactly
`[u^14](phi'/phi)T_(2nu-1)T_(4-nu)`. No forcing attachment is assumed.

The specialization logic is deliberately two-stage. A unit ideal over
`Q(nu)` is only generic. The certificate proves
`A1*d6+A2*d7+A3*B+A4*(zYd5-1)=N(nu)`; it gives actual-r unitness only after
the exact checker proves `N((5r+2)/(3r+1)) != 0` for every integer `r>=2`.
Factoring over `Q[nu]` makes this finite: nonlinear irreducible factors have no
rational root, and each linear root is tested using
`r=(2-nu)/(3nu-5)`. The excluded `nu=5/3` cube control remains explicit. No
claim is made that `N` is nonzero at every real point of the interval; that
stronger sufficient predicate is unnecessary for the discrete family.

The packet also includes a disabled binding template whose Linux/EC2/UID and
source-pin checks precede `exec` of Singular, plus a concrete contract. The
proposed but unexecuted envelope is one AWS process group, wall 3600s, CPU
3300s, memory 34359738368 bytes, output 268435456 bytes. ROOT must select a
reviewer, bind genuine registration/source/native pins, and authorize any
fresh AWS run under independently reviewed cap and cleanup machinery.

No source, checker, CAS, import, syntax test, dummy, fixture, worker, network,
or protected tree was executed or accessed. Generic nonunit/timeout, lift or
identity failure, or an actual-r denominator exception remains honest `GAP`;
none supplies a source point. Even a complete unit result would not establish
the unreviewed forcing attachment, REG, source zero, all F10, or JC2.

First action `2026-09-12T18:42:57.157888897Z`; original reserve
`2026-09-12T19:00:00Z`, HARD `2026-09-12T19:03:00Z`, never reset. Basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`. Exactly the three named inputs
were hash-pinned then freshly read WHOLE; no linked bodies or peer output were
consumed. This is source preparation only and grants no compute authority.

Frozen source pins: `eliminate.sing`
`8b8e8541141ee6a863b3fe97c09eb705431fb34ba1df9abd62dce36c5a7553ec`;
`check-certificate.sing`
`27383b9d9c819639b1115d3129834caa193da6642c75cc17699ff5d9a157b742`;
`run-aws.template.sh`
`bcdb4c6e765c66c8e2698a5f6d2fe7209deb9c32f5e30c2bc17b208ac056d4be`;
`CONTRACT.md`
`ddac6d970539b8b0c8e13d7ba6fb5d8f6573713e1ab8b69d0cc599bd0b8905e0`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3397`.
- Body SHA-256:
  `b84133586e7b3e02cf0a29129f05daa092b8eeec1f5a80fe0276f026c581cd30`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
