import json, string, sys

def usage():
    print('usage: split_guess_words.py in.json')

if len(sys.argv) != 2:
    usage()
    sys.exit()

input_filename = sys.argv[1]

print('Processing ' + input_filename)

# Snork JSON
f = open(input_filename)
guess_words = json.load(f)

print(f"{len(guess_words)} words in input file")

# Initialize dict of arrays, keyed by first letter
split_words = {}

for letter in list(string.ascii_uppercase):
    split_words[letter] = []

# Bin words from JSON array into split_words
for word in guess_words:
    word = word.upper()
    split_words[word[0]].append(word)

f.close()

# Print word counts per letter
for letter in split_words:
    print(f"{letter}: {len(split_words[letter])}")

# Dump words into text files, one per starting letter
for letter in split_words:
    out_filename = f"{letter}_WORDS.TEXT"
    print(f"Writing {out_filename}...")
    with open("out/" + out_filename, 'x') as f:        
        for word in split_words[letter]:
            f.write(word[1:])
        
print('Done.')
