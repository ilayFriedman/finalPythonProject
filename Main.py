import time
import dask.bag as db
import dask.dataframe as dd
import json
import os
import nltk
nltk.download('wordnet')
import gensim
from gensim import corpora, models
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
class DataBase:

    def __init__(self,pathToDataSet):
        self.review_Json = db.read_text(pathToDataSet + "review.json").map(json.loads).to_dataframe()
        self.business_Json = db.read_text(pathToDataSet + "business.json").map(json.loads).to_dataframe()
        self.checkin_Json = db.read_text(pathToDataSet + "checkin.json").map(json.loads).to_dataframe()
        self.photo_Json = db.read_text(pathToDataSet + "photo.json").map(json.loads).to_dataframe()
        self.tip_Json = db.read_text(pathToDataSet + "tip.json").map(json.loads).to_dataframe()
        self.user_Json = db.read_text(pathToDataSet + "user.json").map(json.loads).to_dataframe()

    def getSimillar(self,bussinessName,categoriesSim,locationSim,hoursSim):
        print(self.business_Json[self.business_Json['name']==bussinessName].compute())

    def preprocess_reviews_text(self, text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
                result.append(WordNetLemmatizer().lemmatize(token, pos='v'))
        return result

    def summarize_reviews(self, business_id):
        self.review_Json['processed review'] = self.review_Json['text'].map(self.preprocess_reviews_text)
        dictionary = corpora.Dictionary(self.review_Json['processed review'].compute())
        dictionary.filter_extremes(no_below=15, no_above=0.75, keep_n=100000)
        bow_corpus = [dictionary.doc2bow(review) for review in self.review_Json['processed review'].compute()]


        tfidf = models.TfidfModel(bow_corpus)
        lda_model_tfidf = models.LdaMulticore(tfidf[bow_corpus], num_topics=10, id2word=dictionary, passes=2,
                                                     workers=4)

        for idx, topic in lda_model_tfidf.print_topics(-1):
            print('Topic: {} Word: {}'.format(idx, topic))




if __name__ == '__main__':

    cwd = os.getcwd()
    test = DataBase(cwd + "/miniCorpus/")
    #test.getSimillar("Arizona Biltmore Golf Club",True,True,True)
    test.summarize_reviews("Gyrez6K8f1AyR7dzW9fvAw")