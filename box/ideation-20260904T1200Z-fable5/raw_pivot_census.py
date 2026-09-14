import re, sys, collections
path=sys.argv[1]
term_re=re.compile(r'(?<![\w^])([+-]?)\s*(\d*)\*?((?:[A-Za-z_]\w*(?:\^\d+)?\*?)*)')
var_re=re.compile(r'([A-Za-z_][A-Za-z0-9_]*)(?:\^(\d+))?')
rows=0; mono=0; piv_rows=0; pivvars=set(); bucket=collections.Counter(); hp_piv=collections.Counter(); hp_rows=collections.Counter()
with open(path,encoding='utf-8') as f:
    next(f)
    for line in f:
        parts=line.rstrip('\n').split('|')
        if len(parts)<5: continue
        hp=parts[1]; expr=parts[4].strip()
        if expr.startswith('(') and expr.endswith(')'): expr=expr[1:-1]
        # split into terms on top-level +/- (expanded polynomial, no parentheses inside)
        terms=re.split(r'(?=[+-])', expr.replace(' ',''))
        terms=[t for t in terms if t and t not in '+-']
        rows+=1; hp_rows[hp]+=1
        n=len(terms)
        bucket['1' if n==1 else '2-3' if n<=3 else '4-10' if n<=10 else '11-100' if n<=100 else '>100']+=1
        if n==1: mono+=1
        # variable occurrence per term
        occ=collections.Counter(); deg1=[]
        for t in terms:
            vs=var_re.findall(t)
            names=[v for v,_ in vs]
            for v in set(names): occ[v]+=1
            if len(vs)==1 and (vs[0][1]=='' or vs[0][1]=='1'):
                deg1.append(vs[0][0])
        cand=[v for v in deg1 if occ[v]==1]
        if cand:
            piv_rows+=1; hp_piv[hp]+=1
            pivvars.update(cand)
print("rows",rows,"monomial_rows",mono,"rows_with_raw_unit_pivot",piv_rows,"distinct_pivotable_vars",len(pivvars))
print("term buckets",dict(bucket))
print("by h_power rows",dict(hp_rows),"pivot rows",dict(hp_piv))
print("pivotable vars sample",sorted(pivvars)[:40])
