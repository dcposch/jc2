import sys; sys.path.insert(0,'/tmp/nvm')
from synth import analyse_cluster
# positive control: reproduce the cluster of (x, x*y) : D=2, p1,p2 on L, p3 on E2
print("control (x,xy):", {k:v for k,v in analyse_cluster(2, [(1,['L']),(1,['L']),(1,[1])]).items()
                          if k in ('D','N','kappa','Lam','sat','ok')})
# control: (x, y+x^3):  D=3, p1 on L, p2 on L&E1, p3 on E1&E2, p4 on E3, p5 on E4
print("control (x,y+x^3):", {k:v for k,v in analyse_cluster(3,
      [(2,['L']),(1,['L',0]),(1,[0,1]),(1,[2]),(1,[3])]).items()
      if k in ('D','N','kappa','Lam','sat','ok')})
# control: (x, x^2 y^2): D=4, from engine  a=(?), rebuild by hand not needed
