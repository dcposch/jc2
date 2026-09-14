# Round 2 numerical audit of the labelled descent

Fresh execution: `python3 box/ctop-gate-20260905/r2-enum-audit.py > box/ctop-gate-20260905/r2-enum-audit.log`.
Runtime 22.484 seconds. Artifacts: `r2-enum-audit.py`, `r2-enum-audit.json`,
`r2-enum-audit.log`. This is an arithmetic/census audit, not a proof that any
formal descended label is the characteristic datum of an actual pair.

## Inputs and independence

The root mechanically verified the seven charged input hashes before this task.
This executable imports the exact frozen enumerator
`/tmp/jc2-lane.yqyWvI/inputs/moh_skeleton_full.py`, SHA-256
`d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2`.
It imports the campaign operative `Tree` from
`box/centre-gate-20260903/opus5_probe.py`, SHA-256
`4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9`.
An assertion checks that the tree's `B` import resolves to the charged frozen
enumerator, not its adjacent copy. Python bytecode writes are disabled.

The enumerator is run afresh at every degree 16 through 200, with `Kmin=2` and
`full=True`. The operative tree uses `gate=False`, `ode=True`, `capacity=False`,
`passport=False`, `recenter=True`. Its `embeds(V)` is the same operative predicate
as `scope_enum.operative`: both initialize `_memo`, demand
`d_s > V_s > d_s/2`, and invoke `ok(s-1,(V_s,),True,(V_{s-1},...,V_2))`.
This audit reuses the authorized operative screen, not its cached row list.

Child labels are rebuilt using exact `Fraction(u_s,d_s)` multiplication and
independent prefix gcds (`reduce(gcd,[n,*M[:i]])` for each prefix). No banked
`descend()` or previous replay function is called. Every parent is separately
checked by `windows_ok()` and `full_ok()`. The replay JSON is loaded only after
fresh regeneration. All **1,420 operative row dictionaries**, including every
raw/effective vector and predicate, match the charged replay exactly. The
complete census and operative summary dictionaries also match exactly. Charged
replay SHA-256 is
`3123aa9992ec170d1e38404761ade428e8bf7105c04f532c95b8fb90bf5a811e`.

## Counts reproduced

| Quantity | Count |
|---|---:|
| Frozen (1)-(13) census | 24,063 |
| Operative tree residue | 1,420 |
| Operative `u_s=1` | 1,110 |
| Raw labelled C-TOP failures on `u_s=1` | 970 |
| Effective labelled C-TOP failures on `u_s=1` | 936 |
| Effective labelled C-TOP survivors on `u_s=1` | 174 |
| Operative `u_s>=2` | 310 |
| C-TOP-only formal residual | 484 |

The operative `u_s` histogram is `{1:1110,2:265,3:34,4:9,5:2}`. Raw heights
are `{2:43,3:414,4:797,5:166}`; effective heights are
`{2:67,3:426,4:791,5:136}`. The 174 labelled survivors occupy 46 parent degree
pairs. Their **raw** height histogram is `{2:24,3:100,4:41,5:9}`, the histogram
printed in the charged report. Their **effective** height histogram is
`{2:48,3:86,4:31,5:9}`. The 936 failures by effective height are
`{3:244,4:565,5:127}`. No effective-height-2 `u_s=1` operative row fails.

The 310 `u_s>=2` rows include 225 numerical C-TOP failures, left unlicensed by
the charged report. There are 90 labelled U-NEG rows: 84 with `u_s=1`, all among
the 936 C-TOP failures, and six with `u_s>=2`. Thus **if both proposed licences
were valid**, their joint formal residue would be `1420-936-6=478`; 484 is the
C-TOP-only residual, not the result of applying both kills.

## Gcd derivation and index correction

Put `q=d_s` and write `a_0=n/q`, `a_i=M_i/q` for `1<=i<s`. These are integers
and `gcd(a_0,...,a_{s-1})=1` by the definition of `d_s`. The raw child labels are
`n'=u_s*a_0`, `M'_i=u_s*a_i`. Therefore

