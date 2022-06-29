def parni(n):
    for i in range (n):
        if i%2==0:
            yield i
            
def neparni(x):
    for i in range (x):
        if i%2==1:
            yield i


par=parni(30)
nepar=neparni(20)

print(next(par))
print(next(par))
print(next(par))
print(next(par))

print(next(nepar))
print(next(nepar))
print(next(nepar))
print(next(nepar))
