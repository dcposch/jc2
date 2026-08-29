#!/usr/bin/env python3
"""Fast deterministic gates for the Sigray root/nonroot M=1 repair.

This is intentionally a unit/smoke suite, not a census.  It exercises the
scope boundary and the formerly suppressed root menus in well under a second
apart from importing the exact-arithmetic engines.
"""
from fractions import Fraction as Fr
from pathlib import Path
from contextlib import redirect_stdout
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sheet6_campaign as sc
import h3_check as h3
import hiii_compose as hiii
import twopole_check as tp


def check_dispositions():
    root_m1 = sc.Node(Fr(1, 2), 1, 1, 1, 1, tag="synthetic-root")
    assert sc.dispose_m1(root_m1) == sc.TERMINAL_ROOT_M1
    assert sc.dispose_m1(root_m1, certified_nonroot=True) == sc.KILL_NR_M1

    # Pole metadata is an independent nonroot certificate even when a unit
    # fixture deliberately copies the numerical axis signature.
    pole_like = sc.Node(Fr(1, 2), 1, 1, 1, 1, tag="synthetic-pole")
    assert sc.dispose_m1(pole_like, certified_nonroot=True) == sc.KILL_NR_M1
    return "disposition root/NR/pole certificates"


def check_shared_bfs_order():
    entry = sc.Node(Fr(1), 2, 2, 3, 2, tag="synthetic-entry")
    root = sc.Node(Fr(1, 2), 1, 1, 1, 1, tag="synthetic-root")
    nonroot_m1 = sc.Node(Fr(1, 2), 2, 1, 1, 1, tag="synthetic-nonroot")
    old_step = sc.step
    try:
        sc.step = lambda _: [
            ('CONT', 0, root, 'synthetic root child'),
            ('CONT', 0, nonroot_m1, 'synthetic nonroot M1 child'),
        ]
        result = sc.bash(entry, budget=0, maxdepth=1)
    finally:
        sc.step = old_step
    assert len(result['root']) == 1
    assert sc.TERMINAL_ROOT_M1 in result['root'][0][0][-1]
    assert not result['frontier']       # nonroot M1 was pruned, not enqueued
    return "sheet6_campaign.bash root-before-M filter"


def check_hidden_branches_restored():
    mu1_parent = sc.Node(Fr(1, 2), 3, 2, 2, 2)
    mu2_parent = sc.Node(Fr(5, 4), 3, 2, 2, 2)
    mu1_roots = [o for o in sc.step(mu1_parent)
                 if o[0] == 'CONT' and sc.has_root_signature(o[2])
                 and 'mu=1 MU1' in o[3]]
    mu2_roots = [o for o in sc.step(mu2_parent)
                 if o[0] == 'CONT' and sc.has_root_signature(o[2])
                 and 'mu=2 I' in o[3]]
    assert mu1_roots and all(o[2].M == 1 for o in mu1_roots)
    assert mu2_roots and all(o[2].M == 1 for o in mu2_roots)
    # The omitted mu=2 IIb/III paths have nu_F>=2 and M_F=1, so the common
    # step may still prune them structurally as certified NR-M1.
    assert not any(o[0] == 'CONT' and ('mu=2 IIb' in o[3] or 'mu=2 III' in o[3])
                   for o in sc.step(mu2_parent))
    return "mu=1 single-orbit and mu=2 case-I root emission"


def check_mu1_unbounded_and_zero_cost_tails():
    witness = sc.Node(Fr(1, 100), 101, 1, 100, 1,
                      tag="root-cap-witness")
    red = sc.reduce_ratio(witness.rho, witness.nu, witness.kap, 1, 'II')
    assert red == dict(a=100, b=1, c=100, e=100, m0=0,
                       n0=(0, 1), style='II')

    # KMAX is intentionally irrelevant for MU1: the exact divisor solver
    # must find the l=98 root even under a nominal zero cap.
    solutions = []
    for cap in (0, 1, 48, 120):
        pts, fams, cert = sc.solve_pattern(red, 1, 'MU1', KMAX=cap)
        assert (98, 1, 0) in pts and not fams
        assert cert.startswith('EXACT MU1 divisor solve')
        assert 'box' not in cert.lower() and 'KMAX' not in cert
        solutions.append(pts)
    assert all(pts == solutions[0] for pts in solutions)

    # The a=c=0 specialization is also exact: it is an all-m family and
    # therefore cannot be mistaken for a finite-search closure.
    degenerate = dict(a=0, b=1, c=0, e=3, m0=0,
                      n0=(0, 1), style='II')
    pts, fams, cert = sc.solve_pattern(degenerate, 1, 'MU1', KMAX=0)
    assert not pts and fams == [
        ('MU1', 1, 1, 'ALL m>=0 exact constant-ratio family')]
    assert cert.startswith('EXACT MU1 degenerate')

    outcomes = sc.step_one_branch(witness, 1, 'MU1')
    roots = [o for o in outcomes if o[0] == 'CONT'
             and sc.has_root_signature(o[2])]
    assert roots and roots[0][1] == 0
    assert sc.dispose_constructed_child(roots[0][2]) == sc.TERMINAL_ROOT_M1

    # Every still-capped zero-charge IIa_0 search carries mandatory OPEN.
    iia0 = sc.step_one_branch(sc.V96, 2, 'IIa_0')
    assert any(o[0] == 'OPEN' and 'zero-charge tail' in o[1]
               and 'NO_VERDICT' in o[1] for o in iia0)
    tp_tail = tp.mu1_children(sc.Node(Fr(1), 2, 1, 5, 2))
    assert any(o[0] == 'OPEN' and 'NO_VERDICT' in o[1] for o in tp_tail)
    iv_rows, _ = h3.iv_dispositions(
        sc.Node(Fr(1, 2), (1, 2), 2, (0, 1), 2), lam=0, td=6)
    assert any(verdict == 'OPEN_s_tail' for _, verdict, _ in iv_rows)
    return "unbounded MU1 l=98 and mandatory zero-charge cap residues"


