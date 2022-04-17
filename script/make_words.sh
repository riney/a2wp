#!/bin/sh

rm out/*.TEXT
python3 util/split_guess_words.py words/guess_words.json
python3 util/convert_puzzle_words.py words/puzzle_words.json
