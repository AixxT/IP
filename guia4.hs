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

----11.a)
factorial :: Integer -> Float
factorial n | n == 0 = 1.0
            | otherwise = fromIntegral n * factorial (n-1)

eAprox :: Integer -> Float
eAprox n | n == 0 = ( 1 / factorial 0 )
         | otherwise =  1 / (factorial n) + (eAprox (n-1))

----11.b)
e = eAprox 9

----12)
sucesionA :: Integer -> Float
sucesionA n | n == 1 = 2
            | otherwise = 2 + (1 / (sucesionA (n-1)))

raizDe2Aprox :: Integer -> Float
raizDe2Aprox n = sucesionA n - 1

----13)
sumatoriaMesima :: Integer -> Integer -> Integer
sumatoriaMesima m i | m == 1 = i
                    | i == 1 = 1 * m
                    | otherwise = i ^ m + (sumatoriaMesima(m-1) i)

dobleSumatoria :: Integer -> Integer -> Integer
dobleSumatoria n m | n == 1 = sumatoriaMesima m 1
                   | otherwise = sumatoriaMesima m n + dobleSumatoria (n-1) m

----14)
potenciasDeM :: Integer -> Integer -> Integer
potenciasDeM q m | q == 1 = 1 * m 
                 | m == 1 = q
                 | otherwise = q ^ m + potenciasDeM q (m-1)

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = (potenciasDeM q m ) * (potenciasDeM q n)

----15)
sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m | n == 1 = sumaRacionalesM 1 m 
                   | otherwise = sumaRacionalesM n m + sumaRacionales (n-1) m

sumaRacionalesM :: Integer -> Integer -> Float
sumaRacionalesM n m | m == 1 = fromIntegral n
                      | otherwise = fromIntegral n / fromIntegral m + sumaRacionalesM n (m-1)

----16)                     







