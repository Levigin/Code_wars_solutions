class N:
    def __init__(s,x,y):s.x,s.y=x,y
class value(int):1
for n,o in zip('add sub mul truediv mod pow'.split(),[lambda x,y:x+y,lambda x,y:x-y,lambda x,y:x*y,lambda x,y:x/y,lambda x,y:x%y,lambda x,y:x**y]):
    setattr(__import__(__name__),n,type(n,(N,),{'compute':lambda s,o=o:o(s.x,s.y)}))

a, b = value(5), value(2)

print(add(a, b).compute())
print(sub(a, b).compute())
print(mul(a, b).compute())
print(truediv(a, b).compute())
print(mod(a, b).compute())
print(pow(a, b).compute())

