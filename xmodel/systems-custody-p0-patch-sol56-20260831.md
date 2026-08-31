# D1 — Canonical seal boundary

`verify_bytes` now accepts exactly the UTF-8 byte string emitted by `_canonical_seal`; its fixed post-body line ending is LF, while an LF- or CRLF-terminated marker remains part of the body and is hashed byte-for-byte.  The divert classifier consequently treats a valid canonical seal plus even one suffix byte (and every CRLF-encoded or otherwise noncanonical seal tail) as overflow, preserving the untouched input in the raw bank and the complete tail in the overflow bank instead of reporting `CLEAN_SEALED`.

# D2 — Unterminated marker

Divert still detects an exact standalone marker at EOF, but it no longer calls that report clean when the marker has no LF or CRLF terminator: it returns the distinct, non-mutating `UNTERMINATED_MARKER` status.  `lane.sh` maps that status to `report_state=PARTIAL_NO_MARKER` and forces final rc 7, matching `verify`'s existing refusal to regard the same bytes as sealed.

# D3 — Divert race and cleanup

The diversion attempt tracks only the raw and overflow files it successfully created; every pre-replace failure removes those files, so an occupied overflow target cannot strand a new raw artifact or disturb the pre-existing overflow.  The existing last-moment report reread is changed from an error-only comparison into a retry boundary: if bytes or metadata changed, the staged report and this attempt's sidecars are removed, the newly read stable bytes are reclassified, and only an unchanged classification reaches `os.replace`; the requested larger fsync/manifest transaction redesign remains out of scope.

# S1 — Charged-path lexical hardening

The launcher scopes `LC_ALL=C` to charged-path shell patterns and ASCII folds, rejects absolute paths plus `.`/`..` components, folds case for both the `jc2-lean` exclusion and basename-uniqueness key, and calls a small `os.lstat` walker that rejects a symlink at every charged relative-path component without resolving it.  Lexical exclusion runs before that walker, so excluded aliases are refused without traversal; the deliberately scoped fix retains the existing hash/copy flow rather than introducing the deferred dirfd/openat redesign, and the provider keeps its inherited locale.

# S5 — Uniform hardening exit status and adapter receipt

Launch-time report-path and charged-input contract refusals now return 7, as do all post-run BODY-END boundary failures regardless of a nonzero provider result; a no-marker report remains informational only when no BODY-END contract was declared.  The status returned directly by `wait` is captured before any lane override and added to the receipt as `adapter_exit_code`, while the existing `exit_code` field continues to record the final lane rc, preserving both facts without renaming or changing any existing receipt key.

# R4 — Receipt-safe paths

Before any prompt-derived path can be emitted into a receipt, the launcher rejects Unicode control, format, surrogate, and line-separator categories: the CLI-supplied prompt pathname is checked without reflecting the unsafe value, and each charged path is checked before diagnostics, manifest construction, or receipt emission.  These refusals use the same rc 7 hardening-contract path, safe path fields use `printf` rather than implementation-defined `echo`, printable non-ASCII prompt filenames remain allowed, and charged paths remain intentionally ASCII-only under the S1 bytewise policy.

# Unified diff

