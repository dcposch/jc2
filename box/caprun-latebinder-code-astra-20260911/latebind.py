"""Pure-data candidate binder. No I/O, CLI, observations or release authority."""
import copy
import hashlib
import json
import re

PHASES = ('refuse-status', 'refuse-caps', 'refuse-inventory', 'refuse-source',
          'refuse-hash', 'valid', 'startup-produce', 'startup-check', 'dummy')
NAMES = ('ROOT-REGISTRATION.preholder.json', 'AUTHORITIES.preholder.json',
         'ROOT-EXECUTION-CARD.preholder.md', 'final-install.preholder.sh')
STATUS = 'CANDIDATE_NOT_INSTALLED_NOT_RELEASED'
FREEZE = 'ROOT_FREEZE_EXACT_PREFLIGHT9_REGISTRATION_ONLY'
HEX = re.compile(r'[0-9a-f]{64}')
TOKEN = re.compile(r'JC2_[A-Z0-9_]+_PLACEHOLDER')
MAX_INPUT = 131072
MAX_OUTPUT = 131072
MAX_TOTAL = 524288


def need(ok, reason):
    if not ok:
        raise ValueError(reason)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def keys(obj, expected, name):
    need(type(obj) is dict and set(obj) == set(expected), name + ' keys')


def digest(value):
    need(type(value) is str and HEX.fullmatch(value) is not None, 'digest')
    return value


def positive(value):
    need(type(value) is int and 0 < value < 2**64, 'positive integer')
    return value


def pairs(items):
    out = {}
    for key, value in items:
        need(key not in out, 'duplicate JSON key')
        out[key] = value
    return out


def no_number(value):
    raise ValueError('non-integer JSON number')


def integer(value):
    need(len(value) <= 20, 'integer length')
    out = int(value)
    need(abs(out) < 2**64, 'integer bound')
    return out


def text(raw):
    need(type(raw) is bytes and 0 < len(raw) <= MAX_INPUT, 'input bytes')
    value = raw.decode('utf-8', 'strict')
    need('\x00' not in value and '\r' not in value, 'text control')
    return value


def load(raw):
    value = json.loads(text(raw), object_pairs_hook=pairs, parse_int=integer,
                       parse_float=no_number, parse_constant=no_number)
    count = [0]
    def walk(x, depth):
        count[0] += 1
        need(depth <= 16 and count[0] <= 20000, 'JSON shape bound')
        if type(x) is dict:
            for k, v in x.items():
                need(type(k) is str and len(k) <= 4096, 'JSON key')
                walk(v, depth + 1)
        elif type(x) is list:
            for v in x:
                walk(v, depth + 1)
        else:
            need(type(x) in (str, int, bool, type(None)), 'JSON type')
            if type(x) is str:
                need(len(x) <= 32768, 'JSON string bound')
    walk(value, 0)
    return value


def encode(value, pretty=False):
    args = {'ensure_ascii': True, 'allow_nan': False}
    if pretty:
        args['indent'] = 2
    else:
        args.update(sort_keys=True, separators=(',', ':'))
    raw = (json.dumps(value, **args) + '\n').encode('ascii')
    need(len(raw) <= MAX_OUTPUT, 'output bound')
    return raw


def ph(name):
    return 'JC2_' + name.upper().replace('-', '_') + '_PLACEHOLDER'


def replace_exact(value, replacements):
    for old, (new, count) in replacements.items():
        need(value.count(old) == count, 'text multiplicity: ' + old)
        value = value.replace(old, new)
    need(TOKEN.search(value) is None, 'leftover placeholder')
    return value.encode('utf-8')


