import wikipedia

pages = ['Orange (fruit)', 'Banana', 'Pear', 'Watermelon', 'Apple (fruit)', 'Cambodia', 'New York City', 'Palestine (Region)', 'Nicaragua', 'Cosovo']
for p in pages:
    wiki = wikipedia.page(p)
    print(f'\t{wiki.title} \n {wiki.summary}\n\n\n')