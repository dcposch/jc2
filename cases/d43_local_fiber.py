#!/usr/bin/env python3
"""Exact local-generation audit for the D43 fixed parked fiber.

This is deliberately a bounded local calculation, not a full-file solve.
It loads the 184 point-specialized graph rows, translates the certified
point to the origin, and chooses 111 original rows and 111 variables whose
Jacobian minor is a unit.  Constant row operations normalize that minor to
the identity.  In the local degree ordering with pivot variables first, the
normalized rows have pairwise-coprime leading monomials (the distinct pivot
variables), hence are already a local standard basis by Buchberger's product
criterion.  Singular is used only for exact local normal forms of all source
rows against that certified basis; ``std`` is never called.

The result certifies the 156-variable graph fiber only.  It does not by
itself certify the 184-variable total D43 family.
"""

import argparse
import hashlib
import itertools
import json
import os
import pickle
import subprocess
import tempfile


HERE = os.path.dirname(os.path.abspath(__file__))
PRIME = 105337


def sha256_path(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(8 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def add_scaled(target, source, scale, p):
    scale %= p
    if not scale:
        return
    for monomial, coefficient in source.items():
        value = (target.get(monomial, 0) + scale * coefficient) % p
        if value:
            target[monomial] = value
        else:
            target.pop(monomial, None)


def multiply(left, right, p):
    result = {}
    for lm, lc in left.items():
        for rm, rc in right.items():
            monomial = tuple(sorted(lm + rm))
            value = (result.get(monomial, 0) + lc * rc) % p
            if value:
                result[monomial] = value
            else:
                result.pop(monomial, None)
    return result


def translate(row, point, p):
    """Return row(y + point), in the same tuple-of-variable representation."""
    result = {}
    for monomial, coefficient in row.items():
        term = {(): coefficient % p}
        for variable, occurrences in itertools.groupby(monomial):
            exponent = sum(1 for _ in occurrences)
            scalar = point[variable] % p
            factor = {}
            for power in range(exponent + 1):
                value = (pow(scalar, exponent - power, p) *
                         __import__("math").comb(exponent, power)) % p
                if value:
                    factor[(variable,) * power] = value
            term = multiply(term, factor, p)
        add_scaled(result, term, 1, p)
    return result


def jacobian(rows, variables, point, p):
    matrix = []
    for row in rows:
        gradient = []
        for variable in variables:
            value = 0
            for monomial, coefficient in row.items():
                multiplicity = monomial.count(variable)
                if not multiplicity:
                    continue
                term = coefficient * multiplicity % p
                removed = False
                for name in monomial:
                    if name == variable and not removed:
                        removed = True
                    else:
                        term = term * point[name] % p
                value = (value + term) % p
            gradient.append(value)
        matrix.append(gradient)
    return matrix


def independent_minor(matrix, p):
    """Canonical original row IDs and columns of a full-rank minor."""
    work = [[value % p for value in row] for row in matrix]
    row_ids = list(range(len(work)))
    rank = 0
    columns = []
    for column in range(len(work[0])):
        pivot = next((index for index in range(rank, len(work))
                      if work[index][column]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        row_ids[rank], row_ids[pivot] = row_ids[pivot], row_ids[rank]
        inverse = pow(work[rank][column], -1, p)
        work[rank] = [value * inverse % p for value in work[rank]]
        for index in range(rank + 1, len(work)):
            if work[index][column]:
                scale = work[index][column]
                work[index] = [(left - scale * right) % p
                               for left, right in zip(work[index],
                                                      work[rank])]
        columns.append(column)
        rank += 1
    return row_ids[:rank], columns


def inverse_matrix(matrix, p):
    size = len(matrix)
    work = [[value % p for value in row] +
            [1 if i == j else 0 for j in range(size)]
            for i, row in enumerate(matrix)]
    for column in range(size):
        pivot = next(index for index in range(column, size)
                     if work[index][column])
        work[column], work[pivot] = work[pivot], work[column]
        inverse = pow(work[column][column], -1, p)
        work[column] = [value * inverse % p for value in work[column]]
        for index in range(size):
            if index != column and work[index][column]:
                scale = work[index][column]
                work[index] = [(left - scale * right) % p
                               for left, right in zip(work[index],
                                                      work[column])]
    assert all(work[i][j] == (1 if i == j else 0)
               for i in range(size) for j in range(size))
    return [row[size:] for row in work]


def polynomial_text(row, positions, p):
    if not row:
        return "0"
    terms = []
    for monomial, coefficient in sorted(
            row.items(), key=lambda item: (len(item[0]),
                                            tuple(positions[x]
                                                  for x in item[0]))):
        factors = []
        for variable, occurrences in itertools.groupby(monomial):
            exponent = sum(1 for _ in occurrences)
            factors.append(variable if exponent == 1 else
                           "%s^%d" % (variable, exponent))
        terms.append(str(coefficient % p) +
                     ("*" + "*".join(factors) if factors else ""))
    return "+".join(terms)


def singular_program(variables, basis, rows, p):
    positions = {name: index for index, name in enumerate(variables)}
    lines = ["option(redSB);", "ring r=%d,(%s),ds;" %
             (p, ",".join(variables))]
    for index, row in enumerate(basis):
        lines.append("poly g%d=%s;" %
                     (index + 1, polynomial_text(row, positions, p)))
    lines.append("ideal G=%s;" %
                 ",".join("g%d" % (i + 1) for i in range(len(basis))))
    lines.append('attrib(G,"isSB",1);')
    for index, row in enumerate(rows):
        lines.append("poly f%d=%s;" %
                     (index + 1, polynomial_text(row, positions, p)))
    lines.append("ideal F=%s;" %
                 ",".join("f%d" % (i + 1) for i in range(len(rows))))
    lines.extend([
        "ideal H=reduce(F,G);",
        "int nonzero=0;",
        "int terms=0;",
        "int i;",
        "for (i=1; i<=size(H); i++) {",
        "  if (H[i] != 0) { nonzero=nonzero+1; terms=terms+size(H[i]); }",
        "}",
        'print("D43_LOCAL_REMAINDERS "+string(nonzero)+" "+string(terms));',
        "quit;",
    ])
    return "\n".join(lines) + "\n"


def normalized_basis(rows, matrix, variables, p):
    selected_rows, selected_columns = independent_minor(matrix, p)
    rank = len(selected_rows)
    minor = [[matrix[row][column] for column in selected_columns]
             for row in selected_rows]
    inverse = inverse_matrix(minor, p)
    sources = [rows[index] for index in selected_rows]
    basis = []
    for coefficients in inverse:
        result = {}
        for scale, source in zip(coefficients, sources):
            add_scaled(result, source, scale, p)
        basis.append(result)
    pivot_names = [variables[index] for index in selected_columns]
    pivot_set = set(pivot_names)
    free_names = [name for index, name in enumerate(variables)
                  if index not in set(selected_columns)]
    for index, row in enumerate(basis):
        linear = {monomial: coefficient for monomial, coefficient in row.items()
                  if len(monomial) == 1}
        assert linear.get((pivot_names[index],)) == 1
        assert not any(name in pivot_set and name != pivot_names[index]
                       for monomial in linear for name in monomial)
    return selected_rows, selected_columns, pivot_names, free_names, basis


def normalize_selected(rows, matrix, selected_rows, selected_columns,
                       variables, p):
    assert len(selected_rows) == len(selected_columns)
    minor = [[matrix[row][column] for column in selected_columns]
             for row in selected_rows]
    inverse = inverse_matrix(minor, p)
    sources = [rows[index] for index in selected_rows]
    basis = []
    for coefficients in inverse:
        result = {}
        for scale, source in zip(coefficients, sources):
            add_scaled(result, source, scale, p)
        basis.append(result)
    pivot_names = [variables[index] for index in selected_columns]
    pivot_set = set(pivot_names)
    free_names = [name for index, name in enumerate(variables)
                  if index not in set(selected_columns)]
    for index, row in enumerate(basis):
        linear = {monomial: coefficient for monomial, coefficient in row.items()
                  if len(monomial) == 1}
        assert linear.get((pivot_names[index],)) == 1
        assert not any(name in pivot_set and name != pivot_names[index]
                       for monomial in linear for name in monomial)
    return pivot_names, free_names, basis


def extend_echelon(echelon, row, p):
    """Insert one row into a nested row-echelon basis, if independent."""
    reduced = [value % p for value in row]
    for pivot, source in echelon:
        if reduced[pivot]:
            scale = reduced[pivot]
            reduced = [(left - scale * right) % p
                       for left, right in zip(reduced, source)]
    pivot = next((index for index, value in enumerate(reduced) if value),
                 None)
    if pivot is None:
        return None
    inverse = pow(reduced[pivot], -1, p)
    reduced = [value * inverse % p for value in reduced]
    echelon.append((pivot, reduced))
    return pivot


def singular_reduce(variables, basis, rows, p, timeout):
    if not rows:
        return {
            "returncode": 0, "nonzero": 0, "remainder_terms": 0,
            "program_sha256": None, "stdout_tail": "no dependent rows",
            "stderr_tail": "",
        }
    program = singular_program(variables, basis, rows, p)
    try:
        with tempfile.TemporaryDirectory(prefix="d43-local-fiber-") as tempdir:
            script = os.path.join(tempdir, "certificate.sing")
            with open(script, "w") as handle:
                handle.write(program)
            completed = subprocess.run(
                ["Singular", "-q", script], text=True, capture_output=True,
                timeout=timeout, check=False)
    except subprocess.TimeoutExpired as error:
        return {
            "returncode": None, "nonzero": None, "remainder_terms": None,
            "program_sha256": hashlib.sha256(
                program.encode("ascii")).hexdigest(),
            "stdout_tail": (error.stdout or b"")[-2000:].decode(
                "utf-8", "replace") if isinstance(error.stdout, bytes)
                else (error.stdout or "")[-2000:],
            "stderr_tail": (error.stderr or b"")[-2000:].decode(
                "utf-8", "replace") if isinstance(error.stderr, bytes)
                else (error.stderr or "")[-2000:],
            "timeout_seconds": timeout,
        }
    marker = next((line for line in completed.stdout.splitlines()
                   if line.startswith("D43_LOCAL_REMAINDERS ")), None)
    if completed.returncode != 0 or marker is None:
        return {
            "returncode": completed.returncode,
            "nonzero": None, "remainder_terms": None,
            "program_sha256": hashlib.sha256(
                program.encode("ascii")).hexdigest(),
            "stdout_tail": completed.stdout[-2000:],
            "stderr_tail": completed.stderr[-2000:],
        }
    nonzero, remainder_terms = map(int, marker.split()[1:])
    return {
        "returncode": completed.returncode,
        "nonzero": nonzero, "remainder_terms": remainder_terms,
        "program_sha256": hashlib.sha256(
            program.encode("ascii")).hexdigest(),
        "stdout_tail": completed.stdout[-2000:],
        "stderr_tail": completed.stderr[-2000:],
    }


def run(bank_path, certificate_path, out_path, timeout):
    with open(bank_path, "rb") as handle:
        bank = pickle.load(handle)
    certificate = json.load(open(certificate_path))
    p = int(bank["prime"])
    assert p == PRIME == int(certificate["prime"])
    variables = list(bank["variables"])
    point = {name: int(certificate["point"]["graph_156"][name]) % p
             for name in variables}
    rows = bank["rows"]
    assert len(rows) == 184 and len(variables) == 156
    matrix = jacobian(rows, variables, point, p)
    translated = [translate(row, point, p) for row in rows]
    assert all(not row.get((), 0) for row in translated)
    bands = sorted({int(label[0]) for label in bank["row_labels"]})
    prefix_indices = []
    nested_selected = []
    nested_columns = []
    echelon = []
    band_reports = []
    previous_rank = 0
    final_selected_rows = final_selected_columns = None
    final_pivot_names = None
    all_pass = True
    for band in bands:
        current_indices = [index for index, label in enumerate(
            bank["row_labels"]) if int(label[0]) == band]
        prefix_indices.extend(current_indices)
        for index in current_indices:
            pivot = extend_echelon(echelon, matrix[index], p)
            if pivot is not None:
                nested_selected.append(index)
                nested_columns.append(pivot)
        rank = len(nested_selected)
        pivot_names, free_names, basis = normalize_selected(
            translated, matrix, nested_selected, nested_columns,
            variables, p)
        selected_set = set(nested_selected)
        dependent = [index for index in current_indices
                     if index not in selected_set]
        reduction = singular_reduce(
            pivot_names + free_names, basis,
            [translated[index] for index in dependent], p, timeout)
        passed = reduction["nonzero"] == 0
        all_pass = all_pass and passed
        band_reports.append({
            "band": band,
            "rows_in_band": len(current_indices),
            "prefix_rows": len(prefix_indices),
            "prefix_rank": rank,
            "rank_increment": rank - previous_rank,
            "dependent_rows_checked": dependent,
            "normal_form": reduction,
            "pass": passed,
        })
        print("band %d: prefix rank %d (+%d), dependent %d, local NF %s" %
              (band, rank, rank - previous_rank, len(dependent),
               "PASS" if passed else "FAIL/TIMEOUT"), flush=True)
        previous_rank = rank
        final_selected_rows = list(nested_selected)
        final_selected_columns = list(nested_columns)
        final_pivot_names = pivot_names
        if not passed:
            break
    rank = previous_rank
    assert rank <= 111
    result = {
        "status": ("EXACT FIXED-FIBER LOCAL CERTIFICATE" if all_pass and
                   len(band_reports) == len(bands) else
                   "FIXED-FIBER LOCAL AUDIT INCOMPLETE"),
        "scope": "D43 graph equations after fixing the parked A14 point",
        "prime": p,
        "ambient_variables": len(variables),
        "rows": len(rows),
        "completed_prefix_jacobian_rank": rank,
        "completed_prefix_tangent_dimension": len(variables) - rank,
        "full_fiber_jacobian_rank": 111,
        "certified_local_dimension": (len(variables) - rank
                                      if all_pass and
                                      len(band_reports) == len(bands)
                                      else None),
        "selected_rows": final_selected_rows,
        "pivot_variables": final_pivot_names,
        "standard_basis_reason":
            "normalized lowest-degree leading monomials are distinct variables; product criterion",
        "local_normal_forms": {
            "method": "bandwise induction",
            "bands_completed": len(band_reports),
            "bands_total": len(bands),
            "dependent_rows_checked": sum(
                len(report["dependent_rows_checked"])
                for report in band_reports),
            "nonzero_remainders": sum(
                report["normal_form"]["nonzero"] or 0
                for report in band_reports),
        },
        "localized_generation": all_pass and len(band_reports) == len(bands),
        "bands": band_reports,
        "input_hashes": {
            "pointbank_sha256": sha256_path(bank_path),
            "certificate_sha256": sha256_path(certificate_path),
        },
        "interpretation":
            "This proves smoothness/dimension 45 only for the fixed parked graph fiber; total-space generation and p-flatness are separate gates.",
    }
    with open(out_path, "w") as handle:
        json.dump(result, handle, indent=1, sort_keys=True)
        handle.write("\n")
    if not (result["localized_generation"] and rank == 111):
        print("D43 fixed graph fiber p=%d: audit incomplete at rank %d -> %s" %
              (p, rank, out_path), flush=True)
        return result
    print("D43 fixed graph fiber p=%d: local dim %d; bandwise generation PASS -> %s" %
          (p, len(variables) - rank, out_path), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bank", default=os.path.join(
        HERE, "d43_full_pointbank_p105337.pkl"))
    parser.add_argument("--certificate", default=os.path.join(
        HERE, "d43_full_certificate_p105337.json"))
    parser.add_argument("--out", required=True)
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    run(args.bank, args.certificate, args.out, args.timeout)


if __name__ == "__main__":
    main()
