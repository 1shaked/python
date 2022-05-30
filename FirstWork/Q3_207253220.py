import string
def solve(A: list) -> int:
    counter = len(string.ascii_lowercase)
    word_dict = {}
    for letter in string.ascii_lowercase:
        word_dict[letter] = 1
    
    totalString = ''.join(A)
    for letter in totalString:
        if letter in word_dict and word_dict[letter] == 1:
            counter -= 1
            word_dict[letter] = 0
        if counter == 0:
            return 1
    return int(counter == 0 )


if __name__ == '__main__':

    A = ["the", "quick", "brown", "fox", "jumps", "over", "the","2" "lazy", "dogs!"]
    print(solve(A))
    
    A = ["fox", "jumps", "over", "the" "lzy", "dogs!"]
    print(solve(A))
    