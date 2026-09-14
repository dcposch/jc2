#!/usr/bin/env python3
"""Exact polynomial composition for the complete declared QQ* graph map."""
from pathlib import Path
import hashlib,time
import sympy as sp
import flint
from flint import fmpq,fmpq_mpoly_ctx
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()

def verify(before,resolved,after,before_free,after_free):
 tick=time.monotonic();src=sorted(before_free,key=str);dst=sorted(after_free,key=str)
 assert src and dst and set(after)==set(before)|set(resolved)
 assert set(resolved)==set(src)-set(dst)
 R=fmpq_mpoly_ctx.get(tuple(map(str,src)),'lex');T=fmpq_mpoly_ctx.get(tuple(map(str,dst)),'lex')
 for ring,n in [(R,len(src)),(T,len(dst))]:
  for i in range(n):
   exponent=tuple(int(i==j) for j in range(n));assert ring.gen(i).to_dict()=={exponent:fmpq(1)}
 srcindex={v:i for i,v in enumerate(src)};dstindex={v:i for i,v in enumerate(dst)};rcache={};tcache={}
 def encode(expr,ctx,index,cache):
  expr=sp.sympify(expr)
  if expr in cache:return cache[expr]
  terms={}
  for monomial,c in expr.as_coefficients_dict().items():
   assert c.is_Rational;exponent=[0]*len(index)
   for variable,power in monomial.as_powers_dict().items():
    if variable==1:continue
    assert variable in index and power.is_Integer and power>=0
    exponent[index[variable]]=int(power)
   key=tuple(exponent);terms[key]=terms.get(key,fmpq(0))+fmpq(int(c.p),int(c.q))
  value=ctx.from_dict(terms);cache[expr]=value;return value
 images=[encode(resolved[x],T,dstindex,tcache) if x in resolved else T.gen(dstindex[x]) for x in src]
 for variable,rhs in before.items():
  got=encode(rhs,R,srcindex,rcache).compose(*images,ctx=T)
  assert got==encode(after[variable],T,dstindex,tcache),('exact native graph image mismatch',str(variable))
 for variable,rhs in resolved.items():assert encode(rhs,T,dstindex,tcache)==encode(after[variable],T,dstindex,tcache)
 return {'field':'Q','source_generator_order':list(map(str,src)),'target_generator_order':list(map(str,dst)),
  'explicit_generator_images':[[str(x),str(resolved[x]) if x in resolved else str(x)] for x in src],
  'source_and_target_generator_images_checked':True,'all_complete_map_images_verified':len(after),
  'no_quotient_used_in_QQstar_map_composition':True,'helper_sha256_at_import':OWN_SHA256,'python_flint':flint.__version__,'elapsed_seconds':time.monotonic()-tick}
