main :: IO()
main = do
    putStrLn$show$sum$integer_digits$factorial 100


integer_digits :: Integer -> [Int]
integer_digits a = [read(x:[]) | x<-(show(a))]

factorial :: Integer -> Integer
factorial 1 = 1
factorial n = n * factorial(n - 1)