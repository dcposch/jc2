#!/usr/bin/env python3
"""Set exact FLINT worker parallelism before running an immutable driver."""
import argparse,hashlib,json,runpy,sys
from pathlib import Path
import flint
p=argparse.ArgumentParser();p.add_argument('--threads',type=int,default=8);p.add_argument('--driver',type=Path,required=True);p.add_argument('--configuration',type=Path,required=True);args,rest=p.parse_known_args()
assert args.threads>0
flint.ctx.threads=args.threads
config={'coefficient_arithmetic':'exact fmpq; execution configuration only','python_flint':flint.__version__,
    'threads':flint.ctx.threads,'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'driver':str(args.driver.resolve()),'driver_sha256':hashlib.sha256(args.driver.read_bytes()).hexdigest()}
args.configuration.write_text(json.dumps(config,indent=2,sort_keys=True)+'\n')
sys.argv=[str(args.driver)]+rest
runpy.run_path(str(args.driver),run_name='__main__')
