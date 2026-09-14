# Narrow two-line exact-stream repair gate

Write exactly xmodel/d125-small-exact-solver-delta-gate-sol56-20260907.md.
At most1000words and10minutes, due2026-09-07 01:15UTC. All producers are
terminal/idle. This is ONLY the two-check delta from the terminal original
Sol review, not another full solver/caller/source/limits review.

Read all frozen inputs in {{LANE_INPUTS}}. The patch removes .strip() from
the empty-stderr condition and requires I_SIZE to equal the number of
nonzero indexed engine rows, counting duplicate nonzero positions separately.
Original arithmetic, asymmetric proper-superideal criterion, original-row
unit identity, serializer and static caller already passed the parent gate.
Root independently read/replayed that gate. Actual engineering controls and
all-six full source streams are separately root accepted; do not repeat them.

Independently test the repaired exact.py on pinned actual control.stdout
(six indexed I rows, three nonzero entries, duplicate x, six T rows), and
reject actual changed whitespace stderr and I_SIZE 3->0 as well as upward
count corruption. Test a correct all-zero row stream at parser scope if useful;
do not confuse parser acceptance with a valid unit/properness certificate.
Use your own tiny stdlib checker, accept --inputs PATH for later relocation,
normal and -O, explicit runtime checks/no removable Assert nodes. At most
30wall/25CPU/512MiB per command. No CAS, AWS, SSH, full-source arithmetic,
new lanes, live peer material, shared-ledger or frozen-input edits.
Own evidence only box/d125-small-exact-solver-delta-gate-sol56-20260907/.

State CONFIRMED/REFUTED/GAP only for repaired literal-stderr and size/index
semantics, with concrete tests. No new framework or unrelated hardening.
If a flaw remains report it and seal, do not repair inputs. ROOT owns any
subsequent deployment/solver authorization. This gate authorizes neither.

Publication: skeleton without BODY-END; bounded appends; unique standalone
<!-- BODY-END --> only after completion with nothing after. No authored seal
and no line beginning charge_basis; expected ABSENT.

charged_input=xmodel/d125-small-exact-solver-strict-repair-astra-20260907.md
charged_input=xmodel/d125-small-exact-solver-code-gate-sol56-20260907.md
charged_input=box/d125-small-exact-solver-strict-repair-20260907/exact.py
charged_input=box/d125-small-exact-solver-strict-repair-20260907/exact-two-checks.patch
charged_input=box/d125-small-exact-solver-engineering-20260907/evidence/control.stdout
