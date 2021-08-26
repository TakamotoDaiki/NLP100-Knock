import joblib
import numpy as np

from DN52 import argparse_imf

def get_topk_indices(array, k=10):
    unsorted_max_indices = np.argpartition(-array, k)[:k]
    max_weights = array[unsorted_max_indices]
    max_indices = np.argsort(-max_weights)
    return unsorted_max_indices[max_indices]

def show_weights(args):
    vectorizer = joblib.load(args.feats)
    feature_names = np.array(vectorizer.get_feature_names())

    clf = joblib.load(args.model)
    coefs = clf.coef_
    y_labels = clf.classes_
    for coef, y_label in zip(coefs, y_labels):
        max_k_indices = get_topk_indices(coef)
        print(y_label)
        for name, weight in zip(feature_names[max_k_indices], coef[max_k_indices]):
            print(name, weight, sep='\t')
        print('---')
        min_k_indices = get_topk_indices(-coef)
        for name, weight in zip(feature_names[min_k_indices], coef[min_k_indices]):
            print(name, weight, sep='\t')
        print()

def main():
    args = argparse_imf()
    show_weights(args)

if __name__ == '__main__':
    main()
