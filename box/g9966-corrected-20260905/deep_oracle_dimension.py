#!/usr/bin/env python3
"""Bounded exact AST exporter for expanded QQ polynomials; no SymPy parsing.
Each accepted AST is a sum of rational monomials. Fractions are evaluated with
Fraction, exponents must be nonnegative Python integers, and every variable is
checked in the declared complete free ring. Every row is multiplied by its
recorded nonzero integer denominator before Singular serialization.
"""
import argparse,ast,hashlib,json,math,re,subprocess,sys,time
from fractions import Fraction
from pathlib import Path
sys.setrecursionlimit(100000)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def monomial(node,allowed):
 if isinstance(node,ast.Constant):
  assert isinstance(node.value,int) and not isinstance(node.value,bool);return Fraction(node.value),{}
 if isinstance(node,ast.Name):assert node.id in allowed;return Fraction(1),{node.id:1}
 if isinstance(node,ast.UnaryOp):
  c,m=monomial(node.operand,allowed);assert isinstance(node.op,(ast.UAdd,ast.USub));return (-c if isinstance(node.op,ast.USub) else c),m
 assert isinstance(node,ast.BinOp)
 if isinstance(node.op,ast.Pow):
  assert isinstance(node.right,ast.Constant) and isinstance(node.right.value,int) and node.right.value>=0
  c,m=monomial(node.left,allowed);n=node.right.value;return c**n,{v:k*n for v,k in m.items() if k*n}
 a,m=monomial(node.left,allowed);b,n=monomial(node.right,allowed)
 if isinstance(node.op,ast.Div):assert not n and b;return a/b,m
 assert isinstance(node.op,ast.Mult)
 out=m.copy()
 for v,k in n.items():out[v]=out.get(v,0)+k
 return a*b,out
def polynomial(text,allowed):
 tree=ast.parse(text,mode='eval').body;stack=[(1,tree)];out={}
 while stack:
  sign,node=stack.pop()
  if isinstance(node,ast.BinOp) and isinstance(node.op,(ast.Add,ast.Sub)):
   stack.append((sign,node.left));stack.append((-sign if isinstance(node.op,ast.Sub) else sign,node.right));continue
  c,m=monomial(node,allowed);key=tuple(sorted(m.items()));out[key]=out.get(key,Fraction(0))+sign*c
 return {m:c for m,c in out.items() if c}
def encode(poly):
 den=math.lcm(*(c.denominator for c in poly.values())) if poly else 1;terms=[]
 for m,c in sorted(poly.items()):
  value=c*den;assert value.denominator==1
  terms.append(str(value.numerator)+''.join('*'+v+('^'+str(n) if n!=1 else '') for v,n in m))
 return '+'.join(terms) or '0',den
def controls():
 p=polynomial('q**9/32768 + 1/2',{'q'});a,d=encode(p);assert p=={(('q',9),):Fraction(1,32768),():Fraction(1,2)} and d==32768
 for bad in ('q**1.0','1/q','sqrt(2)','hidden+q'):
  try:polynomial(bad,{'q'})
  except (AssertionError,ValueError,TypeError):pass
  else:raise AssertionError(bad)
 return {'rational_power_primitive':a,'multiplier':d,'negative_controls':4}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--state',type=Path,required=True);ap.add_argument('--oracle',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args();begin=time.monotonic()
 old=json.loads(a.state.read_text());oracle=json.loads(a.oracle.read_text());assert oracle['map_before']==old['cumulative_map'];assert oracle['branch']==old['branch'];assert oracle['tp']==old['last_completed_t']+1
 allowed=set(old['free_after']);branch=old['branch'];loc='rho' if branch=='delta2' else 'c';zloc='Zrho' if branch=='delta2' else 'Zc';assert zloc not in allowed and loc in allowed
 cfg=old['coefficient_quotient'];assert polynomial(cfg['polynomial'],allowed)==polynomial(oracle['metadata']['relation'],allowed)
 assert oracle['metadata']['combined_A_plus_B_delta_rows'] is True and oracle['metadata']['conjugate_selected'] is False
 rows=old['residual_rows']+[(f'oracle_J{oracle["tp"]}_k{k}',v) for k,v in sorted(oracle['rows'].items(),key=lambda kv:int(kv[0]))]
 entries=[];multipliers=[]
 for label,expr in rows:
  pol=polynomial(expr,allowed);entry,den=encode(pol);entries.append(entry);multipliers.append([label,str(den),len(pol)])
 print(f'{branch}: exact AST encoded {len(entries)} rows in {time.monotonic()-begin:.2f}s',flush=True)
 script='ring R=0,('+','.join(sorted(allowed)+[zloc])+'),dp;\nideal I='+','.join(entries)+f',{zloc}*{loc}-1;\nideal S=std(I);\nprint("BEGIN_DIM");print(dim(S));print("END_DIM");\nprint("BEGIN_GB");print(S);print("END_GB");\n'
 script+=f'ideal C0={loc},{zloc}*{loc}-1;ideal C1={loc}-1,{zloc}*{loc}-1;\nprint("BEGIN_CTL");print(reduce(1,std(C0)));print(reduce(1,std(C1)));print("END_CTL");quit;\n'
 sing=a.output.with_suffix('.sing');sing.write_text(script)
 result={'status':'DIMENSION_PENDING','branch':branch,'t':oracle['tp'],'state':str(a.state),'state_sha256':sha(a.state),'oracle':str(a.oracle),'oracle_sha256':sha(a.oracle),'driver_sha256':sha(__file__),'field':'Q','ordered_full_free_ring':sorted(allowed),'localizer_wrapper':f'{zloc}*{loc}-1','exact_map_equality':True,'exact_relation_equality':True,'oracle_metadata':oracle['metadata'],'controls':controls(),'integer_row_multipliers_and_terms':multipliers,'singular_sha256':sha(sing)}
 a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 run=subprocess.run(['Singular','-q',str(sing)],capture_output=True,text=True,check=True);out=run.stdout+run.stderr;a.output.with_suffix('.sing.out').write_text(out)
 assert not re.search(r'(^|\n)\s*\?',out) and 'error' not in out.lower(),out[:1000]
 dim=int(out.split('BEGIN_DIM\n')[1].split('\nEND_DIM')[0].strip());ctl=out.split('BEGIN_CTL\n')[1].split('\nEND_CTL')[0].strip();assert ctl=='0\n1'
 result.update({'status':'PASS','dimension':dim,'unit_ideal':dim==-1,'elapsed_seconds':time.monotonic()-begin,'singular_output_sha256':sha(a.output.with_suffix('.sing.out'))});a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n');print(f'{branch}: J{oracle["tp"]} full-ring dimension={dim}',flush=True)
if __name__=='__main__':main()
