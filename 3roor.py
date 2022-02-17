import numpy as np
def itermethods(x,es,maxit):
  i = 0
  sum = 0
  cur_approx = 0
  sign = -1


  while True:
    sign *=  -1
    prev_approx = cur_approx
    sum = sum + sign* x**i/np.math.factorial(i)

    cur_approx = sum
    if cur_approx != 0:

      ea = abs((cur_approx - prev_approx)/cur_approx)

    if ea <= es or i >= maxit:
      break
    i = i + 2
  return cur_approx , ea

if __name__ == '__main__':
  n = 3
  es = (0.5 * 10**(2-n))/100
  print(es)
  x = 0.25
  maxit = 10
  approx_result, ea = itermethods(x,es,maxit)
  f=lambda x:np.cos(x)
  print('True Cox(x) = ' , f(x) , "approx cos(X) = ", approx_result , "ea" , ea )
