main :: IO()
main = do
    putStrLn$show$sum$filter is_prime [1..2000000]

prime_list :: Int -> [Int]
prime_list ub = prime_list_helper ub 3 [2]


prime_list_helper :: Int -> Int -> [Int] -> [Int]
prime_list_helper ub p pl
    | ub < p                           = pl
    | and$map (/=0) (map (p `mod`) pl) = prime_list_helper ub (p + 2) (p:pl)
    | otherwise                        = prime_list_helper ub (p + 2) pl

is_prime :: Integer -> Bool
is_prime p = p > 1 && null[() | k <- [2..floor(sqrt(fromIntegral(p)))], p `mod` k == 0]
