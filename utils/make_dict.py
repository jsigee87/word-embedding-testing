# Author John Sigmon
# Created 7/9/18
# Last modified 7/9/18

# If you download the glove embeddings,
# this will pickle them for you.

import pickle as pkl

filepath = 'data/glove/'
filename = 'glove.6B.300d.txt'

def make_array(s):
    return [float(num) for num in s]
                    
with open(filepath + filename, 'r') as f:
    glove = [line.strip('\n') for line in f]

glove_dict = {}
for line in glove:
    split_line = line.split()
    key = split_line[0]
    nums = split_line[1:]
    array = make_array(nums)
    glove_dict[key] = array

with open('glove_dict', 'wb') as f:
    pkl.dump(glove_dict, f)
