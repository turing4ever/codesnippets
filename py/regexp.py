import re
from collections import Counter

text = 'Awesome, I am doing the #100DaysOfCode challenge'
print(text.startswith('Awesome'))
print(text.endswith('challenge'))
print('100daysofcode' in text.lower())
print(text.replace('100', '200'))
print(re.search(r'I am', text))
print(re.match(r'I am', text))
print(re.match(r'Awesome.*challenge', text))

text = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been
the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and
scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into
electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus
PageMaker including versions of Lorem Ipsum"""
cnt = Counter(re.findall(r'[A-Z][a-z0-9]+', text))
print(cnt.most_common(5))
