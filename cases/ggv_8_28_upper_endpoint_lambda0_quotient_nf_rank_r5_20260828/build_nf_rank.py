#!/usr/bin/env python3
"""Compile reducer-safe ambient quotient residuals and exact rank certificates."""

from __future__ import annotations
import argparse, hashlib, importlib.util, itertools
from pathlib import Path

R1_SHA="409d0f586e14750df2792ab9c0027dfc4678f4fe1848eba1087dbefbd5ef9ce9"
COMPONENTS={"p":"P","c8p02":"C8P02","q1p02":"Q1P02","q1p03":"Q1P03","triple02":"TRIPLE02","triple03":"TRIPLE03"}

def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as s:
  for b in iter(lambda:s.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def load(path):
 if sha(path)!=R1_SHA:raise SystemExit('R1_COMPILER_SOURCE_DRIFT')
 spec=importlib.util.spec_from_file_location('r1',path)
 if spec is None or spec.loader is None:raise SystemExit('R1_IMPORT_FAILURE')
 m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def inputs(r1_path,matrix_path,archive_path,component):
 r1=load(r1_path); assignment=r1.matrix_assignment(matrix_path); factors,_=r1.factor_lookup(r1.archive_members(archive_path)); label=COMPONENTS[component]; zeros,factor=r1.component_spec(label,factors)
 if factor is None or factor in {'1','16'}:raise SystemExit('NONTRIVIAL_FACTOR_REQUIRED')
 specialized,counts=r1.specialize(assignment,zeros); remaining=[p for p in r1.PARAMETERS if p not in zeros]
 return label,zeros,factor,remaining,specialized,counts
def ambient_header(label,factor,remaining):
 lines=[
  f'ring ambient=0,({",".join(remaining)}),dp;',
  f'poly BRANCH_FACTOR={factor};',
  'if(BRANCH_FACTOR==0 || deg(BRANCH_FACTOR)==0){ print("FATAL_ZERO_OR_UNIT_FACTOR"); quit; }',
  'ideal BRANCH_IDEAL=BRANCH_FACTOR; ideal BRANCH_SB=std(BRANCH_IDEAL);',
  'poly BRANCH_REMAINDER=reduce(BRANCH_FACTOR,BRANCH_SB); poly UNIT_REMAINDER=reduce(1,BRANCH_SB);',
  'poly ADVERSARIAL_DISPLAYED_FACTOR=BRANCH_FACTOR; poly ADVERSARIAL_NF=reduce(ADVERSARIAL_DISPLAYED_FACTOR,BRANCH_SB); poly ADVERSARIAL_MUTATION_NF=reduce(ADVERSARIAL_DISPLAYED_FACTOR+1,BRANCH_SB);',
  'print("AMBIENT_BRANCH_REDUCER_ZERO="+string(BRANCH_REMAINDER==0)); print("AMBIENT_BRANCH_IDEAL_PROPER="+string(UNIT_REMAINDER!=0));',
  'print("ADVERSARIAL_DISPLAYED_FACTOR_NONZERO="+string(ADVERSARIAL_DISPLAYED_FACTOR!=0)); print("ADVERSARIAL_IDEAL_FACTOR_NF_ZERO="+string(ADVERSARIAL_NF==0)); print("ADVERSARIAL_MUTATION_NF_NONZERO="+string(ADVERSARIAL_MUTATION_NF!=0));',
  'if(BRANCH_REMAINDER!=0 || UNIT_REMAINDER==0 || ADVERSARIAL_DISPLAYED_FACTOR==0 || ADVERSARIAL_NF!=0 || ADVERSARIAL_MUTATION_NF==0){ print("FATAL_REDUCER_ADVERSARIAL_FIXTURE"); quit; }',
  f'write("{label}_BRANCH_FACTOR.txt",string(BRANCH_FACTOR));',
  f'write("{label}_BRANCH_STANDARD_BASIS.txt",string(BRANCH_SB));',
  'print("PINNED_STANDARD_BASIS_REDUCER_PASS=1");',
 ]
 if factor=='q2':
  lines.extend([
   'poly ADVERSARIAL_LITERAL_Q2=q2; poly ADVERSARIAL_LITERAL_Q2_NF=reduce(ADVERSARIAL_LITERAL_Q2,BRANCH_SB);',
   'print("ADVERSARIAL_LITERAL_Q2_AMBIENT_NONZERO="+string(ADVERSARIAL_LITERAL_Q2!=0)); print("ADVERSARIAL_LITERAL_Q2_NF_ZERO="+string(ADVERSARIAL_LITERAL_Q2_NF==0));',
   'if(ADVERSARIAL_LITERAL_Q2==0 || ADVERSARIAL_LITERAL_Q2_NF!=0){ print("FATAL_LITERAL_Q2_ADVERSARIAL_FIXTURE"); quit; }',
  ])
 return lines
def reduce_script(label,zeros,factor,remaining,assignment,counts):
 lines=['// Explicit ambient normal-form residual reduction.']+ambient_header(label,factor,remaining)+[assignment,'matrix B=M; int i; int j; int step=1; int found; int pi; int pj; int pivot_count=0; int invariant_failures=0; int operation_reductions=0; poly swap_entry; poly multiple; number inverse_unit;',f'string PIVOTFILE="{label}_NF_RATIONAL_UNIT_PIVOTS.tsv"; string RESIDUALFILE="{label}_NF_RESIDUAL_MATRIX.tsv";','write(PIVOTFILE,"step|source_row|source_col|pivot");','for(i=1;i<=106;i=i+1){ for(j=1;j<=105;j=j+1){ B[i,j]=reduce(B[i,j],BRANCH_SB); operation_reductions=operation_reductions+1; } }','while(step<=105){ found=0; pi=0; pj=0; for(i=step;i<=106 && found==0;i=i+1){ for(j=step;j<=105 && found==0;j=j+1){ B[i,j]=reduce(B[i,j],BRANCH_SB); operation_reductions=operation_reductions+1; if(B[i,j]!=0 && deg(B[i,j])==0){ found=1; pi=i; pj=j; } } } if(found==0){ step=106; } else { for(j=1;j<=105;j=j+1){ swap_entry=B[step,j]; B[step,j]=B[pi,j]; B[pi,j]=swap_entry; } for(i=1;i<=106;i=i+1){ swap_entry=B[i,step]; B[i,step]=B[i,pj]; B[i,pj]=swap_entry; } B[step,step]=reduce(B[step,step],BRANCH_SB); operation_reductions=operation_reductions+1; if(B[step,step]==0 || deg(B[step,step])!=0){ invariant_failures=invariant_failures+1; } inverse_unit=1/leadcoef(B[step,step]); for(i=step+1;i<=106;i=i+1){ multiple=reduce(B[i,step]*inverse_unit,BRANCH_SB); operation_reductions=operation_reductions+1; for(j=step;j<=105;j=j+1){ B[i,j]=reduce(B[i,j]-multiple*B[step,j],BRANCH_SB); operation_reductions=operation_reductions+1; } } for(j=step+1;j<=105;j=j+1){ multiple=reduce(B[step,j]*inverse_unit,BRANCH_SB); operation_reductions=operation_reductions+1; for(i=step;i<=106;i=i+1){ B[i,j]=reduce(B[i,j]-multiple*B[i,step],BRANCH_SB); operation_reductions=operation_reductions+1; } } for(i=1;i<=106;i=i+1){ if(i!=step && reduce(B[i,step],BRANCH_SB)!=0){ invariant_failures=invariant_failures+1; } } for(j=1;j<=105;j=j+1){ if(j!=step && reduce(B[step,j],BRANCH_SB)!=0){ invariant_failures=invariant_failures+1; } } write(PIVOTFILE,string(step)+"|"+string(pi)+"|"+string(pj)+"|"+string(B[step,step])); pivot_count=pivot_count+1; step=step+1; } }','if(pivot_count>=105){ print("FATAL_NO_RESIDUAL"); quit; }','int residual_rows=106-pivot_count; int residual_cols=105-pivot_count; matrix R[residual_rows][residual_cols]; int nf_drift=0;','write(RESIDUALFILE,"rows|"+string(residual_rows)+"|cols|"+string(residual_cols));','for(i=1;i<=residual_rows;i=i+1){ for(j=1;j<=residual_cols;j=j+1){ R[i,j]=reduce(B[pivot_count+i,pivot_count+j],BRANCH_SB); operation_reductions=operation_reductions+1; if(R[i,j]-reduce(R[i,j],BRANCH_SB)!=0){ nf_drift=nf_drift+1; } write(RESIDUALFILE,string(i)+"|"+string(j)+"|"+string(R[i,j])); } }',f'print("STRATUM_LABEL={label}"); print("ZERO_VARIABLES={",".join(zeros) if zeros else "NONE"}");',f'print("TOKEN_REPLACEMENTS={";".join(f"{k}:{v}" for k,v in counts.items())}");','print("NF_RATIONAL_UNIT_PIVOT_COUNT="+string(pivot_count)); print("NF_RESIDUAL_ROWS="+string(residual_rows)); print("NF_RESIDUAL_COLS="+string(residual_cols)); print("NF_OPERATION_REDUCTIONS="+string(operation_reductions)); print("NF_DRIFT_COUNT="+string(nf_drift)); print("NF_PIVOT_INVARIANT_FAILURES="+string(invariant_failures));','if(nf_drift!=0 || invariant_failures!=0){ print("FATAL_NF_OR_PIVOT_INVARIANT"); quit; }','print("EXPLICIT_NF_AFTER_EVERY_ENTRY_OPERATION=1"); print("NF_RESIDUAL_REDUCTION_COMPLETE=1"); quit;','']
 return '\n'.join(lines)
def read_residual(path):
 lines=path.read_text().splitlines(); fields=lines[0].split('|');
 if len(fields)!=4 or fields[0]!='rows' or fields[2]!='cols':raise SystemExit('RESIDUAL_HEADER_FAILURE')
 nr,nc=int(fields[1]),int(fields[3]); M=[['0']*nc for _ in range(nr)];seen=set()
 for line in lines[1:]:
  i,j,v=line.split('|',2);i=int(i);j=int(j)
  if not(1<=i<=nr and 1<=j<=nc) or (i,j) in seen:raise SystemExit('RESIDUAL_INDEX_FAILURE')
  seen.add((i,j));M[i-1][j-1]=v.replace(' ','')
 if len(seen)!=nr*nc:raise SystemExit('RESIDUAL_COMPLETENESS_FAILURE')
 return M
def max_matching(rows,cols,support):
 match={}
 def aug(r,seen):
  for c in cols:
   if (r,c) not in support or c in seen:continue
   seen.add(c)
   if c not in match or aug(match[c],seen):match[c]=r;return True
  return False
 return sum(aug(r,set()) for r in rows)
def perfect(rows,cols,support):return max_matching(rows,cols,support)==len(rows)
def rank_script(label,factor,remaining,M,structural_path):
 nr,nc=len(M),len(M[0]); support={(i+1,j+1) for i,row in enumerate(M) for j,v in enumerate(row) if v!='0'}; r=max_matching(tuple(range(1,nr+1)),tuple(range(1,nc+1)),support)
 rsets=[(rs,cs) for rs in itertools.combinations(range(1,nr+1),r) for cs in itertools.combinations(range(1,nc+1),r) if perfect(rs,cs,support)]
 higher=[];slot=0
 if r<min(nr,nc):
  for rs in itertools.combinations(range(1,nr+1),r+1):
   for cs in itertools.combinations(range(1,nc+1),r+1):
    slot+=1; ok=perfect(rs,cs,support);higher.append(f"{slot}|{','.join(map(str,rs))}|{','.join(map(str,cs))}|{'MATCHABLE' if ok else 'STRUCTURAL_ZERO'}")
 if any(line.endswith('|MATCHABLE') for line in higher):raise SystemExit('HIGHER_SUPPORT_BOUND_FAILURE')
 structural_path.write_text('slot|rows|cols|classification\n'+'\n'.join(higher)+'\n')
 vals=','.join(v for row in M for v in row)
 lines=['// Exact ambient NF rank certificate.']+ambient_header(label,factor,remaining)+[f'matrix R[{nr}][{nc}]={vals};','int i; int j; int support_replay_failures=0; int entry_nf_reductions=0;','for(i=1;i<=nrows(R);i=i+1){ for(j=1;j<=ncols(R);j=j+1){ R[i,j]=reduce(R[i,j],BRANCH_SB); entry_nf_reductions=entry_nf_reductions+1; } }']
 for i in range(1,nr+1):
  for j in range(1,nc+1):
   if (i,j) in support:lines.append(f"if(R[{i},{j}]==0){{ support_replay_failures=support_replay_failures+1; }}")
   else:lines.append(f"if(R[{i},{j}]!=0){{ support_replay_failures=support_replay_failures+1; }}")
 lines += [f'string CANDIDATES="{label}_STRUCTURAL_RANK_CANDIDATES_RAW_NF.tsv"; string WITNESS="{label}_RANK_WITNESS.tsv";','write(CANDIDATES,"slot|rows|cols|raw_determinant|normal_form"); write(WITNESS,"slot|rows|cols|normal_form");','int candidate_count=0; int nf_nonzero_count=0; int witness_found=0; int determinant_nf_reductions=0;']
 if r==0:
  lines += ['poly DRAW=1; poly DNF=reduce(DRAW,BRANCH_SB); determinant_nf_reductions=determinant_nf_reductions+1; candidate_count=1;','write(CANDIDATES,"1|EMPTY|EMPTY|"+string(DRAW)+"|"+string(DNF));','if(DNF!=0){ nf_nonzero_count=1; witness_found=1; write(WITNESS,"1|EMPTY|EMPTY|"+string(DNF)); }','kill DRAW; kill DNF;']
 else:
  for idx,(rs,cs) in enumerate(rsets,1):
   entries=','.join(f'R[{i},{j}]' for i in rs for j in cs)
   lines += [f'matrix S[{r}][{r}]={entries}; poly DRAW=det(S); poly DNF=reduce(DRAW,BRANCH_SB); determinant_nf_reductions=determinant_nf_reductions+1; candidate_count=candidate_count+1;',f'write(CANDIDATES,"{idx}|{",".join(map(str,rs))}|{",".join(map(str,cs))}|"+string(DRAW)+"|"+string(DNF));',f'if(DNF!=0){{ nf_nonzero_count=nf_nonzero_count+1; if(witness_found==0){{ witness_found=1; write(WITNESS,"{idx}|{",".join(map(str,rs))}|{",".join(map(str,cs))}|"+string(DNF)); }} }}','kill S; kill DRAW; kill DNF;']
 lines += [f'print("STRUCTURAL_RANK_BOUND={r}"); print("STRUCTURAL_RANK_CANDIDATE_COUNT="+string(candidate_count)); print("RANK_CANDIDATE_NF_NONZERO_COUNT="+string(nf_nonzero_count)); print("RANK_WITNESS_NF_NONZERO="+string(witness_found));',f'print("HIGHER_MINOR_SIZE={r+1}"); print("HIGHER_MINOR_FORMAL_SLOT_COUNT={len(higher)}"); print("HIGHER_MINOR_MATCHABLE_SLOT_COUNT=0");','print("SUPPORT_REPLAY_FAILURES="+string(support_replay_failures)); print("ENTRY_NF_REDUCTIONS="+string(entry_nf_reductions)); print("DETERMINANT_NF_REDUCTIONS="+string(determinant_nf_reductions));','if(support_replay_failures!=0 || witness_found!=1){ print("FATAL_RANK_CERTIFICATE_REPLAY"); quit; }','print("EVERY_HIGHER_MINOR_STRUCTURALLY_ZERO_AFTER_NF=1"); print("EXACT_QUOTIENT_RANK_CERTIFICATE_COMPLETE=1"); quit;','']
 return '\n'.join(lines),r,len(rsets),len(higher)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--phase',choices=('reduce','rank'),required=True);ap.add_argument('--r1-compiler',type=Path,required=True);ap.add_argument('--matrix',type=Path,required=True);ap.add_argument('--factor-archive',type=Path,required=True);ap.add_argument('--component',choices=sorted(COMPONENTS),required=True);ap.add_argument('--residual',type=Path);ap.add_argument('--output-dir',type=Path,required=True);a=ap.parse_args()
 label,zeros,factor,remaining,assignment,counts=inputs(a.r1_compiler,a.matrix,a.factor_archive,a.component);a.output_dir.mkdir(parents=True,exist_ok=True)
 if a.phase=='reduce':
  text=reduce_script(label,zeros,factor,remaining,assignment,counts);name=f'{a.component}_nf_reduce.sing'
 else:
  if a.residual is None:raise SystemExit('RESIDUAL_REQUIRED')
  M=read_residual(a.residual);text,r,c,h=rank_script(label,factor,remaining,M,a.output_dir/f'{label}_HIGHER_MINOR_STRUCTURAL_SLOTS.tsv');name=f'{a.component}_nf_rank.sing';print(f'STRUCTURAL_RANK_BOUND={r}');print(f'RANK_CANDIDATES={c}');print(f'HIGHER_MINOR_SLOTS={h}')
 (a.output_dir/name).write_text(text);(a.output_dir/f'BUILD_MANIFEST_{a.phase}.tsv').write_text(f'phase|component|label|script|sha256\n{a.phase}|{a.component}|{label}|{name}|{hashlib.sha256(text.encode()).hexdigest()}\n');print(f'COMPONENT={a.component}');print(f'LABEL={label}');print(f'PHASE={a.phase}');print('NO_QRING_AMBIENT_NF_ONLY=1');print('NF_RANK_BUILD_PASS')
if __name__=='__main__':main()
