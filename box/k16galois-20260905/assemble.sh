#!/bin/bash
# assemble the report from the section files, in order; append-only from the sections (never rebuilt from the report)
cd /home/ubuntu/jc2/box/k16galois-20260905
OUT=/home/ubuntu/jc2/xmodel/k16-gamma-galois-fable5-20260905.md
cat sections/00_header.md sections/00_verdict.md sections/01_custody.md sections/02_setting.md sections/03_lemmas.md \
    sections/04_results.md sections/05_instrument.md sections/06_colon.md sections/07_uniform.md sections/08_fallacy.md \
    sections/09_artifacts.md sections/10_disposition.md sections/11_opens.md sections/12_collision.md > "$OUT"
printf '\n<!-- BODY-END -->\n' >> "$OUT"
wc -c "$OUT"