```diff
--- ops/lane.sh
+++ ops/lane.sh
@@ -42,6 +42,24 @@
   echo "unknown adapter: $adapter" >&2
   exit 2
 }
+command -v python3 >/dev/null 2>&1 || {
+  echo "python3 is required for lane validation" >&2
+  exit 2
+}
+receipt_path_is_safe() {
+  python3 - "$1" <<'PY'
+import sys
+import unicodedata
+
+for character in sys.argv[1]:
+    if unicodedata.category(character) in {"Cc", "Cf", "Cs", "Zl", "Zp"}:
+        raise SystemExit(1)
+PY
+}
+if ! receipt_path_is_safe "$prompt_file"; then
+  echo "prompt path contains a control or line-separator character; run refused" >&2
+  exit 7
+fi
 [ -f "$prompt_file" ] || {
   echo "prompt file not found: $prompt_file" >&2
   exit 2
@@ -57,10 +75,6 @@
 seal_tool=$script_dir/seal.py
 [ -f "$seal_tool" ] && [ ! -L "$seal_tool" ] || {
   echo "required seal tool missing: $seal_tool" >&2
-  exit 2
-}
-command -v python3 >/dev/null 2>&1 || {
-  echo "python3 is required for charge-basis validation" >&2
   exit 2
 }
 sandbox_exec=/usr/bin/sandbox-exec
@@ -162,6 +176,7 @@
 inputs_dir=$lane_tmp_dir/inputs
 inputs_manifest=$lane_tmp_dir/charged-inputs.list
 inputs_post_manifest=$lane_tmp_dir/charged-inputs-post.list
+input_basename_keys=$lane_tmp_dir/charged-input-basename-keys.list
 # Keep this lexical: boundary setup must neither resolve nor inspect the excluded
 # nested worktree.  Seatbelt resolves aliases when enforcing the path filter.
 excluded_tree=$repo_root/jc2-lean
@@ -215,7 +230,7 @@
 # response cannot be lost to a misdirected or unwritten report.
 if ! grep -F "xmodel/$tag.md" "$prompt_snapshot" >/dev/null 2>&1; then
   echo "prompt does not name its mandated report path xmodel/$tag.md; run refused" >&2
-  exit 2
+  exit 7
 fi
 
 # A prompt that instructs the BODY-END convention declares the marker
@@ -235,53 +250,102 @@
 if grep -F "$input_placeholder" "$prompt_snapshot" >/dev/null 2>&1; then
   prompt_has_placeholder=1
 fi
+charged_path_is_lexically_valid() {
+  (
+    LC_ALL=C
+    export LC_ALL
+    case "$1" in
+      /*|*..*|*[!A-Za-z0-9/._-]*) exit 1 ;;
+    esac
+    case "/$1/" in
+      */./*) exit 1 ;;
+    esac
+    exit 0
+  )
+}
+charged_path_is_regular_without_symlinks() {
+  python3 - "$repo_root" "$1" <<'PY'
+import os
+import stat
+import sys
+
+root, relative = sys.argv[1:]
+parts = relative.split("/")
+current = root
+for index, component in enumerate(parts):
+    current = os.path.join(current, component)
+    try:
+        info = os.lstat(current)
+    except OSError:
+        raise SystemExit(1)
+    if stat.S_ISLNK(info.st_mode):
+        raise SystemExit(1)
+    if index < len(parts) - 1 and not stat.S_ISDIR(info.st_mode):
+        raise SystemExit(1)
+    if index == len(parts) - 1 and not stat.S_ISREG(info.st_mode):
+        raise SystemExit(1)
+PY
+}
 input_count=0
 if [ -n "$charged_inputs" ] || [ "$prompt_has_placeholder" -eq 1 ]; then
   if [ -z "$charged_inputs" ] || [ "$prompt_has_placeholder" -eq 0 ]; then
     echo "charged_input declarations and the $input_placeholder placeholder must appear together; run refused" >&2
-    exit 2
+    exit 7
   fi
   case "$inputs_dir" in
     *[!A-Za-z0-9/._-]*)
       echo "lane inputs directory has unsupported characters: $inputs_dir" >&2
-      exit 2
+      exit 7
       ;;
   esac
   mkdir "$inputs_dir" || exit 2
   while IFS= read -r charged_rel; do
     [ -n "$charged_rel" ] || continue
-    case "$charged_rel" in
-      /*|*..*|*[!A-Za-z0-9/._-]*)
-        echo "invalid charged input path: $charged_rel" >&2
-        exit 2
-        ;;
+    if ! receipt_path_is_safe "$charged_rel"; then
+      echo "charged input path contains a control or line-separator character; run refused" >&2
+      exit 7
+    fi
+    if ! charged_path_is_lexically_valid "$charged_rel"; then
+      echo "invalid charged input path: $charged_rel" >&2
+      exit 7
+    fi
+    charged_rel_fold=$(printf '%s' "$charged_rel" | LC_ALL=C tr 'A-Z' 'a-z') || exit 2
+    case "$charged_rel_fold" in
       jc2-lean|jc2-lean/*)
         echo "charged input inside the excluded tree refused: $charged_rel" >&2
-        exit 2
+        exit 7
         ;;
     esac
+    if ! charged_path_is_regular_without_symlinks "$charged_rel"; then
+      echo "charged input missing or not a regular file, or has a symlink component: $charged_rel" >&2
+      exit 7
+    fi
     charged_src=$repo_root/$charged_rel
-    if [ ! -f "$charged_src" ] || [ -L "$charged_src" ]; then
-      echo "charged input missing or not a regular file: $charged_rel" >&2
-      exit 2
+    charged_base=$(basename "$charged_rel")
+    charged_base_key=$(printf '%s' "$charged_base" | LC_ALL=C tr 'A-Z' 'a-z') || exit 2
+    charged_dest=$inputs_dir/$charged_base
+    duplicate_base=0
+    if [ -f "$input_basename_keys" ]; then
+      if grep -Fqx -e "$charged_base_key" "$input_basename_keys"; then
+        duplicate_base=1
+      fi
     fi
-    charged_base=$(basename "$charged_rel")
-    charged_dest=$inputs_dir/$charged_base
-    if [ -e "$charged_dest" ]; then
+    if [ "$duplicate_base" -eq 1 ] || [ -e "$charged_dest" ]; then
       echo "duplicate charged input basename: $charged_base" >&2
-      exit 2
+      exit 7
     fi
+    printf '%s\n' "$charged_base_key" >> "$input_basename_keys" || exit 2
     charged_src_sha=$(sha256_file "$charged_src") || exit 2
     cp "$charged_src" "$charged_dest" || exit 2
     chmod 400 "$charged_dest" || exit 2
     charged_snap_sha=$(sha256_file "$charged_dest") || exit 2
     if [ "$charged_snap_sha" != "$charged_src_sha" ]; then
       echo "charged input changed while being snapshotted: $charged_rel" >&2
-      exit 2
+      exit 7
     fi
     input_count=$((input_count + 1))
     printf '%s %s %s\n' "$charged_rel" "$charged_base" "$charged_src_sha" \
       >> "$inputs_manifest"
   done <<CHARGED_INPUTS_EOF
 $charged_inputs
 CHARGED_INPUTS_EOF
@@ -339,7 +403,7 @@
   echo "pid=$$"
   echo "host=$(hostname)"
   echo "basis=$basis"
-  echo "prompt=$prompt_file"
+  printf '%s\n' "prompt=$prompt_file"
   echo "prompt_sha256=$prompt_sha"
   echo "adapter_sha256=$adapter_sha"
   echo "launcher=ops/lane.sh"
@@ -381,7 +445,8 @@
 child_pid=$!
 echo "child_pid=$child_pid" >> "$run_file"
 wait "$child_pid"
-rc=$?
+adapter_exit_code=$?
+rc=$adapter_exit_code
 
 if [ -n "$caught_signal" ]; then
   while kill -0 "$child_pid" 2>/dev/null; do
@@ -432,19 +497,24 @@
         ;;
       NO_MARKER)
         report_state=PARTIAL_NO_MARKER
-        if [ "$body_end_contract" = DECLARED ] && [ "$rc" -eq 0 ]; then
+        if [ "$body_end_contract" = DECLARED ]; then
           echo "report has no BODY-END under a declared contract; banked as partial" >> "$log_file"
           rc=7
         fi
         ;;
+      UNTERMINATED_MARKER)
+        report_state=PARTIAL_NO_MARKER
+        echo "report has an unterminated BODY-END marker; banked as partial" >> "$log_file"
+        rc=7
+        ;;
       MULTI_MARKER)
         report_state=AMBIGUOUS_MULTI_MARKER
         echo "report has multiple BODY-END markers; not repaired" >> "$log_file"
-        [ "$rc" -ne 0 ] || rc=7
+        rc=7
         ;;
       *)
         report_state=UNVERIFIED
-        [ "$rc" -ne 0 ] || rc=7
+        rc=7
         ;;
     esac
   else
@@ -452,7 +522,7 @@
     seal_boundary=ERROR
     report_state=UNVERIFIED
     echo "seal boundary check failed; result is quarantined" >> "$log_file"
-    [ "$rc" -ne 0 ] || rc=7
+    rc=7
   fi
 fi
 
@@ -521,6 +591,7 @@
 end_utc=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
 {
   echo "end_utc=$end_utc"
+  echo "adapter_exit_code=$adapter_exit_code"
   echo "exit_code=$rc"
   echo "post_prompt_sha256=$post_prompt_sha"
   echo "post_adapter_sha256=$post_adapter_sha"
--- ops/seal.py
+++ ops/seal.py
@@ -2,8 +2,13 @@
 """Stamp or verify the campaign's BODY-END report integrity seal.
 
 Only a standalone ``<!-- BODY-END -->`` line is a marker.  Inline or quoted
-mentions are ordinary body text.  The tool never discovers files: every path
-must be supplied explicitly.  A body hash detects accidental or concurrent
+mentions are ordinary body text.  The sole canonical post-body seal is the
+exact UTF-8 serialization returned by the module's canonical-seal serializer:
+its text, order, wrapping, punctuation, and LF line endings are fixed.  CRLF is
+accepted in the body and marker line, where both bytes are hashed, but never in
+the post-body seal.  Any other post-body prefix, suffix, CRLF, or lone carriage
+return makes the seal invalid.  The tool never discovers files: every path must
+be supplied explicitly.  A body hash detects accidental or concurrent
 mutation; it is not an authenticity signature.  Full-file hashes and external
 run receipts remain separate custody evidence.
 """
@@ -252,6 +257,9 @@
         raise SealError(
             f"frozen basis mismatch: declared {basis}, expected {expected_basis}"
         )
+    canonical = _canonical_seal(len(body), actual_sha, basis)
+    if data[boundary:] != canonical:
+        raise SealError("post-body seal is not the canonical LF serialization")
     return len(body), actual_sha, basis
 
 
@@ -384,92 +392,120 @@
     """Split non-whitespace overflow after a sole BODY-END out of a report.
 
     The charged report keeps every byte through the marker line; the exact
-    overflow bytes land in ``overflow_path`` and, when ``raw_path`` is given,
-    the untouched original is preserved there first.  A report whose
-    post-marker content is whitespace or a valid canonical seal is left
-    unmodified.  Zero or multiple markers are reported, never repaired.
+    overflow bytes land in overflow_path and, when raw_path is given, the
+    untouched original is preserved there first.  A report whose post-marker
+    content is whitespace or exactly one canonical seal is left unmodified.
+    Zero, multiple, and unterminated markers are reported, never repaired.
     """
     parent_fd, name, parent, parent_info = _open_parent(path)
     temp_name: str | None = None
-    try:
-        data, original = _read_regular_at(parent_fd, name)
-        markers = _marker_boundaries(data, require_newline=False)
-        if not markers:
-            return {"status": "NO_MARKER", "bytes": len(data)}
-        if len(markers) > 1:
-            return {"status": "MULTI_MARKER", "markers": len(markers)}
-        boundary = markers[0]
-        body = data[:boundary]
-        tail = data[boundary:]
-        body_sha = hashlib.sha256(body).hexdigest()
-        if not tail.strip():
-            return {
-                "status": "CLEAN",
+    created_paths: list[Path] = []
+    reclassified = False
+
+    def cleanup_created() -> None:
+        for artifact in reversed(created_paths):
+            try:
+                artifact.unlink()
+            except FileNotFoundError:
+                pass
+        created_paths.clear()
+
+    try:
+        while True:
+            data, original = _read_regular_at(parent_fd, name)
+            try:
+                markers = _marker_boundaries(data, require_newline=True)
+            except SealError:
+                return {"status": "UNTERMINATED_MARKER", "bytes": len(data)}
+            if not markers:
+                return {"status": "NO_MARKER", "bytes": len(data)}
+            if len(markers) > 1:
+                return {"status": "MULTI_MARKER", "markers": len(markers)}
+            boundary = markers[0]
+            body = data[:boundary]
+            tail = data[boundary:]
+            body_sha = hashlib.sha256(body).hexdigest()
+            if not tail.strip():
+                return {
+                    "status": "CLEAN",
+                    "body_bytes": len(body),
+                    "body_sha256": body_sha,
+                }
+            try:
+                verify_bytes(data)
+                return {
+                    "status": "CLEAN_SEALED",
+                    "body_bytes": len(body),
+                    "body_sha256": body_sha,
+                }
+            except SealError:
+                pass
+
+            result: dict[str, object] = {
+                "status": "DIVERTED",
                 "body_bytes": len(body),
                 "body_sha256": body_sha,
+                "overflow": str(overflow_path),
+                "overflow_bytes": len(tail),
             }
-        try:
-            verify_bytes(data)
-            return {
-                "status": "CLEAN_SEALED",
-                "body_bytes": len(body),
-                "body_sha256": body_sha,
-            }
-        except SealError:
-            pass
-
-        result: dict[str, object] = {
-            "status": "DIVERTED",
-            "body_bytes": len(body),
-            "body_sha256": body_sha,
-            "overflow": str(overflow_path),
-            "overflow_bytes": len(tail),
-        }
-        if raw_path is not None:
-            result["raw"] = str(raw_path)
-            result["raw_sha256"] = _write_exclusive(raw_path, data)
-        result["overflow_sha256"] = _write_exclusive(overflow_path, tail)
-
-        try:
-            current = os.stat(name, dir_fd=parent_fd, follow_symlinks=False)
-        except OSError as exc:
-            raise SealError(
-                f"cannot recheck target before truncation: {exc}"
-            ) from exc
-        if stat.S_ISLNK(current.st_mode) or not stat.S_ISREG(current.st_mode):
-            raise SealError("target changed to a symlink or non-regular file")
-        if _identity(current) != _identity(original):
-            raise SealError("target identity changed while preparing divert")
-
-        temp_fd, temp_name = _create_temp_at(
-            parent_fd, name, stat.S_IMODE(original.st_mode)
-        )
-        with os.fdopen(temp_fd, "wb") as handle:
-            handle.write(body)
-            handle.flush()
-            os.fsync(handle.fileno())
-
-        latest_data, latest = _read_regular_at(parent_fd, name)
-        if _snapshot(latest) != _snapshot(original) or latest_data != data:
-            raise SealError("target changed before atomic truncation")
-        _check_parent_path(parent, parent_info)
-        os.replace(temp_name, name, src_dir_fd=parent_fd, dst_dir_fd=parent_fd)
-        temp_name = None
-
-        installed, _ = _read_regular_at(parent_fd, name)
-        if installed != body:
-            raise SealError("installed body differs from staged bytes")
-        try:
-            os.fsync(parent_fd)
-        except OSError:
-            pass
-        return result
+            try:
+                if raw_path is not None:
+                    result["raw"] = str(raw_path)
+                    result["raw_sha256"] = _write_exclusive(raw_path, data)
+                    created_paths.append(raw_path)
+                result["overflow_sha256"] = _write_exclusive(overflow_path, tail)
+                created_paths.append(overflow_path)
+
+                temp_fd, temp_name = _create_temp_at(
+                    parent_fd, name, stat.S_IMODE(original.st_mode)
+                )
+                with os.fdopen(temp_fd, "wb") as handle:
+                    handle.write(body)
+                    handle.flush()
+                    os.fsync(handle.fileno())
+
+                # Re-read immediately before replacement.  A cooperative late
+                # writer gets one fresh classification rather than stale
+                # truncation; repeated mutation fails closed.
+                latest_data, latest = _read_regular_at(parent_fd, name)
+                if _snapshot(latest) != _snapshot(original) or latest_data != data:
+                    os.unlink(temp_name, dir_fd=parent_fd)
+                    temp_name = None
+                    cleanup_created()
+                    if reclassified:
+                        raise SealError(
+                            "target changed repeatedly before atomic truncation"
+                        )
+                    reclassified = True
+                    continue
+                _check_parent_path(parent, parent_info)
+                os.replace(
+                    temp_name,
+                    name,
+                    src_dir_fd=parent_fd,
+                    dst_dir_fd=parent_fd,
+                )
+                temp_name = None
+                created_paths.clear()
+
+                installed, _ = _read_regular_at(parent_fd, name)
+                if installed != body:
+                    raise SealError("installed body differs from staged bytes")
+                try:
+                    os.fsync(parent_fd)
+                except OSError:
+                    pass
+                return result
+            except Exception:
+                cleanup_created()
+                raise
     finally:
         if temp_name is not None:
             try:
                 os.unlink(temp_name, dir_fd=parent_fd)
             except FileNotFoundError:
                 pass
+        cleanup_created()
         os.close(parent_fd)
 
 
--- ops/test_lane_fallacy.py
+++ ops/test_lane_fallacy.py
@@ -112,6 +112,7 @@
 else
   printf '# fake report\n' > "xmodel/$FAKE_TAG.md"
 fi
+exit "$FAKE_EXIT_CODE"
 """,
             encoding="utf-8",
         )
@@ -126,8 +127,11 @@
         mode: str = "",
         report: str | None = None,
         prompt_text: str | None = None,
+        adapter_exit_code: int = 0,
+        prompt_name: str = "request.txt",
+        env_overrides: dict[str, str] | None = None,
     ) -> tuple[subprocess.CompletedProcess[str], Path, Path, Path]:
-        prompt = root / "request.txt"
+        prompt = root / prompt_name
         if prompt_text is None:
             prompt_text = (
                 f"Investigate the bounded lane. Write the single report to "
@@ -144,6 +148,7 @@
                 "FAKE_PROMPT_PATH": str(prompt_path),
                 "FAKE_TAG": tag,
                 "FAKE_MODE": mode,
+                "FAKE_EXIT_CODE": str(adapter_exit_code),
                 "FAKE_BOUNDARY_RESULT": str(boundary_result),
                 "FAKE_EXCLUDED_TREE": str(root / "jc2-lean"),
                 "FAKE_EXCLUDED_ALIAS": str(root / "excluded-alias"),
@@ -154,6 +159,8 @@
             report_source = root / f"{tag}.report-source"
             report_source.write_text(report, encoding="utf-8")
             env["FAKE_REPORT_SOURCE"] = str(report_source)
+        if env_overrides is not None:
+            env.update(env_overrides)
         result = subprocess.run(
             ["/bin/sh", str(root / "ops" / "lane.sh"), "fake", tag, str(prompt)],
             cwd=root,
@@ -203,6 +210,7 @@
         self.assertEqual(run["post_fallacy_sha256"], run["fallacy_sha256"])
         self.assertEqual(run["post_model_prompt_sha256"], run["model_prompt_sha256"])
         self.assertEqual(run["charge_basis_status"], "ABSENT")
+        self.assertEqual(run["adapter_exit_code"], "0")
         self.assertEqual(run["final_status"], "DONE")
 
         ephemeral_prompt = Path(prompt_path.read_text(encoding="utf-8").strip())
@@ -359,7 +367,7 @@
         result, _, capture, _ = self.run_lane(
             root, "nopath", prompt_text="Investigate the bounded lane.\n"
         )
-        self.assertEqual(result.returncode, 2)
+        self.assertEqual(result.returncode, 7)
         self.assertIn("does not name its mandated report path", result.stderr)
         self.assertFalse(capture.exists())
         self.assertFalse((root / "xmodel" / "nopath.run.v2").exists())
@@ -425,6 +433,36 @@
                 "charged_input=refs/../secret.md\n"
                 "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
                 "invalid charged input path",
+            ),
+            (
+                "dot-exclusion-alias",
+                "charged_input=./jc2-lean/secret.md\n"
+                "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
+                "invalid charged input path",
+            ),
+            (
+                "uppercase-excluded-tree",
+                "charged_input=JC2-LEAN/secret.md\n"
+                "Read {{LANE_INPUTS}}/secret.md then write xmodel/%s.md.\n",
+                "excluded tree",
+            ),
+            (
+                "dot-component",
+                "charged_input=refs/./packet.md\n"
+                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
+                "invalid charged input path",
+            ),
+            (
+                "absolute-path",
+                "charged_input=/tmp/packet.md\n"
+                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
+                "invalid charged input path",
+            ),
+            (
+                "control-character",
+                "charged_input=refs/bad\tname.md\n"
+                "Read {{LANE_INPUTS}}/packet.md then write xmodel/%s.md.\n",
+                "control",
             ),
         )
         for tag, template, error in cases:
@@ -435,9 +473,99 @@
                 result, _, capture, _ = self.run_lane(
                     root, tag, prompt_text=template % tag
                 )
-                self.assertEqual(result.returncode, 2, result.stderr)
+                self.assertEqual(result.returncode, 7, result.stderr)
                 self.assertIn(error, result.stderr)
                 self.assertFalse(capture.exists())
+
+    def test_non_ascii_charged_input_is_refused_under_utf8_locale(self) -> None:
+        root = self.make_repo()
+        packet = root / "refs" / "café.md"
+        packet.parent.mkdir()
+        packet.write_text("x\n", encoding="utf-8")
+        tag = "non-ascii"
+        prompt_text = (
+            "charged_input=refs/café.md\n"
+            "Read {{LANE_INPUTS}}/café.md then write "
+            f"xmodel/{tag}.md.\n"
+        )
+        result, _, capture, _ = self.run_lane(
+            root,
+            tag,
+            prompt_text=prompt_text,
+            env_overrides={"LC_ALL": "en_US.UTF-8", "LANG": "en_US.UTF-8"},
+        )
+        self.assertEqual(result.returncode, 7, result.stderr)
+        self.assertIn("invalid charged input path", result.stderr)
+        self.assertFalse(capture.exists())
+        self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())
+
+    @unittest.skipUnless(hasattr(os, "symlink"), "symlinks unavailable")
+    def test_charged_input_ancestor_symlink_is_refused(self) -> None:
+        root = self.make_repo()
+        target = root / "actual"
+        target.mkdir()
+        (target / "secret.md").write_text("x\n", encoding="utf-8")
+        refs = root / "refs"
+        refs.mkdir()
+        (refs / "alias").symlink_to(target, target_is_directory=True)
+        tag = "ancestor-symlink"
+        prompt_text = (
+            "charged_input=refs/alias/secret.md\n"
+            "Read {{LANE_INPUTS}}/secret.md then write "
+            f"xmodel/{tag}.md.\n"
+        )
+        result, _, capture, _ = self.run_lane(root, tag, prompt_text=prompt_text)
+        self.assertEqual(result.returncode, 7, result.stderr)
+        self.assertIn("symlink component", result.stderr)
+        self.assertFalse(capture.exists())
+        self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())
+
+    def test_casefolded_charged_input_basenames_are_refused(self) -> None:
+        root = self.make_repo()
+        first = root / "refs" / "Packet.md"
+        second = root / "other" / "packet.md"
+        first.parent.mkdir()
+        second.parent.mkdir()
+        first.write_text("one\n", encoding="utf-8")
+        second.write_text("two\n", encoding="utf-8")
+        tag = "casefold-basename"
+        prompt_text = (
+            "charged_input=refs/Packet.md\n"
+            "charged_input=other/packet.md\n"
+            "Read both files under {{LANE_INPUTS}} and write "
+            f"xmodel/{tag}.md.\n"
+        )
+        result, _, capture, _ = self.run_lane(root, tag, prompt_text=prompt_text)
+        self.assertEqual(result.returncode, 7, result.stderr)
+        self.assertIn("duplicate charged input basename", result.stderr)
+        self.assertFalse(capture.exists())
+        self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())
+
+    def test_prompt_path_control_characters_are_refused(self) -> None:
+        controls = (
+            ("LF", "\n"),
+            ("CR", "\r"),
+            ("TAB", "\t"),
+            ("DEL", "\x7f"),
+            ("NEL", "\u0085"),
+            ("LS", "\u2028"),
+            ("PS", "\u2029"),
+            ("BIDI", "\u200e"),
+        )
+        for label, character in controls:
+            with self.subTest(label=label):
+                root = self.make_repo()
+                tag = f"control-{label.lower()}"
+                result, _, capture, _ = self.run_lane(
+                    root,
+                    tag,
+                    prompt_name=f"request{character}injected=1.txt",
+                )
+                self.assertEqual(result.returncode, 7, result.stderr)
+                self.assertIn("control", result.stderr)
+                self.assertNotIn("injected=1", result.stderr)
+                self.assertFalse(capture.exists())
+                self.assertFalse((root / "xmodel" / f"{tag}.run.v2").exists())
 
     def test_overflow_after_body_end_is_diverted_not_lost(self) -> None:
         root = self.make_repo()
@@ -515,6 +643,51 @@
         log = (root / "xmodel" / f"{tag}.log").read_text(encoding="utf-8")
         self.assertIn("banked as partial", log)
 
+    def test_unterminated_marker_is_partial_contract_failure(self) -> None:
+        root = self.make_repo()
+        tag = "unterminated"
+        report = "# review\n\n<!-- BODY-END -->"
+        prompt_text = (
+            f"Review the claim and write the single report to xmodel/{tag}.md, "
+            "ending its body with a standalone <!-- BODY-END --> line.\n"
+        )
+        result, _, _, _ = self.run_lane(
+            root, tag, report=report, prompt_text=prompt_text
+        )
+        self.assertEqual(result.returncode, 7, result.stderr)
+        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
+        self.assertEqual(run["seal_boundary"], "UNTERMINATED_MARKER")
+        self.assertEqual(run["report_state"], "PARTIAL_NO_MARKER")
+        self.assertEqual(run["adapter_exit_code"], "0")
+        self.assertEqual(run["exit_code"], "7")
+        self.assertEqual(run["report_sha256"], sha256(report.encode("utf-8")))
+        self.assertEqual(run["final_status"], "FAILED")
+        self.assertFalse((root / "xmodel" / f"{tag}.raw.md").exists())
+        self.assertFalse((root / "xmodel" / f"{tag}.overflow").exists())
+
+    def test_boundary_failure_overrides_nonzero_adapter_exit(self) -> None:
+        root = self.make_repo()
+        tag = "adapter-failed-boundary"
+        report = "# markerless provider failure\n"
+        prompt_text = (
+            f"Review the claim and write the single report to xmodel/{tag}.md, "
+            "ending its body with a standalone <!-- BODY-END --> line.\n"
+        )
+        result, _, _, _ = self.run_lane(
+            root,
+            tag,
+            report=report,
+            prompt_text=prompt_text,
+            adapter_exit_code=23,
+        )
+        self.assertEqual(result.returncode, 7, result.stderr)
+        run = parse_run(root / "xmodel" / f"{tag}.run.v2")
+        self.assertEqual(run["adapter_exit_code"], "23")
+        self.assertEqual(run["exit_code"], "7")
+        self.assertEqual(run["seal_boundary"], "NO_MARKER")
+        self.assertEqual(run["report_state"], "PARTIAL_NO_MARKER")
+        self.assertEqual(run["final_status"], "FAILED")
+
     def test_missing_marker_without_contract_is_informational(self) -> None:
         root = self.make_repo()
         result, _, _, _ = self.run_lane(root, "nocontract")
--- ops/test_seal.py
+++ ops/test_seal.py
@@ -44,13 +44,14 @@
 def sealed(body: str, *, size_delta: int = 0, digest: str | None = None) -> str:
     data = body.encode("utf-8")
     actual = hashlib.sha256(data).hexdigest()
-    return body + (
-        "\n## Seal\n\n"
-        "- Body definition: test fixture.\n"
-        f"- Body bytes: `{len(data) + size_delta}`.\n"
-        f"- Body SHA-256: `{digest or actual}`.\n"
-        f"- Frozen basis: `{BASIS}`.\n"
-    )
+    return (
+        data
+        + SEAL_MODULE._canonical_seal(
+            len(data) + size_delta,
+            digest or actual,
+            BASIS,
+        )
+    ).decode("utf-8")
 
 
 class SealTest(unittest.TestCase):
@@ -131,20 +132,19 @@
         self.assertIn("declared", wrong.stderr)
         self.assertIn("expected", wrong.stderr)
 
-    def test_crlf_body_and_post_body_metadata(self) -> None:
+    def test_crlf_body_uses_canonical_lf_seal(self) -> None:
         body = b"# CRLF\r\n\r\n<!-- BODY-END -->\r\n"
         digest = hashlib.sha256(body).hexdigest()
-        post = (
-            "\r\n## Seal\r\n\r\n"
-            "- Body definition: test fixture.\r\n"
-            f"- Body bytes: `{len(body)}`.\r\n"
-            f"- Body SHA-256: `{digest}`.\r\n"
-            f"- Frozen basis: `{BASIS}`.\r\n"
-        ).encode("utf-8")
+        post = SEAL_MODULE._canonical_seal(len(body), digest, BASIS)
         path = self.make_file("placeholder")
         path.write_bytes(body + post)
         result = run("verify", "--expected-basis", BASIS, str(path))
         self.assertEqual(result.returncode, 0, result.stderr)
+
+        path.write_bytes(body + post.replace(b"\n", b"\r\n"))
+        noncanonical = run("verify", "--expected-basis", BASIS, str(path))
+        self.assertNotEqual(noncanonical.returncode, 0)
+        self.assertIn("canonical LF serialization", noncanonical.stderr)
 
     def test_missing_and_duplicate_metadata_fail(self) -> None:
         body = "# Metadata\n\n" + MARKER
@@ -287,6 +287,30 @@
         self.assertEqual(path.read_text(encoding="utf-8"), sealed(body))
         self.assertFalse(overflow.exists())
         self.assertFalse(raw.exists())
+
+    def test_canonical_seal_with_suffix_is_diverted(self) -> None:
+        body = "# report\n\nVERDICT: CONFIRMED\n\n" + MARKER
+        body_bytes = body.encode("utf-8")
+        suffix = b"503 upstream timeout\n"
+        original = sealed(body).encode("utf-8") + suffix
+        tail = original[len(body_bytes):]
+        path = self.make_file("placeholder")
+        path.write_bytes(original)
+
+        verified = run("verify", str(path))
+        self.assertNotEqual(verified.returncode, 0)
+        result, overflow, raw = self.divert(path)
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assertIn("status=DIVERTED", result.stdout)
+        self.assertEqual(path.read_bytes(), body_bytes)
+        self.assertEqual(overflow.read_bytes(), tail)
+        self.assertEqual(raw.read_bytes(), original)
+        self.assertIn(
+            f"overflow_sha256={hashlib.sha256(tail).hexdigest()}", result.stdout
+        )
+        self.assertIn(
+            f"raw_sha256={hashlib.sha256(original).hexdigest()}", result.stdout
+        )
 
     def test_overflow_is_diverted_with_exact_hashes(self) -> None:
         body = "# report\n\nVERDICT: CONFIRMED\n\n" + MARKER
@@ -306,6 +330,32 @@
         self.assertIn(f"overflow_sha256={tail_sha}", result.stdout)
         self.assertIn(f"raw_sha256={raw_sha}", result.stdout)
 
+    def test_unterminated_marker_is_typed_and_untouched(self) -> None:
+        original = "# report\n\n<!-- BODY-END -->"
+        path = self.make_file(original)
+        result, overflow, raw = self.divert(path)
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assertIn("status=UNTERMINATED_MARKER", result.stdout)
+        self.assertEqual(path.read_text(encoding="utf-8"), original)
+        self.assertFalse(overflow.exists())
+        self.assertFalse(raw.exists())
+
+    def test_crlf_marker_divert_preserves_exact_boundary(self) -> None:
+        body = b"# report\r\n\r\n<!-- BODY-END -->\r\n"
+        tail = b"provider timeout\r\n"
+        original = body + tail
+        path = self.make_file("placeholder")
+        path.write_bytes(original)
+        result, overflow, raw = self.divert(path)
+        self.assertEqual(result.returncode, 0, result.stderr)
+        self.assertIn("status=DIVERTED", result.stdout)
+        self.assertEqual(path.read_bytes(), body)
+        self.assertEqual(overflow.read_bytes(), tail)
+        self.assertEqual(raw.read_bytes(), original)
+        self.assertIn(
+            f"body_sha256={hashlib.sha256(body).hexdigest()}", result.stdout
+        )
+
     def test_zero_and_multiple_markers_are_reported_not_repaired(self) -> None:
         no_marker = self.make_file("# partial draft without a marker\n")
         result, overflow, raw = self.divert(no_marker)
@@ -337,6 +387,43 @@
         self.assertIn("cannot create", result.stderr)
         self.assertEqual(path.read_text(encoding="utf-8"), body + "tail\n")
         self.assertEqual(overflow.read_text(encoding="utf-8"), "occupied\n")
+        self.assertFalse(raw.exists())
+
+    def test_change_before_replace_is_reclassified(self) -> None:
+        body = ("# report\n\n" + MARKER).encode("utf-8")
+        first_tail = b"first provider error\n"
+        late_tail = b"late provider error\n"
+        path = self.make_file("placeholder")
+        path.write_bytes(body + first_tail)
+        overflow = path.parent / "report.overflow"
+        raw = path.parent / "report.raw.md"
+        original_read = SEAL_MODULE._read_regular_at
+        calls = 0
+
+        def raced_read(parent_fd: int, name: str):
+            nonlocal calls
+            calls += 1
+            if calls == 2:
+                fd = os.open(name, os.O_WRONLY | os.O_APPEND, dir_fd=parent_fd)
+                with os.fdopen(fd, "ab") as handle:
+                    handle.write(late_tail)
+            return original_read(parent_fd, name)
+
+        with mock.patch.object(
+            SEAL_MODULE, "_read_regular_at", side_effect=raced_read
+        ):
+            result = SEAL_MODULE.divert_path(path, overflow, raw)
+        original = body + first_tail + late_tail
+        self.assertEqual(result["status"], "DIVERTED")
+        self.assertEqual(path.read_bytes(), body)
+        self.assertEqual(overflow.read_bytes(), first_tail + late_tail)
+        self.assertEqual(raw.read_bytes(), original)
+        self.assertEqual(result["raw_sha256"], hashlib.sha256(original).hexdigest())
+        self.assertEqual(
+            result["overflow_sha256"],
+            hashlib.sha256(first_tail + late_tail).hexdigest(),
+        )
+        self.assertEqual(list(path.parent.glob(f".{path.name}.seal-*")), [])
 
     def test_optimized_mode_matches(self) -> None:
         body = "# report\n\n" + MARKER
```

