import json,sys,copy,subprocess,os
P=json.load(open("cert_pristine.json"))
def find(c,r,col):
    for e in c["selected_matrix_entries"]:
        if e["row"]==r and e["column"]==col: return e
    return None
muts={}
def M(name,fn):
    c=copy.deepcopy(P); fn(c); muts[name]=c
M("M1_diagonal_1_to_2",       lambda c: find(c,0,0).__setitem__("terms",[[-1,-1,"2"]]))
M("M2_forbidden_upper_entry", lambda c: c["selected_matrix_entries"].append({"row":5,"column":7,"terms":[[-1,-1,"1"]]}))
M("M3_offdiag_coeff_perturbed",lambda c: [e for e in c["selected_matrix_entries"] if e["row"]>e["column"]][0]["terms"][0].__setitem__(2,"999"))
M("M4_delete_one_entry",      lambda c: c["selected_matrix_entries"].pop(500))
M("M5_basis_poly_coeff",      lambda c: c["basis"][3]["polynomial"][0].__setitem__(2,"13/7"))
M("M6_source_combination",    lambda c: c["basis"][10]["source_combination"].__setitem__(list(c["basis"][10]["source_combination"])[0],"7"))
M("M7_swap_selected_row",     lambda c: c["basis"][4].__setitem__("selected_J_row",c["basis"][5]["selected_J_row"]))
M("M8_source_column_entry",   lambda c: c["source_columns"][0][0].__setitem__(2,"5"))
M("M9_minor_size_188",        lambda c: c["minor"].__setitem__("size",188))
M("M10_free_constant_not_1",  lambda c: c["basis"][191].__setitem__("polynomial",[[0,0,"2"]]))
env=dict(os.environ); env["MUTATE"]="1"
res={}
for k,c in muts.items():
    json.dump(c,open("filtered_basis_certificate.json","w"),sort_keys=True,separators=(",",":"))
    p=subprocess.run([sys.executable,"verify_patched.py"],capture_output=True,text=True,env=env,timeout=300)
    last=[l for l in p.stderr.strip().splitlines() if l.strip()][-1] if p.stderr.strip() else "(no stderr)"
    res[k]=(p.returncode,last)
    print(f"{k:28s} rc={p.returncode}  {last[:70]}")
open("../mutation_results.txt","w").write("\n".join(f"{k}\trc={v[0]}\t{v[1]}" for k,v in res.items())+"\n")
print("ALL MUTATIONS REJECTED:",all(v[0]!=0 for v in res.values()))
