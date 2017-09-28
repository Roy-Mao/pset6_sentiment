import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # self.positives; self.negatives; use dict; spaces -> str.strip; str.startswith
        #tokenize text; tokens = self.tokenizer.tokenize(text)
        # with open("file.txt") as lines: for line in lines: to do sth
        self.positives = {}
        self.negatives = {}
        with open(positives, "r") as pf:
            lines = pf.readlines()
            for line in lines:
                if ((not line.startswith(';')) and (not line.startswith('\n'))):
                    line = line.strip('\n')
                    self.positives[line] = 1
        pf.close()
        with open(negatives, "r") as nf:
            lines = nf.readlines()
            for line in lines:
                if ((not line.startswith(';')) and (not line.startswith('\n'))):
                    line = line.strip('\n')
                    self.negatives[line] = 1
            
            
                

        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        scores = 0
        tokenizer = nltk.tokenize.TweetTokenizer(strip_handles=True, reduce_len=True)
        tokens = tokenizer.tokenize(text);  #tokens shold be a list of string
        for token in tokens:
            token = token.lower()
            if token in self.positives:
                scores += 1
            elif token in self.negatives:
                scores -= 1
            else:
                scores += 0
        return scores
                
                
                

        # TODO.
