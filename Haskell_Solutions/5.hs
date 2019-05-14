main :: IO()
main = do
    putStrLn$show$head(filter is_div [1,2..])

is_div :: Int -> Bool
is_div a =  and $ map (==0) (map (a `mod`) [1..20]) 