from pathlib import Path

import re

DATE_PAT = re.compile(r'\d\d\d\d-\d\d-\d\d')

cwd = Path.cwd()

paths = cwd.glob('*.md')

for path in paths:
    print(path)
    if path.name in '_index.md':
        continue

    text = path.read_text()
    text = text.replace('\ntags', f'\nslug: {path.stem.lower()}\ntags')

    date = DATE_PAT.search(text)[0]

    date = date.replace('-', '')

    new_name = f'{date}_{path.stem}'.lower()

    drc = cwd / new_name
    filename = drc / 'index.md'

    print(filename)
    print(text)

    drc.mkdir()

    with open(filename, 'w') as f:
        print(text, file=f)
