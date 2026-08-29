# H19R2 V1 forbidden-module probe erratum

Date: 2026-08-27

Scope: execution-only repair before any algebra.

The first dual launch used stamp `20260827T021649Z` at these immutable remote
job roots:

- `r6a`: `/home/ubuntu/jobs/td6_coordinate12_h19r2_20260827T021649Z_r6a`
- `box01`: `/home/ubuntu/jobs/td6_coordinate12_h19r2_20260827T021649Z_box01`

Both lanes failed closed in less than one second, at the same import-safety
probe and before importing the frozen parent or constructing any algebraic
object.  Python's `importlib.util.find_spec("sage.all")` raises
`ModuleNotFoundError` when the parent package `sage` is absent; it does not
return `None`.  The old client therefore rejected the desired environment in
which Sage was not installed.

The repair catches only `ModuleNotFoundError`, records that outcome as an
absent module, and retains the assertions that every forbidden name is both
unloaded and undiscoverable.  The forbidden list, environment pins, source
pins, algebra, controls, outputs, stop rule, caps, and preregistered claim are
unchanged.

Failed V1 custody:

```text
client_sha256=00f172e6825ccbdf2d7136e28b77b479f3c27900c3ab3e0581d112cbdd472cc1
manifest_sha256=6b9ef0a71db51171e23aee04eda5f42c53a233bc096ef07b4cb73faf3cd8ed7b
stdout_sha256=b3df10b81460396ec5290c88d575f7ac96665822195b6a51fc87b29a9d4d2c19
r6a_stderr_sha256=0063dedf68fa6dd539e5a6e61c1dd756dc8ab0885a109368284de9afc28a700d
box01_stderr_sha256=0ede55904ed43b7bae804a21449a0d4e1d334177c01aac4aacf9b35b02dcf749
r6a_rc=1
box01_rc=1
maximum_rss_kib=44084
mathematical_result=NONE
```

The V1 remote evidence is preserved.  It is an aborted/fail-closed software
control and must never be cited as a mathematical result.
