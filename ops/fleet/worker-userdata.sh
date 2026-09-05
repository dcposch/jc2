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
# --- system CAS stack (universe already enabled on the Ubuntu EC2 AMI) ---
# Neutralise first-boot apt contention: unattended-upgrades holds the dpkg lock
# for ~20 min on a fresh image; stop the timers and wait for the lock cleanly.
systemctl stop apt-daily.timer apt-daily-upgrade.timer unattended-upgrades.service 2>/dev/null || true
systemctl disable apt-daily.timer apt-daily-upgrade.timer 2>/dev/null || true
for i in $(seq 1 180); do fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1 || break; sleep 5; done
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Acquire::ForceIPv4=true -o DPkg::Lock::Timeout=900 -y"
$APT update
$APT install singular msolve python3-pip python3-venv rsync git build-essential \
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
