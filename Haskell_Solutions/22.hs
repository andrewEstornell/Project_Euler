main :: IO()
main = do
    let abs = filter is_abundant [12,13..28123]
    putStrLn$show$length$abs
    putStrLn$show$sum(filter (is_not_ab_sum abs) [12,13..28123])

is_abundant :: Int -> Bool
is_abundant 1 = False
is_abundant n = sum(facts ++ [n `div` x | x <- facts , x < floor(sqrt(fromIntegral n))]) > n
    where facts = [x | x<-[1..floor(sqrt(fromIntegral(n-1)))], n `mod` x == 0]

is_not_ab_sum :: [Int]-> Int -> Bool
is_not_ab_sum abs n = null [(a, b) | a<-fil_abs, b<-fil_abs, a + b == n]
    where fil_abs = (filter (< n - 12) abs)