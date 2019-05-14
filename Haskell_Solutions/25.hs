main :: IO()
main = do
    putStrLn$show(fib_list (10^1000) 1 2 0)




fib_list :: Integer -> Integer -> Integer -> Int -> Int
fib_list l f1 f2 i
    | f2 < l  = fib_list l f2 (f1 + f2) (i + 1)
    | f2 >= l = i - 2