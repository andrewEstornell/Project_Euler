main :: IO()
main = do
    let lar = largest_length 1000000 1 0 0
    putStrLn$show$lar
    --putStrLn$show$colatz lar

largest_length :: Int -> Int -> Int -> Int -> Int
largest_length ub n ll ln
    | n > ub = ln
    | cl > ll   = largest_length ub (n + 1) cl n
    | otherwise = largest_length ub (n + 1) ll ln
        where cl = colatz_length n 0

colatz_length :: (Integral a) => a -> a -> a
colatz_length 1 n       = n + 1
colatz_length a n
    | even a = colatz_length (a `div` 2) (n + 1)
    | odd  a = colatz_length (3 * a + 1) (n + 1)

colatz :: (Integral a) => a -> [a]
colatz 1 = [1]
colatz n
    | even n = n : colatz (n `div` 2)
    | odd  n = n : colatz (3 * n + 1) 

