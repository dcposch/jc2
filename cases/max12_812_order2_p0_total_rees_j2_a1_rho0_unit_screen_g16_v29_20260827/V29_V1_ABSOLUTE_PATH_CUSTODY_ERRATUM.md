# V29 V1 absolute-path custody erratum

Date: 2026-08-27

The V1 exact-Q compiler stopped before emitting an input script.  Its V28
manifest contains the absolute path of the earlier Box02 producer.  Because
that old tree still existed on Box02, V1 selected it and then correctly
rejected it as outside the newly registered source root.  On Box03 the old
Box02 path did not exist, so the identical frozen V1 selected the bundled
copy and the characteristic-65521 lane proceeded.

This is a path-selection defect only.  R1 imports the frozen V1 compiler at
SHA-256 `bdce64b98449195ad1fe16a09ce0f23b36560d03a6a4559c5e36ab27cd538f29`
and remaps exactly the seven manifest names `Tg16_1_q.poly` through
`Tg16_7_q.poly` to V1's hash-pinned bundled V28 directory.  Every other path,
hash, polynomial transformation, control, and Singular command remains V1.
The V1 modular lane remains valid and running; R1 relaunches exact Q only.

