# Proposed predicate correction — NOT APPLIED / NOT DISPATCHABLE

Frozen caller SHA da3d8d503f9246fd33d0cde372ccb642140e174c53a0599921ee4ab07b399b67
stopped at its final dummy predicate. No mathematical child started. Do not edit
or replay that caller, its remote bytes, or frozen builder/checker.

The current predicate incorrectly asks every identity_checks result to be MATCH.
CAPRUN records two different event types. Actual preserved sequence:

1. before-term: MATCH, observed PID/PGID 2628 and matching boot/start identity.
2. before-term-send: SENT, signal 15.
3. before-kill: MATCH, the same identity.
4. before-kill-send: SENT, signal 9.

The proposed replacement for THIS expected RSS/TERM-ignoring dummy is an exact
four-entry sequence check against the four triples below, plus unchanged
namespace/PGID/source-hash/cleanup/RSS requirements already in the caller:

```python
expected_events = [
    ("before-term", "MATCH", None),
    ("before-term-send", "SENT", 15),
    ("before-kill", "MATCH", None),
    ("before-kill-send", "SENT", 9),
]
observed_events = [
    (event.get("stage"), event.get("result"), event.get("signal"))
    for event in telemetry["identity_checks"]
]
require(observed_events == expected_events, "unexpected dummy identity/signal sequence")
```

This is a review proposal only, not a new accepted caller or permission to
reuse the old worker/directory/output names. A fresh invitation must determine
whether and how to freeze, independently review and dispatch a corrected
variant. Original STOP bytes remain immutable. No CAS or mathematical output
was produced, and no source theorem is affected by this event-type mismatch.
