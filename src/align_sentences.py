FILE = "to_align.txt"
output = {'grc' : {}, 'en': {}}
with open(FILE, 'r', encoding="UTF-8") as f:
    for line in f:
        if not line.strip():
            continue
        try:
            ref, contents = line.strip().split(' ', maxsplit=1)
            tag, lang = ref.split('@', maxsplit=1)
            output[lang][tag] = contents.strip()
        except:
            print(line)
            exit()

OFILE = 'aligned_section.txt'

with open(OFILE, 'w', encoding="UTF-8") as g:
    for tag, contents in output['grc'].items():
        en = output['en'][tag]
        print(f"{tag}@grc {contents}", file=g)
        print(f"{tag}@en {en}", file=g)
        print('', file=g)