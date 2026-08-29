#!/usr/bin/env python3
"""Bounded hostile fixtures for the D43 v3 custody contract.

These fixtures are macOS-portable: live-kernel readers take injected proc
roots, meminfo files, and cgroup directories, and the kernel flock fixtures
hold the lease from a real subprocess.  Unit-test assertions may be
assertions; every production check under test is an explicit exception.
"""

import argparse
import importlib.util
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
    "d43_job_contract_v3", HERE / "job_contract_v3.py")
CONTRACT = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = CONTRACT
spec.loader.exec_module(CONTRACT)

CLI = [sys.executable, "-B", str(HERE / "job_contract_v3.py")]
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
                 str(HERE / "job_contract_v3.py")],
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
        registration = self.tmp / "REGISTERED.json"
        registration.write_text('{"stub": true}\n')
        proc_root = self.tmp / "proc"
        make_proc_entry(proc_root, 4242)
        inner = (
            '"%s" -B "%s" lease-record --fd 9 --lock-path "%s" '
            '--job-root "%s" --job-tag job-tag-1 --archive-sha256 %s '
            '--registration "%s" --launcher-path "%s" --launcher-pid 4242 '
            '--proc-root "%s" --output "%s" > "%s"'
            % (sys.executable, HERE / "job_contract_v3.py", self.lock,
               job_root, ARCHIVE_SHA, registration,
               HERE / "job_contract_v3.py", proc_root,
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

    def test_unsafe_members_refused(self):
        def passthrough(out, members):
            for member, data in members:
                out.addfile(member, __import__("io").BytesIO(data))

        def with_traversal(out, members):
            passthrough(out, members)
            info = tarfile.TarInfo("data/../../evil.txt")
            info.size = 4
            out.addfile(info, __import__("io").BytesIO(b"evil"))

        def with_absolute(out, members):
            passthrough(out, members)
            info = tarfile.TarInfo("/evil.txt")
            info.size = 4
            out.addfile(info, __import__("io").BytesIO(b"evil"))

        def with_symlink(out, members):
            passthrough(out, members)
            info = tarfile.TarInfo("data/link")
            info.type = tarfile.SYMTYPE
            info.linkname = "/etc/passwd"
            out.addfile(info)

        def with_duplicate(out, members):
            passthrough(out, members)
            member, data = members[0]
            out.addfile(member, __import__("io").BytesIO(data))

        def with_extra(out, members):
            passthrough(out, members)
            info = tarfile.TarInfo("data/extra.txt")
            info.size = 5
            out.addfile(info, __import__("io").BytesIO(b"extra"))

        def without_manifest(out, members):
            for member, data in members:
                if member.name != "meta/MANIFEST.sha256":
                    out.addfile(member, __import__("io").BytesIO(data))

        def tampered_payload(out, members):
            for member, data in members:
                if member.name == "data/a.txt":
                    data = b"tampered\n"
                    member.size = len(data)
                out.addfile(member, __import__("io").BytesIO(data))

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

    def test_corrupt_outer_bytes_refused(self):
        path = self.tmp / "corrupt.tar.gz"
        self.build(path)
        raw = bytearray(path.read_bytes())
        raw[len(raw) // 2] ^= 0xFF
        path.write_bytes(bytes(raw))
        with self.assertRaises(Exception):
            self.replay(path)


class TerminalDecisionTest(unittest.TestCase):
    """Every mandatory latch flips the single terminal authority."""

    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp()).resolve()
        cls.lock = cls.tmp / "host.lock"
        cls.job_root = cls.tmp / "job-tag-9"
        cls.job_root.mkdir()
        registration = cls.tmp / "REGISTERED.json"
        registration.write_text('{"stub": true}\n')
        proc_root = cls.tmp / "proc"
        make_proc_entry(proc_root, 4242)
        inner = (
            '"%s" -B "%s" lease-record --fd 9 --lock-path "%s" '
            '--job-root "%s" --job-tag job-tag-9 --archive-sha256 %s '
            '--registration "%s" --launcher-path "%s" --launcher-pid 4242 '
            '--proc-root "%s" --output "%s" > /dev/null'
            % (sys.executable, HERE / "job_contract_v3.py", cls.lock,
               cls.job_root, ARCHIVE_SHA, registration,
               HERE / "job_contract_v3.py", proc_root,
               cls.job_root / "RUN_LEASE.json"))
        cls.holder = LeaseHolder(cls.lock, inner)
        cls.lease_path = cls.job_root / "RUN_LEASE.json"
        cls.nonce = json.loads(cls.lease_path.read_text())["run_nonce"]
        cls.candidate = cls.job_root / "FINALIZE_CANDIDATE.json"
        cls.candidate.write_text(json.dumps({
            "schema": CONTRACT.CANDIDATE_SCHEMA,
            "status": CONTRACT.CANDIDATE_STATUS,
            "terminal_authority": False,
            "run_nonce": cls.nonce,
            "lease_sha256": CONTRACT.sha256_path(cls.lease_path),
            "manifest_sha256": "11" * 32,
            "preflight_receipt_sha256": "22" * 32,
            "pilot_gate_sha256": "33" * 32,
            "merge_receipt_sha256": "44" * 32,
            "merge_payload_sha256": "55" * 32,
            "semantic_sha256": "66" * 32,
            "exact_inventory": {"live_rows": 29, "exact_zero_rows": 155},
        }, indent=1) + "\n")
        for name in ("violations_census.json", "pgid_census.json",
                     "tag_census.json"):
            (cls.job_root / name).write_text("[]\n")
        (cls.job_root / "archive.sha256").write_text(
            "77" * 32 + "  job-tag-9.terminal.tar.gz\n")

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
            "--archive-sha-sidecar": self.job_root / "archive.sha256",
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

    def test_positive_terminal_only_with_every_gate_clean(self):
        result, terminal = self.decide()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(terminal["status"], CONTRACT.POSITIVE_TERMINAL)
        self.assertTrue(terminal["positive"])
        self.assertEqual(terminal["run_nonce"], self.nonce)
        self.assertEqual(terminal["terminal_archive_sha256"], "77" * 32)
        self.assertEqual(terminal["candidate_binding"]["semantic_sha256"],
                         "66" * 32)
        self.assertEqual(terminal["failed_gates"], [])

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

    def test_forged_candidates_are_refused(self):
        good = json.loads(self.candidate.read_text())
        forgeries = {
            "schema": dict(good, schema="FORGED"),
            "status": dict(good, status="COMPLETE"),
            "authority": dict(good, terminal_authority=True),
            "nonce": dict(good, run_nonce="00" * 32),
            "missing-hash": {k: v for k, v in good.items()
                             if k != "semantic_sha256"},
            "malformed-hash": dict(good, merge_payload_sha256="zz"),
        }
        for name, forged in forgeries.items():
            path = self.job_root / ("forged_%s.json" % name)
            path.write_text(json.dumps(forged))
            result, terminal = self.decide({"--candidate": path})
            self.assertEqual(result.returncode, 3, name)
            self.assertIn("candidate_parsed_and_bound",
                          terminal["failed_gates"], name)
        result, terminal = self.decide(
            {"--candidate": self.job_root / "absent.json"})
        self.assertEqual(result.returncode, 3)

    def test_missing_sidecar_and_lease_failure(self):
        result, terminal = self.decide(
            {"--archive-sha-sidecar": self.job_root / "absent.sha256"})
        self.assertEqual(result.returncode, 3)
        self.assertIn("archive_outer_sha_present", terminal["failed_gates"])
        result, terminal = self.decide({"--job-tag": "wrong-tag"})
        self.assertEqual(result.returncode, 3)
        self.assertIn("lease_valid_and_held", terminal["failed_gates"])

    def test_omitted_or_malformed_arguments_are_refused(self):
        for omit in ("--monitor-stop-clean", "--archive-ready",
                     "--oom-kill-count", "--tag-census"):
            result, _ = self.decide(omit=omit)
            self.assertEqual(result.returncode, 2, omit)
        for overrides in ({"--swap-violation": 2},
                          {"--archive-ready": "true"},
                          {"--monitor-started": ""}):
            result, _ = self.decide(overrides)
            self.assertEqual(result.returncode, 2, overrides)


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
        self.refuse(HERE / "job_contract_v3.py", "lease-probe",
                    "--lock-path", "/tmp/x")

    def test_preflight_refuses_optimized(self):
        self.refuse(HERE / "aws_preflight_v3.py", "--manifest", "x",
                    "--run-dir", "x", "--lease", "x", "--output", "x")

    def test_producer_refuses_optimized(self):
        self.refuse(HERE / "selected_rows_v3.py", "registry")

    def test_forged_receipt_rejected_identically(self):
        # The v2 hostile fixture: a forged failing preflight receipt was
        # ACCEPTED under -O.  In v3 both interpreters must reject it.
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
            "    'rows_v3', %r)\n"
            "rows = importlib.util.module_from_spec(spec)\n"
            "sys.modules[spec.name] = rows\n"
            "spec.loader.exec_module(rows)\n"
            "manifest, digest = rows.load_manifest(Path(%r))\n"
            "lease = {'run_nonce': '00' * 32}\n"
            "rows.validate_preflight_receipt(Path(%r), manifest, digest,\n"
            "                                lease, '11' * 32)\n"
            "print('FORGED_ACCEPTED')\n"
            % (str(HERE / "selected_rows_v3.py"),
               str(HERE / "PIPELINE_MANIFEST_V3.json"), str(forged)))
        for flags in ([], ["-O"]):
            result = subprocess.run(
                [sys.executable] + flags + ["-c", program],
                capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, flags)
            self.assertNotIn("FORGED_ACCEPTED", result.stdout, flags)


if __name__ == "__main__":
    unittest.main()
