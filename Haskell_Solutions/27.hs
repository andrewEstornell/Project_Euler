import Data.List

main :: IO()
main = do
    putStrLn$show$prime_length [poly 1 41 x | x<-[1..]]




is_prime :: Int -> Bool
is_prime n = n > 1 && null [() | x<-[2,3..sqt], n `mod` x == 0]
    where sqt = floor(sqrt(fromIntegral(n)))


poly :: Int -> Int -> Int -> Int
poly a b x = x^2 + a*x + b

prime_length :: [Int] -> Int
prime_length ps = length$(takeWhile is_prime ps)