#!/usr/bin/env python3
"""Root-gated prospective caller. NO authority file is distributed with this prep."""
import argparse
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parent))
import exact as E
import hybrid as H

INSTANCE = 'i-0da0cebfc97c9fd54'
CWD = '/home/ubuntu/d125-hybrid81-exact-solver-20260907'
SOURCE = Path('/home/ubuntu/d125-hybrid-affine-pilot-20260907/construction.jsonl')
RUNNER_SHA = '4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2'
BINARY_SHA = '90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4'
PLAN_SHA = '38bc496f9f2eb7f7519c70bbabe0eab8586c56264b7e20c0078fc71cb818cd6d'
CAPS = {'decision_seconds': 300, 'verify_seconds': 120, 'control_seconds': 10,
        'total_seconds': 450, 'as_bytes': 16*1024**3, 'rss_bytes': 16*1024**3,
        'stream_bytes': 64*1024**2}
CONTROL_VARS = ['x']
CONTROL_TEXT = ['0', 'x', '0', 'x', '1-x', '0']


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1024*1024), b''):
            h.update(part)
    return h.hexdigest()


def write_new(path, data):
    with Path(path).open('xb') as stream:
        stream.write(data); stream.flush(); os.fsync(stream.fileno())


def pins():
    return {'driver.py': file_sha(__file__), 'exact.py': file_sha(Path(__file__).with_name('exact.py')),
            'run_capped.py': RUNNER_SHA, 'Singular': BINARY_SHA,
            'hybrid.py': file_sha(Path(__file__).with_name('hybrid.py')),
            'source.jsonl': H.CONSTRUCTION_SHA, 'original_source': H.ORIGINAL_SHA, 'registration': PLAN_SHA}


def authority_check(a, phase, observed, expected_pins):
    E.need(a.get('schema') == 'jc2.d125-hybrid81-solver-authority/v1' and a.get('root_green') is True,
           'explicit root GREEN absent')
    expected_mode = 'engineering_control' if phase == 'control' else 'solver'
    E.need(phase in ('control', 'decision', 'verify') and a.get('mode') == expected_mode,
           'engineering/solver authority separation')
    E.need(isinstance(a.get('job_id'), str) and a['job_id'].strip(), 'job registration absent')
    E.need(a.get('pins') == expected_pins and a.get('caps') == CAPS, 'code/source/cap pins drift')
    E.need(observed['system'] == 'Linux' and observed['vendor'] == 'Amazon EC2'
           and observed['instance'] == a.get('instance_id') == INSTANCE, 'registered Linux EC2 required')
    E.need(observed['cwd'] == a.get('cwd') == CWD and observed['boot'] == a.get('boot_id')
           and bool(observed['boot']), 'cwd/boot binding')
    start = datetime.fromisoformat(a.get('started_utc', '').replace('Z', '+00:00'))
    end = datetime.fromisoformat(a.get('deadline_utc', '').replace('Z', '+00:00'))
    E.need(start.tzinfo is not None and end.tzinfo is not None, 'timezone absent')
    E.need(0 < end.timestamp()-start.timestamp() <= 450 and
           start.timestamp() <= observed['now'] < end.timestamp(), 'deadline/total budget')
    if expected_mode == 'solver':
        E.need(a.get('full_stream_gate_accepted') is True, 'full-stream gate not accepted')
        for name in ('full_stream_gate_sha256', 'engine_index_control_sha256',
                     'output_limit_control_sha256', 'descendant_control_sha256'):
            value = a.get(name, '')
            E.need(isinstance(value, str) and len(value) == 64 and
                   all(c in '0123456789abcdef' for c in value), 'missing accepted control '+name)
    remaining = math.floor(end.timestamp()-observed['now'])
    E.need(remaining >= 1, 'less than one second remains')
    return min(CAPS[phase+'_seconds'], remaining)


def observed_host():
    return {'system': platform.system(), 'vendor': Path('/sys/class/dmi/id/sys_vendor').read_text().strip(),
            'instance': Path('/sys/class/dmi/id/board_asset_tag').read_text().strip(),
            'boot': Path('/proc/sys/kernel/random/boot_id').read_text().strip(),
            'cwd': str(Path.cwd().resolve()), 'now': time.time()}


def context(authority_path, phase):
    raw = Path(authority_path).read_bytes(); a = E.strict_json(raw)
    duration = authority_check(a, phase, observed_host(), pins())
    E.need(str(Path(__file__).resolve().parent) == CWD, 'code not in registered fresh cwd')
    E.need(file_sha(Path(CWD)/'run_capped.py') == RUNNER_SHA, 'runner drift')
    E.need(file_sha('/usr/bin/Singular') == BINARY_SHA, 'binary drift')
    return a, E.digest(raw), duration


