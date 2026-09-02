#!/usr/bin/env python3
"""Reidemeister-Schreier + Fox calculus for H = rho^{-1}(Stab_0) <= G_{p,q}.

G = <x1,x2 | R>,  R = x1^p x2^-q.
Right action on cosets:  i . x = P_x(i),  P_x = rho(x)^{-1}  (transport conv.)
"""
import sys, itertools
from fractions import Fraction
sys.path.insert(0,'/tmp/cuspa')
from cover_h1 import perm_inv, perm_mul
import sympy as sp

def schreier(P, N):
    """P[g] = right-action perm for generator g+1. Return transversal words."""
    ng = len(P)
    Pi = [perm_inv(p) for p in P]
    t = [None]*N; t[0] = []
    tree = set()          # (i, signed letter) edges used in the tree
    order=[0]; seen={0}
    while order:
        i = order.pop(0)
        for g in range(ng):
            for sgn in (1,-1):
                jj = P[g][i] if sgn>0 else Pi[g][i]
                if jj not in seen:
                    seen.add(jj); t[jj] = t[i] + [sgn*(g+1)]
                    tree.add((i, sgn*(g+1))); tree.add((jj, -sgn*(g+1)))
                    order.append(jj)
    assert all(x is not None for x in t), "rho not transitive"
    return t, tree

def act(P, Pi, i, letter):
    g = abs(letter)-1
    return P[g][i] if letter>0 else Pi[g][i]

def rs_presentation(P, N, relator):
    """Return (gens, rels, gen_index) with gens = list of (i,g) Schreier gens."""
    ng = len(P); Pi=[perm_inv(p) for p in P]
    t, tree = schreier(P,N)
    # Schreier generators gamma_{i,g}, g=0..ng-1 ; trivial iff edge in tree
    gidx = {}
    gens = []
    for i in range(N):
        for g in range(ng):
            if (i, g+1) in tree:      # tree edge -> trivial generator
                continue
            gidx[(i,g)] = len(gens); gens.append((i,g))
    def rewrite(word, start=0):
        """tau of a word that lies in H, starting at coset `start` (must return)."""
        out=[]; i=start
        for letter in word:
            g=abs(letter)-1
            if letter>0:
                if (i,g) in gidx: out.append(gidx[(i,g)]+1)
                i = P[g][i]
            else:
                i = Pi[g][i]
                if (i,g) in gidx: out.append(-(gidx[(i,g)]+1))
        assert i==start, "word not in H"
        return out
    rels=[]
    for i in range(N):
        rels.append(rewrite(relator, i))
    return gens, rels, gidx, t, rewrite

def abelianization(gens, rels):
    n=len(gens)
    M = sp.zeros(len(rels), n)
    for r,rel in enumerate(rels):
        for L in rel:
            M[r, abs(L)-1] += (1 if L>0 else -1)
    return M

def smith_with_transform(M):
    """Return (D, U, V) with U*M*V = D  (sympy)."""
    from sympy.matrices.normalforms import smith_normal_decomp_domain
    return smith_normal_decomp_domain(M, domain=sp.ZZ)

def fox_alexander(gens, rels, ab_map, nvar, tvars):
    """ab_map[k] = vector (length nvar) = image of Schreier generator k in Z^j.
    Returns the Alexander matrix over Laurent polys."""
    def mono(vec):
        e = sp.Integer(1)
        for i,c in enumerate(vec):
            if c: e *= tvars[i]**int(c)
        return e
    rows=[]
    for rel in rels:
        row=[sp.Integer(0)]*len(gens)
        cur = [0]*nvar            # exponent of the prefix
        for L in rel:
            k=abs(L)-1
            if L>0:
                row[k] += mono(cur)
                cur = [cur[i]+ab_map[k][i] for i in range(nvar)]
            else:
                cur = [cur[i]-ab_map[k][i] for i in range(nvar)]
                row[k] -= mono(cur)
        rows.append(row)
    return sp.Matrix(rows)
