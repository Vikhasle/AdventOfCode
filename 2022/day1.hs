parseInput :: [String] -> Int -> [Int]
parseInput [] n = [n]
parseInput (x:xs) n =
    if x == ""
        then n : parseInput xs 0
        else parseInput xs ((read x :: Int) + n)

qs [] = []
qs (x:xs) = qs [y | y <- xs, y > x] ++ [x] ++ qs [y | y <- xs, y <= x]

main :: IO ()
main = do
    input <- getContents
    print "Part1"
    print $ foldr max 0 $ parseInput (lines input) 0
    print "Part2"
    print $ sum $ take 3 $ qs $ parseInput (lines input) 0
