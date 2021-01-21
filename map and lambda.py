# def fibonacci(nterms):
#     a = 0
#     b = 1
#     l = []

#     if nterms == 0:
#         pass
#     elif nterms == 1:
#         l.append(a)

#     else:
#         l.append(a)
#         l.append(b)
#         for i in range(2, nterms):
#             c = a + b
#             a = b
#             b = c
#             l.append(c)
#         return l 


# cube = lambda x: x**3


# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))
# Program to find whether given input string has balanced brackets or not
def isBalanced(s):
    a = []
    for i in range(len(s)):
        if s[i] in ['{', '[', '(']:
            a.append(s[i])
        if s[i] == '}':
            if a:
                if a[-1] == '{':
                    a.pop()
                else:
                    break
            else:
                return "NO"
        if s[i] == ']':
            if a:
                if a[-1] == '[':
                    a.pop()
                else:
                    break
            else:
                return "NO"
        if s[i] == ')':
            if a:
                if a[-1] == '(':
                    a.pop()
                else:
                    break
            else:
                return "NO"
    if a:
        return "NO"

    else:
        return "YES"


inp = input('Enter your query string: ')
#sample input: {)[](}]}]}))}(())(

print(isBalanced(inp))
