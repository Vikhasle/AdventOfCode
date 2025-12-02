<?php


function manhattan($point_a, $point_b)
{
    return abs($point_a[0] - $point_b[0]) + abs($point_a[1] - $point_b[1]);
}

function print_arr($arr)
{
    for ($i = 0; $i < count($arr); $i++) {
        printf("%s,", $arr[$i]);
    }
    echo ("\n");
}

function collide($line_a, $line_b)
{
    if ($line_a[0][0] - $line_a[1][0] != 0) {
        if ($line_b[0][1] - $line_b[1][1] != 0) {
            $b1 = $line_a[0][1];
            $b2 = $line_b[0][0];
            if ($line_b[0][1] < $b1 && $line_b[1][1] > $b1 || $line_b[0][1] > $b1 && $line_b[1][1] < $b1) {
                if ($line_a[0][0] < $b2 && $line_a[1][0] > $b2 || $line_a[0][0] > $b2 && $line_a[1][0] < $b2) {
                    return true;
                }
            }
            return false;
        } else {
            return false;
        }
    } else {
        if ($line_b[0][0] - $line_b[1][0] != 0) {
            $b1 = $line_a[0][0];
            $b2 = $line_b[0][1];
            if ($line_b[0][0] < $b1 && $line_b[1][0] > $b1 || $line_b[0][0] > $b1 && $line_b[1][0] < $b1) {
                if ($line_a[0][1] < $b2 && $line_a[1][1] > $b2 || $line_a[0][1] > $b2 && $line_a[1][1] < $b2) {
                    return true;
                }
            }
            return false;
        } else {
            return false;
        }
    }
}

function part_One($input)
{
    $isections = [];
    $path = [];
    for ($wire = 0; $wire < count($input); $wire++) {
        $curr = [0, 0];
        $curr_wire_path = [];
        $input[$wire] = explode(",", $input[$wire]);
        for ($i = 0; $i < count($input[$wire]); $i++) {
            $prev = $curr;
            if ($input[$wire][$i][0] == 'R') {
                $curr[0] += intval(ltrim($input[$wire][$i], 'R'));
            } elseif ($input[$wire][$i][0] == 'L') {
                $curr[0] -= intval(ltrim($input[$wire][$i], 'L'));
            } elseif ($input[$wire][$i][0] == 'U') {
                $curr[1] += intval(ltrim($input[$wire][$i], 'U'));
            } else {
                $curr[1] -= intval(ltrim($input[$wire][$i], 'D'));
            }
            for ($j = 0; $j < count($path); $j++) {
                if (collide([$prev, $curr], [$path[$j][0], $path[$j][1]])) {
                    $diff_x = $prev[0] - $path[$j][0][0];
                    $diff_y = $prev[1] - $path[$j][0][1];
                    array_push($isections, [$prev[0] + $diff_x, $prev[1] + $diff_y]);
                }
            }
            array_push($curr_wire_path, [$prev, $curr]);
        }
        $path = array_merge($path, $curr_wire_path);
    }
    for ($i = 0; $i < count($isections); $i++) {
        print_arr($isections[$i]);
    }
    $temp = manhattan([0, 0], $isections[0]);
    for ($i = 0; $i < count($isections); $i++) {
        if (manhattan([0, 0], $isections[$i]) < $temp) {
            $temp = manhattan([0, 0], $isections[$i]);
        }
    }
    return $temp;
}

//$test = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83";
//$test=[R8, U5, L5, D3]
//echo (part_One($test));
$file = fopen("test.txt", "r");
$inp = [];
while (!feof($file)) {
    array_push($inp, fgets($file));
}
fclose($file);
array_pop($inp);
//print_arr($inp);
echo (part_One($inp));
//echo (collide([[0, 2], [4, 2]], [[2, 4], [2, 0]]));
echo ("\n");
