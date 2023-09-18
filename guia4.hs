----1)
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci (n-2)

----2)
parteEntera :: Float -> Integer
parteEntera x | (x >= 0) = round x
              | otherwise = -(parteEntera (-x) - 1)

----3)
esDivisible :: Integer -> Integer -> Bool
esDivisible a b | (a - b == 0) = True
                | (a - b < 0) = False
                | otherwise = (esDivisible (a-b) b)

----4)
nesimoImpar :: Integer -> Integer
nesimoImpar n | n == 1 = 1
              | otherwise = (nesimoImpar (n-1) + 2)

sumaImpares :: Integer -> Integer
sumaImpares n | n == 1 = nesimoImpar 1
              | otherwise = sumaImpares (n-1) + nesimoImpar n

----5)
medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n-2)

----6)
sumaDigitos :: Integer -> Integer
sumaDigitos n | (n >= 0) && (n <= 9) = n
              | otherwise = sumaDigitos (mod n 10) + sumaDigitos (div n 10)

----7)
todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | (n >= 0) && (n <= 9) = True
                      | otherwise = ((mod n 10) == mod (div n 10) 10) && todosDigitosIguales (div n 10)

----8)
cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == 1 = n
                 | otherwise = iesimoDigito (mod (div n (10^(i-1))) 10) i

----9)
esCapicua :: Integer -> Bool
esCapicua n | (cantDigitos n) == 1 = True
            | otherwise = ((iesimoDigito n 1) == (iesimoDigito n (cantDigitos n))) && esCapicua (mod (div n 10) (10^((cantDigitos (div n 10))-1)))

----10.a)
f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = (2^n) + (f1(n-1))

----10.b)
f2 :: Integer -> Float -> Float
f2 n q | n == 1 = q
       | otherwise = (q^n) + (f2(n-1) q)

----10.c)
f3 :: Integer -> Float -> Float
f3 n q | n == 0 = q
       | otherwise = (q^(2*n)) + (f3(n-1) q)

----10.d)
f4 :: Integer -> Float -> Float
f4 n q | n == 0 = q
       | otherwise = (q^(2*n)) + (f4(n-1) q) - (f2 n q)



