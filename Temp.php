<?php
// Simple PHP script for testing

// Print a greeting
echo "Hello, World!\n";

// Define variables
$name = "PHP Developer";
$year = 2024;

// Print variables
echo "Welcome, " . $name . "! It is " . $year . ".\n";

// Function to calculate the sum of two numbers
function sum($a, $b) {
    return $a + $b;
}

// Calculate and print the sum of two numbers
$result = sum(5, 3);
echo "The sum of 5 and 3 is " . $result . ".";
?>