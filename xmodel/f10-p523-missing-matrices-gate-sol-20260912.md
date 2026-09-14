# p=523 missing determinant matrices — independent Sol gate

- First action: `2026-09-12T04:37:31.877112776Z`.
- Basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
- Scope: model-side manual reconstruction of h2,h3,h5,h6 all columns and h4 columns A=1,T; full M2–M6 and determinants; h5/h6 source inverse identities.
- No local arithmetic/scientific execution, import, AST, syntax, test, CAS, dummy, fixture, payload, network, AWS, SSH, Git, process, or protected-tree action.

## Status

Transactional skeleton opened without completion marker; all three inputs hash-pinned before fresh reads.

## 1. Literal reconstruction setup

Work throughout in `F_523`. I use only the charged leading inputs

`C=T^3+381T+381`, `D=T^5+T^3+159T^2+6T+465`.

The producer literally defines

`O_h(A,B)=10CB'-(17-h)C'B+(10-h)AD'-17A'D`.

Write `k=17-h`, `s=10-h`, `B=sum_{j=0}^4 b_jT^j`, and `E=sAD'-17A'D-target`. Extracting degrees 6 down to 2 in `O_h-target` gives, with absent coefficients zero,

`q_j=10j-3k`,

`q_{n-2} b_{n-2} = -[E_n+381(10n-k)b_n+(3810 mod 523)(n+1)b_{n+1}]`, `n=6,...,2`.

This is the producer's descending `upper` loop reconstructed coefficientwise, not a determinant evaluated on a supplied matrix. The low output rows and third row are

`r1=E1+381(10-k)b1+298b2`, `r0=E0-k*381*b0+149b1`, `rho=149b0-17*465*A0`.

The source target is zero except at `(h,A)=(4,T^2)`, where it is `-2T^6`; hence that case has `E6=5s-34+2`. The remaining nonzero `E` coefficients are:

- `A=1`: `E4=5s,E2=3s,E1=318s,E0=6s`.
- `A=T`: `E5=5s-17,E3=3s-17,E2=(2s-17)159,E1=6(s-17),E0=-17*465`.
- `A=T^2`: `E6=5s-34+2[h=4],E4=3s-34,E3=(2s-34)159,E2=6(s-34),E1=-34*465`.

## 2. Complete fifteen-column upper table

Each `b` entry is `(b0,b1,b2,b3,b4)`. `q*b` lists, in descending coefficient order, the five independently reduced left sides `(q4b4,q3b3,q2b2,q1b1,q0b0)`; direct substitution in the bracket above gives the same residues. `col` is `(r1,r0,rho)` recomputed from the low formulas.

|h|A|b|q*b mod523|col|
|---:|---|---|---|---|
|2|1|(138,0,420,0,0)|(0,0,483,0,66)|(92,62,105)|
|2|T|(107,400,0,141,0)|(0,500,0,121,415)|(480,323,253)|
|2|T²|(88,112,143,0,315)|(517,0,86,264,224)|(155,158,37)|
|3|1|(515,0,168,0,0)|(0,0,488,0,336)|(513,351,317)|
|3|T|(98,482,0,263,0)|(0,505,0,266,68)|(187,375,481)|
|3|T²|(216,8,177,0,262)|(522,0,290,267,342)|(163,171,281)|
|4|1|(335,0,442,0,0)|(0,0,493,0,10)|(259,260,170)|
|4|T|(470,509,0,292,0)|(0,510,0,406,498)|(246,432,471)|
|4|T²|(446,191,36,0,2)|(2,0,362,214,388)|(449,331,33)|
|5|1|(416,0,165,0,0)|(0,0,498,0,191)|(29,229,210)|
|5|T|(436,70,0,350,0)|(0,515,0,272,517)|(457,194,112)|
|5|T²|(83,287,453,0,133)|(9,0,74,383,150)|(383,99,338)|
|6|1|(248,0,82,0,0)|(0,0,503,0,184)|(81,380,282)|
|6|T|(303,360,0,1,0)|(0,520,0,88,461)|(311,205,169)|
|6|T²|(263,54,451,0,2)|(14,0,413,327,212)|(213,452,485)|

Representative integer reductions covering every arithmetic pattern are:

- h2,T²: `(-5)315=-1575=-3*523-6`, `(-25)143=-3575=-7*523+86`, `(-35)112=-3920=-8*523+264`, `(-45)88=-3960=-8*523+224`.
- h3,T: `(-12)263=-3156=-7*523+505`, `(-32)482=-15424=-30*523+266`, `(-42)98=-4116=-8*523+68`.
- h4,T²: `1*2=2`, `(-19)36=-684=-2*523+362`, `(-29)191=-5539=-11*523+214`, `(-39)446=-17394=-34*523+388`.
- h5,T²: `4*133=532=523+9`, `(-16)453=-7248=-14*523+74`, `(-26)287=-7462=-15*523+383`, `(-36)83=-2988=-6*523+150`.
- h6,T²: `7*2=14`, `(-13)451=-5863=-12*523+413`, `(-23)54=-1242=-3*523+327`, `(-33)263=-8679=-17*523+212`.

Low-row samples cross the independent stages: h2,T² has `r1=403+187*112+298*143=155`, `r0=-485*88+149*112=158`, `rho=149*88=37`; h5,T has `r1=451+284*70=457`, `r0=463-388*436+149*70=194`, `rho=149*436=112`; h6,T² has `r1=403+142*54+298*451=213`, `r0=-7*263+149*54=452`, `rho=149*263=485`, all modulo 523.

