# Labelled one-P0 U2 td12 budget kill R1

`check.py` composes three already reviewed interfaces:

1. equality in the corrected arrival-subtree mass floor forces three
   `(a,b,nu)=(1,2,3)` pole subtrees at type `(2,3)`;
2. the corrected inner-U2 handshake requires both inner arrivals at
   `(w,3|M)=(1,3|M)`, while the outer sibling must arrive at `w=2`;
3. the cap-free reduced P0 closure gives minimum lambda 5 for each inner
   arrival and proves zero-price transitions cannot raise the pole seed
   `w=3/2` to the sibling target.

Thus the three disjoint pole branches cost at least `5+5+1=11`, exceeding
the global `td-2=10` budget at `td=12`.

Run:

```text
PYTHONDONTWRITEBYTECODE=1 python3 check.py
PYTHONDONTWRITEBYTECODE=1 python3 -O check.py
```

Scope is the corrected labelled `U2--P0--U2` route under actual source
landing and the reviewed P0/AF2 grammar. It does not exclude other U2
routes, prove a landing or realization theorem, or settle JC2.
