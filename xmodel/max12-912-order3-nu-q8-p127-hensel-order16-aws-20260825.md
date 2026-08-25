# Selected-Q8 moving-v Hensel coordinate lift through order 16

Date: 2026-08-25  
Status: **PRODUCER-EXACT FORMAL/MOD-127 CUSTODY; review required**

## Exact result

On AWS r6d (`ip-172-30-0-45`), Singular 4.3.2 reconstructed the six selected
quotient coordinates

```text
(c,d2,d4,x1,x3,x5)
```

and the localization inverse in

```text
F_127[v,s]/(H(25+s,v),s^16),  s=w-25.
```

The run proves within this truncated algebra:

- the base fibre has `deg_v H(25,v)=190`;
- `gcd(det(J6),H(25,v))=gcd(H_v(25,v),H(25,v))=1`;
- the moving standard monomials are exactly `v^i*s^j` for
  `0<=i<190`, `0<=j<16`, hence quotient dimension `3040`;
- all coefficient corrections `1,...,15` completed;
- the six original divided quotient rows, the candidate `H` relation, the
  moving-v relation, and the localizer inverse all reduce to zero
  (`final_fail=0`).

This independently extends the already-passing order-eight checkpoint. It
supports higher-order simultaneous rational reconstruction, but is not such
a reconstruction itself.

## Source and AWS custody

The run started `2026-08-25T04:26:09Z` and ended
`2026-08-25T04:29:57Z`, rc zero. Wall time was `3:48.39`; maximum RSS was
`55,908 KiB`; no swaps occurred.

Pinned producer sources:

```text
run_moving_remote.sh  80204ac9dd47dbaa8172bad602e5ae049916b904fafec84bcae950b09d6dc268
generate_moving.py    ae3eafd0faa1d36817434cb2cb849a6ee62f4fec7bc8af46a1c3a90643bfff53
generate.py           4d075593a3e4e6566cb68a0fc6accc1cd6cb38e7539ed1829c2558b7e6d4bd2d
shape samples         0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231
candidate H           9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce
quotient compiler     22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545
```

Frozen run artifacts:

```text
input.sing       518d9c643009dcb1df8651e687fe8d869d7bc04f21c6902041f62155d3e99f62
result.out       d4a00d5f5922022fa6de0e2e32398e923128b297100a37e1b688f067b4bfc1cb
run.meta         b1f91f21b45c50992550cb33231411b1de8fce7f81793f2fdf81c4229dbb5697
stderr.log       23a57f40539d29f12f00bccc5e662715b5698f05066d34b04dfb7e6c2c2d260b
generator.stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

The lightweight verifier checks every hash, endpoint, leading monomial,
coefficient step, final row, and resource sentinel.

## Scope firewall

This is an exact formal-local statement over `F_127` through `s^16`. It does
not prove that the seven series are rational functions on `H`, that `H` is a
component of the original quotient, that full Q8 contact limits exist, that
the characteristic-zero branches do not merge modulo 127, or that any Keller
trajectory exists or is excluded. Acceptance of a global graph requires a
common-denominator reconstruction followed by exact substitution modulo `H`
in every original row. The separate six-item no-merger checklist remains
fully charged.
