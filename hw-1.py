s = input(':')

def palindrom(s):
    if len(s) % 2 != 0:
        return False
    else:
        if s[:len(s)//2] == s[:len(s)//2 - 1:-1]:
            return True
        else:
            return False



print(palindrom(s))
print(palindrom('лепсспел'))