def expected_command(r, label):
    """Reconstruct the entire prepared argv from its fixed metadata schema."""
    f, cg, mount = r['files'], r['cgroup_path'], r['output_mount']
    profile = r['profiles']['dummy' if label == 'dummy' else 'control']
    out = [f['python'], '-I', '-S', '-B', f['caprun'],
           '--closed-child-cgroup', cg + '/' + label,
           '--closed-child-device', ph('CHILD_DEVICE'),
           '--closed-child-inode', ph('CHILD_' + label + '_INODE'),
           '--closed-outer-cgroup', cg, '--closed-outer-device', ph('OUTER_DEVICE'),
           '--closed-outer-inode', ph('OUTER_INODE'),
           '--closed-boot-id', r['boot_id'], '--closed-pid-namespace', r['pid_namespace'],
           '--wall-seconds', str(profile[0]), '--cpu-seconds', str(profile[1]),
           '--rss-bytes', str(profile[2]), '--rss-sample-seconds', '0.05',
           '--term-grace-seconds', '1', '--stdout-file', mount + '/' + label + '.stdout',
           '--stderr-file', mount + '/' + label + '.stderr',
           '--telemetry-file', mount + '/' + label + '.telemetry.json',
           '--cwd', r['science_dir'], '--', f['setpriv'], '--reuid', str(r['uid']),
           '--regid', str(r['gid']), '--clear-groups', '--no-new-privs', '--',
           f['python'], '-E', '-s', '-S', '-B']
    authpath = r['authority_dir'] + '/' + label + '.json'
    payload = r['writer_dir'] + '/' + label + '.payload'
    if label in ('valid', 'dummy'):
        return out + [f['probe'], '--registration', r['outer_argv'][-1],
                      '--policy', authpath, '--policy-sha256', ph(label + '_POLICY_SHA'),
                      '--mode', label, '--output', payload]
    mode = 'check' if label == 'startup-check' else 'produce'
    tag = 'WRONG-JOB' if label.startswith('startup-') else r['jobtag']
    d = '0'*64 if label == 'refuse-hash' else ph(label + '_AUTH_SHA')
    return out + [r['science_dir'] + '/' + mode + '.py', '--registered-job', tag,
                  '--authorization', authpath, '--authorization-sha256', d,
                  '--input' if mode == 'check' else '--output', payload]


def expected_authority(r, label):
    payload = r['writer_dir'] + '/' + label + '.payload'
    if label in ('valid', 'dummy'):
        return {'schema': 'f10-necessary-rows-root-policy/v1',
                'root_registration_path': r['outer_argv'][-1], 'job_tag': r['jobtag'],
                'label': label, 'artifact': payload, 'science_outcome': 'NONE',
                'source_files': copy.deepcopy(r['source_files']),
                'limits': copy.deepcopy(r['source_limits']),
                'profile': r['profiles']['dummy' if label == 'dummy' else 'control'][:],
                'closed_scope': {'path': r['cgroup_path'] + '/' + label,
                                 'device': None, 'inode': None}}
    mode = 'check' if label == 'startup-check' else 'produce'
    a = {'job_tag': r['jobtag'], 'status': 'REGISTERED', 'authority': 'ROOT-CAPRUN',
         'mode': mode, 'artifact': {'path': payload, 'sha256': '0'*64 if mode == 'check' else 'UNFORMED'},
         'files': copy.deepcopy(r['source_files']),
         'runtime': {'python_sha256': r['pins'][r['files']['python']],
                     'native_inventory_path': r['source_native_manifest'],
                     'native_inventory_sha256': r['pins'][r['source_native_manifest']]},
         'limits': copy.deepcopy(r['source_limits']), 'contract_sha256': r['contract_sha256'],
         'source_pins': copy.deepcopy(r['source_pins']), 'place': copy.deepcopy(r['place'])}
    if label == 'refuse-status':
        a['status'] = 'DISABLED'
    elif label == 'refuse-caps':
        a['limits']['cpu_seconds'] = '599'
    elif label == 'refuse-inventory':
        del a['files']['check.py']
    elif label == 'refuse-source':
        a['files']['produce.py'] = '0'*64
    return a


