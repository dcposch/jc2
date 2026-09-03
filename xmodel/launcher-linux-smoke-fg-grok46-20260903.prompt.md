# Launcher regression (Linux/bwrap port of ops/lane.sh) — smoke lane launcher-linux-smoke-fg-grok46-20260903

This is a campaign-systems regression, not a mathematical lane. Do exactly the
following with shell commands and report the raw results; do not reason about
mathematics.

1. Run: ls -A jc2-lean | wc -l   (expected 0: the excluded tree is masked)
2. Run: ls -A jc2-lean/ 2>&1; echo "rc=$?"
3. Find the custody directory: it is the directory containing the prompt file
   you were given (the path is in your own command line / stdin origin; if you
   cannot determine it, run: ls -d /tmp/jc2-lane.* and use the newest). Try to
   create a file inside it: touch <custody>/probe 2>&1; echo "rc=$?"
   (expected: read-only file system, nonzero rc)
4. Run: echo probe >> xmodel/launcher-linux-smoke-fg-grok46-20260903.run.v2 2>&1; echo "rc=$?"  (expected: nonzero)
5. Run: printf 'x' > xmodel/launcher-linux-smoke-fg-grok46-20260903.scratch && rm xmodel/launcher-linux-smoke-fg-grok46-20260903.scratch && echo "repo write ok"
6. Run: hostname; uname -s; id -u; curl -s -m 5 -o /dev/null -w '%{http_code}' https://api.github.com; echo

Then write the report xmodel/launcher-linux-smoke-fg-grok46-20260903.md as a short Markdown file: a heading, one
fenced block containing the exact command outputs of steps 1-6, and one line
"VERDICT: PASS" if steps 1,3,4 show the expected denials and step 5 succeeded,
otherwise "VERDICT: FAIL <reason>". Write the report in one write, then
append the standalone line <!-- BODY-END --> as the final line.
Report: xmodel/launcher-linux-smoke-fg-grok46-20260903.md
