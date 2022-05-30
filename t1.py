def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # N = input()
    N = 3
    for i in range(N):
        romanStr = input()
        units = ["I", "II", "III" , 'IV' , 'V', 'VI', 'VII', 'VIII', "IX"]
        tens = ['X', "XX", "XXX", 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['M', 'MM', 'MMM']
        allTypes = [units, tens, hundreds, thousands][::-1]
        isError = False
        lenRom = len(romanStr)
        copy = romanStr
        while len(copy) > 0 and len(allTypes) > 0:
            currentUnit = allTypes[0]
            # check units
            firstNum = copy[0]
            lastTwo = copy[:2]
            last3 = copy[:3]
            last4 = copy[:4]
            isLastTwo = lastTwo in currentUnit and len(lastTwo) == 2
            isLast3 = last3 in currentUnit and len(last3) == 3
            isLast4 = last4 in currentUnit and len(last4) == 4
            
            if (firstNum in currentUnit and not (isLastTwo or isLast3 or isLast4) ):
                copy = copy[1::]
                isError = False
            elif (isLastTwo and not (isLast3 or isLast4) ):
                copy = copy[2::]
                isError = False
            elif (isLast3 and not (isLast4) ):
                copy = copy[3::]
                isError = False
            elif (isLast4):
                copy = copy[4::]
                isError = False
            else:
                
                isError = True
                # copy = ''
            allTypes.pop(0)
        
        if (isError or len(copy) != 0 ):
            print("NO")
        else:
            print("YES")

    return 0

if __name__ == '__main__':
    main()