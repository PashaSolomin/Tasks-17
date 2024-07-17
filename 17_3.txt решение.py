s=[int(y) for y in open('17_3.txt')]
b=[]
def div(x):
    d=set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            d.add(i)
            d.add(x//i)
    return sorted(d)
def dig(z):
    digits=[0]*10
    for i in range(len(str(z))):
        digits[int(str(z)[i])]+=1
    return digits
for t in range(len(s)-1):
    d1=dig(abs(s[t]))
    d2=dig(abs(s[t+1]))
    k=0
    for l in range(10):
        if d1[l]==d2[l] and d1[l]!=0:
            k+=1
    if (k==2)+(len(str(s[t+1]))==len([z for z in div(abs(s[t])) if z%2==0 and 10<=z<=99]))==1:
        b.append(s[t]+s[t+1])
print(len(b),min(b))
