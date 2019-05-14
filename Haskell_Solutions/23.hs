main :: IO()
main = do
    let l = [0, 1, 2, 3]--, 4, 5, 6, 7, 8, 9]
    let p = (permutations l (length l))
    let ps = quick_sort(map digit_to_int p)
    putStrLn$show$ p --select_element ps 10
    --putStrLn$show(permutations l (length l))

permutations :: [Int]-> Int -> [[Int]]
permutations _ 0 = []
permutations (x:xs) n = [ x: l | l<-(rotations xs (length xs))] ++ (permutations (xs ++ [x]) (n - 1)) 

quick_sort :: [Int] -> [Int]
quick_sort [] = []
quick_sort (x:xs) = quick_sort(lower_xs) ++ [x] ++ quick_sort(upper_xs)
    where upper_xs = [a | a<-xs, a <= x]
          lower_xs = [a | a<-xs, a > x]

select_element :: [Int] -> Int -> Int
select_elements [] _ = 0
select_element (x:xs) 0 = x
select_element (x:xs) n = select_element xs (n - 1)

rotations :: [Int] -> Int -> [[Int]]
rotations [] _ = []
rotations _ 0  = []
rotations (x:xs) n = (rot) : (rotations rot (n -1))
    where rot = xs ++ [x]

unique :: (Eq a) => [a] -> [a]
unique [] = []
unique (x:xs)
    | x `elem` xs = unique xs
    | otherwise   = x : unique xs


digit_to_int = foldl addDigit 0
   where addDigit num d = 10*num + d


remove_head :: [Int] -> [Int]
remove_head [] = []
remove_head (x:xs) = xs




permute :: [Int] -> [[Int]]
permute [] = []
permute (x:xs) = [x: r | r<-rxs] ++ permute(xs)
    where rxs = rotate xs

rotate :: [Int] -> Int -> [[Int]]
rotate  
rotate (x:xs) n = []
    
swapping :: [Int] -> [Int]
swapping [] = []
swapping (x:xs) = ((last xs) : init xs) ++ [x]