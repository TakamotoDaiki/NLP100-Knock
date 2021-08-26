from gensim.models import KeyedVectors
import numpy as np
from sklearn.cluster import KMeans

def main():
    model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz', binary=True)
    countries = set()
    with open('ans64.txt') as f:
        for line in f:
            line = line.split()
            if line[0] in ['capital-common-countries', 'captal-world']:
                countries.add(line[2])
            elif line[0] in ['currency', 'gram6-nationality-adjective']:
                countries.add(line[1])
    countries = list(countries)
    countries_vec = [model[country] for country in countries]

    kmeans = KMeans(n_clusters=5)
    kmeans.fit(countries_vec)
    for i in range(5):
        cluster = np.where(kmeans.labels_ == i)[0]
        print('cluster', i+1)
        print(', '.join([countries[k] for k in cluster]))

if __name__ == '__main__':
    main()
