#!/usr/bin/env python3
"""src/app.html + vendor/xlsx.full.min.js → dist/육아휴직관리.html (단일 파일)"""
import pathlib
root = pathlib.Path(__file__).parent
src = (root/'src'/'app.html').read_text(encoding='utf-8')
lib = (root/'vendor'/'xlsx.full.min.js').read_text(encoding='utf-8')
assert '</script' not in lib.lower(), 'lib contains </script>'
assert src.count('/*__XLSX__*/') == 1
out = src.replace('/*__XLSX__*/', lib)
dst = root/'dist'/'육아휴직관리.html'
dst.write_text(out, encoding='utf-8')
print(dst, f'{dst.stat().st_size/1024:.0f} KB')
