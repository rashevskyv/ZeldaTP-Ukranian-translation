import json, sys
from fontTools.ttLib import TTFont
src, tmap, out_up, out_tp = sys.argv[1:5]
f = TTFont(src); cm = f.getBestCmap()
# U+02BC (Ukrainian apostrophe) = the right single quote glyph
for t in f['cmap'].tables:
    if t.isUnicode(): t.cmap[0x2BC] = cm[0x2019]
f.save(out_up)
m = json.load(open(tmap, encoding='utf-8'))
f = TTFont(out_up); cm = f.getBestCmap(); log = []
for cyr, slot in m.items():
    if len(cyr) != 1 or len(slot) != 1: continue
    if ord(cyr) not in cm: log.append(f'no glyph {cyr}'); continue
    if ord(slot) < 0xA0 or ord(slot) > 0xFF: log.append(f'slot outside Latin-1 {cyr}->{slot!r}'); continue
    for t in f['cmap'].tables:
        if t.isUnicode(): t.cmap[ord(slot)] = cm[ord(cyr)]
f.save(out_tp)
open('mk.log', 'w', encoding='utf-8').write('\n'.join(log) + f'\nmapped {len(m)}\n' + ' '.join(f'{k}{v}' for k, v in m.items()))
