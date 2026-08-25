# Max12 `(9,12)` corrected-Q8 `(w,v)` support checkpoint

Date: 2026-08-25  
Status: **producer-exact finite-box certificate; support evidence only**

## Exact result

On the selected corrected-Q8 formal branch at the good reduction

```text
ell=10007,       v(0)=980,       det(J_6)=2820 != 0 mod ell,
```

the exact Hensel series were lifted through order 191.  With

```text
v=(x3-2*x5)/x5,
```

every rectangular monomial matrix for `(w,v)` and `(theta,v)` with

```text
1 <= d_left <= 24,       1 <= d_right <= 16,
(d_left+1)*(d_right+1) <= 176
```

has full column rank on the first 176 coefficients.  There are 279 tested
rectangles per pair, hence 558 full-column-rank matrices.  The last 16 series
coefficients were reserved as holdout, but no fit nullity produced a
candidate.  The common tested-rectangle hash is

```text
53e58cd468b83d6cc26308f659ae37085154fcbad430cfb1998257a280246f6b.
```

The AWS lane `q8_wv_support_p10007_v1` ran on `ip-172-30-0-45` from
`2026-08-25T01:28:49Z` to `01:30:18Z`, returned zero, and had empty worker
and supervisor stderr.  The result SHA-256 is

```text
1e3e81739f214b37bd81bad378167baafd48d51a5691ef0dcf3f5af2e4fb8c31.
```

## Scope

One good reduction exactly excludes a nonzero rational-coefficient polynomial
relation whose rectangular support lies in the displayed box, by primitive
integer reduction and the unit Hensel Jacobian.  This does not exclude sparse
relations outside the rectangles, algebraic-coefficient relations, rational
relations with denominators, a high-degree plane equation, or a global
component relation.  It supplies no normalization, genus, trajectory,
maximum-twelve, counterexample, or JC2 conclusion.

The negative result reinforces the reviewed local conclusion that the Taylor
coordinates are freely varying to substantial order.  It lowers the expected
gain of further blind support expansion: component grouping and projective
boundary remain the decisive gates.

## Custody and replay

The portable case is

```text
cases/max12_912_order3_nu_q8_wv_support_aws_20260825/
```

with source hashes

```text
wv_support.py   22a2c8f651032c6aa3e9720a9c5a7ae880017b7b1289bbb47e8ebad4469affd3
run_remote.sh   82cf839dfb3d3c8747776aa412fefafcca716fc07f52f0faccf5b3d720356edd
parent worker   c36d6cf1ca538a39923412075fb44be77ed30023107f4eac755722b7d796dea0
```

The local audit is deliberately lightweight:

```sh
python3 cases/max12_912_order3_nu_q8_wv_support_aws_20260825/audit.py
```

It checks every harvested/source hash, AWS metadata, good-reduction fields,
and reconstructs the 279-rectangle set and hash.  The substantive exact
Hensel/rank computation remains AWS-only under the standing compute policy.
