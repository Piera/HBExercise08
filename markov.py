#!/usr/bin/env python

import sys
import random


def make_chains(words):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    words_list = words.strip().split()
    chains = {}
    for i in range(len(words_list)-2):
        word_one = words_list[i]
        word_two = words_list[i+1]
        word_three = words_list[i+2]
        # d = {key: [word_one, word_two]}
        key = (word_one, word_two)
        # d[key].append(word_two)
        #value = [word_three]
        if key not in chains:
            chains[key]=[word_three]
        else:
            chains[key].append(word_three)
    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    keys = chains.keys()  # [("word_one", "word_two")]
    k = random.choice(keys) # ("word_one", "word_two")
    while k in chains:
        p_values = chains[k]
        value = random.choice(p_values) # "word_three"
        output = [k[0],  k[1],  value] # "word_oneword_twoword_three"
        print str.join(" ", output)
        k = (output[-2], output[-1])
    return k
 
def main(filename):
    args = sys.argv
    script, filename = args

    # Change this to read input_text from a file
    f = open(filename)
    words = f.read()

    chain_dict = make_chains(words)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main("twain_two.txt")