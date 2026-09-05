#!/bin/bash
# jc2 fleet worker provisioning (cloud-init user-data). Idempotent, fail-gated.
# Installs the campaign CAS stack: Singular, msolve, python-flint, sympy,
# and the campaign PyPI tools qqideal + msolveio (latest). SSH via jc2-fleet.
set -x
exec > /var/log/jc2-provision.log 2>&1
# --- SSH key (belt-and-suspenders; --key-name jc2-fleet also injects it) ---
mkdir -p /home/ubuntu/.ssh
cat >> /home/ubuntu/.ssh/authorized_keys <<'PUBKEY'
__JC2_FLEET_PUB__
PUBKEY
chown -R ubuntu:ubuntu /home/ubuntu/.ssh; chmod 700 /home/ubuntu/.ssh; chmod 600 /home/ubuntu/.ssh/authorized_keys
# --- system CAS stack (universe for singular/msolve) ---
add-apt-repository -y universe
export DEBIAN_FRONTEND=noninteractive
apt-get update -y
apt-get install -y singular msolve python3-pip python3-venv rsync git build-essential \
  libgmp-dev libmpfr-dev libflint-dev time || exit 1
# --- python CAS tools (campaign) ---
pip3 install --break-system-packages --upgrade sympy python-flint qqideal msolveio || \
  pip3 install --break-system-packages --upgrade sympy python-flint qqideal msolveio || exit 1
# --- record versions + success gate ---
{ echo "singular=$(which Singular)"; echo "msolve=$(which msolve)";
  python3 -c "import sympy,flint,qqideal,msolveio as m; print('sympy',sympy.__version__); print('qqideal',getattr(qqideal,'__version__','?')); print('msolveio',getattr(m,'__version__','?'))"; } > /home/ubuntu/PROVISION_VERSIONS 2>&1
chown ubuntu:ubuntu /home/ubuntu/PROVISION_VERSIONS
# only mark done if the python stack imports cleanly
python3 -c "import sympy, qqideal, msolveio" && { touch /home/ubuntu/PROVISION_DONE; chown ubuntu:ubuntu /home/ubuntu/PROVISION_DONE; }
