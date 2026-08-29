#!/usr/bin/env python3
"""Test wrapper: replays st39_transport_check.py and pins the check census.

The expected census is 24,987:
  P1  5*2 + 6 + 3 + 4*5 = 39
  P2  401*20 + 2001*7 = 22,027   (20 ok() per t in the first loop)
  P3  401*6 = 2,406
  P4  (3+1)*2 + (1+1)*2 + (2+1) = 15
  P5  7
  P6  8 runs * ~9 = 72  (2 t-independent + per-branch counts)
Exact total is asserted against the module counter, not this comment.
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))

def main():
    out = subprocess.run([sys.executable,
                          os.path.join(HERE, "st39_transport_check.py")],
                         capture_output=True, text=True)
    if out.returncode != 0:
        print(out.stdout); print(out.stderr)
        raise SystemExit("TEST FAIL: nonzero exit")
    line = out.stdout.strip().splitlines()[-1]
    if not line.startswith("ST39_TRANSPORT_CHECK_PASS"):
        raise SystemExit("TEST FAIL: missing pass banner: " + line)
    n = int(line.split("checks=")[1])
    if n != 24987:
        raise SystemExit("TEST FAIL: check census %d != 24987" % n)
    # mutation guard: a wrong stage ratio must fail if injected
    src = open(os.path.join(HERE, "st39_transport_check.py")).read()
    bad = src.replace('Fr(QH, DH) == Fr(6, 7)', 'Fr(QH, DH) == Fr(5, 7)')
    assert bad != src
    p = subprocess.run([sys.executable, "-c", bad], capture_output=True,
                       text=True, cwd=HERE)
    if p.returncode == 0:
        raise SystemExit("TEST FAIL: stage-ratio mutation not caught")
    bad2 = src.replace("omega ** (-15)", "omega ** (-14)")
    assert bad2 != src
    p2 = subprocess.run([sys.executable, "-c", bad2], capture_output=True,
                        text=True, cwd=HERE)
    if p2.returncode == 0:
        raise SystemExit("TEST FAIL: twin-law mutation not caught")
    print("ST39_TRANSPORT_TEST_PASS checks=%d mutations=2" % n)

if __name__ == "__main__":
    main()
