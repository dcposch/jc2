#!/usr/bin/env python3
"""Bounded no-CAS process tree used only by process-group regression."""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--marker", type=Path, required=True)
    parser.add_argument("--depth", type=int, required=True)
    arguments = parser.parse_args()
    assert arguments.marker.is_dir()
    payload = bytearray(8 * 1024 * 1024)
    payload[0] = arguments.depth
    child = None
    if arguments.depth > 0:
        child = subprocess.Popen([
            sys.executable, str(Path(__file__).resolve()),
            "--marker", str(arguments.marker.resolve()),
            "--depth", str(arguments.depth - 1),
        ])
    try:
        while True:
            time.sleep(1)
    finally:
        if child is not None and child.poll() is None:
            child.terminate()


if __name__ == "__main__":
    main()
