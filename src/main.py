def add(a, b, c=0):
   if not isinstance(a, (int, float)):
       return -1
   if not isinstance(b, (int, float)):
       return -1
   if not isinstance(c, (int, float)):
       return -1
   if not (0 <= a <= 10):
       return -2
   if not (0 <= b <= 10):
       return -2
   if not (0 <= c <= 10):
       return -2
   return a + b + c
