# td=8 equal-join affine route family R1

This packet proves an exact infinite family inside the current off-axis book
grammar at the unique `td=8,m=2` entry.  Every member has the same reduced
merge successor, while its full merge cell and edge labels grow affinely.
The sum of the recorded lambda lower bounds meets the terminal budget ceiling
at equality; the packet does not claim those lower bounds are exact costs.

Run:

```sh
python3 test_td8_equal_join_route_family_r1.py
python3 -O test_td8_equal_join_route_family_r1.py
python3 td8_equal_join_route_family_r1.py
```

The result is provisional pending different-model review.  The exact
Prop. 8.1(iv)/T1 equation for this off-class family has not been solved, and
the book grammar is not a source-landing or realizability theorem.
