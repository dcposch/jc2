#!/bin/bash
# Pull per-chart verdict lines from every worker into one TSV.
D=/home/ubuntu/jc2/box/k4ray-strata-solve-20260905
SSHO="-i $HOME/.ssh/jc2-fleet -o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=10"
for ip in 172.30.0.60 172.30.0.246 172.30.0.9 172.30.0.88; do
 ( timeout 90 ssh $SSHO ubuntu@$ip "
   cd $D/logs 2>/dev/null || exit 0
   for f in *.job.log; do
     s=\${f%.job.log}
     m=\$(grep -ao 'MSJOB__RESULT .*' \$s.mod.log 2>/dev/null | tail -1)
     mv=\$(echo \"\$m\" | grep -o '\"verdict\": \"[A-Z_0-9]*\"' | head -1 | sed 's/.*: \"//;s/\"//')
     mw=\$(echo \"\$m\" | grep -o '\"msolve_wall\": [0-9.]*' | sed 's/.*: //')
     fw=\$(echo \"\$m\" | grep -o '\"form_wall\": [0-9.]*' | sed 's/.*: //')
     bl=\$(echo \"\$m\" | grep -o '\"msolve_basis_length\": [0-9null]*' | sed 's/.*: //')
     ng=\$(echo \"\$m\" | grep -o '\"ngens\": [0-9]*' | sed 's/.*: //')
     nv=\$(echo \"\$m\" | grep -o '\"nvars\": [0-9]*' | sed 's/.*: //')
     qv=\$(grep -ao '\"verdict\": \"[A-Z_0-9]*\"' \$s.exactq.log 2>/dev/null | tail -1 | sed 's/.*: \"//;s/\"//')
     qm=\$(grep -aoE 'GG__[A-Z_]+|Maximum resident set size .*: [0-9]+|Killed|MemoryError|std\\(\\)' \$s.exactq.log 2>/dev/null | tail -1)
     qc=\$(grep -ao 'EXACTQ_RC=[0-9]*' \$s.exactq.log 2>/dev/null | tail -1 | sed 's/.*=//')
     mc=\$(grep -ao 'MOD_RC=[0-9]*' \$s.mod.log 2>/dev/null | tail -1 | sed 's/.*=//')
     dn=\$(grep -c STRATUM_DONE \$f 2>/dev/null)
     e=\$(grep -ao 'MSJOB__RESULT .*' \$s.exactq_ms.log 2>/dev/null | tail -1)
     ev=\$(echo \"\$e\" | grep -o '\"verdict\": \"[A-Z_0-9]*\"' | head -1 | sed 's/.*: \"//;s/\"//')
     ew=\$(echo \"\$e\" | grep -o '\"msolve_wall\": [0-9.]*' | sed 's/.*: //')
     eb=\$(echo \"\$e\" | grep -o '\"msolve_basis_length\": [0-9null]*' | sed 's/.*: //')
     es=\$(echo \"\$e\" | grep -o '\"ms_sha256\": \"[0-9a-f]*\"' | sed 's/.*: \"//;s/\"//' | cut -c1-12)
     echo -e \"\$s\t$ip\t\${mv:-RUNNING}\t\${bl:-.}\t\${mw:-.}\t\${fw:-.}\t\${nv:-.}\t\${ng:-.}\t\${qv:-RUNNING}\t\${qc:-.}\t\${mc:-.}\t\${dn}\t\${ev:-PENDING}\t\${eb:-.}\t\${ew:-.}\t\${es:-.}\t\${qm:-.}\"
   done" ) &
done
wait
