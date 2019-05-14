main :: IO()
main = do
    putStrLn$show$sum(filter (is_amicable [1..10000]))


is_amicable :: Int -> Bool
is_amicable n
    | n == dn   = False
    | n == ddn  = True
    | otherwise = False
        where dn  = sum$prop_divs n
              ddn = sum$prop_divs$dn


prop_divs :: Int -> [Int]
prop_divs 1 = []
prop_divs n = [x | x <- [1..(n-1)], n `mod` x == 0]
