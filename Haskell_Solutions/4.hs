main :: IO()
main = do
    putStrLn(show(maximum(filter is_pal (map_mult [100,101..999]))))


map_mult :: [Int] -> [Int]
map_mult [] = []
map_mult (x:xs) = map (*x) [100,101..999] ++ map_mult xs

is_pal :: Int -> Bool
is_pal x = show x == reverse (show x)