def footer(variables, source_hash, control=False):
    """Only control=True avoids slimgb; production caller chooses from checked phase."""
    header = 'JC2CERT 1 '+source_hash+' '+E.ring_id(variables)
    lines = ['option(redSB); short=0;', 'int ci;', 'print("'+header+'");',
             'print("I_SIZE "+string(size(I)));',
             'print("I_BEGIN "+string(ncols(matrix(I))));',
             'for(ci=1;ci<=ncols(matrix(I));ci++){print("I "+string(ci)+" "+string(I[ci]));}',
             'print("I_END");',
             'ideal G=ideal(1);' if control else 'ideal G=slimgb(I);',
             'print("G_BEGIN "+string(ncols(matrix(G))));',
             'for(ci=1;ci<=ncols(matrix(G));ci++){print("G "+string(ci)+" "+string(G[ci]));}',
             'print("G_END");', 'int hasunit=0;',
             'for(ci=1;ci<=ncols(matrix(G));ci++){if(G[ci]!=0 && deg(G[ci])==0){hasunit=1;}}',
             'if(hasunit){', 'matrix T=lift(I,ideal(1));', 'matrix CHECK=matrix(I)*T;',
             'print("T_BEGIN "+string(nrows(T)));',
             'for(ci=1;ci<=nrows(T);ci++){print("T "+string(ci)+" "+string(T[ci,1]));}',
             'print("T_END");',
             'if(nrows(CHECK)==1 && ncols(CHECK)==1 && ncols(T)==1){print("CHECK "+string(CHECK[1,1]));}',
             'print("END UNIT");', '}else{print("END NONUNIT");}', 'quit;']
    return '\n'.join(lines)+'\n'


def control_input():
    prefix = 'ring R=0,(x),dp;\nideal I='+','.join(CONTROL_TEXT)+';\n'
    return prefix+footer(CONTROL_VARS, E.digest(prefix.encode()), control=True)


def check_control(stdout, stderr):
    prefix = 'ring R=0,(x),dp;\nideal I='+','.join(CONTROL_TEXT)+';\n'
    engine, basis, cofactors = E.parse_result(stdout, stderr, CONTROL_VARS, E.digest(prefix.encode()))
    E.need(cofactors is not None, 'index-control cofactor absent')
    rows = [E.polynomial(t, CONTROL_VARS) for t in CONTROL_TEXT]
    verdict, mapping, lifted = E.unit_certificate(rows, engine, cofactors)
    return {'verdict': verdict, 'original_rows': len(rows), 'engine_columns': len(engine),
            'cofactor_rows': len(cofactors), 'engine_to_original': mapping}


def limits(phase):
    memory = 512*1024**2 if phase == 'control' else CAPS['as_bytes']
    resource.setrlimit(resource.RLIMIT_AS, (memory, memory))
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAPS['stream_bytes'], CAPS['stream_bytes']))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def arm_deadline(a, duration):
    """One wall timer covers source parsing and survives execve; never reset."""
    end = datetime.fromisoformat(a['deadline_utc'].replace('Z', '+00:00')).timestamp()
    signal.signal(signal.SIGALRM, signal.SIG_DFL)
    signal.pthread_sigmask(signal.SIG_UNBLOCK, {signal.SIGALRM})
    remaining = min(duration, end-time.time())
    E.need(remaining > 0, 'absolute payload deadline expired')
    signal.setitimer(signal.ITIMER_REAL, remaining)


