# Q8-contact Galois-primitivity gate (AWS-only replay)

This bounded exact replay factors the corrected squarefree octic `Q8` modulo
good primes.  It searches for certified Frobenius patterns `[8]` and `[1,7]`.
The first proves irreducibility over `Q`; the second supplies a seven-cycle.
Together they make the Galois action on the eight corrected-Q8 contacts
primitive: a nontrivial block has size two or four, while the corresponding
wreath-product stabilizers have orders `384` and `1152`, neither divisible
by seven.

Because the reviewed local theorem gives every corrected-Q8 point a unique
selected **non-parity** formal branch (in addition to the parity branch), the
partition of the eight contacts by geometric irreducible component is
Galois-invariant.  Primitivity therefore leaves only two possibilities:

1. one geometric component contains all eight contacts; or
2. eight conjugate geometric components contain one contact each.

The replay does **not** decide between those alternatives.  It is an exact
group-theoretic reducer for the separately running component computation.
Run it only on AWS, even though its resource cost is tiny.
