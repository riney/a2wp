import json, string, sys

def usage():
    print('usage: convert_puzzle_words.py in.json')

if len(sys.argv) != 2:
    usage()
    sys.exit()

input_filename = sys.argv[1]

print('Processing ' + input_filename)

# Snork JSON
f = open(input_filename)
words = json.load(f)

print(f"{len(words)} words in input file")

# Dump words into text file
out_filename = "WORDS.TEXT"
with open("out/" + out_filename, 'x') as f:
    print(f"Writing {out_filename}...")
    for word in words:
        f.write(word.upper())

print('Done.')
