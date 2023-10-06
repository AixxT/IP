----1.1)
longitud :: [t] -> Integer 
longitud [] = 0
longitud (_:xs) = 1 + longitud xs

--1.2)
ultimo :: [t] -> t
ultimo (x:xs) | longitud (x:xs) == 1 = x
              | otherwise = ultimo (xs)

--1.3)
principio :: [t] -> [t]
principio (x:xs) | longitud (x:xs) == 1 = []
                 | otherwise = x : principio xs

--1.4)
reverso :: [t] -> [t]
reverso (x:xs) | longitud (x:xs) == 1 = [x]
               | otherwise = (ultimo (x:xs)) : reverso ( principio (x:xs))


----2)
pertenece :: (Eq t) => t -> [t] -> Bool
{-pertenece n l | (longitud l == 0) = False
              | (n == head l) = True
              | otherwise = pertenece n (tail l)
-}
pertenece n (x:xs) | (longitud (x:xs) == 0) = False
                     | (n == x) = True
                     | otherwise = pertenece n (xs)


--2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales l = todosIgualesAux (head l) l

todosIgualesAux :: (Eq t) => t -> [t] -> Bool
todosIgualesAux e l | (longitud l == 1) && (e == head l) = True
                    | otherwise = ( e == head l) && todosIgualesAux e (tail l)

--2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos (x:xs) | tail xs == [] = True
                      | pertenece x xs = False
                      | otherwise = todosDistintos xs

--2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos (x:xs) | pertenece x xs = True 
                    | tail xs == [] = False
                    | otherwise = hayRepetidos xs

