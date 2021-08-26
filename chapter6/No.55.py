from sklearn.metrics import confusion_matrix

from DN52 import argparse_imf
from DN54 import predict

def main():
    args = argparse_imf()
    y_true, y_pred = predict(args)
    labels = ('b', 'e', 't', 'm')
    matrix = confusion_matrix(y_true, y_pred, labels=labels)
    print(labels)
    print(matrix)

if __name__ == '__main__':
    main()
