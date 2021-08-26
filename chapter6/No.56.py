from sklearn.metrics import classification_report

from DN52 import argparse_imf
from DN54 import predict

def main():
    args = argparse_imf()
    y_true, y_pred = predict(args)
    print(classification_report(y_true, y_pred, digits=4))

if __name__ == '__main__':
    main()