# Test inventory

- `test_exact_appendix_delivery_hashes_and_cleanup` — changed to assert the additive `adapter_exit_code=0` receipt field on an ordinary successful lane.
- `test_prompt_without_report_path_is_refused` — changed to require the uniform launch-time contract rc 7 and no adapter run or receipt.
- `test_charged_input_contract_fails_closed` — changed to require rc 7 and expanded with `./jc2-lean`, uppercase `JC2-LEAN`, exact `.` component, absolute path, and charged-path control-character cases, while retaining the declaration/placeholder, missing-file, literal exclusion, and `..` cases.
- `test_non_ascii_charged_input_is_refused_under_utf8_locale` — new; supplies a real non-ASCII charged file under `en_US.UTF-8` and verifies bytewise rejection with rc 7 before launch or receipt.
- `test_charged_input_ancestor_symlink_is_refused` — new; verifies an intermediate directory symlink is rejected without adapter execution or receipt creation.
- `test_casefolded_charged_input_basenames_are_refused` — new; verifies differently cased basenames from separate directories collide under the explicit folded uniqueness key on any filesystem.
- `test_prompt_path_control_characters_are_refused` — new; verifies LF, CR, tab, DEL, NEL, Unicode line/paragraph separators, and a bidi format control in a real prompt filename all return 7 without reflecting injected text or creating a receipt.
- `test_unterminated_marker_is_partial_contract_failure` — new; drives an EOF marker without newline through the lane and asserts `UNTERMINATED_MARKER`, `PARTIAL_NO_MARKER`, adapter rc 0, final rc 7, unchanged report hash, failed final status, and no sidecars.
- `test_boundary_failure_overrides_nonzero_adapter_exit` — new; verifies a markerless declared-contract report from an adapter exiting 23 records `adapter_exit_code=23` but forces receipt/process `exit_code=7` and partial failed state.
- `test_crlf_body_uses_canonical_lf_seal` — replaces the prior permissive CRLF-metadata test; it accepts a CRLF body/marker with the exact LF seal and rejects a CRLF-encoded post-body seal.
- `test_canonically_sealed_report_is_untouched` — its shared fixture now uses the real `_canonical_seal` serialization, so `CLEAN_SEALED` is exercised only by canonical bytes.
- `test_canonical_seal_with_suffix_is_diverted` — new; verifies a valid canonical seal plus a provider-error line fails verification and diverts to a body-only report, byte-exact complete-tail overflow, and byte-exact raw bank with matching hashes.
- `test_unterminated_marker_is_typed_and_untouched` — new; verifies divert returns `UNTERMINATED_MARKER` without changing the report or creating raw/overflow files.
- `test_crlf_marker_divert_preserves_exact_boundary` — new; verifies the CRLF marker terminator stays in the charged body/hash and raw/overflow bytes split exactly after it.
- `test_existing_overflow_target_fails_exclusively` — changed to assert that the failed attempt leaves no newly created raw file while preserving both the report and occupied overflow.
- `test_change_before_replace_is_reclassified` — new; injects a late same-inode append at the immediate reread and verifies stale sidecars are removed, the enlarged overflow is reclassified and banked, and no temp file leaks.

<!-- BODY-END -->
