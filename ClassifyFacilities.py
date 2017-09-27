import nltk
from nltk.stem.snowball import SnowballStemmer
import re
import pandas as pd

class ClassifyFacilities:

    def __init__(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        self._stemmer = SnowballStemmer("english")
        self._stopwords = nltk.corpus.stopwords.words('english')
        self._exclusions = []

    def classify(self, facilities, exclusions):
        self._load_vocab(facilities, exclusions)
        return self

    def get_vocab():
        return self._vocab_frame

    def _load_vocab(self, facilities, exclusions):
        self._exclusions = ['New','York','Miami','San','Francisco','Dallas','NY','FL','Florida','CA','California','TX','Texas','sleep']
        vocab_stemmed = []
        vocab_tokenized = []
        for i in facilities:
            allwords_stemmed = self._tokenize_and_stem(i, exclusions) #for each item in 'synopses', tokenize/stem
            vocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list

            allwords_tokenized = self._tokenize_only(i, exclusions)
            vocab_tokenized.extend(allwords_tokenized)

        self._vocab_frame = pd.DataFrame({'words': vocab_tokenized}, index = vocab_stemmed)


    def _tokenize_and_stem(self, text, exclusions):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        names = [n.lower() for n in names]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token) and not(token.lower() in exclusions):
                filtered_tokens.append(token)
        stems = [self._stemmer.stem(t) for t in filtered_tokens]
        return stems


    def _tokenize_only(self, text, exclusions):
        # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
        tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
        names = [n.lower() for n in names]
        filtered_tokens = []
        # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
        for token in tokens:
            if re.search('[a-zA-Z]', token) and not(token.lower() in exclusions):
                filtered_tokens.append(token)
        return filtered_tokens
