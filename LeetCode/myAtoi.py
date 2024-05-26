INT_MAX = 2**31 - 1
INT_MIN = -2**31

def myAtoi(str):
    result = 0
    sign = 1
    n = len(str)
    index = 0

    while (index < n and (str[index] == ' ')):
        index += 1

    if index < n and (str[index] == '-' or str[index] == '+'):
        if (str[index] == '-'):
            sign = -1
        index += 1
    
    while index < n and str[index].isdigit():
        digit = int(str[index])
        
        if result > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result *10 + digit
        index += 1
    
    return sign * result

print(myAtoi("+45"))