FILE = "grammar_aligned.txt"

output = {'en': {}, 'grc': {}}


with open(FILE, 'r', encoding="UTF-8") as f:
    section_counter = 0
    sections_seen = []
    for line in f:
        if not line.strip():
            continue
        try:
            ref, contents = line.strip().split(' ', maxsplit=1)
            tag, lang = ref.split('@', maxsplit=1)
            if 'h1' in tag:
                if tag not in sections_seen:
                    section_counter += 1
                    sections_seen.append(tag)
            _, rest = tag.split('.', maxsplit=1)
            tag = f"{section_counter:0>2}.{rest}"
            output[lang][tag] = contents.strip()
        except:
            print(line)
            exit()

with open(FILE.replace('grammar', 'new_grammar'), 'w', encoding="UTF-8") as f:
    for (tag, contents) in output['grc'].items():
        print(f"{tag}@grc {contents}", file=f)
        print(f"{tag}@en {output['en'][tag]}", file=f)
print("DONE")
