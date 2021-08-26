import argparse
import json

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def argparse_imf():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-m', '--model')
    parser.add_argument('-f', '--feats')
    args = parser.parse_args()
    return args

def load_xy(filename):
    x = []
    y = []
    with open(filename) as f:
        for line in f:
            dic = json.loads(line)
            y.append(dic.pop('**LABEL**'))
            x.append(dic)
    return x, y

def main():
    args = argparse_imf()
    x_train, y_train = load_xy(args.input)

    vectorizer = DictVectorizer()
    x_train = vectorizer.fit_transform(x_train)
    y_train = np.array(y_train)
    clf = LogisticRegression(random_state=0, max_iter=1000, verbose=1)
    clf.fit(x_train, y_train)

    joblib.dump(clf, args.model, compress=3)
    joblib.dump(vectorizer, args.feats, compress=3)

if __name__ == '__main__':
    main()
