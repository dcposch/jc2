# Concrete operator corrections and no-HOME dispatcher copy

ROOT,2026-09-12. SOURCE-ONLY / UNREVIEWED / UNBOUND / UNEXECUTED.
No worker allocation, interpreter/import/syntax/dummy/CAS execution or changed
physical/scientific cap. Original accepted sources remain untouched.

The fully delivered Sol commands were terminal before custody-first intake,
all six input checks and expected report transaction passed, and report,
manifest, custody, PINS and143-line COMMANDS were read WHOLE. The design
is useful but two exact-check defects remain:

1. `test ! -s cgroup.procs` examines pseudo-file stat size, not kernel content.
   The new copy reads at most one byte into a regular bounded evidence file
   and checks that file is empty. Under set-e a failed head read aborts;
   no pipeline masks its status. Empty read proves emptiness at that instant,
   NOT future quiescence. Existing no-child-directory and final exact cgroup
   disappearance checks remain mandatory; no claim from stat size survives.
2. Shell command substitution strips trailing LFs. The new expected one-line
   runner stdout is materialized and compared by cmp, including the single LF.
   The exact seven-key cgroup_controls schema is now also compared explicitly.

Separate mandatory instruction compliance: the old dispatcher created a child
environment HOME equal to its output directory. The new immutable candidate
removes only that key, preserving the same otherwise-allowlisted environment
and all flags, sources, phases, DATA controls, limits, clocks and outputs.
HOME is absent in that explicitly constructed child environment, not assigned
or repurposed; no inherited PYTHON/environment variables are newly admitted.
The operator launch already avoids assigning HOME. Existing -E/-s/-S/-B and
TMP/XDG cache routing remain; actual native/import qualification is separate.

Sources: Sol COMMANDS ade4e33d13f3ca336840be7566dddb9145e747b549382e93f5c62a08704b889c;
old dispatcher3832f0085f2d2f651e48cfe04cd7a33d95fa4b627fc8078d262008d696249e0b;
unchanged CAPRUN4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2;
probe16d723b7fbe6dc218351274e4078df1959add5c2914174079d707fdc14e17158.
Different-model focused DELTA FIRST before either new copy is used. This is
one correction of identified defects, not a new controller or general re-review.
No scientific result, runtime fit, complete closure or launch authority.
