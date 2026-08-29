#!/usr/bin/env python3
"""Bounded hostile fixtures for the D43 v4 custody contract.

These fixtures are macOS-portable: live-kernel readers take injected proc
roots, meminfo files, and cgroup directories, and the kernel flock fixtures
hold the lease from a real subprocess.  Unit-test assertions may be
assertions; every production check under test is an explicit exception.

Relative to v3 this suite additionally covers the Opus 5 v3 hostile-review
repair set: the terminal's value binding of every payload-bearing candidate
field (the v3 suite's happy-path fixture carried fabricated digests and
thereby enshrined the copy-through; the v4 fixture is honest), the
sidecar-named archive rehash, full-member-set archive census including
directory members, the real-PGID and mode-consistent cgroup gates, and the
authority-bearing launcher post-mortem gate.
"""

import argparse
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "d43_job_contract_v4", HERE / "job_contract_v4.py")
CONTRACT = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = CONTRACT
spec.loader.exec_module(CONTRACT)

CLI = [sys.executable, "-B", str(HERE / "job_contract_v4.py")]
NONCE = "ab" * 32
ARCHIVE_SHA = "cd" * 32

HOLDER_SCRIPT = r"""
exec 9>>"$1"
python3 -c 'import fcntl; fcntl.flock(9, fcntl.LOCK_EX | fcntl.LOCK_NB)' \
  || exit 9
if [ -n "$2" ]; then
  eval "$2" || exit 8
fi
echo HELD
exec sleep 120
"""


def run_cli(*args, expect=None):
    result = subprocess.run(CLI + [str(a) for a in args],
                            capture_output=True, text=True)
    if expect is not None and result.returncode != expect:
        raise AssertionError("rc=%d stdout=%r stderr=%r" % (
            result.returncode, result.stdout, result.stderr))
    return result


def write_json(path: Path, value) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=1, sort_keys=True) + "\n")
    return CONTRACT.sha256_path(path)


def make_proc_entry(proc_root: Path, pid: int, state="S", ppid=1, pgid=None,
                    sid=None, starttime=100, uid=None, job_tag=None,
                    rss_kib=100):
    pgid = pid if pgid is None else pgid
    sid = pid if sid is None else sid
    uid = os.getuid() if uid is None else uid
    entry = proc_root / str(pid)
    entry.mkdir(parents=True, exist_ok=True)
    tail = [state, str(ppid), str(pgid), str(sid), "0", "-1", "4194304"]
    tail += ["0"] * 12
    tail += [str(starttime), "0", "0"]
    (entry / "stat").write_text(
        "%d (proc%d) %s\n" % (pid, pid, " ".join(tail)))
    (entry / "status").write_text(
        "Name:\tproc%d\nUid:\t%d\t%d\t%d\t%d\nVmRSS:\t%d kB\n" %
        (pid, uid, uid, uid, uid, rss_kib))
    environ = b"PATH=/usr/bin\0"
    if job_tag is not None:
        environ += b"JOB_TAG=" + job_tag.encode() + b"\0"
    (entry / "environ").write_bytes(environ)
    (entry / "cmdline").write_bytes(b"python3\0proc%d\0" % pid)
    return entry


