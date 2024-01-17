

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn_crfsuite import CRF
from sklearn_crfsuite.metrics import flat_classification_report

from majorityvoting import MajorityVotingTagger
from get_data_feature import get_feature, get_sentences, word2features, sent2features, sent2labels, sent2tokens




# MajorityVoting Tagger
def report_MajorityVotingTagger(input_file):

    data = pd.read_csv(input_file, encoding="latin1")
    data = data.fillna(method="ffill")
    # print(len(list(set(data["Word"].values))))  # Unique Words in corpus
    words = data["Word"].values.tolist()
    tags = data["Tag"].values.tolist()

    pred = cross_val_predict(estimator=MajorityVotingTagger(), X=words, y=tags, cv=5)
    report = classification_report(y_pred=pred, y_true=tags)
    print(report)


# RandomForest Classifier
def report_RandomForestClassifier(input_file):

    data = pd.read_csv(input_file, encoding="latin1")
    data = data.fillna(method="ffill")
    # print(len(list(set(data["Word"].values))))  # Unique Words in corpus
    words = [get_feature(w) for w in data["Word"].values.tolist()]
    tags = data["Tag"].values.tolist()

    pred = cross_val_predict(RandomForestClassifier(n_estimators=20), X=words, y=tags, cv=5)
    report = classification_report(y_pred=pred, y_true=tags)
    print(report)


# RandomForest Classifier
def report_RandomForestClassifier2(input_file):
    
    data = pd.read_csv(input_file, encoding="latin1")
    data = data.fillna(method="ffill")

    out = []
    y = []
    mv_tagger = MajorityVotingTagger()
    tag_encoder = LabelEncoder()
    pos_encoder = LabelEncoder()

    words = data["Word"].values.tolist()
    pos = data["POS"].values.tolist()
    tags = data["Tag"].values.tolist()

    mv_tagger.fit(words, tags)
    tag_encoder.fit(tags)
    pos_encoder.fit(pos)

    sentences = get_sentences(data)
    for sentence in sentences:
        for i in range(len(sentence)):
            w, p, t = sentence[i][0], sentence[i][1], sentence[i][2]
            
            if i < len(sentence)-1:
                # 如果不是最后一个单词，则可以用到下文的信息
                mem_tag_r = tag_encoder.transform(mv_tagger.predict([sentence[i+1][0]]))[0]
                true_pos_r = pos_encoder.transform([sentence[i+1][1]])[0]
            else:
                mem_tag_r = tag_encoder.transform(['O'])[0]
                true_pos_r =  pos_encoder.transform(['.'])[0]
                
            if i > 0: 
                # 如果不是第一个单词，则可以用到上文的信息
                mem_tag_l = tag_encoder.transform(mv_tagger.predict([sentence[i-1][0]]))[0]
                true_pos_l = pos_encoder.transform([sentence[i-1][1]])[0]
            else:
                mem_tag_l = tag_encoder.transform(['O'])[0]
                true_pos_l =  pos_encoder.transform(['.'])[0]
            #print (mem_tag_r, true_pos_r, mem_tag_l, true_pos_l)
            
            out.append(np.array([w.istitle(), w.islower(), w.isupper(), len(w), w.isdigit(), w.isalpha(),
                                    tag_encoder.transform(mv_tagger.predict([sentence[i][0]])),
                                    pos_encoder.transform([p])[0], mem_tag_r, true_pos_r, mem_tag_l, true_pos_l]))
            y.append(t)

    pred = cross_val_predict(RandomForestClassifier(n_estimators=20), X=out, y=y, cv=5)
    report = classification_report(y_pred=pred, y_true=y)
    print(report)

# crf
def report_crf(input_file):

    data = pd.read_csv(input_file, encoding="latin1")
    data = data.fillna(method="ffill")

    sentences = get_sentences(data)
    X = [sent2features(s) for s in sentences]
    y = [sent2labels(s) for s in sentences]

    crf = CRF(algorithm='lbfgs',
          c1=0.1,
          c2=0.1,
          max_iterations=100)
    # pred = cross_val_predict(estimator=crf, X=X, y=y, cv=5)
    try:
        crf.fit(X=X, y=y)
    except AttributeError:
        pass
    pred = crf.predict(X=X)
    report = flat_classification_report(y_pred=pred, y_true=y)
    print(report)


if __name__ == "__main__":
    input_file = "ner_dataset.csv"
    report_MajorityVotingTagger(input_file)
    report_RandomForestClassifier(input_file)
    report_RandomForestClassifier2(input_file)
    report_crf(input_file)
    

