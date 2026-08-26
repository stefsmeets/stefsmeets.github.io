import subprocess as sp
from pathlib import Path

cwd = Path.cwd()
paths = cwd.glob('*.pdf')

for path in paths:
    print(path)
    stem = path.stem
    sp.run(f'convert -resize 640x {stem}.pdf[0] thumb_{stem}.webp'.split())
