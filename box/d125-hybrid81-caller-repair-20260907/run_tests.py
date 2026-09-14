"""One bounded normal/-O stdlib batch; no CAS or production inputs."""
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

resource.setrlimit(resource.RLIMIT_AS, (512*1024**2,)*2)
resource.setrlimit(resource.RLIMIT_CPU, (25, 25))
resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
signal.alarm(30)
started = time.monotonic()
results = []
for mode in ([], ['-O']):
    completed = subprocess.run([sys.executable, '-B', *mode, '-m', 'unittest', '-v', 'test_exact','test_hybrid','test_caller'],
          cwd=Path(__file__).resolve().parent, capture_output=True, text=True,
          env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'}, timeout=max(1, 29-(time.monotonic()-started)))
    results.append({'mode': mode or ['normal'], 'returncode': completed.returncode,
                    'stdout': completed.stdout, 'stderr': completed.stderr})
    if completed.returncode:
        break
report = json.dumps({'results': results, 'wall_seconds': time.monotonic()-started,
                    'child_usage': list(resource.getrusage(resource.RUSAGE_CHILDREN))}, sort_keys=True)+'\n'
if len(sys.argv) == 2:
    with Path(sys.argv[1]).open('x') as out:
        out.write(report)
print(report, end='')
raise SystemExit(0 if len(results) == 2 and all(r['returncode'] == 0 for r in results) else 1)
