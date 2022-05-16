import re


FILES = ['pron', 'conn', 'adv']

FILE = '..\\originals\\dyscolus\\'
OFILE = '..\\docs\\dyscolus_'


END_PUNC = ".?!"



HEADER = """<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
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

def handle_poss_blockquote(l):
    if re.findall(r'\d+\)', l) != []:
        return f"<blockquote>{l}</blockquote>"
    return l


def process_lines(lines, ofile):
    lines = [x.strip() for x in lines if x.strip()]
    last_line = lines[0]
    print('<p>', end='',file=ofile)
    for line in lines[1:]:
        
        if (last_line[-1] in ')]' and last_line[-2] in END_PUNC) or last_line[-1] in END_PUNC:
            if line[0].isupper():
                print(handle_poss_blockquote(last_line) + '</p>\n<p>',file=ofile)
            else:
                print(handle_poss_blockquote(last_line), end=' ', file=ofile)
        else:
            print(handle_poss_blockquote(last_line), end=' ', file=ofile)
        last_line = line
    print(last_line + '</p>', end='', file=ofile)




def process_file(fpath, opath):
    with open(fpath, 'r', encoding='utf-8') as f, open(opath, 'w', encoding="utf-8") as g:
        print(HEADER, file=g)        
        header, rest = f.read().split("\n\n", maxsplit=1)
        header = header.replace('\n', '<br />')
        print(f"<h1>{header}</h1>", file=g)
        lines = re.sub(r'(\S)-\s+', r'\1', rest).split('\n')
        process_lines(lines, g)
        print(FOOTER, file=g)


for f in FILES:
    process_file(FILE + f + '.txt', OFILE + f + '.html')
