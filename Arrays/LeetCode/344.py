s1='Amor'
s2='Sutil'

def reverse_tp(s):
    # two pointers
    s=list(s)
    n=len(s)-1
    for i in range(n//2+1):
        s[i],s[n-i]=s[n-i],s[i]
    return ''.join(s)

def reverse_bitwise(s):
    # bitwise approach
    s=list(s)
    n=len(s)-1
    for i in range(n//2+1):
        s[i],s[~i]=s[~i],s[i]
    return ''.join(s)
print(reverse_tp(s1),reverse_tp(s2))
print('FIM')
print(reverse_bitwise(s1),reverse_bitwise(s2))
