# hcl_training_tasks
code 1:
```
numbers =  input().split(',')
res=[]
for i in numbers:
    dec = int(i,2)
    if dec%5==0:
        res.append(i)
print(','.join(res))
```

code 2:
```
a = input()
l=0
d=0
for i in a:
    if i.isalpha():
        l+=1
    if i.isdigit():
        d+=1
print("LETTERS :", l)
print("DIGITS :", d)
```
