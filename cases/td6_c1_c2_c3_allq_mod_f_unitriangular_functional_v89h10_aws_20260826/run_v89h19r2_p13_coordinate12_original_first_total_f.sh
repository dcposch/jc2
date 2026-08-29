#!/usr/bin/env bash
set -euo pipefail

[[ "$(uname -s)" == Linux ]] || exit 97
grep -q 'Amazon EC2' /sys/devices/virtual/dmi/id/sys_vendor || exit 96

case "${AWS_RUN_TAG:-}" in
  td6_v89h19r2_p13_c12_first_total_*) ;;
  *) echo "refusing non-AWS or misregistered tag" >&2; exit 95 ;;
esac

: "${TD6_OUTPUT_DIR:?TD6_OUTPUT_DIR is required}"
: "${TD6_H15_ARCHIVE:?TD6_H15_ARCHIVE is required}"
[[ -f "$TD6_H15_ARCHIVE" ]] || exit 94

[[ "${TD6_Q_EXPONENT:-}" == 2 ]] || exit 88
[[ "${TD6_Q_SCOPE:-}" == q2-q14-q16-q24 ]] || exit 87
[[ "${TD6_PIVOT_POLICY:-}" == ascending ]] || exit 86
[[ "${TD6_PIVOT_SCOPE:-}" == all-staged ]] || exit 85
[[ "${TD6_F_SPECIALIZATION:-}" == exact-C-equals-V2-minus-U3-over-U ]] || exit 84
[[ "${OMP_NUM_THREADS:-}" == 1 ]] || exit 83
[[ "${OPENBLAS_NUM_THREADS:-}" == 1 ]] || exit 82

EXPECTED_ARCHIVE_SHA=2c13bd51601a64f3c2410bf4d36460f9f8741312aeef649299a22eb4fae3ff81
OBSERVED_ARCHIVE_SHA=$(sha256sum "$TD6_H15_ARCHIVE" | cut -d ' ' -f 1)
[[ "$OBSERVED_ARCHIVE_SHA" == "$EXPECTED_ARCHIVE_SHA" ]] || exit 81

unset PYTHONOPTIMIZE
[[ "$(python3 -c 'import sys; print(sys.flags.optimize)')" == 0 ]] || exit 80

FLINT_VERSION=$(python3 -c 'import flint; print(flint.__version__)')
[[ "$FLINT_VERSION" == 0.9.0 ]] || exit 79
FLINT_MODULE=$(python3 -c 'import flint.pyflint as p; print(p.__file__)')
FLINT_MODULE_SHA=$(sha256sum "$FLINT_MODULE" | cut -d ' ' -f 1)
[[ "$FLINT_MODULE_SHA" == 1f7ef1f52024937f542772ff9190e2f74449228cd69a6746b6608fbbd449d138 ]] || exit 78
PACKAGES=$(python3 -m pip freeze | sort | tr '\n' ',')
[[ "$PACKAGES" == "python-flint==0.9.0," ]] || exit 77
python3 -c 'import importlib.util,sys; sys.exit(0 if all(importlib.util.find_spec(n) is None for n in ("sage","sympy","singular","PySingular")) else 1)' || exit 76

sha256sum -c SOURCE_P13_FULL_NORMAL_FORM.sha256
sha256sum -c SOURCE_P12_FULL_NORMAL_FORM.sha256
sha256sum -c SOURCE_P12_FLAG.sha256
sha256sum -c PAYLOAD_CLOSURE.sha256
sha256sum -c SOURCE_RAW_P13_COORDINATE12_AUDIT_R1.sha256
sha256sum -c SOURCE_P13_COORDINATE12_ORIGINAL_FIRST_TOTAL_F.sha256

printf 'runner=run_v89h19r2_p13_coordinate12_original_first_total_f.sh\n'
printf 'python_flint=%s\n' "$FLINT_VERSION"
printf 'python_flint_module_sha256=%s\n' "$FLINT_MODULE_SHA"
printf 'python_packages=%s\n' "$PACKAGES"
printf 'h15_archive_sha256=%s\n' "$OBSERVED_ARCHIVE_SHA"

exec python3 replay_v89h19r2_p13_coordinate12_original_first_total_f.py
