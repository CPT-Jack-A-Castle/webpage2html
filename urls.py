#!/usr/bin/env python3

import os

with open('urls.txt', 'r') as f:
	raw = f.read().splitlines()

urls = {}
for addr in raw:
	name = addr.replace('#', '.').replace('?', '.').replace('&', '.').replace('@', '.').replace('%', '.')
	name = name.split('://', maxsplit=1)[1].replace('/', '-').strip('-')
	urls[addr] = name

i = 1
for key, val in urls.items():
	print(f'({i}/{len(urls)}) {key}')
	os.system(f'python webpage2html.py -k {key} -o html/{val}.html')
	i += 1