## 3. Reconstructed matrices and five determinants

Rows are exactly `(r1,r0,rho)` and columns exactly `(1,T,T²)`, as in the producer's `matrix = [[columns[j][i]...]]` transpose:

```
M2 = [[ 92,480,155],[ 62,323,158],[105,253, 37]]
M3 = [[513,187,163],[351,375,171],[317,481,281]]
M4 = [[259,246,449],[260,432,331],[170,471, 33]]
M5 = [[ 29,457,383],[229,194, 99],[210,112,338]]
M6 = [[ 81,311,213],[380,205,452],[282,169,485]]
```

For each matrix I independently formed the unsigned first-row minors `(m11,m12,m13)` and used `det=M11*m11-M12*m12+M13*m13`. The unreduced minor differences and determinant expansions are:

|h|minor integer differences|reduced minors|determinant integer reduction|
|---:|---|---|---|
|2|`11951-39974; 2294-16590; 15686-33915`|`(219,348,76)`|`92*219-480*348+155*76=-135112=-259*523+345`|
|3|`105375-82251; 98631-54207; 168831-118875`|`(112,492,271)`|`513*112-187*492+163*271=9625=18*523+211`|
|4|`14256-155901; 8580-56270; 122460-73440`|`(88,426,381)`|`259*88-246*426+449*381=89065=170*523+155`|
|5|`65572-11088; 77402-20790; 25648-40740`|`(92,128,75)`|`29*92-457*128+383*75=-27103=-52*523+93`|
|6|`99425-76388; 184300-127464; 64220-57810`|`(25,352,134)`|`81*25-311*352+213*134=-78905=-151*523+68`|

Thus the requested determinants are `(345,211,155,93,68)`, all nonzero. Independent unit witnesses are `345*285=98325=188*523+1`, `211*233=49163=94*523+1`, `155*27=4185=8*523+1`, `93*45=4185=8*523+1`, and `68*100=6800=13*523+1`.

## 4. Source inverse[2][2] identities for h5,h6

The arithmetic source's `invert_matrix` contract is the ordinary inverse, so entry `[2][2]` is the top-left 2x2 cofactor times the determinant inverse. I reconstructed both cofactors from the matrices:

- h5: `29*194-457*229=-99027=-190*523+343`; hence `inverse[2][2]=45*343=15435=29*523+268`. The producer's literal ratio is `(3(5-3)-2)/(27-5)=2/11`. The charged `H7_5=428` and `11^-1=428` give `2*428*428=366368=700*523+268`.
- h6: `81*205-311*380=-101575=-195*523+410`; hence `inverse[2][2]=100*410=41000=78*523+206`. The literal ratio is `(3(6-3)-2)/(27-6)=7/21=1/3`; with `H7_6=95` and `3^-1=349`, `95*349=33155=63*523+206`.

Both source-specific equalities hold without assuming either residue from an inverse array.

## 5. Required negative control

If the h4,T² target is wrongly set to zero, `E6=-4` rather than `-2`. The same upper solve yields

`b=(18,178,238,0,4)`, with pivot products `(4,0,185,68,344)`, instead of `(446,191,36,0,2)`. Its low column is `(192,128,67)`, not `(449,331,33)`. Holding the independently reconstructed first two h4 columns fixed gives wrong-target determinant

`259*36-246*367+192*381=-7806=-15*523+39`,

not 155. The control detects the exact source attachment even though the wrong determinant also happens to be nonzero.

## 6. Verdict, scope, and controls

**CONFIRMED** for the exact requested attachment: starting from the literal charged `O_h`, descending solve, h4 target, row order, and column order, the independently reconstructed M2–M6 determinants are respectively `345,211,155,93,68`; the h5/h6 `inverse[2][2]` source identities are `268=268` and `206=206`. All five determinant nodes are units, with the explicit inverse products above.

This confirms only these five fixed-place source matrix attachments. The charged leading C,D and named initial/late scalar checks were treated as inputs and not rederived. No degree, full-place, rank, full-source execution, source exclusion, all-r, characteristic-zero, or JC2 claim follows. Fable's M1/h4-third work was not read; h4 third was independently reconstructed here because the complete M4 determinant requires it.

The three inputs were hash-pinned before fresh WHOLE inert reads. `produce.py` was read lines 1–369; `arithmetic.py` lines 1–350, with 240–350 explicitly recovered; the Astra report lines 1–249 was read as advisory and its requested values were not used as premises. Post-read hashes are required unchanged in `PINS.json`/custody.

Manual controls included all fifteen upper-polynomial pivot products, all fifteen low columns, five three-minor determinant expansions, five scalar inverse products, two source-specific cofactor identities, and the wrong-h4-target mutation. No local/scientific subprocess, arithmetic implementation, Python/JS/CAS/import/AST/syntax/test/dummy/fixture/payload, SSH/AWS/network/Git/process/protected-tree action occurred. No code or shared ledger was edited.

QUANTITY: 15 basis columns, five 3x3 matrices/determinants, five determinant inverses, two source inverse-entry identities, one negative target mutation. All are decided in this exact scope; no GAP remains within it.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8450`.
- Body SHA-256:
  `432fc6a2639a4e5e4a6e30f403a6bb68fe108c462c76e45917e30a870d2d2506`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
