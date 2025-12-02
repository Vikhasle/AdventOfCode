
data Expr = Num Int | Par Expr | Binary Expr Op Expr deriving (Show)

data Op = Add | Mul deriving(Show)


	evalExp :: Expr -> Int
	evalExp (Num i) = i
	evalExp (Par e) = evalExp e
evalExp (Binary e1 op e2) = evalCalc op (evalExp e1) (evalExp e2)

	evalCalc :: Op -> Int -> Int -> Int
	evalCalc Add a b = a + b
	evalCalc Mul a b = a * b

	parse :: [Str] -> Expr
parse (x:xs)


	parseInput :: [String] ->

main:: IO()
	main = do
	input <- getContents
	print "Part 1"
	print $
