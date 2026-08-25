# Pointwise final-G8 and Q6/divided-high gate

The three direct-replayed terminal-row models separate at the first source
row omitted by their parent formula.

| displayed model | final G8 after Q7 | Q6 + R12..R7 |
|:---|:---|:---|
| base 303 / `0102020` | fails by `2*x^8` | not typed after failure |
| base 513 / `0201000` | fails by `2*x^8` | not typed after failure |
| base 519 / `0201020` | passes | rank `(16,17)`, hence inconsistent |

For base 519 the complete 70-by-16 affine system consists of seven Q6 rows
and 63 divided-carry rows in degrees 12 through 7.  Its exact sparse
left-null certificate is

```text
2*Q6[x^4*y^2] + 2*Q6[x^5*y] + R9[x^7*y^2] = 2  in F3,
```

while the same combination annihilates every one of the 16 H7/J7 columns.
The matrix SHA-256 is
`20d945bef43b865be1ccb2b3592af6e82a14e9f3cea4e5029c22bddacb29ccf0`;
the RHS SHA-256 is
`779b2d4f5c575159ac17500a4792ea9f5aad6b52415f99680153f19309e9f0b0`.

Every statement is about the displayed solver representatives only.  The
parent fibres contain other Q9/Q8/Q7 states, and their existence is not
decided here.
