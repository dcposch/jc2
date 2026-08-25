# V54D canonical reverse first-stage denominator diagnostic

V54B completed the six-row reverse/deferred fraction-free diagnostic but
wrote two artifacts with Python object-address representations.  Its stdout
algebra is retained only as diagnostic evidence.  V54C then reached the same
six exact rows but failed only while calling the canonical serializer through
the wrong module namespace.  V54D fixes that one reporter call and writes the
canonical `E(C,V,U)[beta]` representation supplied by the pinned N13 parent.

V54D additionally asserts the ordered center-ring coefficient denominators

```text
U^4 H, U^4 H, U^5, U^4 H^2, U^3 H^4, H^8
```

and their common denominator `U H^8`.  These assertions concern denominator
support only.  The beta-dependent pivot product remains a nonunit defining
one reverse chart and is never inverted or treated as a cover.

AWS replay:

```sh
sha256sum -c SOURCE.sha256
sha256sum -c V54D_SOURCE.sha256
mkdir -p artifacts
TD6_OUTPUT_DIR="$PWD/artifacts" ./run_v54d.sh \
  > v54d.stdout 2> v54d.stderr
```

The only success marker is
`TD6-A3-Q2-REVERSE-DENOMINATOR-V54D PASS`.  Promotion also requires both
saved pivot artifacts to be address-free and byte-identical on an independent
AWS replay.  This is not a full V50 source identity, generic-open cover,
fixed-A3 kill, TD6 theorem, SP-2 theorem, or JC2 result.
