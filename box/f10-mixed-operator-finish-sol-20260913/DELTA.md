# Operator finish delta

INTERNAL / UNREVIEWED / UNEXECUTED / UNBOUND.

The unit derivative changes only the two selected integration areas:

1. It renders the frozen ISO-Z TERM/deadline instants as
   `YYYY-MM-DD HH:MM:SS UTC`, checks epoch round trips, and supplies only those
   rendered strings to `--on-calendar`. Admission/deadline values and caps do
   not change.
2. It captures `systemctl show` status explicitly. A loaded unit retains the
   prior cgroup-empty, reset-failed and final-absence path. A show failure is
   accepted only with successful real wait status, reachable manager, empty
   terminal-property output and already absent expected cgroup; it records the
   unloaded outcome. Existing-unit failures still reach the final wait-rc-zero
   predicate. No blank ControlGroup is consumed.

All other unit bytes are inherited. The accepted dispatcher is untouched.

PREPARE static verdict: REFUTED for promotion as written. Its four metadata
services each unconditionally run `systemctl show UNIT.service` after
`systemd-run --wait`; a successful transient may already be unloaded, so the
same diagnosed post-wait condition can abort preparation. This is fail-closed,
not false success, but requires its own future source delta/review. No PREPARE
source was modified here.
