import argparse
import json

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

from DN52 import argparse_imf, load_xy

def predict(args):
    x_test, y_true = load_xy(args.input)

    vectorizer = joblib.load(args.feats)
    x_test = vectorizer.transform(x_test)
    y_true = np.array(y_true)

    clf = joblib.load(args.model)
    y_pred = clf.predict(x_test)

    return y_true, y_pred

def main():
    args = argparse_imf()
    y_true , y_pred = predict(args)
    accuracy = accuracy_score(y_true, y_pred) * 100
    print('Accuracy: %.3f' % accuracy)

if __name__ == '__main__':
    main()
