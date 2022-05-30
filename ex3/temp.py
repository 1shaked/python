def permute(A):
    return list(permutations(A))
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:

            return


def permutations_list(iterable, r=None):
    print(iterable)
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    res = []
    res.append(tuple(pool[i] for i in indices[:r]))
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                res.append(tuple(pool[i] for i in indices[:r]))
                
        else:

            return
        
    return res


res = permutations_list('ABC')
print(res)

def test(A: str):
    if (len(A) == 1):
        return f'{A},'
    permutations_list: list[str] = []
    for index, s in enumerate(A):
        obj: list[str] = test(A[0 : index : ] + A[index + 1 : :])
        print(obj)
        for element in obj:
            pass


def test(A: str, saved_dict: dict = None):
    if (len(A) == 1):
        return f'{A},'
    totalString = ''
    if saved_dict == None:
        saved_dict = {}
    for index, s in enumerate(A):
        saved_dict[s] = {} 
        remainString = A[0: index] + A[index+1 ::]
        testString = test(remainString)
        totalString += f'{s}{testString}'
