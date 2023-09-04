--estanRelacionados :: Integer -> Integer -> Bool

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



