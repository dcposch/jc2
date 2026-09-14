# Native collector reference — no copy or execution

Use only the retained cache-corrected template at
`/home/ubuntu/jc2/box/f10-r2-fullunit-ready-deployment-prep-astra-20260910/native-metadata.template.sh`,
SHA256 `e6d3c105e8e0c558356c7db891d9a8a6c5d09a758eef2dd3627ba30eb5923848`.
It was read WHOLE as documentary input. It is not copied, altered or run here.

The collector is an observation template, not the contact dispatcher's schema
or a completeness proof. In particular its old R2 runtime-comparison language
does not describe this dispatcher. The new dispatcher consumes ONLY a manifest
with schema `f10-native-closure/v1` and a `files` dictionary, 1–1500 canonical
absolute file paths mapped to SHA256, total at most 262144 bytes. Do not feed
the R2 six-field schema or enlarge these consumer bounds. Never truncate an
oversized closure to make it pass.

ROOT separately retains and authenticates the original directory inventories,
aliases, explicit absences, python_path and loader-cache observations. This
includes installed pyc and ZIP/site-startup implications; -B prevents writes,
not reads. The reference template's Python-version assumptions must match the
future explicitly selected environment or remain a blocker, not trigger an
automatic install, fallback or rewritten collector in this packet.

Future metadata collection requires separate ROOT authority. Actual worker,
boot, interpreter, native and device facts are observed after allocation and
before immutable registration or science. Offline acceptance of the schema,
collector/reference plan and full-cgroup supervisory design comes BEFORE any
allocation. No current worker/native fact is asserted here.
