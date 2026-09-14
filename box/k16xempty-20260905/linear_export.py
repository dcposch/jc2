from pathlib import Path
import sys
T=int(sys.argv[1]); root=Path('box/k16xempty-20260905').resolve(); out=root/f'linear_t{T}_terms.txt'; out.unlink(missing_ok=True)
s=f'''< "{root}/controls_t{T}_raw.sing";
proc dumprow(poly ff, string label)
{{
  write("{out}",label);
  while(ff!=0){{write("{out}",string(leadcoef(ff))+"|"+string(leadexp(ff))); ff=ff-lead(ff);}}
}}
for(int kk=1;kk<=size(rows);kk++){{dumprow(rows[kk],"ROW "+string(kk+1));}}
dumprow(target^2,"TARGET");
print("LINEAR_EXPORT_DONE t={T}");
quit;
'''
(root/f'linear_t{T}_export.sing').write_text(s)
