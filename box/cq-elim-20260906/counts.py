import json
def T(d): return (d+1)*(d+2)//2          # coeffs of a poly of total degree <= d
def rows_char(n,m,D2):
    """Astra (2): q_pq=0 (q>D2), q_{p,D2}=0 (p>0), q_{0,D2}-lam=0, Z*lam-1 ; p+q<=L"""
    L=2*n
    a=sum(L-q+1 for q in range(D2+1,L+1))     # q > D2
    b=L-D2                                    # q = D2, p>0  (p<=L-D2)
    return a+b+1+1
def report(tag,n,m,D2):
    L=2*n; drop=D2+m-2-n
    F=T(n); G=T(m); Q=T(D2)
    jac=T(n+m-2)                              # J(F,G)-1 coefficient rows
    ch=rows_char(n,m,D2)
    degblk=sum((119 if False else (D2+m-2-nu)+1) for nu in range(1,drop+1))
    out=dict(tag=tag,n=n,m=m,D2=D2,L=L,drop=drop,
      F_block=F,G_block=G,Q_block=Q,QF_ratio=round(Q/F,4),
      unk_F=F+G+7, unk_CQ=Q+G+7, unk_ratio=round((Q+G+7)/(F+G+7),4),
      rows_F=jac+ch, rows_CQ=jac+degblk,
      jac=jac, char=ch, degblk=degblk,
      rows_ratio=round((jac+degblk)/(jac+ch),4),
      obstr_per_band=None)
    print("=== %s  n=%d m=%d D2=%d ==="%(tag,n,m,D2))
    print("  UNKNOWNS   F-chart: F %d + G %d + (a,b,c,d,e0,lam,Z) 7 = %d"%(F,G,F+G+7))
    print("             CQ-chart: Q %d + G %d + 7                  = %d"%(Q,G,Q+G+7))
    print("             Q-block/F-block = %.4f   total = %.4f"%(Q/F,(Q+G+7)/(F+G+7)))
    print("  ROWS       F-chart: Jacobian %d + characteristic %d = %d"%(jac,ch,jac+ch))
    print("             CQ-chart: Keller (E2) %d + degree-drop %d = %d"%(jac,degblk,jac+degblk))
    print("             ratio = %.4f"%((jac+degblk)/(jac+ch)))
    print("  degree-drop block: %d bands, %d rows total; %d are the obstruction rows"
          %(drop,degblk,0))
    return out
o1=report("(99,66)",99,66,55)
print()
o2=report("D=108",108,72,63)
json.dump([o1,o2],open('box/cq-elim-20260906/counts.json','w'),indent=1)
