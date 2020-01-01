import time
import dask.bag as db
import dask.dataframe as dd
import json
import os
import nltk
nltk.download('wordnet')
import gensim
from gensim import corpora, models
from nltk.corpus import wordnet as wn
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
        self.domain_stopwords = ("super", "eat", "shop", "husband", "wife", "great", "place", "excellent", "good")

    def getSimillar(self,bussinessName,categoriesSim,locationSim,hoursSim):
        print(self.business_Json[self.business_Json['name']==bussinessName].compute())

    def preprocess_reviews_text(self, text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2 and token not in self.domain_stopwords:
                result.append(WordNetLemmatizer().lemmatize(token, pos='v'))
        return result

    def summarize_reviews(self, business_id):
        self.review_Json['processed review'] = self.review_Json['text'].map(self.preprocess_reviews_text)
        dictionary = corpora.Dictionary(self.review_Json['processed review'].compute())
        dictionary.filter_extremes(no_below=15, no_above=0.50, keep_n=100000)
        bow_corpus = [dictionary.doc2bow(review) for review in self.review_Json['processed review'].compute()]


        num_of_topics = 70
        tfidf = models.TfidfModel(bow_corpus)
        lda_model_tfidf = models.LdaMulticore(tfidf[bow_corpus], num_topics=num_of_topics, id2word=dictionary, passes=7,
                                                     workers=4, alpha=[0.00001]*num_of_topics, eta=[0.00001]*len(dictionary.keys()))

        for idx, topic in lda_model_tfidf.print_topics(-1):
            print('Topic: {} Word: {}'.format(idx, topic))

        # print("review: " + str(bow_corpus[18]))
        # print(str(lda_model_tfidf[bow_corpus[18]]))

        new_text = 'We had dinner at the Bellagio Buffet last night. The service was OK. Our server was great but kind of forgot about us towards the end of our visit. The food was cold. The only good thing there was the crab legs because they\'re suppose to be cold and the tacos because it was freshly made. The food was under a single lamp that didn\'t heat the food at all. We let the server know that the food was cold and he told the manager that was in charge. All she did was come over to ask what the problem was and said she was going to talk to the chief. Have no idea what actually happened though because we didn\'t see her after that. Half the buffet was closed as well so there wasn\'t that many options. I must say i rather go to the Rio buffet. For a high end casino this was a horrible experience.'
        tokens = self.preprocess_reviews_text(new_text)
        print(str(lda_model_tfidf[dictionary.doc2bow(tokens)]))



if __name__ == '__main__':

    cwd = os.getcwd()
    #test = DataBase(cwd + "/miniCorpus/")
    test = DataBase(cwd + "/    ")
    #test.getSimillar("Arizona Biltmore Golf Club",True,True,True)
    test.summarize_reviews("Gyrez6K8f1AyR7dzW9fvAw")