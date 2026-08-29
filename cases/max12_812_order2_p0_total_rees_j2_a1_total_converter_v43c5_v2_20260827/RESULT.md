# V43C5 V2 result: provisional exact total `a1^628` certificate

## Verdict

`PASS-A1-TOTAL-RAW-CIRCUIT-CERTIFICATE-A1-628-V43C5-V2`.

The frozen AWS replay gives an exact arithmetic-circuit certificate

`a1^628 = sum_j M_j(t,X) R_j(t,X)`

in the ordinary polynomial ring `Q[t,X19_total]`, using 25 of the 59 nonzero
literal total raw ordered-a1 rows through grade 19.  Under the exact ring map
`t |-> rho^2`, this is a certificate in `Q[rho,X19_total]`.  It is stronger
than the requested shape `a1^N(1+rho W)`: here `N=628` and `W=0`.

This is provisional until the separately charged different-model review of
the combined total identity completes.  The V43C4 and V43G4 input identities
are already independently reviewed; their reviews are not being treated as a
review of this converter.

## Exact conversion

The reviewed special certificate is

`x := a1^104 = sum_j C_j R_j(0)`.

Writing `R_j(t)=R_j(0)+t Delta_j` and
`H=-sum_j C_j Delta_j` gives

`sum_j C_j R_j(t)=x-tH`.

Set `y=tH` and `Phi=sum_(k=0)^5 x^(5-k)y^k`.  The reviewed generic identity,
normalized over `Q`, is

`t^6 a1^4 = sum_i (G_i/5)R_i(t)`.

The final multiplier circuit therefore sums exactly to

`a1^4 (x-y)Phi + H^6 t^6 a1^4`
`= a1^4 ((x-y)Phi+y^6)`
`= a1^4 x^6 = a1^628`.

No localization, division by `t`, radical inference, completion, or
probabilistic identity check is used.

## Censuses and controls

The corrected literal corpus has 70 named row slots, 59 nonzero rows, 11 zero
slots, 66 positive variables, 65 rho-zero variables, and the sole general-only
variable `ez9`.  The zero slots are

`Tg10_1,Tg10_2,Tg10_3,Tg10_4,Tg10_5,Tg10_6,Tg10_7,`
`Tg11_4,Tg11_6,Tg12_6,Tg13_6`.

Every named-slot hash, nonzero-row hash, zero-row hash, special fibre, and
exact division by `t` was replayed.  The serialized replay rejected all nine
registered mutations: bridge sign; `1/5` normalization; converter power;
target exponent; deletion of the final `Tg19_7` multiplier; literal generic
and special-row corruptions; zero-row-name deletion; and zero-row-hash
corruption.

## Evidence

- proof circuit: 653,350 bytes, 950 expression nodes, 25 final rows, SHA-256
  `f8426bcf6bb4acbe4a2c12e1897588a7b8ce92bc02da84b7fc02d64d64c145e4`;
- result JSON SHA-256
  `215a64b27e3ea43fd3238158a5e07e686d3de4c7d12ff5bde0e691f916938299`;
- AWS evidence manifest SHA-256
  `c9605ac68895530e6fcd0c1d2b0731e6482cfad89f8eb7bf6415d7c7a1e763d4`;
- immutable AWS source manifest SHA-256
  `50cbf25bd443df66944fe0d704e415d0c38d69de0e4058b352d34b4c6f6f1e87`;
- V2 producer SHA-256
  `d1238596e57adda1d40d07b07ce69943c15a26386bd622cfb72408133087e52c`.

The r6b run ended `rc=0` after 239.10 seconds, at 153,180 KiB maximum RSS,
one core, and zero swap.

## Firewall

This certificate concerns only the frozen literal total raw ordered-a1
grade-through-19 ideal.  It does not by itself prove source reachability,
provide a terminal-receiver chain map, identify this ideal with normalized
K00, or prove the order-two/maximum-twelve/JC2 theorem.
