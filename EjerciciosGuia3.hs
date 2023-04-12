
------------------------------------- Ejercicio 1 -------------------------------------
--a)
f :: Integer -> Integer

f n | n == 1 = 8
    | n == 4 = 131
    | n == 16 = 16

--b)
g :: Integer -> Integer

g n | n == 8 = 16
    | n == 16 = 4
    | n == 131 = 1

--c)
h :: Integer -> Integer
k :: Integer -> Integer

h n = g (f n)  --Pongo parentesis para que Haskell priorize hace f(n) antes que g(n)
k n = (f.g) n  -- La composicion de funciones se puede escribir de esta forma tambien ya que es una funcion interna de Haskell



------------------------------------- Ejercicio 2 -------------------------------------

--a)
valorAbsoluto :: Integer -> Integer
--forma1
valorAbsoluto n = abs n    --Para los valores negativos los escribimos entre parentesis ej: -4 es (-4)
--forma2
--valorAbsoluto x | x > 0 = x
--                | otherwise = -x

--b)
maximoAbsoluto :: Integer -> Integer -> Integer

maximoAbsoluto x y | (abs x) > (abs y) = abs x
                   | (abs y) > (abs x) = abs y
                   | otherwise = x

--c)
maximo3 :: Integer -> Integer -> Integer -> Integer

maximo3 x y z | x > y && x > z = x
              | y > x && y > z = y
              | otherwise = z

--d)
algunoEs0 :: Float -> Float -> Bool
--algunoEs0 x y = x == 0 || y == 0

--forma pattern matching
algunoEs0 0 _ = True
algunoEs0 _ 0 = True
algunoEs0 _ _ = False


--e)
ambosSon0 :: Float -> Float -> Bool

--ambosSon0 x y = (x == 0 && y == 0)

--forma pattern matching
ambosSon0 0 0 = True 
ambosSon0 _ _ = False

--f)
mismoIntervalo :: Float -> Float -> Bool

mismoIntervalo x y = (x <= 3 && y <= 3) || ((x > 3 && x <= 7) && (y > 3 && y <= 7)) || (x > 7 && y > 7)

--g)
sumaDistintos :: Integer -> Integer -> Integer -> Integer

sumaDistintos x y z | (x == y) && (x == z) = x
                    | (x == z) = x + y
                    | (x == y) = x + z
                    | (z == y) = x + z
                    | otherwise = x + y + z

--h)
esMultiploDe :: Integer -> Integer -> Bool

esMultiploDe x y = (mod y x) == 0

--i)
digitoUnidades :: Integer -> Integer

digitoUnidades x = (mod x 10)

--j)
digitoDecenas :: Integer -> Integer

digitoDecenas x = div ((mod x 100) - (mod x 10)) 10




------------------------------------- Ejercicio 3 -------------------------------------

estanRelacionados :: Integer -> Integer -> Bool

estanRelacionados x y = mod (-x) y == 0 --Para que esten relacionados el resto de hacer x dividido y debe dar 0 (sirve para positivos y negativos tmb)

--Tomi's way
--estanRelacionados x y = x * x + x * y * (div (-x) y) == 0

-- lo que esta en el requiere del ejercicio lo debo poner?



------------------------------------- Ejercicio 4 -------------------------------------

--a)
prodInt :: (Float,Float) -> (Float,Float) -> (Float,Float)

prodInt (x1,x2) (y1,y2) = (x1 * y1, x2 * y2) --preguntar si hacelo asi esta bien o lo tengo que hacer usando fst, snd como Tomi?

--Tomi's way
--prodInt :: (Float, Float) -> (Float, Float) -> Float 
--prodInt tuplaUno tuplaDos = (fst tuplaUno * fst tuplaDos) + (snd tuplaUno * snd tuplaDos)

--b)
todoMenor :: (Float,Float) -> (Float,Float) -> Bool

todoMenor (x1,x2) (y1,y2) = (x1 < y1) && (x2 < y2) --preguntar si hacelo asi esta bien o lo tengo que hacer usando fst, snd como Tomi?

--Tomi's way
--todoMenor t1 t2 = fst t1 < fst t2 && snd t1 < snd t2

--c)
distanciaPuntos :: (Float, Float) -> (Float, Float) -> Float 

