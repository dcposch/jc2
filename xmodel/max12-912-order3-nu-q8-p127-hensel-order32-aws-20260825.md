# Selected-Q8 moving-v Hensel coordinate lift through order 32

Date: 2026-08-25  
Status: **PRODUCER-EXACT FORMAL/MOD-127 CUSTODY; review required**

## Exact result

AWS Box03 (`ip-172-30-0-249`) ran Singular 4.3.2 in

```text
F_127[v,s]/(H(25+s,v),s^32),  s=w-25.
```

The base checks are unchanged and exact:

```text
deg H(25,v)=190
gcd(det(J6),H(25,v))=1
gcd(H_v(25,v),H(25,v))=1.
```

The leading ideal is `(s^32,v^190)`, so the moving quotient has the exact
`6080` standard monomials `s^j*v^i`, `0<=j<32`, `0<=i<190`. Every
coefficient step `1,...,31` completed, and the six original divided quotient
rows, candidate `H`, moving-v relation, and localizer inverse all vanish at
the endpoint (`final_fail=0`).

The run started `2026-08-25T04:26:09Z`, ended
`2026-08-25T04:42:26Z`, and returned rc zero. Wall time was `16:17.41`,
maximum RSS `90,120 KiB`, with no swaps.

## Custody

The producer-source hashes are identical to order 16:

```text
run_moving_remote.sh  80204ac9dd47dbaa8172bad602e5ae049916b904fafec84bcae950b09d6dc268
generate_moving.py    ae3eafd0faa1d36817434cb2cb849a6ee62f4fec7bc8af46a1c3a90643bfff53
generate.py           4d075593a3e4e6566cb68a0fc6accc1cd6cb38e7539ed1829c2558b7e6d4bd2d
shape samples         0790e9f8bb6b545e742ca9e723c29b9a8dc0268a93dedd91c2f2a7b48f48f231
candidate H           9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce
quotient compiler     22b0cdc446d1e486d08757df5a3fff83b0506a492f16b9b2cf238966eb947545
```

Frozen run hashes:

```text
input.sing       db053e1985483dfc752ac6422e194fd927950d15fdd764984aa39d7245302d03
result.out       a2934a4f02f8e5fad42154dcd69a80cb953db8666761945b9282f45326c92eaa
run.meta         665b596463958d57076d43530b738ce396c77bb346eba3195fc0bcbb5fbfeced
stderr.log       7ed3a251468189eb143595b290ecc08a5e8fe6a09f024abfbe66a0ad43b26ab4
generator.stderr e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Scope

This is a formal-local characteristic-127 lift through `s^32`. It is now a
larger exact input to simultaneous Padé/Berlekamp--Massey, but a recurrence is
provisional until held out at orders 64 and above. A global graph requires
exact rational reconstruction and substitution modulo `H` in all original
rows. Quotient-component membership, full Q8 contact limits, the no-merger
checklist, characteristic zero, and any trajectory conclusion remain open.
