import random
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap

@timing
def m(A, p, q, r):
  lenL = q - p + 1
  lenR = r - q
  L = [0] * (lenL + 1)
  R = [0] * (lenR + 1)
  for i in range(lenL):
    L[i] = A[p + i]
  for i in range(lenR):
    R[i] = A[q + i + 1]
  L[lenL] = R[lenR] =  float("inf") # sentinel
  i = j = 0
  for k in range(p, r):
    if L[i] <= R[j]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      j += 1
  return A

@timing
def m2(L, R):
  o = []
  a = 0
  b = 0
  for i in range(len(L) + len(R)):
    if a >= len(L):
      o.append(R[b])
      b += 1
      continue
    if b >= len(R):
      o.append(L[a])
      b += 1
      continue
    if L[a] >= R[b]:
      o.append(R[b])
      b += 1
    else:
      o.append(L[a])
      a += 1
  return o

n = 500000
l = sorted([random.randint(0, 1000) for r in xrange(n)])
r = sorted([random.randint(0, 1000) for r in xrange(n)])
c = l + r
m(c, 0, n - 1, n * 2 - 1)
m2(l, r)
