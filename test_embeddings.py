# Author John Sigmon
# Date created 7/9/18
# Last modified 7/9/18

import sys
from numpy.linalg import norm
from numpy import dot
import pickle as pkl

class WordEmbeddingTest():
    path_to_dict = None 
    path_to_output = None
    embeddings = None
    scores = {}
    num_words_not_found_MEN = 0
    num_words_not_found_MTurk = 0
    num_words_not_found_SimLex = 0
    num_words_not_found_WS_353 = 0

    def __init__(self, path_to_dict, path_to_output):
        self.path_to_dict = path_to_dict
        self.path_to_output = path_to_output
        with open(path_to_dict, 'rb') as f:
            self.embeddings = pkl.load(f)
        self.scores.fromkeys([
                'MEN',
                'MTurk',
                'SimLex',
                'WS-353'
                ])
    
    def run_all_tests(self):
        self.test_MEN()
        self.test_MTurk()
        self.test_SimLex()
        self.test_WS_353()
        self._write_to_file()

    def test_MEN(self):
        MEN_dir = './MEN/'
        MEN_file = 'MEN_dataset_natural_form_full'
        
        l2_score = []
        l2 = lambda x, y: ((x - y)**2)
        
        with open(MEN_dir + MEN_file, 'r') as f:
            for line in f:
                split_line = line.split()
                word1 = split_line[0]
                word2 = split_line[1]
                score = float(split_line[2]) / float(50)
                # We want to skip words that aren't in our vocab
                try:
                    word1_emb = self.embeddings[word1]
                except:
                    self.num_words_not_found_MEN += 1
                    continue
                try:
                    word2_emb = self.embeddings[word2]
                except:
                    self.num_words_not_found_MEN += 1
                    continue               
        
                my_score = self._cosine(word1_emb, word2_emb)
                l2_score.append(l2(score, my_score))
                del word1_emb
                del word2_emb
        
        avg_l2 = sum(l2_score) / float(len(l2_score))
        del l2_score
        self.scores['MEN'] = avg_l2

    def test_MTurk(self):
        MTurk_dir = './MTurk/'
        MTurk_file = 'MTURK.csv'
        
        l2_score = []
        l2 = lambda x, y: ((x - y)**2)
        
        with open(MTurk_dir + MTurk_file, 'r') as f:
            for line in f:
                split_line = line.split(',')
                word1 = split_line[0]
                word2 = split_line[1]
                score = float(split_line[2]) / float(5)
                # We want to skip words that aren't in our vocab
                try:
                    word1_emb = self.embeddings[word1]
                except:
                    self.num_words_not_found_MTurk += 1
                    continue
                try:
                    word2_emb = self.embeddings[word2]
                except:
                    self.num_words_not_found_MTurk += 1
                    continue               
        
                my_score = self._cosine(word1_emb, word2_emb)
                l2_score.append(l2(score, my_score))
                del word1_emb
                del word2_emb
        
        avg_l2 = sum(l2_score) / float(len(l2_score))
        del l2_score
        self.scores['MTurk'] = avg_l2
    
    def test_SimLex(self):
        SimLex_dir = './SimLex/SimLex-999/'
        SimLex_file = 'SimLex-999.txt'
        
        l2_score = []
        l2 = lambda x, y: ((x - y)**2)
        
        with open(SimLex_dir + SimLex_file, 'r') as f:
            next(f)
            for line in f:
                split_line = line.split()
                word1 = split_line[0]
                word2 = split_line[1]
                score = float(split_line[3]) / float(10)
                # We want to skip words that aren't in our vocab
                try:
                    word1_emb = self.embeddings[word1]
                except:
                    self.num_words_not_found_SimLex += 1
                    continue
                try:
                    word2_emb = self.embeddings[word2]
                except:
                    self.num_words_not_found_SimLex += 1
                    continue               
        
                my_score = self._cosine(word1_emb, word2_emb)
                l2_score.append(l2(score, my_score))
                del word1_emb
                del word2_emb
        
        avg_l2 = sum(l2_score) / float(len(l2_score))
        del l2_score
        self.scores['SimLex'] = avg_l2

    def test_WS_353(self):
        WS_353_dir = './WS-353/'
        WS_353_file = 'combined.tab'
        
        l2_score = []
        l2 = lambda x, y: ((x - y)**2)
        
        with open(WS_353_dir + WS_353_file, 'r') as f:
            next(f)
            for line in f:
                split_line = line.split()
                word1 = split_line[0]
                word2 = split_line[1]
                score = float(split_line[2]) / float(10)
                # We want to skip words that aren't in our vocab
                try:
                    word1_emb = self.embeddings[word1]
                except:
                    self.num_words_not_found_WS_353 += 1
                    continue
                try:
                    word2_emb = self.embeddings[word2]
                except:
                    self.num_words_not_found_WS_353 += 1
                    continue               
        
                my_score = self._cosine(word1_emb, word2_emb)
                l2_score.append(l2(score, my_score))
                del word1_emb
                del word2_emb
        
        avg_l2 = sum(l2_score) / float(len(l2_score))
        del l2_score
        self.scores['WS_353'] = avg_l2

    def _cosine(self, arr1, arr2):
        try:
            arr1 = np.array(arr1)
            arr2 = np.array(arr2)
        except:
            pass
        num = dot(arr1, arr2)
        norm1 = norm(arr1)
        norm2 = norm(arr2)
        return num / (norm1 * norm2)

    def _write_to_file(self):
        target = self.path_to_output
        with open(target, 'w') as f:
            f.write('Scores from embeddings loaded from {}\n'
                    .format(self.path_to_dict))
            f.write('\n')
            for key in self.scores:
                f.write(key + ':\t' + str(self.scores[key]) + '\n')
                num_words = getattr(self, 'num_words_not_found_' + key)
                f.write('Number of words not found:\t{}\n'.format(num_words))
                f.write('\n')

if __name__=='__main__':
    if len(sys.argv) is not 3:
        print('Usage:\ttest_embeddings.py <path_to_pickled_dictionary> ' +
                '<path_for_log_file>')
        sys.exit()
    tester = WordEmbeddingTest(sys.argv[1], sys.argv[2])
    tester.run_all_tests()
