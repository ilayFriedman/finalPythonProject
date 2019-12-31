import time
import dask.bag as db
import dask.dataframe as dd
import json
import os
import nltk
nltk.download('wordnet')
import gensim
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

    def preprocess(self, text):
        result = []
        for token in gensim.utils.simple_preprocess(text):
            if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 2:
                result.append(WordNetLemmatizer().lemmatize(token, pos='v'))
        return result

    def getShitDone(self, business_id):
        # business_reviews = self.review_Json[self.review_Json['business_id'] == business_id].compute() # This gets only the business relevant reviews
        doc_sample = self.review_Json[self.review_Json['business_id'] == business_id]['text']

        print('original document: ')
        words = []
        for word in doc_sample.split(' '):
            words.append(word)
        print(words)
        print('\n\n tokenized and lemmatized document: ')
        print(self.preprocess(doc_sample))




if __name__ == '__main__':

    cwd = os.getcwd()
    test = DataBase(cwd + "/miniCorpus/")
    #test.getSimillar("Arizona Biltmore Golf Club",True,True,True)
    test.getShitDone("Gyrez6K8f1AyR7dzW9fvAw")