distanciaPuntos (x1,x2) (y1,y2) = sqrt ((y1 - x1) ** 2 + (y2 - x2) ** 2) 

--Tomi's way
--distanciaPuntos t1 t2 = sqrt((fst t2 - fst t1)^2 + (snd t2 - snd t1)^2)

--d)
sumaTerna :: (Integer, Integer, Integer) -> Integer

sumaTerna (x1,x2,x3) = x1 + x2 + x3

--e)
sumarSoloMultiplos :: (Integer, Integer, Integer) -> Integer -> Integer

--sumarSoloMultiplos (x1,x2,x3) y | ((mod x1 y) + (mod x2 y) + (mod x3 y) == 0) = x1 + x2 + x3
  --                              | ((mod x1 y) + (mod x2 y) == 0) = x1 + x2
    --                            | ((mod x1 y) + (mod x3 y) == 0) = x1 + x3
      --                          | ((mod x2 y) + (mod x3 y) == 0) = x2 + x3
        --                        | (mod x1 y == 0) = x1
          --                      | (mod x2 y == 0) = x2
            --                    | (mod x3 y == 0) = x3
              --                  | otherwise = 0

--Tomi's Way
sumarSoloMultiplos (x, y, z) n = sum[actualNumber | actualNumber <- [x, y, z], esMultiploDe actualNumber n]

--f) 
posPrimerPar :: (Integer,Integer,Integer) -> Integer

posPrimerPar (x1,x2,x3) | (mod x1 2 == 0) = x1
                        | (mod x2 2 == 0) = x2
                        | (mod x3 2 == 0) = x3
                        | otherwise = 4

--g)
crearPar :: tx -> ty -> (tx,ty)  --las entradas char requieren de esto ' ' o " " y los valores booleanos empiezan con mayuscula
crearPar x y = (x,y)

--h)
invertir :: (tx, ty) -> (ty, tx)
invertir (x, y) = (y, x)


------------------------------------- Ejercicio 5 -------------------------------------

todosMenores :: (Integer, Integer, Integer) -> Bool
todosMenores (x1,x2,x3) = ((funF x1 > funG x1) && (funF x2 > funG x2) && (funF x3 > funG x3))

funF :: Integer -> Integer
funF x | (x <= 7) = x ^ 2  --elevar un numero usando Integers requiere del ^ y no del ** (sirve para floats)
       | otherwise = 2 * x - 1

funG :: Integer -> Integer
funG x | esPar = div x 2
       | otherwise = 3 * x + 1
       where esPar = mod x 2 == 0

{-
    Se envia en orden un valor de la tupla a las funciones f y g, y si los valores de n mutados con f son mayores a los de g vuelve true.
    Ej: (4, 4, 9)
        (16 > 2) && (16 > 2) && (17 > 28) -- Retornaría false.
    Ej 2: (1, 1, 1)
        (1 > 4) -- Como la primera no se cumple el resultado sería false. Haskell es perezoso y evalúa condición por condición de izquierda a derecha.
    Ej 3: (3, 1, 4)
        (9 > 10) -- Como la primera no se cumple el resultado sería false.
    Ej 4: (4, 4, 2)
        (16 > 2) && (16 > 2) && (4 > 1) -- Retornaría true. Todas se cumplen
-}



------------------------------------- Ejercicio 6 -------------------------------------

bisiesto :: Integer -> Bool
bisiesto x | not (esMultiplo x 4) || (esMultiplo x 100 && not (esMultiplo x 400)) = False
           | otherwise = True

esMultiplo :: Integer -> Integer -> Bool
esMultiplo x y = mod x y == 0

------------------------------------- Ejercicio 7 -------------------------------------

distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = abs ((x1 - y1) + (x2 - y2) + (x3 - y3))

------------------------------------- Ejercicio 8 -------------------------------------

comparar :: Integer -> Integer -> Integer

comparar x y | sumaUltimosDosDigitos x < sumaUltimosDosDigitos y = 1
             | sumaUltimosDosDigitos x > sumaUltimosDosDigitos y = -1
             | sumaUltimosDosDigitos x == sumaUltimosDosDigitos y = 0

sumaUltimosDosDigitos :: Integer -> Integer
sumaUltimosDosDigitos x = mod x 10 + div ((mod x 100) - (mod x 10)) 10

