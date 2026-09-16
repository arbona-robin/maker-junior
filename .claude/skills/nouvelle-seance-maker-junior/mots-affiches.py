"""Compte les mots affichés d'une page Markdown : sans alt, chemins, balises ni syntaxe."""
import re, sys
s = sys.stdin.read() if len(sys.argv) < 2 else open(sys.argv[1]).read()
s = re.sub(r'!\[[^\]]*\]\([^)]*\)', ' ', s)          # images (alt non affiché)
s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)        # liens -> texte
s = re.sub(r'\[!(NOTE|TIP|CAUTION|IMPORTANT|WARNING)\]', ' ', s)
s = re.sub(r'<[^>]+>', ' ', s)                        # balises HTML
s = re.sub(r'(?m)^\|?[\s:|-]+\|?$', ' ', s)           # séparateurs de tableau
words = [w for w in s.split() if re.search(r'\w', w)]
print(len(words))
