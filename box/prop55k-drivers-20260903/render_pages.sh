#!/bin/sh
# Re-render the Moh 1983 pages opened by this lane (journal page N = PDF page N-139).
PDF=refs/moh1983_jram340_configurations_of_roots.pdf
mkdir -p pages
for p in 12 25 29 31 35 39 40 42 47 48 49 58 68 69 71; do
  pdftoppm -r 300 -f $p -l $p -png "$PDF" pages/pg
done
