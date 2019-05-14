main :: IO()
main = do
    putStrLn$show$last$gen_prime_factors(600851475143)
    --putStrLn$show$fromInteger$toInteger$5

gen_prime_factors :: Int -> [Int]
gen_prime_factors n = [x | x <- [2,3..round$sqrt(ub)], (n `mod` x) == 0, is_prime x (x - 1)]
    where ub = fromIntegral$n

is_prime :: Int -> Int -> Bool
is_prime n m
        | m == 1 = True
        | n `mod` m == 0 = False
        | otherwise = is_prime n (m - 1)