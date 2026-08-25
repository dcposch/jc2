# Scope erratum — AS F-only `D=7` raw-Q7 13-trit chart

**Status: EXACT WORDING/PROVENANCE CORRECTION; frozen producer bytes are
unchanged.**

This note narrows every unqualified occurrence of “complete accepted chart”
in `as-fonly-d7-global-chart-rawq7-exclusion-20260825.md` (report SHA-256
`839bbdd0eba339d46b867a45d69a160987148695d9f1a1e584bba3331d4208fa`).

The exact object excluded there is the complete displayed **13-trit
Q8-compatible chart over the first emitted Q9-compatible corrected-Q10
predecessor**.  In the frozen predecessor ordering

```text
(Pp,Qq,Rr,Tt,s,w,h,
 fua,fa,fb,fc,fd,fvb,
 d7_1,d7_4,d7_7,d6_1,d6_4,
 c5_0,c5_1,c5_2,c5_3,c5_4,c5_5,
 d5_0,d5_1,d5_2,d5_3,d5_4,d5_5),
```

that predecessor is `c5_5=2` and every other coordinate is zero.  The
13-trit chart is the locus

```text
t10=t11=t12=t13=t15=0,  t17=1
```

inside this predecessor's 19-dimensional Q9 affine fibre.  The checked
raw-Q7 formula exhausts all Q8 and Q7 digits over this chart, but it does
not quantify over the other six Q9 directions or over a different
corrected-Q10 predecessor.

Accordingly, the frozen theorem kills one complete 13-dimensional chart,
not all 11,881 Q9-compatible predecessor states and not even, by itself,
the complete 19-dimensional Q9 fibre over the first predecessor.  The other
11,880 compatible predecessors (spread over 79 structural bases before
removing the first point), the separate `a`/`g` endpoint families, and other
associated-top branches remain outside its scope.

The nonblocking 19-direction successor is a separate producer and must not
be used retroactively to enlarge this theorem.  No count, source row,
formula byte, SAT control, CNF, DRAT trace, or proof-check outcome in the
frozen package changes.

