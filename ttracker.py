import argparse
import datetime
import os
import sys
from pathlib import Path
from subprocess import Popen, PIPE


def subprocess_pain(cmd, stdin):
    with Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE) as p:
        try:
            s, e = p.communicate(os.fsencode(stdin))
        except:
            p.kill()
            p.wait()
            raise
        r = p.poll()
        if r:
            print('dmenu says: nah (%d)' % r)
            sys.exit(1)
        return os.fsdecode(s).strip()


def entry():
    parser = argparse.ArgumentParser(description='Track some time, or something.')
    parser.add_argument('--dmenu', metavar='COMMAND', type=str, default='dmenu',
                        help='command line to use as dmenu (shell expansion is ON)')
    parser.add_argument('--trackfile', metavar='FILE', type=Path,
                        default=Path.home() / '.ttracker',
                        help='file for tracking YOU *tips tinhat*')
    args = parser.parse_args()
    args.trackfile.touch()
    with args.trackfile.open() as fd:
        fd.seek(0)
        things = set()
        for line in fd:
            ts, thing = line.split('$', maxsplit=1)
            things.add(thing.strip())
        things = '\n'.join(sorted(things))
        thing = subprocess_pain(args.dmenu, things)
        # This probably doesn't work with DST
        ts = datetime.datetime.utcnow().isoformat()
        print('Thing:', thing)
    with args.trackfile.open('a+') as fd:
        fd.write('{ts}$ {thing}\n'.format_map(locals()))
