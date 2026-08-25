# AS F-only `D=7`: source-corrected degree-ten carry census

**Status: PRODUCER EXACT; PROVISIONAL PENDING INDEPENDENT SOURCE/RESULT
REVIEW.**

## Headline

The source-corrected top-three next-residual rows do not obstruct the finite
vertical branch.  A source-frozen 27-way exact F3 census on AWS gives

```text
visible predecessor states                       1,085,103
states satisfying N12={C7,D7}=0                    629,115
states satisfying corrected Q11=0                  260,847
states satisfying corrected Q10=0                   33,225
degree-six current-digit spectator completions   24,221,025.       (1)
```

The last number is exactly `729*33225`.  Only 159 of the 2,187 structural
bases retain a visible state after `Q10`, so the row is a strong shrink but
not a finite obstruction.

## 1. Exact source row

Split the first digit as `U=U0+UF,V=V0+VF`, where `UF,VF` are its
homogeneous degree-six Frobenius parts.  The full integer determinant
filtration gives

```text
Q10 = {C7,D5}+{C6,D6}+{C5,D7}
      + ({UF,D6}+{C6,VF})/3
      + {UF,VF}/9                                  mod 3.           (2)
```

The first line is the pure current-digit bracket.  In the second line,
integer derivatives of `UF,VF` supply the displayed factors of three; the
double-Frobenius bracket is divisible by nine.  The exact source audit
proves that both divided terms are nonzero in general and pins their signs.
In particular,

```text
{UF,VF}/9 mod 3
 = (2 fa fc+fua fd) x^2 y^8
 + (fb fc+2 fua fvb) x^5 y^5
 + (2 fb fd+fa fvb) x^8 y^2.                      (3)
```

The compiler constructs (2) from the already divided integer derivatives,
asserts (3) literally, and tests all eleven bidegree coefficients.  It also
asserts that the six homogeneous degree-six Frobenius coefficients of the
*current* digit remain absent: their derivatives retain an extra factor of
three in (2).  Those six directions therefore contribute exactly `3^6`
spectator completions per visible survivor.

Every solution of the frozen predecessor affine system is reconstructed
and tested in order. There is no random sampling, reduced-component
extrapolation, or source-incomplete pure-N replacement.

## 2. Exact partition and certificate

The 2,187 structural bases are ordered lexicographically and partitioned
into 27 contiguous intervals of 81.  The full aggregate histograms are

```text
N12 survivors per base:
  0^1804, 3^116, 6^24, 9^32, 18^4, 27^32, 54^62, 81^12,
  108^22, 162^14, 243^48, 486^2, 2187^10, 6561^2,
  19683^2, 531441^1;

corrected-Q11 survivors per base:
  0^1916, 3^132, 9^4, 27^114, 81^6, 243^4,
  2187^6, 6561^2, 19683^2, 190269^1;

corrected-Q10 survivors per base:
  0^2028, 1^96, 27^42, 81^6, 162^4,
  2187^8, 2349^2, 8667^1.                         (4)
```

The ordered 27-leaf binary Merkle certificate is

```text
def726e4f15602f66f99c600c068d588771e50521d92172e4cebd907e023f5b9. (5)
```

Every leaf-output SHA-256 is printed in the frozen aggregate.  The aggregate
output itself has SHA-256

```text
a9621b0716a2f0d76f79ee0ee235cc33d743ef74af8d91052eec0ea21c1583dd. (6)
```

## 3. Source and remote provenance

Before launch, Box02 verified the transported archive, full transitive
source closure, runner manifest, and the exact-integer divided-Frobenius
source replay.  The latter reproduced the frozen output SHA-256
`5147309670dc3e0d7caaadc93ddf2a08c1c1b97e57cbf182bae6d40fbed123fd`.

```text
transported source archive SHA-256
  7d8811ea7748b8030e21744ef47683e6ba07394f17ca6218a664a47b3c2bc0db
compiler SHA-256
  3837508e6f0ffabbcdecfdc19a9ade1e4068bbece6aba80cfdc6b9937e25a686
runner manifest SHA-256
  b030858e63fe8feae0fc154dac2d5f4b74e1a8a6c240ec31538705e06131f009
source-closure manifest SHA-256
  01273d08ff570fb45c043d3707aa57209f7344a5ee7d749641a79adc24cc7849
source FREEZE SHA-256
  20533de92fb88cd752c29ace7d0350269acbb11e906f39b889491d8463cfc6ec. (7)
```

Execution metadata:

```text
host: Box02, ip-172-30-0-186 (34.203.207.55)
tag: as_d7_corrected_q10_20260825T005148Z
UTC: 2026-08-25T00:53:16Z--00:55:33Z
overall/aggregate rc: 0/0
per-shard cap: one CPU, 8 GiB VM, 12 hours
observed peak RSS: about 21 MB
longest shard: 2:17.63; other shards: about 12--15 seconds.       (8)
```

Source and runner checks passed, the source-audit and aggregate stderr files
are empty, and the transported remote-results archive has SHA-256

```text
e7c943f64de3b9a8d6a8540e9d6110c474d96ccfa9443e98882250dd6c85a526. (9)
```

## 4. Evidence tier and refusal scope

This is an exact aggregate-count/Merkle producer.  Its shards are parallel
partitions of one implementation, not independent mathematical reviews.
Promotion requires independent source/result review.

The result licenses only survival through source-corrected total degrees
twelve, eleven, and ten of this finite branch.  Degree nine is not merely
the next pure bracket row: it also contains the quotient residual and the
first-/next-digit cross.  Its construction requires explicit integer-carry
provenance and a proof that the recorded predecessor state is sufficient.
That source gate remains open.  Lower rows and later Cartier tests also
remain open.  There is no recurrence, all-depth lift/no-lift,
characteristic-zero, counterexample, or JC2 conclusion.
