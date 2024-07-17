s=[int(x) for x in open('17_2.txt')]
c=[]
b=[]
for i in range(len(s)-2):
    if str(s[i])[-1]==str(s[i+2])[-1] and str(s[i])[0]!=str(s[i+1])[0]:
        if (s[i]<0)+(s[i+1]<0)+(s[i+2]<0)==1:
            c.append(s[i]+s[i+1]+s[i+2])
        if s[i]>0 and s[i+1]>0 and s[i+2]>0:
            b.append(s[i]+s[i+1]+s[i+2])
print(len(c),sum(b))