class LeaseHolder:
    """Hold the exclusive kernel flock from a real subprocess."""

    def __init__(self, lock_path: Path, inner_command=""):
        self.process = subprocess.Popen(
            ["/bin/bash", "-c", HOLDER_SCRIPT, "holder",
             str(lock_path), inner_command],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        line = self.process.stdout.readline().strip()
        if line != "HELD":
            stderr = self.process.stderr.read()
            raise AssertionError("holder failed: %r / %r" % (line, stderr))

    def release(self):
        if self.process.poll() is None:
            self.process.terminate()
        self.process.wait()
        self.process.stdout.close()
        self.process.stderr.close()


class LeaseTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.lock = self.tmp / "host.lock"

    def test_probe_and_duplicate_launch_flock(self):
        self.assertFalse(CONTRACT.probe_lock_held(self.lock))
        holder = LeaseHolder(self.lock)
        try:
            self.assertTrue(CONTRACT.probe_lock_held(self.lock))
            run_cli("lease-probe", "--lock-path", self.lock, expect=0)
            # A duplicate launcher's nonblocking acquisition must fail.
            duplicate = subprocess.run(
                ["/bin/bash", "-c",
                 'exec 8>>"$1"; exec "$2" -B "$3" lease-flock --fd 8',
                 "dup", str(self.lock), sys.executable,
                 str(HERE / "job_contract_v4.py")],
                capture_output=True, text=True)
            self.assertEqual(duplicate.returncode, 1)
            self.assertIn("LEASE_FLOCK_ACQUIRED=0", duplicate.stdout)
        finally:
            holder.release()
        self.assertFalse(CONTRACT.probe_lock_held(self.lock))
        run_cli("lease-probe", "--lock-path", self.lock, expect=1)

    def record_lease(self):
        job_root = self.tmp / "job-tag-1"
        job_root.mkdir(exist_ok=True)
        registration = job_root / "records" / "REGISTERED.json"
        registration.parent.mkdir(parents=True, exist_ok=True)
        registration.write_text('{"stub": true}\n')
        proc_root = self.tmp / "proc"
        make_proc_entry(proc_root, 4242)
        inner = (
            '"%s" -B "%s" lease-record --fd 9 --lock-path "%s" '
            '--job-root "%s" --job-tag job-tag-1 --archive-sha256 %s '
            '--registration "%s" --launcher-path "%s" --launcher-pid 4242 '
            '--proc-root "%s" --output "%s" > "%s"'
            % (sys.executable, HERE / "job_contract_v4.py", self.lock,
               job_root, ARCHIVE_SHA, registration,
               HERE / "job_contract_v4.py", proc_root,
               job_root / "RUN_LEASE.json", self.tmp / "nonce.txt"))
        holder = LeaseHolder(self.lock, inner)
        self.addCleanup(holder.release)
        return job_root, holder

    def test_lease_record_and_verify_and_mutations(self):
        job_root, holder = self.record_lease()
        lease_path = job_root / "RUN_LEASE.json"
        lease = json.loads(lease_path.read_text())
        nonce = (self.tmp / "nonce.txt").read_text().strip()
        self.assertEqual(lease["run_nonce"], nonce)
        self.assertEqual(len(nonce), 64)
        self.assertEqual(lease["source_archive_sha256"], ARCHIVE_SHA)
        self.assertIs(lease["terminal_authority"], False)
        verified = CONTRACT.verify_lease(lease_path, job_root, "job-tag-1",
                                         expect_nonce=nonce)
        self.assertEqual(verified["run_nonce"], nonce)
        run_cli("verify-lease", "--lease", lease_path, "--job-root",
                job_root, "--job-tag", "job-tag-1", "--expect-nonce",
                nonce, expect=0)
        for mutate in (
                lambda d: d.update(schema="FORGED"),
                lambda d: d.update(run_nonce="00" * 32),
                lambda d: d.update(job_tag="other-tag"),
                lambda d: d.update(job_root="/elsewhere"),
                lambda d: d.update(terminal_authority=True),
                lambda d: d.update(lock_dev_ino=[1, 2]),
                lambda d: d.pop("launcher")):
            forged = json.loads(lease_path.read_text())
            mutate(forged)
            forged_path = self.tmp / "forged_lease.json"
            forged_path.write_text(json.dumps(forged))
            with self.assertRaises(CONTRACT.CustodyError):
                CONTRACT.verify_lease(forged_path, job_root, "job-tag-1",
                                      expect_nonce=nonce)
        # Releasing the lease must make verification fail (lock not held).
        holder.release()
        with self.assertRaises(CONTRACT.CustodyError):
            CONTRACT.verify_lease(lease_path, job_root, "job-tag-1",
                                  expect_nonce=nonce)


class FreshNamespaceTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        (self.tmp / "source").mkdir()
        records = self.tmp / "records"
        records.mkdir()
        (records / "REGISTERED.json").write_text("{}\n")
        (records / "LAUNCH.json").write_text("{}\n")
        (records / "launch_extract.stderr.txt").write_text("")
        (self.tmp / "RUN_LEASE.json").write_text("{}\n")

    def test_fresh_namespace_passes(self):
        CONTRACT.verify_fresh_namespace(self.tmp)

    def test_stale_artifacts_refused(self):
        cases = {
            "TERMINAL.json": lambda: (self.tmp / "TERMINAL.json")
                .write_text("{}"),
            "output": lambda: (self.tmp / "output").mkdir(),
            "custody": lambda: (self.tmp / "custody").mkdir(),
            "stray": lambda: (self.tmp / "stray.txt").write_text("x"),
            "archive": lambda: (self.tmp / "old.terminal.tar.gz")
                .write_text("x"),
            "record": lambda: (self.tmp / "records" / "PREFLIGHT.json")
                .write_text("{}"),
        }
        for name, plant in cases.items():
            plant()
            with self.assertRaises(CONTRACT.CustodyError, msg=name):
                CONTRACT.verify_fresh_namespace(self.tmp)
            target = {"output": self.tmp / "output",
                      "custody": self.tmp / "custody"}.get(name)
            if target:
                target.rmdir()
            elif name == "TERMINAL.json":
                (self.tmp / "TERMINAL.json").unlink()
            elif name == "stray":
                (self.tmp / "stray.txt").unlink()
            elif name == "archive":
                (self.tmp / "old.terminal.tar.gz").unlink()
            elif name == "record":
                (self.tmp / "records" / "PREFLIGHT.json").unlink()
        CONTRACT.verify_fresh_namespace(self.tmp)


class ProcCensusTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.proc = self.tmp / "proc"

    def test_identity_census_and_tag_census(self):
        make_proc_entry(self.proc, 100, pgid=100, sid=100)
        make_proc_entry(self.proc, 101, ppid=100, pgid=100, sid=100,
                        job_tag="tag-A")
        make_proc_entry(self.proc, 102, pgid=200, sid=200, job_tag="tag-A")
        make_proc_entry(self.proc, 103, pgid=300, sid=300, job_tag="tag-B")
        identity = CONTRACT.read_identity(101, self.proc)
        self.assertEqual((identity["ppid"], identity["pgid"],
                          identity["starttime"]), (100, 100, 100))
        pgid_records, tag_records = CONTRACT.process_records(
            100, "tag-A", set(), self.proc)
        self.assertEqual([r["pid"] for r in pgid_records], [100, 101])
        self.assertEqual([r["pid"] for r in tag_records], [101, 102])
        _, tag_b = CONTRACT.process_records(0, "tag-B", set(), self.proc)
        self.assertEqual([r["pid"] for r in tag_b], [103])

    def test_signal_exact_refuses_identity_drift(self):
        make_proc_entry(self.proc, 100, starttime=500)
        sent = []
        CONTRACT.signal_exact({"pid": 100, "starttime": 500}, 15,
                              self.proc, kill=lambda p, s: sent.append(p))
        self.assertEqual(sent, [100])
        with self.assertRaises(CONTRACT.CustodyError):
            CONTRACT.signal_exact({"pid": 100, "starttime": 501}, 15,
                                  self.proc,
                                  kill=lambda p, s: sent.append(p))
        self.assertEqual(sent, [100])

    def test_kill_tree_reaps_descendants_and_detects_orphans(self):
        make_proc_entry(self.proc, 200, starttime=7)
        make_proc_entry(self.proc, 201, ppid=200)
        make_proc_entry(self.proc, 202, ppid=201)
        make_proc_entry(self.proc, 300)  # unrelated survivor

        def lethal(pid, sig):
            shutil.rmtree(self.proc / str(pid), ignore_errors=True)

        census = self.tmp / "census.json"
        clean = CONTRACT.kill_tree(200, 7, census, self.proc, kill=lethal,
                                   pause=0.01)
        self.assertTrue(clean)
        self.assertEqual(json.loads(census.read_text()), [])
        self.assertTrue((self.proc / "300").exists())
        # An unkillable subtree is a detected orphan, never silently clean.
        make_proc_entry(self.proc, 400, starttime=9)
        make_proc_entry(self.proc, 401, ppid=400)
        clean = CONTRACT.kill_tree(400, 9, census, self.proc,
                                   kill=lambda p, s: None, pause=0.01)
        self.assertFalse(clean)
        survivors = [r["pid"] for r in json.loads(census.read_text())]
        self.assertEqual(survivors, [401, 400])

    def test_cleanup_census_terminates_and_reports(self):
        make_proc_entry(self.proc, 500, pgid=500, job_tag="tag-C")
        make_proc_entry(self.proc, 501, pgid=500)

        def lethal(pid, sig):
            shutil.rmtree(self.proc / str(pid), ignore_errors=True)

        clean = CONTRACT.terminate_and_census(
            500, "tag-C", set(), self.tmp / "pgid.json",
            self.tmp / "tag.json", self.proc, kill=lethal)
        self.assertTrue(clean)
        self.assertEqual(json.loads((self.tmp / "pgid.json").read_text()), [])
        self.assertEqual(json.loads((self.tmp / "tag.json").read_text()), [])

    def test_cgroup_census_strict_parse(self):
        procs = self.tmp / "cgroup.procs"
        procs.write_text("\n")
        self.assertEqual(CONTRACT.parse_cgroup_procs(procs), [])
        procs.write_text("123\n456\n")
        self.assertEqual(CONTRACT.parse_cgroup_procs(procs), [123, 456])
        for bad in ("0\n", "-5\n", "0x10\n", "12a\n", "١٢\n"):
            procs.write_text(bad)
            with self.assertRaises(CONTRACT.CustodyError):
                CONTRACT.parse_cgroup_procs(procs)
        procs.write_text("123\n999\n")
        result = run_cli("cgroup-census", "--path", procs, "--allow-pid",
                         "123", "--output", self.tmp / "cg.json")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads((self.tmp / "cg.json").read_text()),
                         [999])
        result = run_cli("cgroup-census", "--path", procs, "--allow-pid",
                         "123", "--allow-pid", "999", "--output",
                         self.tmp / "cg.json", expect=0)
        self.assertIn("CGROUP_PROCS_EMPTY=1", result.stdout)


def monitor_args(tmp: Path, **overrides):
    values = dict(
        interval=0.01, deadline_epoch=time.time() + 3600,
        memory_max_bytes=1000000, pids_max=16,
        meminfo=str(tmp / "meminfo"), cgroup_dir=None, pgid=0,
        telemetry=tmp / "telemetry.tsv", heartbeat=tmp / "heartbeat.json",
        peak_output=tmp / "peak.json", violations_dir=tmp / "violations",
        watch_ppid=0, kill_on_parent_death="none", max_ticks=2,
        proc_root=tmp / "proc")
    values.update(overrides)
    return argparse.Namespace(**values)


