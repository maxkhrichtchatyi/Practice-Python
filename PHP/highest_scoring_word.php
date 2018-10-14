<?php
/*
 * Given a string of words, you need to find the highest scoring word.
 * Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.
 * You need to return the highest scoring word as a string.
 * If two words score the same, return the word that appears earliest in the original string.
 * All letters will be lowercase and all inputs will be valid.
 */

function high($x)
{
    $max_world = "";
    $max_world_score = 0;

    $words = explode(' ', $x);

    foreach ($words as $word) {
        $current_score = 0;

        for ($i = 0; $i < strlen($word); $i++) {
            $current_score += ord($word[$i]) - ord('a') + 1;
        }

        if ($current_score > $max_world_score) {
            $max_world_score = $current_score;
            $max_world = $word;
        }
    }

    return $max_world;
}

// Return: string
echo high("some string with the highest scoring word");
?>