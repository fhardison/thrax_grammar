from bs4 import BeautifulSoup

with open('src\\grammar_text.html', encoding="UTF-8") as f:
    soup = BeautifulSoup(f)
    parts = soup.find_all(['p', 'h1', 'h2'])
    counter = 0
    for part in parts:
        if part.name == 'h1':
            print(part.text)
        elif part.name == 'h2':
            print(part.text)
            
        elif part.name == 'p':
            print(part.text)
            