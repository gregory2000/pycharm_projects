def a(x):
   return x + 1

def b(x):
   return x + 1.0

def c(x, y):
   return x + y

def e(x, y, z):
   return x >= y and x <= z

def f(x, y):
   x + y - 2

if __name__ == "__main__":
   print e(a(3), b(4), c(3, 4))
   print f