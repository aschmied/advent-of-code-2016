# Advent of Code 2016

This repo contains my solutions to the [Advent of Code 2016](http://adventofcode.com/2016) puzzles. I'm reading [Martin's Clean Code book](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) while solving these, so I'm trying to apply the principles from that book.

# My Favourite Solutions

## [Day 8](http://adventofcode.com/2016/day/8)

There is a small LCD screen controlled by a simple scripting language and we need to determine the text on the screen after a given sequence of instructions.

A `Screen` object stores the screen state and provides an interface for its manipulation, `Instruction` objects manipulate the screen, and a parser reads text and constructs a sequence of instruction objects.

## [Day 9](http://adventofcode.com/2016/day/9)

We are given a compressed input and asked to determine the length of the output. The input is compressed by a run-length scheme. A string like `(mxn)` in the input means the `m` bytes following the `)` should be repeated `n` times. In the first part of the puzzle recursive repeats are ignored: if a repeat sequence appears in a repeated string then we ignore the repeat sequence. In the second part recursive repeats are allowed.

I solved part 1 by decoding the input. For part 2 the output is ~10 GB, so we need to calculate the length of the decoded text without actually decoding it. A recursive approach works.

# Example

I tested these with Python 2.7.8. Run them like:

    cd day01
    python main.py

or for the unit tests:

    cd day01
    python -m unittest discover
