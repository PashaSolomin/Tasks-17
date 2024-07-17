s=[int(x) for x in open('17_1.txt')]
b=[]
for i in range(len(s)-1):
    if (s[i]<0)+(s[i+1]<0)==1 and \
       ((abs(s[i])%2==0 and abs(s[i+1])%2==0) or (abs(s[i])%2!=0 and abs(s[i+1])%2!=0)):
        b.append(s[i]+s[i+1])
print(len(b),int(sum(b)/len(b)))
