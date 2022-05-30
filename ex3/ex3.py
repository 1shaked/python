def permutations(iterable, starter='', into=[]):
    if len(iterable) == 1:
        full_permutation = f'{starter}{iterable}'
        into.append(tuple([l for l in full_permutation]))
        return iterable
    for index,letter in enumerate(iterable):
        remainString = iterable[:index] + iterable[index+ 1:: ]
        starter_str = f'{starter}{letter}'
        permutations(remainString, starter_str, into)
        
    return into


s = 'abc'


pr = permutations('abcd')
print(pr)