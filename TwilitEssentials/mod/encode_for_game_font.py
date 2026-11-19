"""Write proj/res/localization/uk with game-encoded text (Cyrillic -> Latin-1 slots) for keys TE draws with the
Hylia atlas (U+0020..U+00FF only) or the game's message font. Other keys stay Unicode."""
import json, pathlib, shutil, collections
SRC = pathlib.Path(r'E:\Emulators\RomHacking\Zelda\Twilight Princess\GC + Wii\tools\twilit_essentials_uk\uk')
DST = pathlib.Path(r'D:\RomHacking_tmp\te_uk_mod\proj\res\localization\uk')
M = json.loads(pathlib.Path(r'E:\Emulators\RomHacking\Zelda\Twilight Princess\GC + Wii\picoripi\translation_map.json').read_text('utf-8'))
M = {k: v for k, v in M.items() if len(k) == 1 and len(v) == 1}
used = set(M.values())
PUNCT = {'«': '"', '»': '"', '—': '-', '–': '-', '…': '...', '’': "'", 'ʼ': "'", '“': '"', '”': '"', '\u00a0': ' '}
PREFIX = ('advanced_collection.', 'collection.', 'flurry.', 'boss_rush.tutorial.', 'dungeon_rush.tutorial.')
EXACT = {'dungeon_rush.map_label', 'rush.split_time'}
def hylia(k): return (k.startswith(PREFIX) and not k.startswith('collection.') or k.startswith('collection.') and not k.startswith('menus.')) or k in EXACT
bad = collections.Counter()
def enc(s):
    out = []
    for ch in s:
        if ch in M: out.append(M[ch])
        elif ch in PUNCT: out.append(PUNCT[ch])
        elif ord(ch) < 0x80 or (ord(ch) <= 0xFF and ch not in used): out.append(ch)
        else: bad[ch] += 1; out.append('?')
    return ''.join(out)
shutil.rmtree(DST, ignore_errors=True); n = 0
for p in SRC.glob('*/*.json'):
    d = json.loads(p.read_text('utf-8'))
    for k in d:
        if hylia(k): d[k] = enc(d[k]); n += 1
    q = DST / p.parent.name / p.name; q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', 'utf-8', newline='\n')
print('encoded', n, 'unmapped', dict(bad))
