import argparse
import json

import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt
from tqdm import tqdm

from DN52 import load_xy

def get_accuracy(clf, x, y_true):
    y_pred = clf.predict(x)
    return accuracy_score(y_true, y_pred)

def main():
    x_train, y_train = load_xy('train.feature.txt')
    x_valid, y_valid = load_xy('valid.feature.txt')
    x_test, y_test = load_xy('test.feature.txt')

    vectorizer = DictVectorizer()
    x_train = vectorizer.fit_transform(x_train)
    x_valid = vectorizer.transform(x_valid)
    x_test = vectorizer.transform(x_test)

    train_accuracies = []
    valid_accuracies = []
    test_accuracies = []

    for exp in tqdm(range(10)):
        clf = LogisticRegression(random_state=0, max_iter=1000, C=2**exp)
        clf.fit(x_train, y_train)
        train_accuracies.append(get_accuracy(clf, x_train, y_train))
        valid_accuracies.append(get_accuracy(clf, x_valid, y_valid))
        test_accuracies.append(get_accuracy(clf, x_test, y_test))

    cs = [2**c for c in range(10)]
    plt.plot(cs, train_accuracies, label='train')
    plt.plot(cs, valid_accuracies, label='valid')
    plt.plot(cs, test_accuracies, label='test')
    plt.legend()
    plt.savefig('58.png')

if __name__ == '__main__':
    main()
