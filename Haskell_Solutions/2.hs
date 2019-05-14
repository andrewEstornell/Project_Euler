main :: IO()
main = do
    putStrLn$show$sum$[x | x <- gen_fib$1000, x < 4000000, x `mod` 2 == 0]


gen_fib :: Int -> [Integer]
gen_fib 0 = []
gen_fib 1 = [1]
gen_fib 2 = [1, 1]
gen_fib n = x + y : l
    where l@(x:y:xs) = gen_fib(n - 1)
