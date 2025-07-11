
num=(1,2,3,1,1,2,2,2,3,3,33,3,3,5,8,9,8,6)

n=set()
seen=set(
)
for i in num:
    if i in seen:
        n.add(i)
    else:
        print(seen.add(i))



        

print(n)