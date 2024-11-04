pnone_book = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print(pnone_book)

print(pnone_book['Masha'])
print(pnone_book.get('Arseni'))

pnone_book.update({'Kamila': 1981, 'Artem': 1915})
print(pnone_book)

a = pnone_book.pop('Egor')
print(a)
print(pnone_book)

my_set = {1, 'Яблоко', 42.314, 1, 'Яблоко', 42.314}
print(my_set)

my_set.update((5, 6, 1.6))
print(my_set)
