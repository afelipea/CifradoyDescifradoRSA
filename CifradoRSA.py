import random
import numpy as np

#1) pick 2 large prime numbers q1 and q2
def Q():
  q1= random.randint(500, 1000)
  q2= random.randint(500,1000)
  a = [0] * 2
  a[0] = q1
  a[1] = q2
  return a

def isPrime(num):
  if(num <= 3):
    return num > 1 #this checks if the number is 2 or 3
  elif num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while(i*i <= num):
    if num%i==0 or num%(i+2)==0:
      return False
    i = 6 + i
  return True

def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

ar = Q()
while(isPrime(ar[0]) == False or isPrime(ar[1])== False):
  ar = Q()

#Now you have both numbers, find p
p = random.randint(1,500)

while(computeGCD(p,ar[0]-1) != 1 or computeGCD(p,ar[1]-1) != 1):
  #they are not co-primes look again
  p = random.randint(1,500)

#Now you have p, define n, x, public Key and private key
n = ar[0] * ar[1]
y = (ar[0]-1)*(ar[1]-1)
x = 0
while((x*p)%y != 1):
  x = x + 1


publicKey= [p,n]
privateKey = [ar[0], ar[1], x]
message = input("Enter a number that will be your message: ")
encryptedMessage  = (int(message)**p)%n

print ("This is your encrypted message: ", encryptedMessage)
print("This is your private key: ", privateKey[2])
print("This is your public key: ", publicKey)
print("The first element is p and the second one n\nRemember, don't give your private key to anyone!\nHave fun!")
