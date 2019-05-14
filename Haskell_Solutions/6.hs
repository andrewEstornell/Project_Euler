main :: IO()
main = do
    let sum_square = foldl (+) 0 (map (^2) [1,2..100])
    let square_sum = (foldl (+) 0 [1,2..100])^2
    putStrLn$show(square_sum - sum_square)