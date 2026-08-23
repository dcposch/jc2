#!/usr/bin/env bash
# sg_autoupdate.sh -- keep DC's current public IP authorized for ssh (port 22)
# on the fleet security group. Idempotent; safe to run every tick.
#
# Behavior:
#   - IP already authorized  -> "SG: current", exit 0 (no changes).
#   - IP missing             -> authorize <ip>/32, then conservatively prune
#                               stale personal /32s, print one status line.
#   - Exit nonzero ONLY on AWS CLI errors (IP-lookup failure prints a status
#     line and exits 0 so a tick loop doesn't alarm on flaky wifi).
#
# CONSERVATIVE PRUNE POLICY: only /32 rules inside the two known personal
# ranges 149.22.81.* and 149.88.22.* may ever be removed, and never the
# current IP. 69.181.195.82/32 and anything outside those ranges is NEVER
# touched -- other rules may be intentional.

set -u

SG_ID="sg-09ffa8932558f0a79"
PROFILE="personal"
PROTECTED="69.181.195.82/32"
PRUNE_RE='^149\.(22\.81|88\.22)\.[0-9]{1,3}/32$'
IPV4_RE='^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'

# --- 1) current public IP (checkip.amazonaws.com, fallback ifconfig.me) ---
IP="$(curl -s --max-time 10 https://checkip.amazonaws.com 2>/dev/null | tr -d '[:space:]')"
if ! printf '%s' "$IP" | grep -Eq "$IPV4_RE"; then
    IP="$(curl -s --max-time 10 https://ifconfig.me 2>/dev/null | tr -d '[:space:]')"
fi
if ! printf '%s' "$IP" | grep -Eq "$IPV4_RE"; then
    echo "SG: ip-lookup failed (no change)"
    exit 0
fi
CIDR="$IP/32"

# --- 2) current port-22 ingress /32s ---
if ! RULES="$(aws ec2 describe-security-groups --group-ids "$SG_ID" \
        --profile "$PROFILE" \
        --query 'SecurityGroups[0].IpPermissions[?IpProtocol==`tcp` && FromPort<=`22` && ToPort>=`22`].IpRanges[].CidrIp' \
        --output text 2>&1)"; then
    echo "SG: ERROR describe-security-groups failed: $RULES" >&2
    exit 1
fi
# normalize tabs/newlines to one CIDR per line
RULES="$(printf '%s\n' "$RULES" | tr '\t' '\n' | grep -v '^None$' | grep -v '^$' || true)"

# --- 3) already present? ---
if printf '%s\n' "$RULES" | grep -Fxq "$CIDR"; then
    echo "SG: current"
    exit 0
fi

# --- add the current IP ---
if ! ERR="$(aws ec2 authorize-security-group-ingress --group-id "$SG_ID" \
        --profile "$PROFILE" --protocol tcp --port 22 --cidr "$CIDR" 2>&1 >/dev/null)"; then
    if printf '%s' "$ERR" | grep -q 'InvalidPermission.Duplicate'; then
        echo "SG: current"   # raced with another tick; rule exists
        exit 0
    fi
    echo "SG: ERROR authorize failed for $CIDR: $ERR" >&2
    exit 1
fi

# --- 4) conservative prune of stale personal /32s ---
PRUNED=""
RC=0
while IFS= read -r c; do
    [ -n "$c" ] || continue
    [ "$c" = "$CIDR" ] && continue
    [ "$c" = "$PROTECTED" ] && continue
    printf '%s' "$c" | grep -Eq "$PRUNE_RE" || continue
    if ERR="$(aws ec2 revoke-security-group-ingress --group-id "$SG_ID" \
            --profile "$PROFILE" --protocol tcp --port 22 --cidr "$c" 2>&1 >/dev/null)"; then
        PRUNED="$PRUNED $c"
    else
        echo "SG: ERROR revoke failed for $c: $ERR" >&2
        RC=1
    fi
done <<EOF
$RULES
EOF

if [ -n "$PRUNED" ]; then
    echo "SG: added $CIDR (pruned$PRUNED)"
else
    echo "SG: added $CIDR"
fi
exit "$RC"
