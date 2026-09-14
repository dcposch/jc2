"""Exact owner dispatch only under the separately issued physical GREEN."""
from pathlib import Path
import hashlib,subprocess,sys
ROOT=Path('/home/ubuntu/jc2');OWN=ROOT/'box/d125-hybrid-affine-first-attempt-20260907'
b=(ROOT/'box/d125-0220-root-harvest-20260907/HYBRID-PRODUCTION-GREEN.md').read_bytes()
if hashlib.sha256(b).hexdigest()!='cdc48d29ec0037cceca2c75ab0712a40d49cf1004ec80b2a7ea513392d60567e':raise ValueError('GREEN pin')
script='GREEN_BYTES=bytes.fromhex('+repr(b.hex())+')\n'+(OWN/'production_controller.py').read_text()
p=subprocess.Popen(['ssh','-i','/home/ubuntu/.ssh/jc2-fleet','-o','BatchMode=yes','-o','ConnectTimeout=10','ubuntu@172.30.0.56','/usr/bin/python3 -I -B -'],stdin=subprocess.PIPE)
p.communicate(script.encode());raise SystemExit(p.returncode)
