# Launcher Linux smoke (fg-grok46-20260903)

```
$ ls -A jc2-lean | wc -l
0

$ ls -A jc2-lean/ 2>&1; echo "rc=$?"
rc=0

$ touch /tmp/jc2-lane.6On4eU/probe 2>&1; echo "rc=$?"
touch: cannot touch '/tmp/jc2-lane.6On4eU/probe': Read-only file system
rc=1

$ echo probe >> xmodel/launcher-linux-smoke-fg-grok46-20260903.run.v2 2>&1; echo "rc=$?"
--: line 1: xmodel/launcher-linux-smoke-fg-grok46-20260903.run.v2: Read-only file system
rc=1

$ printf 'x' > xmodel/launcher-linux-smoke-fg-grok46-20260903.scratch && rm xmodel/launcher-linux-smoke-fg-grok46-20260903.scratch && echo "repo write ok"
repo write ok

$ hostname; uname -s; id -u; curl -s -m 5 -o /dev/null -w '%{http_code}' https://api.github.com; echo
ip-172-30-0-46
Linux
1000
200
```

VERDICT: PASS
<!-- BODY-END -->
