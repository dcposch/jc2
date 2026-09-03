#!/usr/bin/env python3
"""Emit the t=3 gauged exact-Q system with explicit Rabinowitsch saturation.

This is the same encoding used by the frozen t=2 certificate.  The primary
t=3 driver separately emits and checks elim.lib sat(...)[1]; this alternate
encoding provides an independent exact route if rational sat() is slower.
"""

import argparse
import importlib.util


def load_driver():
    path = "/home/ubuntu/jc2/box/k16t3-20260903/t3/t_order_system.py"
    spec = importlib.util.spec_from_file_location("t_order_system", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--modstd", action="store_true")
    parser.add_argument("--slimgb", action="store_true")
    args = parser.parse_args()
    if args.modstd and args.slimgb:
        parser.error("choose at most one of --modstd and --slimgb")
    driver = load_driver()
    data = driver.build(t=3, gauged=True)
    T = driver.sp.Symbol("T")
    variables = data["params"] + [data["c"], T]
    equations = data["equations"]
    print("// t=3 exact-Q alternate: explicit Rabinowitsch encoding")
    print("// same coefficient equations and variable order as t_order_system.py")
    print('LIB "elim.lib";')
    if args.modstd:
        print('LIB "modstd.lib";')
        print("setcores(1);")
    print("ring RAC=0,(gamma,pi),dp;")
    print("poly FAC=pi;")
    print("poly GAC=pi-(gamma^2)/2;")
    print("poly JAC=diff(FAC,gamma)*diff(GAC,pi)-diff(FAC,pi)*diff(GAC,gamma);")
    print('if (JAC==gamma) { print("CONTROL_ACTUAL_PAIR_PASS J=gamma"); }'
          ' else { print("CONTROL_ACTUAL_PAIR_FAIL"); }')
    print("ring R=0,(%s),dp;" % ",".join(map(str, variables)))
    print("option(redSB);")
    print('if (nameof(basering)=="R") { print("CONTROL_RING_PASS R"); }'
          ' else { print("CONTROL_RING_FAIL"); }')
    # Keep explicit sat() extraction controls even though the main component
    # uses the equivalent Rabinowitsch equation.
    print("ideal C=c;")
    print("ideal CE=c;")
    print("list LE=sat(CE,C);")
    print("ideal SE=LE[1];")
    print('if (typeof(SE)=="ideal" && nameof(basering)=="R" && reduce(1,std(SE))==0)'
          ' { print("CONTROL_EMPTY_PASS"); } else { print("CONTROL_EMPTY_FAIL"); }')
    print("ideal CN=c-1;")
    print("list LN=sat(CN,C);")
    print("ideal SN=LN[1];")
    print('if (typeof(SN)=="ideal" && nameof(basering)=="R" && reduce(1,std(SN))!=0)'
          ' { print("CONTROL_NONEMPTY_PASS"); } else { print("CONTROL_NONEMPTY_FAIL"); }')
    print('print("MAIN_START equations=51 chart_unknowns=36 rabinowitsch_variables=1 characteristic=0");')
    generators = [driver.singular(e) for e in equations] + ["T*c-1"]
    print("ideal I=%s;" % ",\n".join(generators))
    method = "modStd(I,1)" if args.modstd else ("slimgb(I)" if args.slimgb else "std(I)")
    print("ideal G=%s;" % method)
    print('print("MAIN_DONE basis_size=");')
    print("size(G);")
    print('if (reduce(1,G)==0) { print("MAIN_SATURATED_EMPTY"); }'
          ' else { print("MAIN_NONTRIVIAL_SUPERSET_ONLY"); }')
    print("G;")
    print("quit;")


if __name__ == "__main__":
    main()
