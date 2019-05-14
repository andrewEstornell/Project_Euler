main :: IO()
main = do
    putStrLn$show$head$ filter le_num_divs (map triangle_number [1..])
    --putStrLn$show$last$takeWhile(le_num_divs) (map triangle_number [1..])

num_divs :: Int -> Int
num_divs n = 2 * length [x | x<-[1..floor(sqrt(fromIntegral n))], n `mod` x == 0]

triangle_number :: Int -> Int
triangle_number n = sum [1..n]

le_num_divs :: Int -> Bool
le_num_divs n = (num_divs n) > 500

