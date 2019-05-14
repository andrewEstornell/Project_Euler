main :: IO()
main = do
    putStrLn$show$sum$integer_digits(2^1000)


integer_digits :: Integer -> [Int]
integer_digits a = [read(x:[]) | x<-(show(a))]