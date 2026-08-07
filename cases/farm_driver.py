"""Phase 3 farm driver CLI: family -> verdict pipeline (lib/farm.py).

Usage:
  python3 cases/farm_driver.py 9_24                 # one family (S4 alias)
  python3 cases/farm_driver.py 11_33mn23d132        # one family (catalog name)
  python3 cases/farm_driver.py --all-below 150      # the whole deg<=150 catalog
  python3 cases/farm_driver.py --list [--all-below N]      # catalog + cells
  python3 cases/farm_driver.py --queues 4 [--chars 65521]  # manifests -> queue.txt

Options:
  --outdir DIR      farm root (default systems/farm)
  --no-prefilter    disable the SURPLUS-EXT pre-filter (emit everything)
  --chars LIST      comma list, 0 = char 0 (default "65521,0")
  --queues N        after the run (or standalone), write N per-box queue.txt
JC_BACKEND defaults to flint here (lib/FASTCOEF.md); parity-proven identical.
"""
import sys, os, json, argparse

os.environ.setdefault("JC_BACKEND", "flint")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "lib"))
import farm
from families import get_pllc


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("families", nargs="*", help="family names / S4 aliases")
    ap.add_argument("--all-below", type=int, metavar="N",
                    help="run every catalog family with maxdeg <= N")
    ap.add_argument("--outdir", default=os.path.join(ROOT, "systems", "farm"))
    ap.add_argument("--no-prefilter", action="store_true")
    ap.add_argument("--chars", default="65521,0")
    ap.add_argument("--list", action="store_true",
                    help="print the catalog with pre-filter cells; no compute")
    ap.add_argument("--queues", type=int, metavar="N",
                    help="write N per-box queue.txt files from manifests")
    ap.add_argument("--resume", action="store_true",
                    help="skip families whose manifest.json already exists")
    args = ap.parse_args(argv)

    chars = tuple(int(c) for c in args.chars.split(",") if c != "")
    maxdeg = args.all_below or 150
    rows = farm.catalog(maxdeg)
    if args.list:
        settled = 0
        for r in rows:
            pf = farm.prefilter_family(r.cd)
            settled += pf["skip"]
            print(f"{r.name:24s} deg={r.deg:3d} k={pf['k']} "
                  f"d2*={pf['d2star']} yaxis={int(pf['yaxis'])} "
                  f"{pf['cell']}{' [SKIP]' if pf['skip'] else ''}")
        print(f"{len(rows)} families; pre-filter settles {settled} "
              "without compute")
        return 0

    todo = []
    if args.all_below:
        todo = rows
    for spec in args.families:
        todo.append(farm.find_family(spec, maxdeg))
    if not todo and args.queues is None:
        ap.error("no families given (name, --all-below N, --list or --queues)")

    if todo:
        os.makedirs(args.outdir, exist_ok=True)
        pllc = get_pllc(4 * max(max(r.cd.A0.a, r.cd.A0.b) for r in todo))
        settled = emitted = 0
        for r in todo:
            if args.resume and os.path.isfile(
                    os.path.join(args.outdir, r.name, "manifest.json")):
                print(f"== {r.name}: manifest exists, skipped (--resume)",
                      flush=True)
                continue
            print(f"== {r.name} (deg {r.deg}, mn {r.mn})", flush=True)
            man = farm.run_family(r, args.outdir, relroot=ROOT,
                                  prefilter=not args.no_prefilter,
                                  chars=chars, pllc=pllc)
            if man.get("settled_without_compute"):
                settled += 1
                print(f"   verdict: {man['verdict']} (pre-filter, no compute)")
            nsys = sum(len([s for s in e.get("systems", []) if "path" in s])
                       for e in man["cases"])
            emitted += nsys
            print(f"   {man.get('verdict')}: {len(man['cases'])} case(s), "
                  f"{nsys} system file(s)"
                  + (f", statuses: {man['statuses']}" if man["statuses"] else ""),
                  flush=True)
        print(f"DONE: {len(todo)} families, {settled} settled by pre-filter "
              f"without compute, {emitted} system files emitted")

    if args.queues:
        summary = farm.dispatch(args.outdir, args.queues, chars=chars or None)
        for i, (n, b) in enumerate(summary):
            print(f"box{i + 1:02d}: {n} jobs, {b} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
