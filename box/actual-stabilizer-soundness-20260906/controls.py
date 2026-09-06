import json, sys
from fractions import Fraction as F
sys.path.insert(0, "/home/ubuntu/jc2/box/actual-stabilizer-soundness-20260906")
from verify import B, Tree, op_actual, op_coarse, op_live

print("== Moh p.202 table (MOH_TABLE, transcribed verbatim in the charged skeleton) ==")
for (n, m, Ms, V, tag, d1p, d2p, err) in B.MOH_TABLE:
    Vd = dict(V)
    c, a = op_coarse(n, m, Ms, Vd), op_actual(n, m, Ms, Vd)
    S = B.Skel(n, m, Ms, Vd)
    dl = [str(S.delta[i]) for i in range(1, S.s+1)]
    Lc = [S.L(j) for j in range(1, S.s)]
    r = Tree(n, m, Ms, True).run(Vd)
    print(f"  {tag:24s} s={S.s} delta={dl} L_coarse(j=1..s-1)={Lc}  coarse={c} ACTUAL={a}")
    # walk the surviving actual embedding, printing the centre modulus per level
    node = r; chain = []
    while isinstance(node, dict) and "j" in node:
        chain.append((node["j"], node["A"], node["cL"], node["mode"], node["b"], node["orbits"]))
        node = node.get("child")
    print(f"      embedding (j, A_actual, centre_L, mode, b, orbits): {chain}  bottom={node}")

print()
print("== (99,66) case (A) roster row R015 ==")
for Ms, V in [([77, 97], {2: 8, 3: 8})]:
    print("   (99,66)", Ms, V, "coarse", op_coarse(99, 66, Ms, V), "ACTUAL", op_actual(99, 66, Ms, V))

print()
print("== roster 66 ==")
rost = [json.loads(l) for l in open("/home/ubuntu/jc2/box/residual66-20260905/roster.jsonl")]
drop = []
for r in rost:
    s = r["source"]; Ms = s["M"][1:]; V = {i+2: s["V"][i] for i in range(len(s["V"]))}
    c, a = op_coarse(s["n"], s["m"], Ms, V), op_actual(s["n"], s["m"], Ms, V)
    if not c: print("  NOT COARSE-OPERATIVE:", r["row_id"])
    if not a: drop.append((r["row_id"], s["n"], s["m"], Ms, s["V"]))
print("  roster rows dropped by ACTUAL:", drop)
res64 = [r for r in rost if r["row_id"] not in ("R001", "R063")]
ok64 = sum(1 for r in res64 if op_actual(r["source"]["n"], r["source"]["m"], r["source"]["M"][1:],
                                        {i+2: r["source"]["V"][i] for i in range(len(r["source"]["V"]))}))
print(f"  residual 64: {ok64}/64 still actual-operative")
