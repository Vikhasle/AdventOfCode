import Data.Char
import Data.List.Split
import Debug.Trace

exists :: Char -> String -> Maybe Char
exists x "" = Nothing
exists x (y:ys) =
    if x == y
       then Just x
        else exists x ys

findDup :: (String, String) -> Char
findDup ((x:xs), lst2) =
    if exists x lst2 == Nothing
       then findDup (xs, lst2)
        else x

split :: String -> String -> Int -> (String, String)
split tail head 0 = (reverse head, tail)
split (x:xs) head n = split xs (x : head) (n - 1)

part1 :: Int -> [String] -> Int
part1 acc [] = acc
part1 acc (x:xs) =
    let char = ord $ findDup $ split x "" $ (length x) `div` 2
     in if 97 <= char
           then part1 (acc + (char - 96)) xs
            else part1 (acc + (char - 65) + 27) xs


findDup3 :: [String] -> Char
findDup3 [fst, snd, thrd] =


part2 :: Int -> [[String]] -> Int



main :: IO ()
main = do
    input <- getContents
    print "Part1"
    print $ part1 0 $ lines input
