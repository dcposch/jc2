"""One pinned production order plus <=8-variable declared engineering fixtures."""
import hashlib
import json
import re

ORDER_SHA = '64c212c26a9883d1c0f674b93f0246f67e22a8b742b643c6628fd3c14014db66'
DP_NAMES_SHA = 'ccd93ccf39b0109a36dc89d54f1fd281bcef17b1dc5fab3c65f2988027333d73'
RING_SHA = 'd894d6427d39b774c403165c83bffddbe993b96345ee00d652f5af7a06219bca'
COMPARISON = 'lexicographically larger (W1,W2,W3,total,-last,...,-first)'


def need(condition, reason):
    if not condition:
        raise ValueError(reason)


def digest(value):
    return hashlib.sha256((json.dumps(value, sort_keys=True,
                           separators=(',', ':'))+'\n').encode()).hexdigest()


def descriptor(variables, weights):
    result = {'schema': 'jc2.d125-defect-order/v1', 'field': 'Q',
              'variables': list(variables), 'weight_rows': [list(row) for row in weights],
              'tie_break': 'dp', 'comparison': COMPARISON}
    validate(result)
    return result


def validate(order):
    need(set(order) == {'schema', 'field', 'variables', 'weight_rows', 'tie_break', 'comparison'},
         'order descriptor keys')
    names, rows = order['variables'], order['weight_rows']
    need(order['schema'] == 'jc2.d125-defect-order/v1' and order['field'] == 'Q'
         and order['tie_break'] == 'dp' and order['comparison'] == COMPARISON,
         'order descriptor semantics')
    need(type(names) is list and names and len(set(names)) == len(names)
         and all(type(v) is str and re.fullmatch(r'[A-Za-z_][A-Za-z_0-9]*', v) for v in names),
         'order variable names')
    need(type(rows) is list and len(rows) == 3 and all(type(row) is list and
         len(row) == len(names) and all(type(w) is int for w in row) for row in rows),
         'three exact full-length weight rows')
    need(min(rows[0]) > 0, 'positive global first weight')
    need(len(names) <= 8 or (len(names) == 269 and digest(order) == ORDER_SHA),
         'only pinned production order or declared tiny fixture')


def fixed(variables):
    need(digest({'field': 'Q', 'order': 'dp', 'variables': variables}) == DP_NAMES_SHA,
         'production variable identity/order drift')
    rows = [[], [], []]
    for name in variables:
        match = re.fullmatch(r'([AB])_g([0-9]+)_p([0-9]+)', name)
        if match:
            member, i, j = match[1], int(match[2]), int(match[3])
            defect = (15 if member == 'A' else 25)-i-j
            values = (defect, defect if member == 'B' else 0, i if member == 'B' else 0)
        else:
            need(name in ('lambda2', 'lambda3'), 'unexpected production variable')
            values = (3 if name == 'lambda2' else 2, 0, 0)
        for row, value in zip(rows, values):
            row.append(value)
    result = descriptor(variables, rows)
    need(digest(result) == ORDER_SHA, 'production order pin')
    need(hashlib.sha256(ring_declaration(result).encode()).hexdigest() == RING_SHA,
         'production ring declaration pin')
    return result


def ring_declaration(order):
    validate(order)
    return 'ring R=0,('+','.join(order['variables'])+'),('+','.join(
        'a('+','.join(map(str, row))+')' for row in order['weight_rows'])+',dp);\n'


def adapt_prefix(original, variables, order):
    validate(order)
    need(order['variables'] == variables, 'prefix order variables')
    first, separator, tail = original.partition('\n')
    need(separator and first == 'ring R=0,('+','.join(variables)+'),dp;'
         and tail.startswith('ideal I=\n') and tail.endswith(';\n'), 'checked dp source prefix required')
    return ring_declaration(order)+tail


def check_prefix(original, executed, variables, order):
    need(executed == adapt_prefix(original, variables, order),
         'only initial ring line may change; original ideal suffix drift')
