# Independent localizer/elimination route

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Independently reconstruct the same exact `Q(c)` selected saturation by
adjoining `inv*w*x5*(x3-2*x5)-1`, using an elimination block for `inv`, and
contracting.  Test the same centre `(w,u,x1,x3,x5)`.  This is algorithmically
distinct from `elim.lib::sat`; all theorem scope and exceptional-specialization
firewalls of `PREREGISTRATION.md` remain unchanged.

