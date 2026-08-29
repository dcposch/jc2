# V14 custody gap: matrix serialization is incomplete

V14's engine replayed all entries of its `6 x 6` colon-lift matrix in
memory, and its exact-Q and `p=65521` endpoints both selected a unit colon
witness.  However, Singular's `write(filename,matrix)` serialization writes
only the first matrix row.  The harvested `COLON_LIFTS.txt` therefore
contains six entries rather than all 36 and does not preserve all six
multipliers for the chosen witness column.

Consequently V14 remains **provisional / custody-failed for promotion** even
though its in-memory checks passed.  V14R1 freezes the identical algebra,
serializes all 36 entries and the six chosen witness multipliers separately,
then reconstructs and replays the unit identity in a fresh Singular process
from those serialized bytes.  Only V14R1 may support review or promotion.