def write_meminfo(tmp: Path, swap_total=0, swap_free=0):
    (tmp / "meminfo").write_text(
        "MemTotal:       1000000 kB\nMemAvailable:    900000 kB\n"
        "SwapTotal:      %d kB\nSwapFree:       %d kB\n"
        % (swap_total, swap_free))


def write_cgroup(tmp: Path, memory=1000, swap=0, pids=2, oom_kill=0):
    cg = tmp / "cgroup"
    cg.mkdir(exist_ok=True)
    (cg / "memory.current").write_text("%d\n" % memory)
    (cg / "memory.swap.current").write_text("%d\n" % swap)
    (cg / "pids.current").write_text("%d\n" % pids)
    (cg / "memory.events").write_text(
        "low 0\nhigh 0\nmax 0\noom 0\noom_kill %d\n" % oom_kill)
    return cg


class MonitorTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        write_meminfo(self.tmp)

    def violations(self):
        return sorted(p.name for p in (self.tmp / "violations").iterdir())

    def test_clean_run_writes_receipts_and_no_violations(self):
        cg = write_cgroup(self.tmp)
        rc = CONTRACT.run_monitor(monitor_args(self.tmp, cgroup_dir=str(cg)))
        self.assertEqual(rc, 0)
        self.assertEqual(self.violations(), [])
        beat = json.loads((self.tmp / "heartbeat.json").read_text())
        self.assertEqual(beat["tick"], 2)
        peak = json.loads((self.tmp / "peak.json").read_text())
        self.assertEqual(peak["peak_cgroup_memory_bytes"], 1000)
        self.assertTrue((self.tmp / "telemetry.tsv").read_text()
                        .startswith("utc\t"))

    def test_transient_swap_is_sticky(self):
        write_meminfo(self.tmp, swap_total=1024, swap_free=512)
        rc = CONTRACT.run_monitor(monitor_args(self.tmp))
        self.assertEqual(rc, 0)
        self.assertIn("v_HOST_SWAP_NONZERO.json", self.violations())
        # Swap returns to zero: the latch must survive a later clean pass.
        write_meminfo(self.tmp)
        rc = CONTRACT.run_monitor(monitor_args(self.tmp))
        self.assertEqual(rc, 0)
        self.assertIn("v_HOST_SWAP_NONZERO.json", self.violations())
        result = run_cli("violations-census", "--dir",
                         self.tmp / "violations", "--output",
                         self.tmp / "census.json")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads((self.tmp / "census.json").read_text()),
                         ["v_HOST_SWAP_NONZERO.json"])

    def test_timeout_oom_memory_pids_latches(self):
        cg = write_cgroup(self.tmp, memory=2000000, swap=3, pids=99,
                          oom_kill=1)
        rc = CONTRACT.run_monitor(monitor_args(
            self.tmp, cgroup_dir=str(cg), deadline_epoch=time.time() - 1))
        self.assertEqual(rc, 0)
        names = self.violations()
        for expected in ("v_CGROUP_MEMORY_OVER_MAX.json",
                         "v_CGROUP_SWAP_NONZERO.json",
                         "v_CGROUP_PIDS_OVER_MAX.json",
                         "v_OOM_KILL_OBSERVED.json",
                         "v_WHOLE_TIMEOUT.json"):
            self.assertIn(expected, names)

    def test_unreadable_cgroup_fails_closed(self):
        cg = self.tmp / "cgroup"
        cg.mkdir()
        rc = CONTRACT.run_monitor(monitor_args(self.tmp, cgroup_dir=str(cg)))
        self.assertEqual(rc, 0)
        self.assertIn("v_CGROUP_MEMORY_UNREADABLE.json", self.violations())

    def test_supervisor_death_detected(self):
        rc = CONTRACT.run_monitor(monitor_args(
            self.tmp, watch_ppid=os.getppid() + 12345, max_ticks=5))
        self.assertEqual(rc, 3)
        self.assertIn("v_SUPERVISOR_DIED.json", self.violations())

    def test_aggregate_pgid_rss(self):
        proc = self.tmp / "proc"
        make_proc_entry(proc, 700, pgid=77, rss_kib=600)
        make_proc_entry(proc, 701, pgid=77, rss_kib=500)
        make_proc_entry(proc, 702, pgid=78, rss_kib=100000)
        rc = CONTRACT.run_monitor(monitor_args(
            self.tmp, pgid=77, memory_max_bytes=1024 * 1024))
        self.assertEqual(rc, 0)
        self.assertIn("v_AGGREGATE_RSS_OVER_MAX.json", self.violations())
        payload = json.loads(
            (self.tmp / "violations" / "v_AGGREGATE_RSS_OVER_MAX.json")
            .read_text())
        self.assertEqual(payload["aggregate_rss_kib"], 1100)


class ArchiveTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.root = self.tmp / "root"
        (self.root / "data").mkdir(parents=True)
        (self.root / "data" / "a.txt").write_text("alpha\n")
        (self.root / "data" / "b.txt").write_text("beta\n")
        (self.root / "meta").mkdir()
        self.manifest = self.root / "meta" / "MANIFEST.sha256"
        CONTRACT.build_complete_manifest(self.root, self.manifest,
                                         ["data"])

    def build(self, output):
        return CONTRACT.build_deterministic_archive(
            self.root, self.manifest, "meta/MANIFEST.sha256", output)

    def test_manifest_verify_and_census_drift(self):
        count = CONTRACT.verify_complete_manifest(self.root, self.manifest,
                                                  ["data"])
        self.assertEqual(count, 2)
        (self.root / "data" / "c.txt").write_text("gamma\n")
        with self.assertRaisesRegex(CONTRACT.CustodyError, "CENSUS_DRIFT"):
            CONTRACT.verify_complete_manifest(self.root, self.manifest,
                                              ["data"])
        (self.root / "data" / "c.txt").unlink()
        (self.root / "data" / "a.txt").write_text("tampered\n")
        with self.assertRaisesRegex(CONTRACT.CustodyError, "HASH_DRIFT"):
            CONTRACT.verify_complete_manifest(self.root, self.manifest,
                                              ["data"])

    def test_deterministic_rebuild_and_replay(self):
        first = self.build(self.tmp / "one.tar.gz")
        time.sleep(1.1)  # a different wall clock must not change the bytes
        (self.root / "data" / "a.txt").touch()
        second = self.build(self.tmp / "two.tar.gz")
        self.assertEqual(first, second)
        count = CONTRACT.extract_and_verify_archive(
            self.tmp / "one.tar.gz", self.tmp / "replay",
            "meta/MANIFEST.sha256", ["data", "meta"])
        self.assertEqual(count, 2)
        self.assertEqual((self.tmp / "replay" / "data" / "a.txt")
                         .read_text(), "alpha\n")
        with self.assertRaisesRegex(CONTRACT.CustodyError,
                                    "DESTINATION_EXISTS"):
            CONTRACT.extract_and_verify_archive(
                self.tmp / "one.tar.gz", self.tmp / "replay",
                "meta/MANIFEST.sha256", ["data", "meta"])

    def test_archive_build_refuses_source_drift(self):
        (self.root / "data" / "a.txt").write_text("tampered\n")
        with self.assertRaisesRegex(CONTRACT.CustodyError,
                                    "ARCHIVE_SOURCE_HASH_DRIFT"):
            self.build(self.tmp / "bad.tar.gz")

    def hostile_archive(self, mutate):
        path = self.tmp / "hostile.tar.gz"
        base = self.tmp / "base.tar.gz"
        self.build(base)
        with tarfile.open(base, "r:gz") as source:
            members = [(m, source.extractfile(m).read()) for m in
                       source.getmembers()]
        with tarfile.open(path, "w:gz") as out:
            mutate(out, members)
        return path

    def replay(self, path):
        destination = self.tmp / ("replay_%d" % time.monotonic_ns())
        return CONTRACT.extract_and_verify_archive(
            path, destination, "meta/MANIFEST.sha256", ["data", "meta"])

    @staticmethod
    def passthrough(out, members):
        for member, data in members:
            out.addfile(member, io.BytesIO(data))

    def test_unsafe_members_refused(self):
        def with_traversal(out, members):
            self.passthrough(out, members)
            info = tarfile.TarInfo("data/../../evil.txt")
            info.size = 4
            out.addfile(info, io.BytesIO(b"evil"))

        def with_absolute(out, members):
            self.passthrough(out, members)
            info = tarfile.TarInfo("/evil.txt")
            info.size = 4
            out.addfile(info, io.BytesIO(b"evil"))

        def with_symlink(out, members):
            self.passthrough(out, members)
            info = tarfile.TarInfo("data/link")
            info.type = tarfile.SYMTYPE
            info.linkname = "/etc/passwd"
            out.addfile(info)

        def with_duplicate(out, members):
            self.passthrough(out, members)
            member, data = members[0]
            out.addfile(member, io.BytesIO(data))

        def with_extra(out, members):
            self.passthrough(out, members)
            info = tarfile.TarInfo("data/extra.txt")
            info.size = 5
            out.addfile(info, io.BytesIO(b"extra"))

        def without_manifest(out, members):
            for member, data in members:
                if member.name != "meta/MANIFEST.sha256":
                    out.addfile(member, io.BytesIO(data))

        def tampered_payload(out, members):
            for member, data in members:
                if member.name == "data/a.txt":
                    data = b"tampered\n"
                    member.size = len(data)
                out.addfile(member, io.BytesIO(data))

        cases = {
            "traversal": with_traversal,
            "absolute": with_absolute,
            "symlink": with_symlink,
            "duplicate": with_duplicate,
            "extra": with_extra,
            "no-manifest": without_manifest,
            "tampered": tampered_payload,
        }
        for name, mutate in cases.items():
            hostile = self.hostile_archive(mutate)
            with self.assertRaises(CONTRACT.CustodyError, msg=name):
                self.replay(hostile)

    def test_directory_members_refused(self):
        """The v3 census accepted directory members (Opus 5 Finding 2);
        the v4 full-member-set census refuses them outright."""
        def with_directory(out, members):
            self.passthrough(out, members)
            info = tarfile.TarInfo("data/extradir")
            info.type = tarfile.DIRTYPE
            out.addfile(info)

        def with_nested_chain(out, members):
            self.passthrough(out, members)
            for name in ("data/d1", "data/d1/d2", "data/d1/d2/d3"):
                info = tarfile.TarInfo(name)
                info.type = tarfile.DIRTYPE
                out.addfile(info)

        for name, mutate in (("directory", with_directory),
                             ("nested-chain", with_nested_chain)):
            hostile = self.hostile_archive(mutate)
            with self.assertRaisesRegex(CONTRACT.CustodyError,
                                        "ARCHIVE_NONREGULAR_MEMBER",
                                        msg=name):
                self.replay(hostile)

    def test_corrupt_outer_bytes_refused(self):
        path = self.tmp / "corrupt.tar.gz"
        self.build(path)
        raw = bytearray(path.read_bytes())
        raw[len(raw) // 2] ^= 0xFF
        path.write_bytes(bytes(raw))
        with self.assertRaises(Exception):
            self.replay(path)


CLAIM_BOUNDARY = {
    "JC2_counterexample": None,
    "Keller_map": None,
    "all_depth_compatibility": None,
    "banked_NF_presentation_equivalence": None,
    "displayed_E5_E6_unit_extension":
        "E plus one W1*W2 unit equation, with mandatory literal HM/s1F "
        "reconstruction replay; not imposed by row emission",
    "exact_a00pp_raw_J_point": None,
    "full_residue_A_template_point": None,
    "exact_a00pp_row_emitter": None,
}

INVENTORY = {
    "live_rows": 29,
    "exact_zero_rows": 155,
    "live_bands": {"20": 10, "30": 9, "40": 10},
    "max_tail_degree": 2,
    "exact_zero_targets": [[0, index] for index in range(155)],
}

SEMANTIC_SHA = "5e" * 32
TEMPLATE_BRIDGE_SHA = "7a" * 32


class TerminalDecisionTest(unittest.TestCase):
    """Every mandatory latch flips the single terminal authority, and every
    payload-bearing candidate field is recomputed or bound, never copied.

    Unlike the v3 suite (whose happy-path candidate carried fabricated
    digests ``"11"*32 ... "66"*32`` and a sidecar naming a nonexistent
    archive), this fixture builds a fully honest artifact chain: every
    digest in the candidate is the real digest of a real on-disk artifact,
    and the sidecar names a real archive that rehashes to its digest.
    """

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp()).resolve()
        cls.lock = cls.tmp / "host.lock"
        cls.job_root = cls.tmp / "job-tag-9"
        cls.job_root.mkdir()
        cls.records = cls.job_root / "records"
        cls.records.mkdir()
        cls.output = cls.job_root / "output"
        cls.output.mkdir()
        cls.registration = cls.records / "REGISTERED.json"
        cls.registration.write_text('{"stub": true}\n')
        proc_root = cls.tmp / "proc"
        make_proc_entry(proc_root, 4242)
        inner = (
            '"%s" -B "%s" lease-record --fd 9 --lock-path "%s" '
            '--job-root "%s" --job-tag job-tag-9 --archive-sha256 %s '
            '--registration "%s" --launcher-path "%s" --launcher-pid 4242 '
            '--proc-root "%s" --output "%s" > /dev/null'
            % (sys.executable, HERE / "job_contract_v4.py", cls.lock,
               cls.job_root, ARCHIVE_SHA, cls.registration,
               HERE / "job_contract_v4.py", proc_root,
               cls.job_root / "RUN_LEASE.json"))
        cls.holder = LeaseHolder(cls.lock, inner)
        cls.lease_path = cls.job_root / "RUN_LEASE.json"
        cls.nonce = json.loads(cls.lease_path.read_text())["run_nonce"]
        cls.lease_sha = CONTRACT.sha256_path(cls.lease_path)

        # Honest artifact chain, in dependency order.
        cls.manifest_path = cls.job_root / "PIPELINE_MANIFEST.json"
        cls.manifest_sha = write_json(cls.manifest_path, {
            "schema": CONTRACT.MANIFEST_SCHEMA,
            "claim_boundary": CLAIM_BOUNDARY,
        })
        cls.preflight_path = cls.records / "PREFLIGHT.json"
        cls.preflight_sha = write_json(cls.preflight_path, {
            "schema": "jc2.d43.a00pp-exact-source-rows.v4.aws-preflight",
            "pass": True,
            "terminal_authority": False,
            "manifest_sha256": cls.manifest_sha,
        })
        cls.pilot_path = cls.output / "PILOT_GATE.json"
        cls.pilot_sha = write_json(cls.pilot_path, {
            "status": CONTRACT.PILOT_PASS_STATUS,
            "terminal_authority": False,
            "run_nonce": cls.nonce,
            "manifest_sha256": cls.manifest_sha,
        })
        cls.merge_payload_path = (cls.output /
                                  "d43_a00pp_exact_184_raw_J_rows.pkl")
        cls.merge_payload_path.write_bytes(b"MERGE_PAYLOAD_STUB_BYTES\n")
        cls.merge_payload_sha = CONTRACT.sha256_path(cls.merge_payload_path)
        cls.merge_receipt_path = cls.output / "MERGE_RECEIPT.json"
        cls.merge_receipt_sha = write_json(cls.merge_receipt_path, {
            "schema": CONTRACT.MERGE_RECEIPT_SCHEMA,
            "status": CONTRACT.MERGE_STATUS,
            "terminal_authority": False,
            "run_nonce": cls.nonce,
            "lease_sha256": cls.lease_sha,
            "manifest_sha256": cls.manifest_sha,
            "preflight_receipt_sha256": cls.preflight_sha,
            "pilot_gate_sha256": cls.pilot_sha,
            "payload": cls.merge_payload_path.name,
            "payload_sha256": cls.merge_payload_sha,
            "semantic_sha256": SEMANTIC_SHA,
            "template_bridge_sha256": TEMPLATE_BRIDGE_SHA,
            "exact_inventory": INVENTORY,
        })
        cls.candidate = cls.output / "FINALIZE_CANDIDATE.json"
        cls.good_candidate = {
            "schema": CONTRACT.CANDIDATE_SCHEMA,
            "status": CONTRACT.CANDIDATE_STATUS,
            "terminal_authority": False,
            "run_nonce": cls.nonce,
            "lease_sha256": cls.lease_sha,
            "manifest_sha256": cls.manifest_sha,
            "preflight_receipt_sha256": cls.preflight_sha,
            "pilot_gate_sha256": cls.pilot_sha,
            "merge_receipt_sha256": cls.merge_receipt_sha,
            "merge_payload_sha256": cls.merge_payload_sha,
            "semantic_sha256": SEMANTIC_SHA,
            "template_bridge_sha256": TEMPLATE_BRIDGE_SHA,
            "exact_inventory": INVENTORY,
            "claim_boundary": CLAIM_BOUNDARY,
            "utc": "2026-08-29T00:00:00Z",
        }
        write_json(cls.candidate, cls.good_candidate)
        for name in ("violations_census.json", "pgid_census.json",
                     "tag_census.json"):
            (cls.job_root / name).write_text("[]\n")
        cls.archive_path = cls.job_root / "job-tag-9.terminal.tar.gz"
        cls.archive_path.write_bytes(b"TERMINAL_ARCHIVE_STUB_BYTES\n")
        cls.archive_sha = CONTRACT.sha256_path(cls.archive_path)
        cls.sidecar = cls.job_root / "job-tag-9.terminal.tar.gz.sha256"
        cls.sidecar.write_text(
            "%s  job-tag-9.terminal.tar.gz\n" % cls.archive_sha)

    @classmethod
    def tearDownClass(cls):
        cls.holder.release()
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def base_args(self):
        return {
            "--candidate": self.candidate,
            "--lease": self.lease_path,
            "--job-root": self.job_root,
            "--job-tag": "job-tag-9",
            "--manifest": self.manifest_path,
            "--preflight-receipt": self.preflight_path,
            "--pilot-gate": self.pilot_path,
            "--merge-receipt": self.merge_receipt_path,
            "--merge-payload": self.merge_payload_path,
            "--boundary-mode": "systemd_scope",
            "--cleanup-pgid": 4242,
            "--preflight-rc": 0, "--source-check-rc": 0,
            "--f-rc": 0, "--g-rc": 0, "--pair-rc": 0, "--emit-rc": 0,
            "--candidate-rc": 0,
            "--containment-identity-gate": 1, "--monitor-started": 1,
            "--monitor-stop-clean": 1,
            "--monitor-violations": self.job_root / "violations_census.json",
            "--swap-violation": 0, "--swap-total": 0, "--swap-free": 0,
            "--whole-timeout": 0, "--peer-cancelled": 0,
            "--oom-kill-count": 0, "--cleanup-gate": 1,
            "--pgid-census": self.job_root / "pgid_census.json",
            "--tag-census": self.job_root / "tag_census.json",
            "--cgroup-final-gate": 1,
            "--manifest-generator-rc": 0, "--manifest-replay-rc": 0,
            "--archive-replay-rc": 0, "--archive-ready": 1,
            "--archive-sha-sidecar": self.sidecar,
        }

    def decide(self, overrides=None, omit=None):
        arguments = self.base_args()
        if overrides:
            arguments.update(overrides)
        if omit:
            arguments.pop(omit)
        output = self.job_root / ("decision_%d.json" % time.monotonic_ns())
        cli = []
        for key, value in arguments.items():
            cli += [key, value]
        cli += ["--output", output]
        result = run_cli("terminal", *cli)
        terminal = json.loads(output.read_text()) if output.exists() else None
        return result, terminal

    def forged_candidate(self, mutate):
        forged = json.loads(json.dumps(self.good_candidate))
        mutate(forged)
        path = self.job_root / ("forged_%d.json" % time.monotonic_ns())
        path.write_text(json.dumps(forged, indent=1, sort_keys=True) + "\n")
        return path

    def test_positive_terminal_only_with_every_gate_clean(self):
        result, terminal = self.decide()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(terminal["status"], CONTRACT.POSITIVE_TERMINAL)
        self.assertTrue(terminal["positive"])
        self.assertEqual(terminal["run_nonce"], self.nonce)
        self.assertEqual(terminal["failed_gates"], [])
        # The archive digest is the terminal's own rehash of the sidecar's
        # named on-disk archive, not a copied sidecar string.
        self.assertEqual(terminal["terminal_archive_sha256"],
                         self.archive_sha)
        self.assertEqual(terminal["terminal_archive_member"],
                         "job-tag-9.terminal.tar.gz")
        # Every payload-bearing candidate field carries explicit provenance.
        binding = terminal["candidate_binding"]
        for field, prefix in (
                ("lease_sha256", "RECOMPUTED_SHA256:"),
                ("manifest_sha256", "RECOMPUTED_SHA256:"),
                ("preflight_receipt_sha256", "RECOMPUTED_SHA256:"),
                ("pilot_gate_sha256", "RECOMPUTED_SHA256:"),
                ("merge_receipt_sha256", "RECOMPUTED_SHA256:"),
                ("merge_payload_sha256", "RECOMPUTED_SHA256:"),
                ("semantic_sha256", "RECEIPT_CROSSBOUND:"),
                ("template_bridge_sha256", "RECEIPT_CROSSBOUND:"),
                ("exact_inventory", "CONTRACT_CHECKED_29_155_184"),
                ("claim_boundary", "BOUND_TO_REHASHED_MANIFEST"),
                ("registration_sha256", "RECOMPUTED_SHA256:")):
            self.assertIn(field, binding, field)
            self.assertTrue(binding[field]["provenance"].startswith(prefix),
                            (field, binding[field]["provenance"]))
        self.assertEqual(binding["lease_sha256"]["value"], self.lease_sha)
        self.assertEqual(binding["semantic_sha256"]["value"], SEMANTIC_SHA)
        # systemd mode records a real boolean cgroup gate, never a string.
        self.assertIs(terminal["gates"]["cgroup_final_gate"], True)
        self.assertIs(terminal["gates"]["pgid_census_real"], True)
        self.assertIn("gate_provenance", terminal)

    def test_every_flipped_latch_forces_no_verdict(self):
        flips = [
            ({"--preflight-rc": 40}, "preflight_rc_zero"),
            ({"--source-check-rc": 1}, "source_check_rc_zero"),
            ({"--f-rc": 137}, "build_f_rc_zero"),
            ({"--g-rc": 99}, "build_g_rc_zero"),
            ({"--pair-rc": 43}, "pair_rc_zero"),
            ({"--emit-rc": 44}, "emit_rc_zero"),
            ({"--candidate-rc": 45}, "candidate_rc_zero"),
            ({"--containment-identity-gate": 0},
             "containment_identity_gate"),
            ({"--monitor-started": 0}, "monitor_started"),
            ({"--monitor-stop-clean": 0}, "monitor_stop_clean"),
            ({"--swap-violation": 1}, "no_swap_violation"),
            ({"--swap-total": 1024}, "final_swap_zero"),
            ({"--swap-free": 7}, "final_swap_zero"),
            ({"--whole-timeout": 1}, "no_whole_timeout"),
            ({"--peer-cancelled": 1}, "no_peer_cancellation"),
            ({"--oom-kill-count": 1}, "oom_kill_zero"),
            ({"--cleanup-gate": 0}, "cleanup_gate"),
            ({"--cgroup-final-gate": 0}, "cgroup_final_gate"),
            ({"--manifest-generator-rc": 2}, "manifest_generator_rc_zero"),
            ({"--manifest-replay-rc": 2}, "manifest_replay_rc_zero"),
            ({"--archive-replay-rc": 2}, "archive_replay_rc_zero"),
            ({"--archive-ready": 0}, "archive_ready"),
        ]
        for overrides, gate in flips:
            result, terminal = self.decide(overrides)
            self.assertEqual(result.returncode, 3, (overrides, result.stderr))
            self.assertFalse(terminal["positive"], overrides)
            self.assertTrue(terminal["status"].startswith("NO_VERDICT_"),
                            overrides)
            self.assertIn(gate, terminal["failed_gates"], overrides)

    def test_nonempty_censuses_force_no_verdict(self):
        bad = self.job_root / "bad_census.json"
        bad.write_text('[{"pid": 4242}]\n')
        for key, gate in (
                ("--monitor-violations", "monitor_violations_empty"),
                ("--pgid-census", "pgid_census_empty"),
                ("--tag-census", "tag_census_empty")):
            result, terminal = self.decide({key: bad})
            self.assertEqual(result.returncode, 3)
            self.assertIn(gate, terminal["failed_gates"])
        missing = self.job_root / "missing.json"
        for key in ("--monitor-violations", "--pgid-census", "--tag-census"):
            result, terminal = self.decide({key: missing})
            self.assertEqual(result.returncode, 3)

    def test_shape_forged_candidates_are_refused(self):
        forgeries = {
            "schema": lambda d: d.update(schema="FORGED"),
            "status": lambda d: d.update(status="COMPLETE"),
            "authority": lambda d: d.update(terminal_authority=True),
            "nonce": lambda d: d.update(run_nonce="00" * 32),
            "missing-hash": lambda d: d.pop("semantic_sha256"),
            "malformed-hash": lambda d: d.update(merge_payload_sha256="zz"),
            "extra-key": lambda d: d.update(bonus_claim="POINT_EXISTS"),
            "string-inventory": lambda d: d.update(
                exact_inventory="29 live 155 zero"),
        }
        for name, mutate in forgeries.items():
            path = self.forged_candidate(mutate)
            result, terminal = self.decide({"--candidate": path})
            self.assertEqual(result.returncode, 3, name)
            self.assertIn("candidate_schema_valid",
                          terminal["failed_gates"], name)
        result, terminal = self.decide(
            {"--candidate": self.job_root / "absent.json"})
        self.assertEqual(result.returncode, 3)

    def test_value_forged_candidate_digest_fields_are_refused(self):
        """Opus 5 Finding 1: a fabricated candidate must never reach the
        positive terminal.  Every digest value forgery (valid 64-hex shape,
        wrong value) must refuse through its own named binding gate."""
        wrong = "de" * 32
        cases = [
            ("lease_sha256", "candidate_lease_digest_bound"),
            ("manifest_sha256", "candidate_manifest_digest_bound"),
            ("preflight_receipt_sha256", "candidate_preflight_digest_bound"),
            ("pilot_gate_sha256", "candidate_pilot_gate_digest_bound"),
            ("merge_receipt_sha256", "candidate_merge_receipt_digest_bound"),
            ("merge_payload_sha256", "candidate_merge_payload_digest_bound"),
            ("semantic_sha256", "candidate_semantic_crossbound"),
            ("template_bridge_sha256",
             "candidate_template_bridge_crossbound"),
        ]
        for field, gate in cases:
            path = self.forged_candidate(lambda d, f=field:
                                          d.update({f: wrong}))
            result, terminal = self.decide({"--candidate": path})
            self.assertEqual(result.returncode, 3, field)
            self.assertFalse(terminal["positive"], field)
            self.assertIn(gate, terminal["failed_gates"], field)
            self.assertIn(gate, terminal["binding_failures"] or {}, field)

    def test_impossible_inventory_refused(self):
        cases = {
            "negative-live": {"live_rows": -7, "exact_zero_rows": 9999},
            "wrong-total": {"live_rows": 30, "exact_zero_rows": 154},
            "bool-live": {"live_rows": True},
            "bool-zero": {"exact_zero_rows": False},
            "wrong-bands": {"live_bands": {"20": 9, "30": 10, "40": 10}},
            "degree-three": {"max_tail_degree": 3},
            "bool-degree": {"max_tail_degree": True},
            "short-zero-targets": {"exact_zero_targets": [[0, 1]]},
            "duplicate-zero-targets": {
                "exact_zero_targets": [[0, 0]] * 155},
        }
        for name, patch in cases.items():
            inventory = json.loads(json.dumps(INVENTORY))
            inventory.update(patch)
            path = self.forged_candidate(
                lambda d, inv=inventory: d.update(exact_inventory=inv))
            result, terminal = self.decide({"--candidate": path})
            self.assertEqual(result.returncode, 3, name)
            self.assertIn("candidate_inventory_contract",
                          terminal["failed_gates"], name)
        # A key-census mutation (missing key) must also refuse.
        inventory = json.loads(json.dumps(INVENTORY))
        del inventory["live_bands"]
        path = self.forged_candidate(
            lambda d: d.update(exact_inventory=inventory))
        result, terminal = self.decide({"--candidate": path})
        self.assertEqual(result.returncode, 3)
        self.assertIn("candidate_inventory_contract",
                      terminal["failed_gates"])

    def test_claim_boundary_forgeries_refused(self):
        promoted = json.loads(json.dumps(CLAIM_BOUNDARY))
        promoted["exact_a00pp_raw_J_point"] = "EXISTS"
        dropped = json.loads(json.dumps(CLAIM_BOUNDARY))
        del dropped["JC2_counterexample"]
        for name, boundary in (("promoted", promoted), ("dropped", dropped)):
            path = self.forged_candidate(
                lambda d, b=boundary: d.update(claim_boundary=b))
            result, terminal = self.decide({"--candidate": path})
            self.assertEqual(result.returncode, 3, name)
            self.assertIn("candidate_claim_boundary_bound",
                          terminal["failed_gates"], name)

    def test_candidate_mutation_after_producer_exit_refused(self):
        """The producer exited 0 (candidate_rc_zero holds) but the candidate
        file was mutated afterwards: the terminal itself must refuse."""
        mutations = {
            "semantic-swap": (lambda d: d.update(semantic_sha256="ee" * 32),
                              "candidate_semantic_crossbound"),
            "inventory-swap": (
                lambda d: d.update(exact_inventory=dict(
                    json.loads(json.dumps(INVENTORY)), live_rows=28,
                    exact_zero_rows=156)),
                "candidate_inventory_contract"),
            "payload-swap": (
                lambda d: d.update(merge_payload_sha256="ad" * 32),
                "candidate_merge_payload_digest_bound"),
        }
        for name, (mutate, gate) in mutations.items():
            path = self.forged_candidate(mutate)
            result, terminal = self.decide({"--candidate": path,
                                            "--candidate-rc": 0})
            self.assertEqual(result.returncode, 3, name)
            self.assertIn(gate, terminal["failed_gates"], name)
        # Artifact mutation after the candidate was finalized: the merge
        # payload bytes changed on disk while the candidate kept the old
        # (valid-hex) digest.
        mutated_payload = self.job_root / "mutated_payload.pkl"
        mutated_payload.write_bytes(b"POST_EXIT_MUTATION\n")
        result, terminal = self.decide({"--merge-payload": mutated_payload})
        self.assertEqual(result.returncode, 3)
        self.assertIn("candidate_merge_payload_digest_bound",
                      terminal["failed_gates"])

    def test_semantic_receipt_mutation_with_valid_hex_refused(self):
        """The on-disk merge receipt's semantic digest is swapped for a
        different valid 64-hex value.  Both attack variants must refuse:
        receipt-only mutation (rehash mismatch) and the coordinated variant
        where the candidate's receipt digest is updated to match the
        mutated receipt (the semantic crossbind then refuses)."""
        receipt = json.loads(self.merge_receipt_path.read_text())
        receipt["semantic_sha256"] = "ee" * 32
        mutated_receipt = self.job_root / "mutated_receipt.json"
        mutated_sha = write_json(mutated_receipt, receipt)
        # Variant 1: candidate untouched -> receipt digest bind refuses.
        result, terminal = self.decide({"--merge-receipt": mutated_receipt})
        self.assertEqual(result.returncode, 3)
        self.assertIn("candidate_merge_receipt_digest_bound",
                      terminal["failed_gates"])
        # Variant 2: candidate's merge_receipt_sha256 updated consistently
        # -> the rehash passes but the semantic crossbind refuses.
        path = self.forged_candidate(
            lambda d: d.update(merge_receipt_sha256=mutated_sha))
        result, terminal = self.decide({"--candidate": path,
                                        "--merge-receipt": mutated_receipt})
        self.assertEqual(result.returncode, 3)
        self.assertNotIn("candidate_merge_receipt_digest_bound",
                         terminal["failed_gates"])
        self.assertIn("candidate_semantic_crossbound",
                      terminal["failed_gates"])

    def test_dangling_and_drifted_archive_sidecar_refused(self):
        """Opus 5 Finding 1, third sub-claim: the sidecar's named archive
        must be resolved, required regular, and rehashed."""
        dangling = self.job_root / "dangling.sha256"
        dangling.write_text("%s  job-tag-9.terminal.tar.gz\n" % ("77" * 32))
        drifted_dir = self.job_root / "drifted"
        drifted_dir.mkdir(exist_ok=True)
        (drifted_dir / "job-tag-9.terminal.tar.gz").write_bytes(
            b"DIFFERENT_BYTES\n")
        drifted = drifted_dir / "sidecar.sha256"
        drifted.write_text("%s  job-tag-9.terminal.tar.gz\n"
                           % self.archive_sha)
        foreign = self.job_root / "foreign.sha256"
        foreign.write_text("%s  other-job.terminal.tar.gz\n"
                           % self.archive_sha)
        traversal = self.job_root / "traversal.sha256"
        traversal.write_text("%s  ../job-tag-9.terminal.tar.gz\n"
                             % self.archive_sha)
        for name, sidecar in (("dangling", dangling), ("drifted", drifted),
                              ("foreign", foreign),
                              ("traversal", traversal)):
            result, terminal = self.decide(
                {"--archive-sha-sidecar": sidecar})
            self.assertEqual(result.returncode, 3, name)
            self.assertIn("archive_sidecar_bound",
                          terminal["failed_gates"], name)

    def test_registration_drift_refused(self):
        original = self.registration.read_bytes()
        try:
            self.registration.write_text('{"stub": true, "drift": 1}\n')
            result, terminal = self.decide()
            self.assertEqual(result.returncode, 3)
            self.assertIn("candidate_registration_digest_bound",
                          terminal["failed_gates"])
        finally:
            self.registration.write_bytes(original)
        result, _ = self.decide()
        self.assertEqual(result.returncode, 0)

    def test_vacuous_pgid_refused(self):
        """Opus 5 Finding 3a: a vacuity-inducing census parameter must
        never support a positive pgid_census_empty gate."""
        for pgid in (0, 1, -1):
            result, terminal = self.decide({"--cleanup-pgid": pgid})
            self.assertEqual(result.returncode, 3, pgid)
            self.assertIn("pgid_census_real", terminal["failed_gates"], pgid)

    def test_copied_cgroup_gate_refused(self):
        """A cgroup gate value that cannot come from a real cgroup census
        in the declared boundary mode is a copied/forged gate: refuse."""
        cases = [
            ({"--boundary-mode": "setsid_pgid", "--cgroup-final-gate": 1},
             "cgroup_gate_mode_consistent"),
            ({"--boundary-mode": "setsid_pgid", "--cgroup-final-gate": 0},
             "cgroup_gate_mode_consistent"),
            ({"--boundary-mode": "systemd_scope",
              "--cgroup-final-gate": "NOT_APPLICABLE"},
             "cgroup_gate_mode_consistent"),
        ]
        for overrides, gate in cases:
            result, terminal = self.decide(overrides)
            self.assertEqual(result.returncode, 3, overrides)
            self.assertIn(gate, terminal["failed_gates"], overrides)

    def test_fallback_mode_not_applicable_cgroup_is_recorded(self):
        result, terminal = self.decide(
            {"--boundary-mode": "setsid_pgid",
             "--cgroup-final-gate": "NOT_APPLICABLE"})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(terminal["positive"])
        # Recorded as the string NOT_APPLICABLE, never as a copied true.
        self.assertEqual(terminal["gates"]["cgroup_final_gate"],
                         "NOT_APPLICABLE")
        self.assertIn("NOT_APPLICABLE_NO_CGROUP",
                      terminal["gate_provenance"]["cgroup_final_gate"])

    def test_missing_sidecar_and_lease_failure(self):
        result, terminal = self.decide(
            {"--archive-sha-sidecar": self.job_root / "absent.sha256"})
        self.assertEqual(result.returncode, 3)
        self.assertIn("archive_sidecar_bound", terminal["failed_gates"])
        result, terminal = self.decide({"--job-tag": "wrong-tag"})
        self.assertEqual(result.returncode, 3)
        self.assertIn("lease_valid_and_held", terminal["failed_gates"])

    def test_omitted_or_malformed_arguments_are_refused(self):
        for omit in ("--monitor-stop-clean", "--archive-ready",
                     "--oom-kill-count", "--tag-census", "--manifest",
                     "--merge-payload", "--cleanup-pgid", "--boundary-mode"):
            result, _ = self.decide(omit=omit)
            self.assertEqual(result.returncode, 2, omit)
        for overrides in ({"--swap-violation": 2},
                          {"--archive-ready": "true"},
                          {"--monitor-started": ""},
                          {"--boundary-mode": "no_such_mode"},
                          {"--cleanup-pgid": "not-an-int"},
                          {"--cgroup-final-gate": "2"}):
            result, _ = self.decide(overrides)
            self.assertEqual(result.returncode, 2, overrides)


