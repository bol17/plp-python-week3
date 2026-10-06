# Week 3 Assignment: Grade Reporter & Bug Hunt

## Overview
This repository contains two Python scripts demonstrating the use of loops, conditional logic, and debugging techniques.

## Files
* `grade_reporter.py`: Iterates through a list of student scores to determine letter grades, tracks pass/fail counts, and calculates the rounded average score.
* `bug_hunt.py`: A debugged script using a `while` loop to compute the sum of numbers from 1 to 5, featuring explicit comments explaining each bug fix.

## Reflection
The hardest bug to find in Part B was the logical off-by-one error in the condition `while count < 5`. Because Python executed the code without raising any runtime or syntax error messages, the code ran "successfully" but produced an incorrect answer (`10` instead of `15`). I knew something was wrong by comparing the actual output against the expected mathematical result, which highlighted that `5` was never being added to the total.