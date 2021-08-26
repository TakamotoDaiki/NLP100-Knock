from sklearn.ensemble import GradientBoostingClassifier

def main():
    clf = GradientBoostingClassifier(random_state=0, min_samples_split=0.01,
                                     min_samples_leaf=5, max_depth=10,
                                     max_features='sqrt', n_estimators=500,
                                     subsample=0.8)
    clf.fit(x_train, y_train)
    valid_acc = get_accuracy(clf, x_valid, y_valid) * 100
    print('Validation Accuracy: %.3f' % valid_acc)
    test_acc = get_accuracy(clf, x_test, y_test) * 100
    print('Test Accuracy: %.3f' % test_acc)

if __name__ == '__main__':
    main()
