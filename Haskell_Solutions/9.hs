main :: IO()
main = do

    putStrLn$show((\(a, b, c)->(a*b*fromInteger(round(sqrt(fromIntegral(c))))))  (head$filter isTripple [(a, b, (a^2 + b^2)) | a <-[1..1000], b<-[1..1000]]))


isTripple :: (Int, Int, Int) -> Bool
isTripple (a, b, c) = (fromInteger(round(x)) == x) && (a + b + round(x) == 1000)
    where x = sqrt(fromIntegral(c))