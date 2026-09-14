#!/usr/bin/env python3
"""One worker-only dependency/guard preflight; no resultant or source mutation."""
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys


def need(ok, why):
    if not ok:
        raise RuntimeError(why)


instance, tag = sys.argv[1:]
need(re.fullmatch(r"i-[0-9a-f]{17}", instance), "invalid instance")
need(instance != "i-0252f535410c26ebc", "HQ forbidden")
need(re.fullmatch(r"[a-z0-9][a-z0-9-]{0,59}", tag), "invalid tag")
need(Path("/sys/class/dmi/id/sys_vendor").read_text().strip() == "Amazon EC2", "AWS required")
need(Path("/sys/class/dmi/id/board_asset_tag").read_text().strip() == instance, "instance mismatch")
need(os.getresuid() == (65534,)*3 and os.getresgid() == (65534,)*3, "preflight credentials")
need(Path("/proc/self/cgroup").read_text().strip() ==
     "0::/system.slice/jc2-mixres-preflight.service", "preflight cgroup")
need(Path.cwd() == Path("/var/lib/jc2-mixres-preflight"), "preflight cwd")
need(sys.flags.isolated == 1 and sys.flags.no_user_site == 1, "isolated Python required")
os.umask(0o027)
observer = Path("/opt/jc2-mixres20260913a/bundle/observer.py")
need(hashlib.sha256(observer.read_bytes()).hexdigest() ==
     "661b739ed3f86267e9875a83537bd1a75ef5699442c99eb182ec2800f3005858", "observer pin")
compile(observer.read_bytes(), str(observer), "exec")  # syntax only, no execution/import
jobroot = Path("/var/lib/jc2-jobs") / tag
need(not jobroot.exists(), "job already exists before preflight")
for label, candidate, cause in (
    ("hq", "i-0252f535410c26ebc", "ValueError: HQ forbidden"),
    ("instance", "i-00000000000000000", "ValueError: instance mismatch"),
    ("cgroup", instance, "ValueError: exact job cgroup required"),
):
    with open(label + ".stdout", "xb") as out, open(label + ".stderr", "xb") as err:
        result = subprocess.run([sys.executable, "-I", "-B", "-v", str(observer),
                                 "--instance", candidate, "--job-tag", tag,
                                 "--mode", "smoke"], stdout=out, stderr=err,
                                check=False, timeout=15)
        out.flush(); err.flush(); os.fsync(out.fileno()); os.fsync(err.fileno())
    diagnostic = Path(label + ".stderr").read_text()
    need(result.returncode != 0 and diagnostic.splitlines().count(cause) >= 1,
         "wrong negative guard cause: " + label)
    need("import 'sympy" not in diagnostic and "import 'flint" not in diagnostic,
         "scientific import before negative refusal")
    need(Path(label + ".stdout").stat().st_size == 0 and not jobroot.exists(),
         "negative control created output")
    print("GUARD_PASS " + label + " " + cause, flush=True)

import importlib.metadata
import sympy
from sympy.external.gmpy import GROUND_TYPES

def identity(path):
    path = Path(path).resolve(strict=True)
    need(path.is_relative_to("/usr") or path.is_relative_to("/lib"), "non-system dependency path")
    size = path.stat().st_size
    need(size <= 128*1024*1024, "dependency file exceeds preflight bound")
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while chunk := stream.read(1024*1024):
            digest.update(chunk)
    return {"path": str(path), "bytes": str(size), "sha256": digest.hexdigest()}

package = Path(sympy.__file__).resolve(strict=True).parent
need(package.is_relative_to("/usr"), "non-system Sympy package")
paths = sorted(p for p in package.rglob("*") if p.is_file() and p.suffix != ".pyc")
need(len(paths) <= 10000, "package file-count bound")
inventory = [identity(p) for p in paths]
loaded = sorted({str(Path(m.__file__).resolve()) for m in tuple(sys.modules.values())
                 if m is not sys.modules.get("__main__") and
                 getattr(m, "__file__", None) and Path(m.__file__).is_file()})
mapped = sorted({line.split()[-1] for line in Path("/proc/self/maps").read_text().splitlines()
                 if len(line.split()) >= 6 and line.split()[-1].startswith("/")})
dist = importlib.metadata.distribution("sympy")
record = {"tier": "WORKER_DEPENDENCY_OBSERVATION_NOT_MATHEMATICAL_PROOF",
          "instance": instance, "tag": tag, "python": sys.version,
          "python_executable": identity(sys.executable), "isolated": str(sys.flags.isolated),
          "sympy_version": sympy.__version__, "ground_types": str(GROUND_TYPES),
          "ZZ_dtype": str(sympy.ZZ.dtype), "QQ_dtype": str(sympy.QQ.dtype),
          "distribution_version": dist.version,
          "metadata_sha256": hashlib.sha256((dist.read_text("METADATA") or "").encode()).hexdigest(),
          "sympy_package": inventory, "loaded_modules": [identity(p) for p in loaded],
          "mapped_files": [identity(p) for p in mapped]}
raw = (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode()
need(len(raw) <= 7*1024*1024, "dependency record size")
with open("dependencies.json", "xb") as stream:
    stream.write(raw); stream.flush(); os.fsync(stream.fileno())
fd = os.open(".", os.O_RDONLY | os.O_DIRECTORY)
os.fsync(fd); os.close(fd)
print("PREFLIGHT_PASS " + hashlib.sha256(raw).hexdigest(), flush=True)
os.fsync(sys.stdout.fileno())
