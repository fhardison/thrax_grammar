import re

FILE = '..\\originals\\synt.txt'

lines = []
buffer = []
header = ''
l_count = 0

with open(FILE, 'r', encoding='utf-8') as f:
    header, rest = f.read().split("\n\n", maxsplit=1)
    
    for line in re.sub(r'(\S)-\s+', r'\1', rest).split('\n'):
        l = line.strip()
        if not l:
            continue
         
        if '{' in l:
            l = f"<blockquote>{l}</blockquote>"
            lines.append(' '.join(buffer))
            buffer = []
            lines.append(l)
        elif l[-1] in '.?!':
            buffer.append(l)
            lines.append(' '.join(buffer))
            buffer = []
        else:
            buffer.append(l)
    lines.append(' '.join(buffer))


HEADER = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/alpheios-components@latest/dist/style/style-components.min.css"/>
        <link rel="stylesheet" href="typebase.css" type="text/css" />
        <link rel="stylesheet" href="normalize.css" type="text/css" />
        <link rel="stylesheet" href="fonts.css" type="text/css" />
    </head>
<body>
<article style="margin:16px">
    <div class="alpheios-enabled">"""
    

FOOTER = """</article>
</div>
<style>
.en {
    cursor: not-allowed;
}
p {
font-style:normal;
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

OFILE = '..\\docs\\dyscolus_synt.html'

header = header.replace('\n', '<br />')

with open(OFILE, 'w', encoding="UTF-8") as g:
    print(HEADER, file=g)
    print(f"<h1>{header}</h1>", file=g)
    for line in lines:
        print(f"<p>{line}</p>", file=g)
    print(FOOTER, file=g)
    
print("DONE")
            