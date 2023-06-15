ls = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
deger=[]
def func(a):
   if type(a) == list:
      for i in a:
         func(i)
   else:
      global deger
      deger.append(a)
func(ls)
print(deger)