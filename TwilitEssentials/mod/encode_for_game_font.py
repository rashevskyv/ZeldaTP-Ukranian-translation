"""Write proj/res/localization/uk with game-encoded text (Cyrillic -> Latin-1 slots) for keys TE draws with the
Hylia atlas (U+0020..U+00FF only) or the game's message font. Other keys stay Unicode."""
import json, pathlib, shutil, collections
SRC = pathlib.Path(r'E:\Emulators\RomHacking\Zelda\Twilight Princess\GC + Wii\tools\twilit_essentials_uk\uk')
DST = pathlib.Path(r'D:\RomHacking_tmp\te_uk_mod\proj\res\localization\uk')
M = json.loads(pathlib.Path(r'E:\Emulators\RomHacking\Zelda\Twilight Princess\GC + Wii\picoripi\translation_map.json').read_text('utf-8'))
M = {k: v for k, v in M.items() if len(k) == 1 and len(v) == 1}
used = set(M.values())
PUNCT = {'«': '"', '»': '"', '—': '-', '–': '-', '…': '...', '’': "'", 'ʼ': "'", '“': '"', '”': '"', ' ': ' '}
PREFIX = ('advanced_collection.', 'flurry.', 'boss_rush.tutorial.', 'dungeon_rush.tutorial.', 'names.',
          'map_markers.hints.', 'map_markers.compass.', 'map_markers.symbols.', 'map_markers.colors.',
          'map_markers.palette.', 'quick_access.')
EXACT = {'common.done', 'dungeon_rush.map_label', 'dungeon_rush.splits_section', 'dungeon_rush.customize.items_section',
         'rush.best', 'rush.best_2', 'rush.best_3', 'rush.best_seg', 'rush.close', 'rush.continue', 'rush.final_time',
         'rush.new_record_2', 'rush.pb', 'rush.pb_seg', 'rush.personal_best', 'rush.segment', 'rush.split_time',
         'rush.splits', 'rush.sum_of_best', 'rush.sum_of_best_2', 'rush.add_remove', 'rush.clear_slots', 'rush.fight',
         'rush.leaderboard', 'rush.leave_boss_rush', 'rush.start_cave', 'rush.start_master_rush'}
def hylia(k):
    if k.startswith('quick_access.quick_access.') or k in ('quick_access.description', 'quick_access.mods'): return False
    if k.endswith('.help') and not k.startswith('advanced_collection.'): return False
    if k.startswith('collection.'): return True          # item names, descriptions, quest letters and dialogue
    return k.startswith(PREFIX) or k in EXACT
# English 'Style' is one lookup for the settings panel (Unicode font) and the map hint (Latin-1 atlas): only ASCII
# draws the same in both, so the word is Cyrillic look-alike Latin capitals.
ASCII = {'customization.stamina_bar.style': 'CKIH', 'common.done': 'OK', 'map_markers.palette.title': 'Скін  %d/%d'}
# 'Done' is shared the same way: 'OK' is ASCII.
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
        if k in ASCII: d[k] = ASCII[k]
        if hylia(k): d[k] = enc(d[k]); n += 1
    q = DST / p.parent.name / p.name; q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', 'utf-8', newline='\n')
print('encoded', n, 'unmapped', dict(bad))
