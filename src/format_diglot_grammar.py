FILE = "new_grammar_aligned.txt"

output = {'en': {}, 'grc': {}}


with open(FILE, 'r', encoding="UTF-8") as f:
    sections_seen = []
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

HEADER = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/alpheios-components@latest/dist/style/style-components.min.css"/>
    </head>
<body>
    <div class="alpheios-enabled">"""

FOOTER = """    </div>
<style>
.en {
    cursor: not-allowed;
}
</style>
    <script type="text/javascript">
        document.addEventListener("DOMContentLoaded", function(event) {
        import ("https://cdn.jsdelivr.net/npm/alpheios-embedded@latest/dist/alpheios-embedded.min.js").then(embedLib => {
            window.AlpheiosEmbed.importDependencies({ 
            mode: 'cdn'
            }).then(Embedded => {
            new Embedded({clientId: "thrax-grammar-fhard"}).activate();
            }).catch(e => {
            console.error(`Import of Alpheios embedded library dependencies failed: ${e}`)
            })

        }).catch(e => {
            console.error(`Import of Alpheios Embedded library failed: ${e}`)
        })
        });
    </script>
</body>
</html>"""

OFILE = 'diglot.html'

with open(OFILE, 'w', encoding="UTF-8") as g:
    print(HEADER, file=g)
    for tag, contents in output['grc'].items():
        en = output['en'][tag]
        if 'h1' in tag:
            print(f"<h1 class='grc' class='alpheios-enabled' lang='grc'>{contents}</h1>", file=g)
            print(f"<h1 class='en' lang='en'>{en}</h1>", file=g)
        else:
            print("<p>", file=g)
            print(f"<span class='grc' class='alpheios-enabled' lang='grc'>{contents}</span>", file=g)
            print("<br style='margin-bottom:0.25em;' />", file=g)
            print(f"<span class='en' lang='en'>{en}</span>", file=g)
            print("</p>", file=g)
    print(FOOTER, file=g)
