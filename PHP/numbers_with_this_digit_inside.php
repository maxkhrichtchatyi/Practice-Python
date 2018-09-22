<?php
/*
You have to search all numbers from inclusive 1 to inclusive a given number x, that have the given digit d in it.
The value of d will always be 0 - 9.
The value of x will always be greater than 0.

You have to return as an array

the count of these numbers,
their sum
and their product.

For example:

x = 11
d = 1
->
Numbers: 1, 10, 11
Return: [3, 22, 110]

If there are no numbers, which include the digit, return [0,0,0].
*/

function numbersWithDigitInside($x, $d)
{
    $arr = [];

    foreach (range(1, $x) as $number) {
        foreach (str_split($number) as $number_item) {
            if ($d == $number_item) {
                $arr[] = $number;
                break;
            }
        }
    }

    $arr = (array_sum($arr) == 0) ? $arr = [0, 0, 0] : [count($arr), array_sum($arr), array_product($arr)];

    return $arr;
}

// Return: [3, 22, 110]
print_r(numbersWithDigitInside(11, 1));
?>