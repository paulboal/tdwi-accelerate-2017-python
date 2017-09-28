import nltk
from nltk.stem.snowball import SnowballStemmer
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans



class ClassifyFacilities:
    """
    This code takes a list of facilities and makes an attempt to group them into
    categories based on their name.  The intent is to classify facilities as
    hospital, physician office, stand-alone clinic, etc.
    """

    def __init__(self):
        """
        Basic initialization of the object.  This ensures we have the latest
        versions of stopwords and tokenizers as well.
        """
        nltk.download('stopwords')
        nltk.download('punkt')
        self._stemmer = SnowballStemmer("english")
        self._stopwords = nltk.corpus.stopwords.words('english')


    def classify(self, facilities, exclusions, num_clusters):
        """
        Actually does the classification steps.
        """
        self._facilities = facilities
        self._num_clusters = num_clusters
        self._exclusions = [n.lower() for n in exclusions]
        self._load_vocab()
        self._compute_matrix()
        self._cluster()

        return self

    def print_clusters(self):
        print("Top terms per cluster:")
        print()
        #sort cluster centers by proximity to centroid
        order_centroids = self.get_centroids()
        vocab_frame = self.get_vocab()
        terms = self.get_vectorizer().get_feature_names()
        facilities = {'facility': self._facilities, 'cluster': self._clusters}
        frame = pd.DataFrame(facilities, index=self.get_clusters(), columns=['facility', 'cluster'] )

        for i in range(self._num_clusters):
            print("Cluster %d words:" % i, end='')

            for ind in order_centroids[i, :6]: #replace 6 with n words per cluster
                print(' %s' % vocab_frame.ix[terms[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'), end=',')
            print() #add whitespace
            print() #add whitespace

            print("Cluster %d titles:" % i, end='')
            for facility in frame.ix[i]['facility'].values.tolist():
                print(' %s,' % facility, end='')
            print() #add whitespace
            print() #add whitespace

    def get_vocab(self):
        """
        Returns the vocabulary frame of all the tokenized words and stems.
        """
        return self._vocab_frame

    def get_tfidf_matrix(self):
        return self._tfidf_matrix

    def get_vectorizer(self):
        return self._vectorizer

    def get_clusters(self):
        return self._clusters

    def get_centroids(self):
        return self._km.cluster_centers_.argsort()[:, ::-1]

    def get_dist(self):
        return self._dist

    def get_km(self):
        return self._km

    def _cluster(self):
        self._dist = 1 - cosine_similarity(self._tfidf_matrix)
        self._km = KMeans(n_clusters=self._num_clusters)
        self._km.fit(self._tfidf_matrix)
        self._clusters = self._km.labels_.tolist()

    def _compute_matrix(self):
        #define vectorizer parameters
        self._vectorizer = TfidfVectorizer(
            max_df=0.8, max_features=200000,
            min_df=0, stop_words='english',
            use_idf=True, tokenizer=self._tokenize_and_stem, ngram_range=(1,3))

        self._tfidf_matrix = self._vectorizer.fit_transform(self._facilities) #fit the vectorizer to synopses


    def _load_vocab(self):
        vocab_stemmed = []
        vocab_tokenized = []
        for i in self._facilities:
            allwords_stemmed = self._tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
            vocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list

            allwords_tokenized = self._tokenize_only(i)
            vocab_tokenized.extend(allwords_tokenized)

        self._vocab_frame = pd.DataFrame({'words': vocab_tokenized}, index = vocab_stemmed)

    def _tokenize_and_stem(self, text):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token) and not(token.lower() in self._exclusions):
                filtered_tokens.append(token)
        stems = [self._stemmer.stem(t) for t in filtered_tokens]
        return stems

    def _tokenize_only(self, text):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token) and not(token.lower() in self._exclusions):
                filtered_tokens.append(token)
        return filtered_tokens
