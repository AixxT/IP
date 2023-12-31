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

----16.a)                     
menorDivisor :: Integer -> Integer
menorDivisor n = menorDivisorAux n 2

menorDivisorAux :: Integer -> Integer -> Integer
menorDivisorAux n m | mod n m == 0 = m 
                    | otherwise = menorDivisorAux n (m+1)

----16.b)
esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

----16.c)
sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m | esPrimo n && esPrimo m = True
                | n < m = sonCoprimosAux n m n
                | m < n = sonCoprimosAux n m m
                | otherwise = False

sonCoprimosAux :: Integer -> Integer -> Integer -> Bool
sonCoprimosAux n m q | mayorComunDivisor n m q /= 1 = False
                     | otherwise = True

mayorComunDivisor :: Integer -> Integer -> Integer -> Integer
mayorComunDivisor n m q | mod n q == 0 && mod m q == 0 = q
                        | otherwise = mayorComunDivisor n m (q-1)

----16.d) preguntar
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoAux n 2 0 -- i = 2 porque se considera a 2 como el primer primo

nEsimoPrimoAux :: Integer -> Integer -> Integer -> Integer
nEsimoPrimoAux n i k | n == k = i-1 -- k cuenta la cantidad de primos que se encuentra durante las recursiones, por eso termina cuando k = n
                     | esPrimo i = nEsimoPrimoAux n (i+1) (k+1) --si i es primo suma 1 al contador (k) y al i que avanza por los num naturales
                     | otherwise = nEsimoPrimoAux n (i+1) k -- si i no es primo suma 1 hasta encontrar el siguiente primo                   


----17)
esFibonacci :: Integer -> Bool
esFibonacci n = esFibonacciAux n 0

esFibonacciAux :: Integer -> Integer -> Bool
esFibonacciAux n k | n == fibonacci k = True  -- k es un contador de recursiones que se utiliza para avanzar en la sec. fibonacci
                   | (fibonacci k) > n = False -- cuando el valor k-esimo de la secuencia fibonacci es MAYOR que n significa que n no pertenece a la secuencia
                   | otherwise = esFibonacciAux n (k+1) -- suma 1 a k hasta encontrar la igualdad o la superación del valor n


----18)
mayorDigitoPar :: Integer -> Integer
mayorDigitoPar n = mayorDigitoParAux n 0

mayorDigitoParAux :: Integer -> Integer -> Integer --
mayorDigitoParAux n i | (n >= 0) && (n < 10) && n > i && esPar n = n
                      | (n >= 0) && (n < 10) = i
                      | esPar (ultimoDigito n) = mayorDigitoParAux (sacarUltimoDigito n) (ultimoDigito n)
                      | otherwise = mayorDigitoParAux (sacarUltimoDigito n) i
-- i mayor digito par

esPar :: Integer -> Bool
esPar n = (mod n 2) == 0

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimoDigito :: Integer -> Integer
sacarUltimoDigito n = div n 10

----19)
esSumaInicialDePrimos :: Integer -> Bool
esSumaInicialDePrimos n = esSumaInicialDePrimosAux n 0 1

esSumaInicialDePrimosAux :: Integer -> Integer -> Integer -> Bool
esSumaInicialDePrimosAux n k i | k == n = True -- Si k = n quiere decir que n pertenece a la suma de primos
                               | k > n = False -- Llegado este caso, significa que la suma de primos (k) alcanzo un valor mayor que n y nunca fue igual a n
                               | otherwise = esSumaInicialDePrimosAux n (sumaPrimosHasta i) (i+1) -- recursión con k(= a la suma) y aumentando i
-- k = contador de la suma de primos
-- i = indice de suma 

sumaPrimosHasta :: Integer -> Integer
sumaPrimosHasta n | n == 1 = 2
                  | otherwise = nEsimoPrimo n + sumaPrimosHasta (n-1)

----20) No entendí la consigna :B

----21)


