import pathlib
p=pathlib.Path('rank_driver.py'); s=p.read_text()
R=[('poly c{r}=subst(T{k},b3,0);','poly cc{r}=subst(T{k},b3,0);'),
('poly b{r}=subst(diff(T{k},b3),b3,0);','poly bb{r}=subst(diff(T{k},b3),b3,0);'),
('poly a{r}=subst(diff(diff(T{k},b3),b3),b3,0)/2;','poly aa{r}=subst(diff(diff(T{k},b3),b3),b3,0)/2;'),
('if (T{k}-(a{r}*b3^2+b{r}*b3+c{r})!=0)','if (T{k}-(aa{r}*b3^2+bb{r}*b3+cc{r})!=0)'),
('string(deg(a{r}))+\\" size=\\"+string(size(a{r}))+\\" homog=\\"+string(homog(a{r}))','string(deg(aa{r}))+\\" size=\\"+string(size(aa{r}))+\\" homog=\\"+string(homog(aa{r}))'),
('string(deg(b{r}))+\\" size=\\"+string(size(b{r}))+\\" homog=\\"+string(homog(b{r}))','string(deg(bb{r}))+\\" size=\\"+string(size(bb{r}))+\\" homog=\\"+string(homog(bb{r}))'),
('string(deg(c{r}))+\\" size=\\"+string(size(c{r}))+\\" homog=\\"+string(homog(c{r}))','string(deg(cc{r}))+\\" size=\\"+string(size(cc{r}))+\\" homog=\\"+string(homog(cc{r}))'),
('print("A0VALUE: "+string(a0));','print("A0VALUE: "+string(aa0));'),
('if (a0==0) { print("A0_ZERO','if (aa0==0) { print("A0_ZERO'),
('f"poly B{r}=a0*b{r}-a{r}*b0;", f"poly C{r}=a0*c{r}-a{r}*c0;"','f"poly B{r}=aa0*bb{r}-aa{r}*bb0;", f"poly C{r}=aa0*cc{r}-aa{r}*cc0;"'),
('f"if (G{r}-(a0*T{k}-a{r}*T{2*t-1})!=0)','f"if (G{r}-(aa0*T{k}-aa{r}*T{2*t-1})!=0)'),
('f"poly W{r}=a0*C{r}^2-b0*B{r}*C{r}+c0*B{r}^2;"','f"poly W{r}=aa0*C{r}^2-bb0*B{r}*C{r}+cc0*B{r}^2;"'),
('f"if (W{r}-(B{r}^2*T{2*t-1}-G{r}*(a0*G{r}-2*a0*C{r}+b0*B{r}))!=0)','f"if (W{r}-(B{r}^2*T{2*t-1}-G{r}*(aa0*G{r}-2*aa0*C{r}+bb0*B{r}))!=0)'),
('for nm in (f"b{r}", f"c{r}") + ((f"B{r}", f"C{r}") if r >= 1 else ()):','for nm in (f"bb{r}", f"cc{r}") + ((f"B{r}", f"C{r}") if r >= 1 else ()):'),
('L += ["poly a0=imap(S,a0); poly b0=imap(S,b0); poly c0=imap(S,c0);"]','L += ["poly a0=imap(S,aa0); poly b0=imap(S,bb0); poly c0=imap(S,cc0);"]'),
('"int ic; for (ic=1; ic<=size(pd); ic++) { ideal Pc=std(pd[ic][2]); ideal Qc=std(pd[ic][1]); "','"int ic; ideal Pc; ideal Qc; for (ic=1; ic<=size(pd); ic++) { Pc=std(pd[ic][2]); Qc=std(pd[ic][1]); "'),
]
n=0
for a,b in R:
    if a in s: s=s.replace(a,b); n+=1
    else: print("MISSING:",a[:70])
p.write_text(s); print("replacements",n,"of",len(R))
