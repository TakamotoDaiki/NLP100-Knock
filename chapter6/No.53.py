import argparse
import json
import sys

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

from DN51 import make_feats_dict
from DN52 import argparse_imf, load_xy

def predict_label_proba(x, vectorizer, clf):
    x = vectorizer.transform(x)
    y_proba = clf.predict_proba(x)
    y_pred = clf.classes_[y_proba.argmax(axis=1)]
    y_proba_max = y_proba.max(axis=1)
    return y_pred, y_proba_max

def main():
    args = argparse_imf()
    vectorizer = joblib.load(args.feats)
    clf = joblib.load(args.model)
    x = list(map(make_feats_dict, sys.stdin))
    y_pred, y_proba = predict_label_proba(x, vectorizer, clf)
    for label, proba in zip(y_pred, y_proba):
        print('%s\t%.4f' % (label, proba))

if __name__ == '__main__':
    main()
