module Simulacro where

----1)
relacionesValidas :: [(String,String)] -> Bool
relacionesValidas (x:xs) | tuplaValida x && (tail (x:xs) == []) = True
                         | tuplaValida x && (pertenece x xs || pertenece (inverso x) xs) = False                   
                         | otherwise = tuplaValida x && relacionesValidas xs

pertenece :: (Eq t) => t -> [t] -> Bool
pertenece n (x:xs) | n == x = True
                   | tail (x:xs) == [] = False
                   | otherwise = pertenece n xs

inverso :: (String,String) -> (String,String)
inverso (a,b) = (b,a)

tuplaValida :: (String,String) -> Bool
tuplaValida (a,b) = (a /= b)


----2)
personas :: [(String,String)] -> [String]
personas [] = []
personas ((n1,n2):xs) = personasSinRepetidos ( listaPersonas ((n1,n2):xs))

listaPersonas :: [(String,String)] -> [String]
listaPersonas [] = []
listaPersonas ((n1,n2):xs) = n1:n2:listaPersonas xs

personasSinRepetidos :: [String] -> [String]
personasSinRepetidos [] = []
personasSinRepetidos (x:xs) | ((contarRepeticiones x xs 0) >= 1) = personasSinRepetidos xs
                            | otherwise = x:personasSinRepetidos xs

contarRepeticiones :: String -> [String] -> Integer -> Integer
contarRepeticiones _ [] k = k 
contarRepeticiones e (x:xs) k | e == x = contarRepeticiones e xs (k+1)
                              | otherwise = contarRepeticiones e xs k

----3)
amigosDe :: String -> [(String,String)] -> [String]
amigosDe _ [] = []
amigosDe persona ((p1,p2):xs) | (persona == p1) = p2:( amigosDe persona xs)
                              | (persona == p2) = p1:(amigosDe persona xs)
                              | otherwise = amigosDe persona xs

----4)
personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos (x:xs)= personaConMasAmigosAux (listaPersonas (x:xs)) (fst x) 0

personaConMasAmigosAux :: [String] -> String -> Integer -> String
personaConMasAmigosAux [] persona _ = persona
personaConMasAmigosAux (x:xs) persona k | (contarRepeticiones x xs 0) > k = personaConMasAmigosAux xs x (contarRepeticiones x xs 0)
                                        | otherwise = personaConMasAmigosAux xs persona k

