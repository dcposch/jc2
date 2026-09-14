#!/usr/bin/env python3
"""Parse expanded QQ polynomial text by exact rational monomial assembly."""
import ast,sys
from fractions import Fraction
from pathlib import Path
import hashlib
import sympy as sp
OWN_SHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
sys.setrecursionlimit(max(sys.getrecursionlimit(),100000))

def parse(text,variables):
 def mono(node):
  if isinstance(node,ast.Constant):
   assert isinstance(node.value,int) and not isinstance(node.value,bool);return Fraction(node.value),{}
  if isinstance(node,ast.Name):assert node.id in variables;return Fraction(1),{node.id:1}
  if isinstance(node,ast.UnaryOp):
   coefficient,powers=mono(node.operand);assert isinstance(node.op,(ast.UAdd,ast.USub));return (-coefficient if isinstance(node.op,ast.USub) else coefficient),powers
  assert isinstance(node,ast.BinOp)
  if isinstance(node.op,ast.Pow):
   assert isinstance(node.right,ast.Constant) and isinstance(node.right.value,int) and node.right.value>=0
   coefficient,powers=mono(node.left);n=node.right.value;return coefficient**n,{name:power*n for name,power in powers.items() if power*n}
  a,m=mono(node.left);b,n=mono(node.right)
  if isinstance(node.op,ast.Div):assert not n and b;return a/b,m
  assert isinstance(node.op,ast.Mult)
  powers=m.copy()
  for name,power in n.items():powers[name]=powers.get(name,0)+power
  return a*b,powers
 stack=[(1,ast.parse(text,mode='eval').body)];polynomial={}
 while stack:
  sign,node=stack.pop()
  if isinstance(node,ast.BinOp) and isinstance(node.op,(ast.Add,ast.Sub)):
   stack.append((sign,node.left));stack.append((-sign if isinstance(node.op,ast.Sub) else sign,node.right));continue
  coefficient,powers=mono(node);key=tuple(sorted(powers.items()));polynomial[key]=polynomial.get(key,Fraction(0))+sign*coefficient
 terms=[sp.Mul(sp.Rational(c.numerator,c.denominator),*(variables[name]**power for name,power in monomial)) for monomial,c in polynomial.items() if c]
 return sp.Add(*terms)
