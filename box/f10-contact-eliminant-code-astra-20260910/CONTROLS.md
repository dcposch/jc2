# Prospective controls — NONE executed

No certificate or fixture was generated in this lane. The following are
future ROOT registration/gate controls, not requests or authority to run.

1. Valid round trip: future producer certificate must parse and satisfy the
   independent coefficient identity, with CHECK_OK binding its exact byte
   SHA256. Singular completion/exit status alone is insufficient.
2. Changed F: from a valid certificate change ONLY F to F+1, editing or
   adding its constant term canonically. Identity residual becomes 1, so
   the checker rejects (or rejects zero F first if applicable).
3. Changed actual cofactor: change ONLY H4 to H4+1. Residual becomes -I4;
   I4=z*c*A-1 is nonzero (its value at z=0 is -1), so rejection is required.
   This is an arithmetic mutation, not merely a changed digest/header.
4. Omit I4 from the prospective mathematical producer input. At V=W=0,
   A=B=C=0, leaving X free. The changed ideal cannot contain nonzero F(X);
   the producer's dimension guard must refuse it, not emit an eliminant.
   Omitting the H4 block from any serialized certificate is separately a
   parser rejection; it is not evidence for this mathematical control.
5. Reject zero F, F containing V, changed ring/variable order/interface pin,
   duplicate term, negative exponent, zero denominator, truncated endcert,
   extra block or trailing token. Legitimate zero Hi use empty poly blocks.
6. Exercise the producer's F=1/unit-ideal branch and zero cofactor blocks
   only in separately registered non-contact dummy controls. No dummy
   coefficient artifacts, engine runs or resulting PASS exist here.

All controls remain prospective; required syntax/engine/serializer/runtime
validation and external time/memory/output caps are ROOT-owned and pending.