def payload(authority_path, phase):
    a, authority_sha, duration = context(authority_path, phase)
    arm_deadline(a, duration)
    E.need(os.getpid() == os.getpgrp(), 'payload must be exact CAPRUN leader')
    parent = Path('/proc')/str(os.getppid())/'cmdline'
    E.need(str(Path(CWD)/'run_capped.py').encode() in parent.read_bytes().split(b'\0'),
           'CAPRUN parent required')
    limits(phase)
    write_new(phase+'.identity.json', E.canonical({'pid': os.getpid(), 'pgid': os.getpgrp(),
              'start_ticks': Path('/proc/self/stat').read_text().split(') ', 1)[1].split()[19],
              'authority_sha256': authority_sha, 'host': observed_host(), 'phase': phase}))
    if phase == 'control':
        script = control_input()
    else:
        variables, rows, labels, prefix = H.read_hybrid(SOURCE.read_bytes(), production=True)
        if phase == 'verify':
            receipt = E.strict_json(Path('decision.result.json').read_bytes())
            telemetry = E.strict_json(Path('decision.telemetry.json').read_bytes())
            identity = E.strict_json(Path('decision.identity.json').read_bytes())
            E.need(receipt['authority_sha256'] == authority_sha and receipt['runner_rc'] == 0
                   and receipt.get('phase') == 'decision'
                   and receipt.get('source_pins_after') == {'jsonl': H.CONSTRUCTION_SHA},
                   'decision custody/return/source status')
            E.need(telemetry.get('schema') == 'CAPRUN/v1' and telemetry.get('error') is None and
                   telemetry.get('status') == 'NORMAL_EXIT' and telemetry.get('child_returncode') == 0,
                   'decision not normal exact termination')
            E.need(file_sha('decision.identity.json') == receipt['artifacts']['identity.json'] and
                   identity['authority_sha256'] == authority_sha and
                   telemetry['pid'] == telemetry['pgid'] == identity['pid'] == identity['pgid'] and
                   telemetry['cwd'] == CWD and telemetry['start_identity'] ==
                   'boot='+identity['host']['boot']+';start_ticks='+identity['start_ticks'],
                   'decision exact child identity mismatch')
            for name in ('stdout', 'stderr', 'telemetry.json'):
                E.need(file_sha('decision.'+name) == receipt['outputs'][name], 'decision output drift')
            engine, basis, cofactors = E.parse_result(Path('decision.stdout').read_bytes(),
                  Path('decision.stderr').read_bytes(), variables, H.CONSTRUCTION_SHA)
            mapping = E.engine_map(rows, engine)
            if cofactors is None:
                verdict = E.proper_certificate(rows, basis, len(variables))
            else:
                verdict, mapping, unused = E.unit_certificate(rows, engine, cofactors)
            print(json.dumps({'verdict': verdict, 'source_sha256': H.CONSTRUCTION_SHA,
                  'source_rows': len(rows), 'variables': len(variables), 'engine_to_source': mapping,
                  'source_labels_sha256': E.digest(E.canonical(labels)), 'ring_sha256': E.ring_id(variables)}, sort_keys=True))
            return
        script = prefix+footer(variables, H.CONSTRUCTION_SHA)
    E.need(len(script.encode()) <= 2*1024**2, 'input artifact ceiling')
    write_new(phase+'.sing', script.encode('ascii'))
    env = {**os.environ, 'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1',
           'MKL_NUM_THREADS': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
    os.execve('/usr/bin/Singular', ['Singular', '--no-rc', '-q', phase+'.sing'], env)


def launch(authority_path, phase):
    a, authority_sha, duration = context(authority_path, phase)
    E.need(not any(Path(phase+'.'+suffix).exists() for suffix in
           ('sing', 'stdout', 'stderr', 'telemetry.json', 'identity.json', 'launch.json', 'result.json')),
           'fresh exclusive phase paths required')
    memory = 512*1024**2 if phase == 'control' else CAPS['rss_bytes']
    command = [sys.executable, '-I', '-B', str(Path(CWD)/'run_capped.py'), '--wall-seconds', str(duration),
               '--cpu-seconds', str(duration), '--rss-bytes', str(memory), '--cwd', CWD,
               '--stdout-file', phase+'.stdout', '--stderr-file', phase+'.stderr',
               '--telemetry-file', phase+'.telemetry.json', '--', sys.executable, '-I', '-B',
               str(Path(__file__).resolve()), 'payload', '--phase', phase,
               '--authority', str(Path(authority_path).resolve())]
    write_new(phase+'.launch.json', E.canonical({'authority_sha256': authority_sha, 'command': command,
             'caller_pid': os.getpid(), 'caller_pgid': os.getpgrp(), 'phase': phase, 'duration': duration}))
    result = subprocess.run(command, check=False)
    outputs = {name: file_sha(phase+'.'+name) for name in ('stdout', 'stderr', 'telemetry.json')
               if Path(phase+'.'+name).is_file()}
    artifacts = {name: file_sha(phase+'.'+name) for name in ('sing', 'identity.json')
                 if Path(phase+'.'+name).is_file()}
    after = {} if phase == 'control' else {'jsonl': file_sha(SOURCE)}
    if after:
        E.need(after == {'jsonl': H.CONSTRUCTION_SHA}, 'post-run frozen source drift')
    write_new(phase+'.result.json', E.canonical({'authority_sha256': authority_sha,
              'runner_rc': result.returncode, 'outputs': outputs, 'artifacts': artifacts,
              'source_pins_after': after, 'phase': phase}))
    return result.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=('launch', 'payload'))
    parser.add_argument('--phase', choices=('control', 'decision', 'verify'), required=True)
    parser.add_argument('--authority', required=True)
    args = parser.parse_args()
    if args.operation == 'payload':
        payload(args.authority, args.phase)
    else:
        raise SystemExit(launch(args.authority, args.phase))


if __name__ == '__main__':
    main()
