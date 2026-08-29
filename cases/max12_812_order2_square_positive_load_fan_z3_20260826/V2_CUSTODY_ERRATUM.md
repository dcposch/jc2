# V2 custody erratum

The first Box02 run passed the mathematical enumerator and dependency-free
witness checker, but the preregistration promised a recorded wheel hash while
V1 recorded only the package filename and installed version.  V1 is therefore
custody-negative and is retained as a control.  V2 downloads the pinned wheel
before installation, hashes that exact file, installs with `--no-index` from
the recorded wheel directory, and then repeats the enumeration and checker.

No fan equation, solver query, output schema, or mathematical decision rule
changes in V2.

