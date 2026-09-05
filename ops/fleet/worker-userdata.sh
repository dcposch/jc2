#!/bin/bash
# jc2 fleet worker provisioning (cloud-init user-data). AMI-aware + fail-gated.
# On the baked math-hq base AMI, Singular + python + repo are already present, so
# the slow apt path is skipped; only the SSH key, IPv4 preference, and the
# qqideal/msolveio stack (best-effort) are set up. On a bare Ubuntu AMI it falls
# back to the full apt install.
set -x
exec > /var/log/jc2-provision.log 2>&1
# prefer IPv4 globally (subnet has no IPv6 route; IPv6 timeouts stall apt AND pip)
printf 'precedence ::ffff:0:0/96  100\n' >> /etc/gai.conf
# SSH key for math-hq to drive the worker
mkdir -p /home/ubuntu/.ssh
cat >> /home/ubuntu/.ssh/authorized_keys <<'PUBKEY'
__JC2_FLEET_PUB__
PUBKEY
chown -R ubuntu:ubuntu /home/ubuntu/.ssh; chmod 700 /home/ubuntu/.ssh; chmod 600 /home/ubuntu/.ssh/authorized_keys
export DEBIAN_FRONTEND=noninteractive
APT="apt-get -o Acquire::ForceIPv4=true -o DPkg::Lock::Timeout=900 -y"
if ! command -v Singular >/dev/null 2>&1; then
  # bare-AMI fallback: full CAS stack via apt (universe already enabled on Ubuntu EC2 AMI)
  systemctl stop apt-daily.timer apt-daily-upgrade.timer unattended-upgrades.service 2>/dev/null || true
  systemctl disable apt-daily.timer apt-daily-upgrade.timer 2>/dev/null || true
  for i in $(seq 1 180); do fuser /var/lib/dpkg/lock-frontend >/dev/null 2>&1 || break; sleep 5; done
  $APT update
  $APT install singular msolve python3-pip python3-venv rsync build-essential \
    libgmp-dev libmpfr-dev libflint-dev time || exit 1
fi
# msolve + pip stack (best-effort; the Moh charts need only Singular). pip may be absent on the base AMI.
command -v msolve >/dev/null 2>&1 || $APT install msolve 2>/dev/null || true
command -v pip3 >/dev/null 2>&1 || $APT install python3-pip 2>/dev/null || true
pip3 install --break-system-packages --upgrade sympy python-flint qqideal msolveio 2>/dev/null || true
# record + success gate: Singular present AND a working python3 are the essentials
{ echo "singular=$(which Singular)"; echo "msolve=$(which msolve)"; echo "repo=$(ls -d /home/ubuntu/jc2 2>/dev/null)";
  python3 -c "import sympy" 2>&1 && echo "sympy=ok";
  python3 -c "import qqideal,msolveio; print('qqstack=ok')" 2>&1; } > /home/ubuntu/PROVISION_VERSIONS 2>&1
chown ubuntu:ubuntu /home/ubuntu/PROVISION_VERSIONS
command -v Singular >/dev/null 2>&1 && { touch /home/ubuntu/PROVISION_DONE; chown ubuntu:ubuntu /home/ubuntu/PROVISION_DONE; }
