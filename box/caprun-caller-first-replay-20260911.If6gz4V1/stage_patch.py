"""Candidate-only bytes -> allowlisted add-file patch. No I/O or execution."""
import hashlib
import json
import re

PHASES = ('refuse-status', 'refuse-caps', 'refuse-inventory', 'refuse-source',
          'refuse-hash', 'valid', 'startup-produce', 'startup-check', 'dummy')
NAMES = tuple('authority/' + label + '.json' for label in PHASES) + (
    'ROOT-REGISTRATION.json', 'ROOT-EXECUTION-CARD.md',
    'FINAL-INSTALL-INPUTS.sha256', 'final-install.sh', 'SUMMARY.json')
PREFIX = re.compile(r'/home/ubuntu/jc2/box/caprun-stage-exercise-[0-9]{8}\.[A-Za-z0-9]{6,24}')
MAX_FILE = 131072
MAX_TOTAL = 524288
STATUS = 'CANDIDATE_NOT_INSTALLED_NOT_RELEASED'


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def pairs(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate summary key')
        out[key] = value
    return out


def make_patch(candidates, prefix):
    """ROOT must supply a fresh private directory, authenticate inputs and
    verify all returned hashes after apply_patch. This grants no installation
    or release authority and does not verify physical or live observations.
    """
    need(type(prefix) is str and PREFIX.fullmatch(prefix) is not None, 'candidate prefix')
    need(type(candidates) is dict and set(candidates) == set(NAMES), 'exact fourteen outputs')
    decoded = {}
    for name in NAMES:
        raw = candidates[name]
        need(type(raw) is bytes and 0 < len(raw) <= MAX_FILE, 'candidate bytes/size')
        need(raw.endswith(b'\n') and b'\r' not in raw and b'\0' not in raw, 'candidate line format')
        decoded[name] = raw.decode('utf-8', 'strict')
    need(sum(len(raw) for raw in candidates.values()) <= MAX_TOTAL, 'aggregate size')
    summary = json.loads(decoded['SUMMARY.json'], object_pairs_hook=pairs)
    need(type(summary) is dict and summary.get('schema') == 'caprun-latebinding-summary/v1'
         and summary.get('status') == STATUS
         and summary.get('installation_or_release_authorized') is False
         and summary.get('context') in ('HISTORICAL_TEST', 'ROOT_ATTESTED_CANDIDATE'),
         'candidate summary/context')
    records = summary.get('outputs')
    need(type(records) is dict and set(records) == set(NAMES[:-1]), 'summary thirteen outputs')
    expected = {}
    lines = ['*** Begin Patch\n']
    for name in NAMES:
        raw = candidates[name]
        digest = hashlib.sha256(raw).hexdigest()
        if name != 'SUMMARY.json':
            record = records[name]
            need(type(record) is dict and set(record) == {'sha256', 'bytes'}
                 and record['sha256'] == digest and type(record['bytes']) is int
                 and record['bytes'] == len(raw), 'candidate commitment: ' + name)
        path = prefix + '/' + name
        expected[path] = digest
        lines.append('*** Add File: ' + path + '\n')
        # Every content line is prefixed; embedded patch directives remain data.
        lines.extend('+' + line + '\n' for line in decoded[name].split('\n')[:-1])
    lines.append('*** End Patch\n')
    return {'patch': ''.join(lines), 'expected_sha256': expected,
            'status': STATUS, 'context': summary['context'],
            'candidate_bytes': sum(len(raw) for raw in candidates.values())}
