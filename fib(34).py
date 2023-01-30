import time
def fib(n):
    # starting the time
   startTime = time.time() 
   fi = [0] * (n+1) 
   fi[1] = 1
   for i in range (2,n+1): 
      fi[i] = fi[i-1] + fi[i-2] 
    # ending the time
   endTime = time.time() 
   gameTime = endTime - startTime
   return fi[n], gameTime
   
fibvalue,gameTime = fib(34)
print("fib (34): ",fibvalue, end='\n')
print("Time of fib(34): ",gameTime)
