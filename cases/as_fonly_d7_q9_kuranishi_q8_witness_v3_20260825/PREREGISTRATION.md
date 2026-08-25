# Q9-to-Q8 witness certificate V3

V1 correctly failed closed on an incompatibility but asserted compatibility.
V2 was intended to emit the obstruction; it failed closed before output
because its positive substitution check compared a 13-row partial solve to
the unsliced 22-row source vector.  Both frozen failures are preserved and
supply no verdict.

V3 consumes the V2 definition prefix byte-for-byte and changes only that
check to `transition_rows(... )[:rows]`.  It emits the exact ranks and a
directly verified left-null certificate/plus-one control.

