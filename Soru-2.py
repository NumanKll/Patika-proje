ls = [[1, 2], [3, 4], [5, 6, 7]]
def func(a):
   if type(a) == list:
      a.reverse()
      for i in a:
         func(i)
func(ls)
print(ls)