def validate_prepared(r, authorities):
    keys(r, ('schema enabled jobtag exclusive_no_concurrent_writer source_limits limits profiles '
             'environment uid gid instance_id hostname boot_id pid_namespace cgroup_path '
             'aggregate_cpu_start_usec files pins native_manifest source_native_manifest science_dir '
             'wrapper_dir output_mount authority_dir frozen_dir writer_dir durable_dir durable_device '
             'outer_argv admission_deadline_utc mathematical_deadline_utc task_deadline_utc '
             'worker_deadline_utc phase_policy typed_slot_policy commands source_files source_pins '
             'contract_sha256 place review_clearance preflight_policy execution_mode allowed_phases '
             'closed_scope_first_sha256 closed_child_guard').split(), 'registration')
    need(r['schema'] == 'f10-necessary-rows-runtime/closed-child-v1'
         and r['jobtag'] == 'f10-source-cone-r3-necessary-rows-v1', 'schema/job')
    need(r['enabled'] is False and r['exclusive_no_concurrent_writer'] is False, 'prepared flags')
    need(r['execution_mode'] == 'PREFLIGHT_ONLY_9' and r['allowed_phases'] == list(PHASES)
         and r['phase_policy'] is None and r['typed_slot_policy'] == {}
         and r['aggregate_cpu_start_usec'] == '0', 'nine-only policy')
    need(r['source_limits'] == dict(wall_seconds='900', cpu_seconds='600',
         memory_bytes='8589934592', aggregate_bytes='134217728'), 'source limits')
    need(r['limits'] == dict(wall_seconds='3000', cpu_seconds='2100',
         memory_bytes='8589934592', aggregate_bytes='134217728'), 'outer limits')
    need(r['profiles'] == {'control': [5, 3, 8589934592], 'dummy': [5, 3, 33554432],
         'produce': [900, 599, 8589934592], 'check': [900, 599, 8589934592],
         'mutate': [30, 20, 8589934592]}, 'profiles')
    base = r['science_dir'].removesuffix('/science')
    need(re.fullmatch(r'/opt/jc2-closedchild-preflight9-[0-9]{8}[a-z]', base) is not None, 'base path')
    batch = base.rsplit('/', 1)[1]
    for field, expected in {'science_dir': base+'/science', 'wrapper_dir': base+'/wrapper',
            'output_mount': '/run/'+batch, 'authority_dir': '/run/'+batch+'/authority',
            'frozen_dir': '/run/'+batch+'/frozen', 'writer_dir': '/run/'+batch+'/writer',
            'durable_dir': '/var/lib/'+batch+'/custody',
            'cgroup_path': '/sys/fs/cgroup/system.slice/'+batch+'.service',
            'native_manifest': base+'/metadata/native-manifest.json',
            'source_native_manifest': base+'/metadata/source-native-manifest.json',
            'preflight_policy': base+'/metadata/preflight-policy.json'}.items():
        need(r[field] == expected, 'path: '+field)
    f = r['files']
    keys(f, ('python', 'setpriv', 'caprun', 'dispatcher', 'probe', 'mutator'), 'files')
    for name, suffix in {'caprun': '/runtime/run_capped.py', 'dispatcher': '/wrapper/dispatch.py',
                         'probe': '/wrapper/probe.py', 'mutator': '/wrapper/mutate.py'}.items():
        need(f[name] == base+suffix, 'file path')
    need(f['python'] == '/usr/bin/python3.12' and f['setpriv'] == '/usr/bin/setpriv', 'native paths')
    need(r['outer_argv'] == [f['python'], '-I', '-S', '-B', f['dispatcher'],
                           '--registration', base+'/metadata/ROOT-REGISTRATION.json'], 'outer argv')
    need(r['uid'] == 65534 and r['gid'] == 65534 and r['environment'] ==
         {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC'}, 'identity/environment')
    keys(r['commands'], PHASES, 'commands')
    keys(authorities, PHASES, 'authorities')
    g = r['closed_child_guard']
    keys(g, ('schema', 'outer_device', 'outer_inode', 'root_no_migration', 'leaves'), 'guard')
    need(g['schema'] == 'CAPRUN-closed-child/v1' and g['outer_device'] is None
         and g['outer_inode'] is None and g['root_no_migration'] is False, 'unformed guard')
    keys(g['leaves'], PHASES, 'leaves')
    for label in PHASES:
        need(g['leaves'][label] == {'path': r['cgroup_path']+'/'+label,
                                  'device': None, 'inode': None}, 'prepared leaf')
        need(r['commands'][label] == expected_command(r, label), 'whole prepared argv: '+label)
        need(authorities[label] == expected_authority(r, label), 'whole prepared authority: '+label)
    need(r['outer_argv'][-1] not in r['pins'], 'registration self pin')
    for value in r['pins'].values():
        digest(value)
    return base


def bind(bundle, prepared_pins, observation_json, decision_json):
    """Return candidate filename -> bytes; caller authenticates every input."""
    keys(bundle, NAMES, 'bundle')
    keys(prepared_pins, NAMES, 'prepared pins')
    for name in NAMES:
        text(bundle[name])
        need(sha(bundle[name]) == digest(prepared_pins[name]), 'prepared hash: '+name)
    need(sum(map(len, bundle.values())) <= MAX_TOTAL, 'bundle bound')
    r, authorities = load(bundle[NAMES[0]]), load(bundle[NAMES[1]])
    original_r, original_a = copy.deepcopy(r), copy.deepcopy(authorities)
    base = validate_prepared(r, authorities)
    o, decision = load(observation_json), load(decision_json)
    keys(o, ('schema context instance_id hostname boot_id pid_namespace cgroup_path '
             'holder_pid start_ticks invocation_id outer_device outer_inode leaves '
             'coordinator_receipt_sha256 native_manifest_sha256 native_list_sha256').split(), 'observation')
    need(o['schema'] == 'caprun-late-observation/v1' and o['context'] in
         ('HISTORICAL_TEST', 'ROOT_ATTESTED_CANDIDATE'), 'observation context')
    keys(decision, ('schema context prepared_pins observation_sha256 enabled '
                    'exclusive_no_concurrent_writer root_no_migration freeze_token').split(), 'decision')
    need(decision['schema'] == 'ROOT_METADATA_BINDING_ONLY_NOT_RELEASE'
         and decision['context'] == o['context'] and decision['prepared_pins'] == prepared_pins
         and decision['observation_sha256'] == sha(observation_json), 'ROOT binding decision')
    need(all(decision[k] is True for k in ('enabled', 'exclusive_no_concurrent_writer', 'root_no_migration'))
         and decision['freeze_token'] == FREEZE, 'ROOT flags/freeze decision')
    for key in ('instance_id', 'hostname', 'boot_id', 'pid_namespace', 'cgroup_path'):
        need(type(o[key]) is str and o[key] == r[key], 'observed '+key)
    positive(o['holder_pid']); positive(o['start_ticks'])
    need(o['holder_pid'] < 2**31, 'PID bound')
    need(type(o['invocation_id']) is str and re.fullmatch('[0-9a-f]{32}', o['invocation_id']), 'invocation')
    outer = (positive(o['outer_device']), positive(o['outer_inode']))
    need(type(o['leaves']) is list and len(o['leaves']) == 9, 'observed leaf list')
    leaves, identities = {}, {outer}
    for leaf in o['leaves']:
        keys(leaf, ('name', 'path', 'device', 'inode'), 'observed leaf')
        name = leaf['name']
        need(type(name) is str and name in PHASES and name not in leaves, 'duplicate/unknown leaf')
        need(leaf['path'] == r['cgroup_path']+'/'+name, 'observed leaf path')
        ident = (positive(leaf['device']), positive(leaf['inode']))
        need(ident not in identities, 'duplicate cgroup identity')
        identities.add(ident)
        leaves[name] = leaf
    digest(o['coordinator_receipt_sha256']); digest(o['native_list_sha256'])
    need(digest(o['native_manifest_sha256']) == r['pins'][r['native_manifest']], 'native manifest binding')
    r['enabled'] = r['exclusive_no_concurrent_writer'] = True
    g = r['closed_child_guard']
    g['root_no_migration'] = True
    g['outer_device'], g['outer_inode'] = outer
    outputs, changes = {}, []
    for label in PHASES:
        leaf = leaves[label]
        for field in ('device', 'inode'):
            g['leaves'][label][field] = leaf[field]
            if label in ('valid', 'dummy'):
                authorities[label]['closed_scope'][field] = leaf[field]
        raw = encode(authorities[label])
        outputs['authority/'+label+'.json'] = raw
        command = r['commands'][label]
        replacements = {'--closed-child-device': (ph('CHILD_DEVICE'), str(leaf['device'])),
                        '--closed-child-inode': (ph('CHILD_'+label+'_INODE'), str(leaf['inode'])),
                        '--closed-outer-device': (ph('OUTER_DEVICE'), str(outer[0])),
                        '--closed-outer-inode': (ph('OUTER_INODE'), str(outer[1]))}
        if label != 'refuse-hash':
            flag = '--policy-sha256' if label in ('valid', 'dummy') else '--authorization-sha256'
            replacements[flag] = (ph(label+('_POLICY_SHA' if label in ('valid', 'dummy') else '_AUTH_SHA')), sha(raw))
        for flag, (before, after) in replacements.items():
            need(command.count(flag) == 1, 'unique argv flag')
            index = command.index(flag)+1
            need(command[index] == before, 'argv placeholder position')
            command[index] = after
            changes.append({'phase': label, 'index': index, 'old': before, 'new': after})
    need(TOKEN.search(encode(r).decode('ascii')) is None, 'unexpected registration placeholder')
    for a in authorities.values():
        need(TOKEN.search(encode(a).decode('ascii')) is None, 'unexpected authority placeholder')
    outputs['ROOT-REGISTRATION.json'] = encode(r, pretty=True)
    # Reverse precisely the allowlisted edits and compare every other parsed value.
    restored = copy.deepcopy(r)
    restored['enabled'] = restored['exclusive_no_concurrent_writer'] = False
    rg = restored['closed_child_guard']
    rg['root_no_migration'] = False
    rg['outer_device'] = rg['outer_inode'] = None
    for label in PHASES:
        rg['leaves'][label]['device'] = rg['leaves'][label]['inode'] = None
    for change in changes:
        restored['commands'][change['phase']][change['index']] = change['old']
    need(restored == original_r, 'unexpected registration difference')
    restored_a = copy.deepcopy(authorities)
    for label in ('valid', 'dummy'):
        restored_a[label]['closed_scope']['device'] = None
        restored_a[label]['closed_scope']['inode'] = None
    need(restored_a == original_a, 'unexpected authority difference')
    card, installer = text(bundle[NAMES[2]]), text(bundle[NAMES[3]])
    need('Actual worker '+o['instance_id']+', hostname '+o['hostname']+',\n' in card
         and '\nboot '+o['boot_id']+',' in card, 'card worker binding')
    need('jc2_base='+base+'\n' in installer
         and "= '"+o['instance_id']+"'\n" in installer
         and "= '"+o['boot_id']+"'\n" in installer, 'installer worker/base binding')
    common = {ph('CAPTURED_HOLDER_PID'): (str(o['holder_pid']), 1),
              ph('CAPTURED_HOLDER_START_TICKS'): (str(o['start_ticks']), 1),
              ph('CAPTURED_INVOCATION_ID'): (o['invocation_id'], 1),
              ph('FINAL_REGISTRATION_SHA'): (sha(outputs['ROOT-REGISTRATION.json']), 1)}
    card_replacements = dict(common)
    card_replacements.update({
        ph('COORDINATOR_RETIREMENT_TIMER_RECEIPT_SHA'): (o['coordinator_receipt_sha256'], 1),
        '# ROOT closed-child nine-phase execution card — DISABLED\n':
            ('# ROOT closed-child nine-phase execution card — BOUND FOR ONE PREFLIGHT\n', 1),
        'This is an unformed administrative template, not a release or result.':
            ("This is ROOT's actual metadata binding, not a result or automatic token release.", 1),
        'Final registration and holder topology remain unformed in this preholder card.':
            ('Final registration and holder topology are now bound to actual observed values; '
             'ROOT accepts exclusive no-migration/no-entrant trust for this single observation.', 1)})
    outputs['ROOT-EXECUTION-CARD.md'] = replace_exact(card, card_replacements)
    manifest = ''.join(sha(outputs[n])+'  '+n+'\n' for n in
                       ('ROOT-REGISTRATION.json', 'ROOT-EXECUTION-CARD.md'))
    manifest += o['native_list_sha256']+'  native.sha256\n'
    outputs['FINAL-INSTALL-INPUTS.sha256'] = manifest.encode('ascii')
    install_replacements = dict(common)
    install_replacements[ph('FINAL_REGISTRATION_SHA')] = (sha(outputs['ROOT-REGISTRATION.json']), 2)
    install_replacements.update({ph('FINAL_INSTALL_RELEASE'): (FREEZE, 1),
        ph('FINAL_CARD_SHA'): (sha(outputs['ROOT-EXECUTION-CARD.md']), 1),
        ph('FINAL_INSTALL_MANIFEST_SHA'): (sha(outputs['FINAL-INSTALL-INPUTS.sha256']), 1)})
    outputs['final-install.sh'] = replace_exact(installer, install_replacements)
    summary = {'schema': 'caprun-latebinding-summary/v1', 'status': STATUS,
        'context': o['context'], 'input_pins': dict(prepared_pins),
        'observation_sha256': sha(observation_json), 'decision_sha256': sha(decision_json),
        'authority_serialization': 'SORTED_COMPACT_ASCII_NEWLINE',
        'registration_serialization': 'PREPARED_KEY_ORDER_INDENT2_ASCII_NEWLINE',
        'argv_changes': changes, 'guard_outer': list(outer), 'guard_leaves': o['leaves'],
        'flags': ['enabled', 'exclusive_no_concurrent_writer', 'closed_child_guard.root_no_migration'],
        'authority_changes': ['valid.closed_scope.device', 'valid.closed_scope.inode',
                              'dummy.closed_scope.device', 'dummy.closed_scope.inode'],
        'text_changes': {'card': list(card_replacements), 'installer': list(install_replacements)},
        'outputs': {n: {'sha256': sha(raw), 'bytes': len(raw)} for n, raw in outputs.items()},
        'native_list_digest_is_opaque': True, 'installation_or_release_authorized': False}
    outputs['SUMMARY.json'] = encode(summary)
    need(len(outputs) == 14 and all(len(raw) <= MAX_OUTPUT for raw in outputs.values())
         and sum(map(len, outputs.values())) <= MAX_TOTAL, 'aggregate output bound')
    return outputs
