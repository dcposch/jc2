# Local fail-closed negative control

At `2026-08-26T05:37Z`, the frozen compiler was invoked on the local macOS
host with a valid traversal argument and a fresh output path:

```text
python3 compile_weighted_two_chart_v10.py --order forward \
  --output /tmp/v10_weighted_twochart_negative_should_not_exist.json
```

It exited with rc 1 and the sole diagnostic

```text
REFUSE_NON_LINUX
```

before loading V9 or performing algebra.  The requested output file was not
created.  This is only a fail-closed placement control; all substantive exact
algebra ran on the two registered AWS hosts.

