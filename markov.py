#!/usr/bin/env python

import sys
import random


def make_chains(words,x):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    words_list = []
    words_list = words.strip().split()
    chains = {}
    #print "Choose a number between one and ten."
    #x = int(raw_input())
    # list[x] = [:x + 1]
    for i in range(len(words_list)-x):
        # word_one = words_list[i]
        # word_two = words_list[i+1]
        # word_three = words_list[i+2]
        # d = {key: [word_one, word_two]}
        key = tuple(words_list[i:(i+x)])
        # print "Key: ", key
        word_next = words_list[i+x]
        # print "Word next: ", word_next
        # d[key].append(word_two)
        #value = [word_three]
        if key not in chains:
            chains[key]=[word_next]
        else:
            chains[key].append(word_next)
    return chains

def make_text(chains,x):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    keys = chains.keys()  # [("word_one", "word_two")]
    k = random.choice(keys) # ("word_one", "word_two")
    output = list(k)
    while k in chains:
        p_values = chains[k]
        value = random.choice(p_values) # "word_three"
        output.append(value)
        #output = [k[0],  k[1],  value] # "word_oneword_twoword_three"
        # printout = (" ".join(k) + " " + value)
        # print printout
        k = tuple(output[-x:])
    return output
 
def main(filename):
    args = sys.argv
    script, filename = args

    # Change this to read input_text from a file
    f = open(filename)
    words = f.read()
    print "Choose a number between one and ten."
    x = int(raw_input())

    chain_dict = make_chains(words,x)
    # print chain_dict
    random_text = make_text(chain_dict, x)
    print " ".join(random_text)

if __name__ == "__main__":
    main("twain_two.txt")