# Corrected-Q8 named rational contact, order 65536

This AWS-only successor leaves the frozen order-16384 package immutable.  A
hash-pinned adapter changes only the accepted order list of the original
contact generator and runs the rational root `v=58` (`linear58`) through
order `65536`.

The root58 lane had the smallest measured order-16384 peak RSS, albeit by only
288 KiB: `92,956,456` KiB versus `92,956,744` KiB for root67.  Linear memory
scaling from order16384 predicts roughly 363 GiB at order65536; the remote
guard is therefore 512 GiB with an eight-hour time cap.

If the complete fail-closed endpoint passes, then `65536>35582` forces the
**named root58 contact** onto an H-supported mod-127 source component,
conditional on the separately review-pending bidegree residual bound.  No
partial iteration or resource failure is evidence.

