def addMinimum(word):
        x = word
        sum = 0
        x = x.replace('abc',' ')
        y = x
        while(x != ''):
            x = x.replace('ab',' ',1)
            if y != x:
                sum = sum + 1
                y = x
                continue
            x = x.replace('ac',' ',1)
            if y != x:
                sum = sum + 1
                y = x
                continue
            x = x.replace('bc','  ',1)
            if y != x:
                sum = sum +1
                y = x
                continue
            x = x.replace('a',' ',1)
            if y != x:
                sum = sum +2
                y = x
                continue
            x = x.replace('b',' ',1)
            if y != x:
                sum = sum +2
                y = x
                continue
            x = x.replace('c',' ',1)
            if y != x:
                sum = sum +2
                y = x
                continue
            x = x.replace(' ','')
        return sum


word = "aaa"
print(f"for {word}, minimum steps needed to make it a valid string(according to requirement): {addMinimum(word)}")


word = "aaaabb"
print(f"for {word}, minimum steps needed to make it a valid string(according to requirement): {addMinimum(word)}")