```
gcd(n',M'_1,...,M'_{s-1})
  = u_s*gcd(a_0,...,a_{s-1}) = u_s.
```

More generally every raw prefix gcd scales by `u_s/q`. All prefix identities
were checked directly on all 24,063 census rows. This proves an identity of
integer labels; deciding whether the labelled support entries are precisely
the successive first nondivisible exponents of a child's own expansion requires
the separate mathematical identification sought by the user.

There are exactly **90 operative rows** with raw terminal `M'_{s-1}=n'-1`.
Every one has `u_s=1`. Deleting that one terminal entry, its `V` entry, and
resetting the conventional next `V` to the new terminal `d`, yields the 936
effective failures. All 90 fail the raw comparison; 34 pass after the drop and
56 still fail. The two 90-row sets (dropped tail and U-NEG) are disjoint.

For every dropped row, the **raw** terminal gcd is 1 and the **effective**
terminal gcd is strictly greater than 1. Hence the charged prose
`d'_{s'+1}=u_s=1` is not true if `s'` is simultaneously the post-drop effective
height. It is correct for raw `s'=s-1`. After the drop one needs p.174 to remove
the genuine terminal pair and then uses Def 5.1's top convention with the
remaining gcd, which need not be 1. This is an indexing correction, independent
of the unsettled child-data identification.

The campaign already keeps two implementations: `scope_enum.py:37` returns
raw `sp=s-1` and `Vp=V[2:s]` without dropping; `depth.py:48` explicitly drops
terminal `n'-1`, decrements `sp`, and overwrites `Vp[sp+1]=dp[sp+1]`.
Consequently the printed 936 count is consistent with `depth.child`, while the
charged live-height histogram is inherited from the raw enumerator. There is
no 936/174/310 numerical discrepancy after the distinction is made explicit.

## Controls and exact examples

At parent `(96,72)`, full `M=(-72,36,78,94)`, the operative census has three
`V=(V_2,V_3,V_4)` assignments: `(1,1,5)`, `(1,3,5)`, `(4,3,5)`. Each descends
formally to `(n',m')=(16,12)`, `M'=(-12,6,13)`, `d'=(16,4,2,1)`, with no tail
drop. Their copied `V'` are `(1,1)`, `(1,3)`, `(4,3)`. The first passes C-TOP;
the latter two fail `3<=2`. All three were explicitly asserted in the test.
The last is the user's proposed first-principles witness. The enumeration
establishes that the row exists and its labels have the stated values; it does
not construct a child expansion or decide impossibility.

A dropped-tail rescue is parent `(108,72)`,
`M=(-72,84,104,106)`, `V=(8,8,3)`, `u_s=1`. Raw child:
`(27,18)`, `M'=(-18,21,26)`, `d'=(27,9,3,1)`, `V'=(8,8)`.
Raw C-TOP fails `8<=3`. Dropping `26=27-1` gives effective
`M'=(-18,21)`, `d'=(27,9,3)`, `V'_2=8`, and conventional `V'_3=d'_3=3`.
Effective C-TOP passes `8<=9`. This explicitly disproves the claim that the
effective terminal gcd is 1 on all `u_s=1` rows.

A dropped-tail row still labelled failing is parent `(144,96)`,
`M=(-96,-16,72,140,142)`, `V=(1,10,5,3)`. Raw child:
`(36,24)`, `M'=(-24,-4,18,35)`, `d'=(36,12,4,2,1)`, `V'=(1,10,5)`.
After dropping `35=36-1`, effective `M'=(-24,-4,18)`,
`d'=(36,12,4,2)`, `V'=(1,10)`; effective comparison `10<=4` still fails.

All five `u_s=1` rows from the frozen Moh table pass the formal screen. The
labelled root-count identity `(n'/gcd(n',m'))*V_2 > n'` iff
`V_2>gcd(n',m')` passes on all 1,420 operative rows. This last equivalence is
pure arithmetic and supplies no disc centre/radius identification.

No ledger, `jc2-lean`, `ideation-*`, prior artifact, or charged input was edited.
