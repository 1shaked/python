def permutations(iterable, starter='', into=[]):
    if len(iterable) == 1:
        full_permutation = f'{starter}{iterable}'
        into.append(tuple([l for l in full_permutation]))
        return iterable
    for index,letter in enumerate(iterable):
        # abc 
        # bc 
        remainString = iterable[:index] + iterable[index+ 1:: ]
        starter_str = f'{starter}{letter}'
        permutations(remainString, starter_str, into)
        
    return into


if __name__ == '__main__':
    s = 'abc'

    # s = 'a' -> a  11


    pr = permutations('abc')
    print(pr)
