# AWS shell-custody supplement

Deploy the complete source closure at repository-relative paths, verify
`SOURCE_CLOSURE.sha256` and `RUNNER_MANIFEST.sha256`, then run on Box02:

```sh
nohup setsid ./run_remote.sh UNIQUE_UTC_TAG > launch.log 2>&1 < /dev/null &
```

The result is custody-only.  It closes the shell execution residual listed
in Section 8 of the already-confirmed Claude review and changes no theorem
scope.
