# R2 result: adapter failure, no verdict

The Q1P03 full-pilot payload is classified strictly as
`ADAPTER_FAILURE_NO_VERDICT`.  It produced no valid rank-chart, endpoint, or
whole-stratum conclusion.

The generated node reduction itself passed the registered 95 rational-unit
pivots and residual replay.  The next stage was invalid: Singular's
`sat(NODE_IDEAL,DELTA_IDEAL)` returned a one-slot list on this backend, while
the adapter accessed `OPEN_SAT_RESULT[2]`.  Singular printed three diagnostic
lines (`wrong range[2]`, `error occurred`, and `wrong type declaration`) to
stdout yet returned zero.  The R2 parser did not reject those diagnostics and
continued with a false `OPEN_CHART_EMPTY=1` marker.  Consequently all R2 node
records and its raw `NO_VERDICT_OPEN_REMAINDER` marker are quarantined as
adapter output, not algebraic evidence.

The failure was recognized before any chart fanout.  No other component was
launched.  R3 must reject every Singular diagnostic regardless of return code,
require an explicit saturation object type/size marker, and independently
certify each empty-open conclusion by an exact power-membership certificate
before interpreting it.

Scope firewall: this report makes no endpoint claim, no rank-locus claim, no
radical/nilpotence claim, and no statement about any other stratum.

