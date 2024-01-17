
from sklearn.base import BaseEstimator, TransformerMixin


class MajorityVotingTagger(BaseEstimator, TransformerMixin):
    
    def fit(self, X, y):
        """
        X: list of words
        y: list of tags
        """
        word2cnt = {}
        self.tags = []
        for x, t in zip(X, y):
            if t not in self.tags:
                self.tags.append(t)
            if x in word2cnt:
                if t in word2cnt[x]:
                    word2cnt[x][t] += 1
                else:
                    word2cnt[x][t] = 1
            else:
                word2cnt[x] = {t: 1}
        self.mjvote = {}
        
        for k, d in word2cnt.items():
            self.mjvote[k] = max(d, key=d.get)
    
    def predict(self, X, y=None):
        '''
        Predict the the tag from memory. If word is unknown, predict 'O'.
        '''
        return [self.mjvote.get(x, 'O') for x in X]