def check_twopole_suffix_order():
    entry = sc.Node(Fr(1), 2, 2, 3, 2, tag="synthetic-interior-merge")
    root = sc.Node(Fr(1, 2), 1, 1, 1, 1, tag="synthetic-root")
    nonroot_m1 = sc.Node(Fr(1, 2), 2, 1, 1, 1, tag="synthetic-nonroot")
    old_step = tp.hx.step_e5
    try:
        tp.hx.step_e5 = lambda _: [
            ('CONT', 0, root, 'synthetic root child'),
            ('CONT', 0, nonroot_m1, 'synthetic nonroot M1 child'),
        ]
        result = tp.suffix_bash(entry, 0, certified_nonroot=True)
    finally:
        tp.hx.step_e5 = old_step
    assert len(result['sf1']) == 1
    assert result['sf1'][0][-1] == sc.TERMINAL_ROOT_M1
    assert result['frontier'] == 0
    return "twopole suffix root-before-M filter"


def check_review_bfs_order():
    entry = sc.Node(Fr(1), 2, 2, 3, 2, tag="synthetic-entry")
    root = sc.Node(Fr(1, 2), 1, 1, 1, 1, tag="synthetic-root")
    nonroot_m1 = sc.Node(Fr(1, 2), 2, 1, 1, 1, tag="synthetic-nonroot")
    outcomes = [
        ('CONT', 0, root, 'synthetic root child'),
        ('CONT', 0, nonroot_m1, 'synthetic nonroot M1 child'),
    ]
    entries = [("synthetic", 0, True, entry)]

    old_sc_step = sc.step
    try:
        sc.step = lambda _: outcomes
        out = io.StringIO()
        with redirect_stdout(out):
            h3.run(entries, td=3, budget=0, label="synthetic")
        assert "root terminals (case I/single-orbit): 1" in out.getvalue()
    finally:
        sc.step = old_sc_step

    old_e5_step = hiii.step_e5
    try:
        hiii.step_e5 = lambda _: outcomes
        out = io.StringIO()
        with redirect_stdout(out):
            hiii.run_compose(entries, td=3, budget=0, label="synthetic")
        assert "root-signature terminal children: 1" in out.getvalue()
    finally:
        hiii.step_e5 = old_e5_step
    return "h3 and hiii BFS root-before-M filters"


def check_twopole_root_menu():
    menu = list(tp.root_pattern_menu(1, 1, kmax=0, lmax=2))
    exact = [row for row in menu if row[:4] == (0, 1, 2, 3)]
    assert exact and exact[0][4] == 'ROOT_ODE_EXACT_SOLVABLE_L1'
    even = [row for row in menu if row[:4] == (0, 2, 2, 4)]
    assert even and even[0][4] == 'ROOT_ODE_LOG_DEAD_EVEN'

    reachable = (Fr(1), 3, 1, 2, 0, "synthetic-reachable")
    td6_row1 = (Fr(1), 2, 1, 5, 0, "td6-row1-entry")
    assert tp.root_parent_reachable(reachable)
    assert not tp.root_parent_reachable(td6_row1)
    merge_hits = tp.root_merges([reachable])
    assert any(row[2:6] == (1, 1, 0, 1) and
               row[11] == 'ROOT_ODE_EXACT_SOLVABLE_L1'
               for row in merge_hits)
    assert not tp.root_merges([td6_row1])

    # A reachable all-mu=1 fixture really emits the locally solvable l=1
    # root cell; its M=1 is terminal, not an NR-M1 death.
    parent = (Fr(1), 3, 1, 2, 0, "synthetic-reachable")
    emitted = [row for row in tp.l1_merges([parent], LMAX=1)
               if row[3] == 1 and row[4] == 1 and sc.has_root_signature(row[2])]
    assert emitted
    assert sc.dispose_constructed_child(emitted[0][2]) == sc.TERMINAL_ROOT_M1
    return "twopole l>=1 menu, ODE parity, parent reach, and l=1 emission"


def check_no_raw_bfs_m1_filters():
    root = Path(__file__).resolve().parent
    names = ('sheet6_campaign.py', 'h3_check.py', 'hiii_compose.py',
             'twopole_check.py')
    forbidden = re.compile(r"\bif\b[^\n]*(?:child|ch|c2)\.M\s*==\s*1")
    for name in names:
        source = (root / name).read_text()
        match = forbidden.search(source)
        assert match is None, f"raw M1 filter remains: {name}: {match.group(0)}"
    return "static no raw child.M==1 BFS shortcuts"


def main():
    checks = (
        check_dispositions,
        check_shared_bfs_order,
        check_hidden_branches_restored,
        check_mu1_unbounded_and_zero_cost_tails,
        check_twopole_suffix_order,
        check_review_bfs_order,
        check_twopole_root_menu,
        check_no_raw_bfs_m1_filters,
    )
    for check in checks:
        print(f"PASS {check()}")
    print(f"ROOT-AWARE SMOKE PASS: {len(checks)} checks")


if __name__ == '__main__':
    main()
