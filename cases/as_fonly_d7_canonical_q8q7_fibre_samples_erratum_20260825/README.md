# Q8 fibre-coordinate / coefficient-vector erratum

This nonmutating supplement corrects the frozen sampler report's statement
that every Q8 affine particular vector is zero.  The exact predecessor output
uses `s=0` in the 19 RREF fibre coordinates; the corresponding 32-component
affine particular vector `y0` can be nonzero.

`audit_particulars.py` pins all 64 predecessor JSON files and all 64 displayed
`y0` vectors and hashes.  It does not alter the frozen producer bytes.

