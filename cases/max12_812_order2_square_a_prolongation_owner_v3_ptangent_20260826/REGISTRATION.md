# Registration: moving-`p` tangent addendum to square A-prolongation

Date: 2026-08-26

This nonmutating owner-v3 addendum replaces the fixed base parameter by

```text
p -> p+2*sigma*ell,
L(sigma)=z^2+p/2+sigma*ell.
```

It replays the complete seven loaded source rows through grades fourteen and
fifteen and checks the moving Laurent-to-Faber transform, including the
`2*ell*dT/dp` term.  It must also certify

```text
Num14 == -12*B*A^2                  (mod L),
DeltaNum == 12*ell*B*A^2            (mod L),
DeltaNum == -ell*Num14              (mod L),
Num15moving == -A^3                 (mod L, Num14).
```

Run exact `Q` on Box03 and an independent `F_65521` control on r6d, each
with a 16 GiB VM cap, 600-second compiler cap, and 3600-second engine cap.
Record exact tags, job directories, PIDs, input/output hashes, exit codes,
resource use, and zero-swap state.  This is only the moving-base addendum to
the high-contact cone; it proves neither fan exhaustiveness nor square/order2
closure.
