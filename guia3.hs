-- 1.a
f1 :: Integer -> Integer
f1 n | n == 1 = 8
     | n == 4 = 131
     | n == 16 = 16
     | otherwise = 0

-- 1.b
g1 :: Integer -> Integer
g1 n | n == 8 = 16
     | n == 16 = 4
     | n == 131 = 1
     | otherwise = 0

-- 1.c
h1 :: Integer -> Integer
h1 n = f1 ( g1 n)

k1 :: Integer -> Integer
k1 n = g1 (f1 n)

--2.a
absoluto :: Integer -> Integer
absoluto n | n >= 0 = n
            | otherwise = -(n)

--2.b
maximoAbsoluto :: Integer -> Integer -> Integer
maximoAbsoluto n1 n2 | absoluto n1 > absoluto n2 = absoluto n1
                    | otherwise = absoluto n2

--2.c
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 n1 n2 n3 | (n2 > n1) && (n2 > n3) = n2
                 | (n3 > n2) && (n3 > n1) = n3
                 | otherwise = n1

--2.d
algunoEs0 :: Integer -> Integer -> Bool
algunoEs0 n1 n2 = (n1 == 0) || (n2 == 0)

--2.e
ambosSon0 :: Integer -> Integer -> Bool
ambosSon0 n1 n2 = (n1 == n2) && (n1 == 0)

--2.f
mismoIntervalo :: Integer -> Integer -> Bool
mismoIntervalo n1 n2 | (n1 <= 3) && (n2 <=3) = True
                        | (n1 <= 7) && (n2 <= 7) && (n1 > 3) && (n2 > 3) = True
                        | (n1 > 7) && (n2 > 7) = True
                        | otherwise = False

--2.g
sonDistintos :: Integer -> Integer -> Bool
sonDistintos n1 n2 = (n1 /= n2)

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos n1 n2 n3 | (sonDistintos n1 n2) && (sonDistintos n1 n3) = n1 + n2 + n3
                       | (sonDistintos n1 n3) = n1 + n3
                       | (sonDistintos n1 n2) = n1 + n2
                       | otherwise = n1

--2.h
esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe n1 n2 = ((mod n1 n2) == 0)

--2.i
digitoUnidades :: Integer -> Integer
digitoUnidades n = mod n 10

--2.j
digitoDecenas :: Integer -> Integer
digitoDecenas n = div (mod n 100) 10

--3
estanRelacionados :: Integer -> Integer -> Bool
{-El enunciado dice que a y b se relacionan si y solo si 
existe un k entero tal que (a*a)+(a*b*k) = 0 y la unica 
manera de que k sea entero es si b es divisor de a-}
estanRelacionados a b = (mod a b) == 0
                      

--4.a
prodInt :: (Float, Float) -> (Float, Float) -> (Float, Float)
prodInt (a, b) (c, d) = (a * c, b * d)

--4.b
todoMenor :: (Float, Float ) -> (Float, Float) -> Bool
todoMenor (a,b) (c,d) | a < c && b < d = True
                      |otherwise = False

--4.c
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float
distanciaPuntos (a,b) (c,d) = ((c-a) * (d-b)) / 2  

--4.d
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a,b,c) = a + b + c

--4.e
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer
sumarSoloMultiplos (a,b,c) d | d < 0 = 0
                             | ((mod a d == 0) && (mod b d == 0)) && (mod c d == 0) = a + b + c
                             | (mod b d == 0) && (mod c d == 0) = b + c
                             | (mod a d == 0) && (mod c d == 0) = a + c
                             | (mod a d == 0) && (mod b d == 0) = a + b
                             | (mod c d == 0) = c
                             | (mod b d == 0) = b
                             | (mod a d == 0) = a

--4.f
posPrimerPar :: (Integer, Integer, Integer) -> Integer
posPrimerPar (a, b, c) | mod a 2 == 0 = 1
                       | mod b 2 == 0 = 2
                       | mod c 2 == 0 = 3
                       |otherwise = 4

--4.g
crearPar :: t -> t -> (t,t)
crearPar a b = (a,b)

--4.h
invertir :: (t,t) -> (t,t)
invertir (a,b) = (b,a)


-----5)

f :: Integer -> Integer
f n | n <= 7 = n*n
    | n > 7 = (2*n) + 1

g :: Integer -> Integer
g n | mod n 2 == 0 = (div n 2)
    | otherwise = (3*n) + 1

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (a,b,c) | (f(a) > g(a)) && (f(b) > g(b)) && (f(c) > g(c)) = True
                     | otherwise = False


-----6)

bisiesto :: Integer -> Bool 
bisiesto x | mod x 4 == 0 = False
           | (mod x 100 == 0) && (mod x 400 /= 0) = False
           | otherwise = True


-----7)
distanciaManhattan:: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (a,b,c) (d,e,f) = abs ((a-d) + (b-e) + (c-f))


-----8)
sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = (mod x 10) + (mod x 100)

comparar :: Integer -> Integer -> Integer
comparar a b | (sumaUltimosDosDigitos (a)) < (sumaUltimosDosDigitos (b)) = 1
             | (sumaUltimosDosDigitos (a)) > (sumaUltimosDosDigitos (b)) = (-1)
             | otherwise = 0



