# Word Embedding Testing

<p>
There are three files here. One of them downloads and sets up the tests that you need. Another runs the tests. You must provide a pickled python dictionary for your embeddings. The keys should be strings, and the values should be arrays of floats or ints. The final file is a log file for the scores from the GloVe embeddings.
</p>
<p>
Recorded scores are the squared error between the similarity proposed in the tests and the similarity of the word pairs in the embeddings you provide. In theory, a lower score would indicate 'better' embeddings. The GloVe embeddings are provided as reference, as scores are more meaninful in a relative sense than an absolute sense.
</p>

---
## Installation

Run `download.sh`

---
## Usage

Run `test_embeddings.py <path to dict> <log file name>`

---
## Tests

Here are the links to the tests that are used.

MEN:
<a href="http://clic.cimec.unitn.it/~elia.bruni/MEN.html">http://clic.cimec.unitn.it/~elia.bruni/MEN.html</a>

MTurk:
<a href="http://www2.mta.ac.il/~gideon/mturk771.html">http://www2.mta.ac.il/~gideon/mturk771.html </a>

WS-353
<a href="http://alfonseca.org/eng/research/wordsim353.html">http://alfonseca.org/eng/research/wordsim353.html</a>

SimLex
<a href="http://www.cl.cam.ac.uk/~fh295/simlex.html#">http://www.cl.cam.ac.uk/~fh295/simlex.html#</a>

---
## GloVe

Here are the GloVe embeddings used as a baseline.

<a href="https://nlp.stanford.edu/projects/glove/">https://nlp.stanford.edu/projects/glove/</a>