class PostmortemGateTest(unittest.TestCase):
    """Opus 5 Finding 4: the launcher post-mortem census must be
    authority-bearing.  A positive terminal plus an unclean post-mortem
    census yields a non-zero exit and an immutable fault object; the
    original terminal is never modified."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.terminal = self.tmp / "TERMINAL.json"
        self.fault = self.tmp / "TERMINAL_POSTMORTEM_FAULT.json"
        self.pgid = self.tmp / "pm_pgid.json"
        self.tag = self.tmp / "pm_tag.json"

    def write_terminal(self, positive):
        status = (CONTRACT.POSITIVE_TERMINAL if positive
                  else "NO_VERDICT_EMIT_RC_ZERO")
        write_json(self.terminal, {
            "schema": CONTRACT.TERMINAL_SCHEMA,
            "status": status,
            "positive": positive,
            "terminal_authority": True,
        })

    def gate(self, rc):
        return run_cli("postmortem-gate", "--terminal", self.terminal,
                       "--postmortem-rc", rc,
                       "--pgid-census", self.pgid, "--tag-census", self.tag,
                       "--fault-output", self.fault)

    def test_positive_with_unclean_postmortem_emits_immutable_fault(self):
        self.write_terminal(True)
        terminal_bytes = self.terminal.read_bytes()
        self.pgid.write_text("[]\n")
        self.tag.write_text('[{"pid": 999, "state": "S"}]\n')
        result = self.gate(1)
        self.assertEqual(result.returncode, 79, result.stderr)
        self.assertIn("TERMINAL_POSTMORTEM_FAULT", result.stdout)
        self.assertTrue(self.fault.exists())
        fault = json.loads(self.fault.read_text())
        self.assertEqual(fault["schema"], CONTRACT.POSTMORTEM_FAULT_SCHEMA)
        self.assertTrue(fault["voids_positive_terminal"])
        self.assertEqual(fault["terminal_sha256"],
                         CONTRACT.sha256_path(self.terminal))
        self.assertEqual(fault["tag_census"]["content"][0]["pid"], 999)
        # Immutable (0444) and the terminal is byte-unchanged.
        self.assertEqual(os.stat(self.fault).st_mode & 0o777, 0o444)
        self.assertEqual(self.terminal.read_bytes(), terminal_bytes)
        # A positive terminal with a MISSING census is likewise unclean.
        self.tag.unlink()
        fault2 = self.tmp / "fault2.json"
        result = run_cli("postmortem-gate", "--terminal", self.terminal,
                         "--postmortem-rc", 0,
                         "--pgid-census", self.pgid, "--tag-census", self.tag,
                         "--fault-output", fault2)
        self.assertEqual(result.returncode, 79)
        self.assertTrue(fault2.exists())

    def test_positive_clean_and_negative_cases_pass(self):
        self.pgid.write_text("[]\n")
        self.tag.write_text("[]\n")
        self.write_terminal(True)
        result = self.gate(0)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(self.fault.exists())
        # A NO_VERDICT terminal never needs a fault object even when the
        # census is unclean; the failure evidence is the NO_VERDICT itself.
        self.write_terminal(False)
        self.tag.write_text('[{"pid": 999}]\n')
        result = self.gate(1)
        self.assertEqual(result.returncode, 0)
        self.assertFalse(self.fault.exists())
        # An unreadable terminal is treated as positive: fail closed.
        self.terminal.write_text("NOT JSON")
        result = self.gate(0)
        self.assertEqual(result.returncode, 79)
        self.assertTrue(self.fault.exists())

    def test_fault_object_never_overwritten(self):
        self.write_terminal(True)
        self.pgid.write_text('[{"pid": 7}]\n')
        self.tag.write_text("[]\n")
        result = self.gate(1)
        self.assertEqual(result.returncode, 79)
        first = self.fault.read_bytes()
        time.sleep(1.1)
        result = self.gate(1)
        self.assertEqual(result.returncode, 79)
        self.assertEqual(self.fault.read_bytes(), first)


class OptimizedPythonTest(unittest.TestCase):
    """python -O must refuse to run any production custody path at all."""

    def refuse(self, *argv):
        result = subprocess.run(
            [sys.executable, "-O"] + [str(a) for a in argv],
            capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("OPTIMIZED_PYTHON_REFUSED", result.stderr)
        return result

    def test_contract_refuses_optimized(self):
        self.refuse(HERE / "job_contract_v4.py", "lease-probe",
                    "--lock-path", "/tmp/x")

    def test_terminal_and_postmortem_gate_refuse_optimized(self):
        # The two authority-bearing subcommands must fail closed under -O
        # before parsing a single argument.
        self.refuse(HERE / "job_contract_v4.py", "terminal")
        self.refuse(HERE / "job_contract_v4.py", "postmortem-gate")

    def test_preflight_refuses_optimized(self):
        self.refuse(HERE / "aws_preflight_v4.py", "--manifest", "x",
                    "--run-dir", "x", "--lease", "x", "--output", "x")

    def test_producer_refuses_optimized(self):
        self.refuse(HERE / "selected_rows_v4.py", "registry")

    def test_forged_receipt_rejected_identically(self):
        # The v2 hostile fixture: a forged failing preflight receipt was
        # ACCEPTED under -O.  Since v3 both interpreters must reject it.
        tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, tmp, True)
        forged = tmp / "PREFLIGHT.json"
        forged.write_text(json.dumps({
            "schema": "FORGED", "pass": False,
            "manifest_sha256": "WRONG",
            "operational_source_list_sha256": "WRONG",
            "live_identity": {}, "live_tag": {},
            "terminal_authority": True,
        }))
        program = (
            "import importlib.util, json, sys\n"
            "from pathlib import Path\n"
            "spec = importlib.util.spec_from_file_location(\n"
            "    'rows_v4', %r)\n"
            "rows = importlib.util.module_from_spec(spec)\n"
            "sys.modules[spec.name] = rows\n"
            "spec.loader.exec_module(rows)\n"
            "manifest, digest = rows.load_manifest(Path(%r))\n"
            "lease = {'run_nonce': '00' * 32}\n"
            "rows.validate_preflight_receipt(Path(%r), manifest, digest,\n"
            "                                lease, '11' * 32)\n"
            "print('FORGED_ACCEPTED')\n"
            % (str(HERE / "selected_rows_v4.py"),
               str(HERE / "PIPELINE_MANIFEST_V4.json"), str(forged)))
        for flags, expected_refusal in (
                ([], "preflight receipt schema drift"),
                (["-O"], "OPTIMIZED_PYTHON_REFUSED")):
            result = subprocess.run(
                [sys.executable] + flags + ["-c", program],
                capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, flags)
            self.assertNotIn("FORGED_ACCEPTED", result.stdout, flags)
            # Pin the refusal reason so a missing manifest or import error
            # can never make this fixture pass vacuously.
            self.assertIn(expected_refusal, result.stderr, flags)


if __name__ == "__main__":
    unittest.main()
