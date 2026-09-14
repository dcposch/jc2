# AST-only literal dump of the frozen client.py; never imports or executes it.
import ast, hashlib, sys
sys.dont_write_bytecode=True
p='/tmp/jc2-lane.YwoVCk/inputs/client.py'
raw=open(p,'rb').read()
print('client_sha256',hashlib.sha256(raw).hexdigest())
tree=ast.parse(raw)
for node in tree.body:
    if isinstance(node,ast.Assign):
        names=[t.id for t in node.targets if isinstance(t,ast.Name)]
        try:
            val=ast.literal_eval(node.value)
            s=repr(val)
            print('LITERAL',names,s if len(s)<600 else s[:600]+'...')
        except Exception as e:
            print('NONLITERAL',names,type(node.value).__name__)
    elif isinstance(node,(ast.FunctionDef,ast.ClassDef)):
        print('DEF',node.name,'lines',node.lineno,'-',node.end_lineno)
    elif isinstance(node,(ast.Import,ast.ImportFrom)):
        print('IMPORT',ast.dump(node)[:120])
