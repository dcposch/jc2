# State-complete Q2/Q1 QF_BV deployment V2

Consume the V1 emitter and replay bytes at SHAs
`8e2a13b3c833d4104709d26cabc7031c100c230d57eea991c84d891a8917b7f0`
and `8d6c12069a99ccde806c5ba6198bf3afa4ba2bb96557e8372d28ed622848da3f`.
V1 deployment failed closed before emission because its runner omitted the
required nested `PARENT_OUTPUT_JSON` environment variable.

V2 changes only custody/deployment: it supplies separate nested parent-output
paths to the emitter and replay.  Mathematical formula, SAT replay, UNSAT
scope, and refusal scope are exactly those preregistered by V1.
