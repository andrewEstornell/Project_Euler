main :: IO()
main = do
    putStrLn$show$head$prime_list 10001


prime_list :: Int -> [Int]
prime_list n = prime_list_helper n 2 []

prime_list_helper ::  Int -> Int -> [Int] -> [Int]
prime_list_helper 0 _ l = l
prime_list_helper n p l
    | and $ map (/=0) (map (p `mod`) l) = prime_list_helper (n - 1) (p + 1) (p : l)
    | otherwise         = prime_list_helper n (p + 1) l