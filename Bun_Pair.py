a=list(map(int,input().split()))
count=1
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if(a[i]==a[j]):
      count+=1
print(count-1)
