#1
def is_palindrome(s): # строка  - s
    chars = list(s) #разделение символов строки и перенос в список
    print(chars)
    reversed_chars = chars[::-1] #в обратном порядке тот же список
    print(reversed_chars)
    if chars == reversed_chars:
        return True
    else:
        return False

print(is_palindrome("лепсспел"))
print(is_palindrome("hello"))

#2
def is_palidrome2(s): #строка - s
    n = len(s)
    for i in range (n//2):
        if s[i]!= s[n - 1 - i]: #сравнение символов сначала и с конца строки
            return False
    return True
