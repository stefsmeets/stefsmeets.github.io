# Fix security policy in `convert`:
#     https://stackoverflow.com/a/65682705

import subprocess as sp
from pathlib import Path
import sys

cwd = Path.cwd()

if sys.argv[1:]:
    paths = (Path(path) for path in sys.argv[1:])
else:
    paths = cwd.glob('*.pdf')

for path in paths:
    stem = path.stem

    infile = f'{stem}.pdf'
    outfile = f'thumb_{stem[0:30]}.webp'

    if Path(outfile).exists():
        continue

    print(f'{infile} -> {outfile}')

    sp.run(f'convert -resize 640x -background white -flatten {infile}[0] {outfile}'.split())
