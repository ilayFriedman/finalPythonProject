import csv

import nltk
import numpy as np
from collections import Counter
from fuzzywuzzy import fuzz
import string
import dask.bag as db
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('wordnet')
import gensim
from nltk.stem import WordNetLemmatizer
import gensim.models.doc2vec
import re
assert gensim.models.doc2vec.FAST_VERSION > -1, "This will be painfully slow otherwise"
import os

class DataBase:

    def __init__(self,path):
        self.review_Json = db.read_text(path + "selected_entries_reviews_30k.json").map(json.loads).to_dataframe()
        # self.business_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\business_MinCorpus.json").map(json.loads).to_dataframe()
        # self.checkin_Json = db.read_text(pathToDataSet+"\\checkin.json").map(json.loads).to_dataframe()
        # self.photo_Json = db.read_text(pathToDataSet+"\\photo.json").map(json.loads).to_dataframe()
        # self.tip_Json = db.read_text(pathToDataSet+"\\tip.json").map(json.loads).to_dataframe()
        # self.user_Json = db.read_text(pathToDataSet+"\\user.json").map(json.loads).to_dataframe()
        self.REPLACE_NO_SPACE = re.compile("[.;:!\'?,\"()\[\]]*")
        stopwords = ["look", "amaze", "ask", "tell", "know", "work", "think", "est", "les", "bite", "little", "use",
                     "pour", "leave", "right", "left", "hot", "star", "que", "appointment", "far", "felt", "start",
                     "knowledgeable", "actually", "seen", "job", "day", "visit", "busy", "local", "smaller", "big",
                     "neighborhood", "iced", "toast", "morning", "benedict", "getting", "phone", "family", "stay",
                     "thank", "hotel", "vegas", "favorite", "wasn", "special", "order", "table", "glad", "country",
                     "joint", "absolutely", "wish", "guys", "ready", "items", "future", "week", "sitting", "high",
                     "kind", "major", "venue", "machine", "extremely", "moved", "helpful", "phoenix", "lacking",
                     "especially", "like", "time", "food", "super", "eat", "shop", "husband", "wife", "great", "place",
                     "excellent", "good", "got", "nice", "come", "came", "go", "went", "best", "said", "try",
                     "definitely", "way", "they", "love", "going", "took", "pretty", "nice", "better", "amazing",
                     "delicious", "told", "awesome", "recommend", "sure", "looked", "told", "friendly", "line", "best",
                     "nice", "store", "overall", "won", "bit", "thing", "away", "probably", "want", "lot", "worth",
                     "point", "need", "gave", "looking", "maybe", "years", "house", "called", "having", "review",
                     "remember", "needed", "entire", "large", "thought", "loved", "small", "thing", "customer",
                     "perfect"]

        lemmatized_stopwords = []
        lemmatizer = WordNetLemmatizer()

        for token in stopwords:
            lemmatized_token = lemmatizer.lemmatize(token, pos='v')
            lemmatized_stopwords.append(lemmatized_token)
        self.domain_stopwords = gensim.parsing.preprocessing.STOPWORDS.union(set(lemmatized_stopwords))

    def similarity_By_Categories(self, bussinessName, minPercent):
        bussinessCategories = \
        self.business_Json[self.business_Json['name'] == bussinessName]['categories'].compute().tolist()[0].replace(
            ', ', ',').split(",")
        namesAns = []
        # print(bussinessCategories)
        # print("#############")
        for index, bussinessNameI in self.business_Json.iterrows():
            if bussinessNameI['categories'] is not None:
                categoryAnswers = []
                maxAns = []
                for bi in bussinessCategories:
                    # print(bussinessName['categories'].split(","))
                    for category in bussinessNameI['categories'].split(","):
                        # print(category.strip() + "," + bi + " : " + str(fuzz.partial_ratio(category.strip(), bi)))
                        categoryAnswers.append(fuzz.partial_ratio(category.strip(), bi))
                    maxAns.append(max(categoryAnswers))
                    categoryAnswers.clear()
                # print(maxAns)
                if (round(sum(maxAns) / len(maxAns), 3) >= minPercent and bussinessNameI['name'] != bussinessName):
                    namesAns.append([bussinessNameI['name'], round(sum(maxAns) / len(maxAns), 3) / 100])
                # print(round(sum(maxAns) / len(maxAns),3) )
                # print(bussinessName['name'])
                # print("----------------")
        # print(namesAns)
        return namesAns

    def similarity_By_GPS(self, bussinessName, maxRadius):
        import geopy.distance
        coordsX = self.business_Json[self.business_Json['name'] == bussinessName]['latitude'].compute().tolist()[0]
        coordsY = self.business_Json[self.business_Json['name'] == bussinessName]['longitude'].compute().tolist()[0]
        namesAns = []
        for index, bussinessNameI in self.business_Json.iterrows():
            calc = geopy.distance.distance((coordsX, coordsY),
                                           (bussinessNameI['latitude'], bussinessNameI['longitude'])).km
            if bussinessNameI['latitude'] is not None and bussinessNameI[
                'longitude'] is not None and calc < maxRadius and calc != 0:
                namesAns.append([bussinessNameI['name'], 1 - (calc / maxRadius)])
        # print(sorted(namesAns, key=lambda x: x[1], reverse=True))
        return sorted(namesAns, key=lambda x: x[1], reverse=True)

    '''
    @:return: Model
    '''

    def buildModel(self):
        cleanReviews = []
        ratesBinary = []
        for index, review in self.review_Json.iterrows():
            cleanReviews.append(self.REPLACE_NO_SPACE.sub("", review['text'].lower()))
            if int(review['stars']) < 4:
                ratesBinary.append(-1)  ## negative rate
            else:
                ratesBinary.append(1)  ## positive rate

        print("done iterating! now CV")
        cv = CountVectorizer(binary=True)
        cv.fit(cleanReviews)
        X = cv.transform(cleanReviews)
        print("done CV, now build")

    # FIND BEST C parameter
    #         X_train, X_val, y_train, y_val = train_test_split(X, ratesBinary, train_size=0.75)
    #         for c in [0.01, 0.05, 0.25, 0.5, 1]:
    #             lr = LogisticRegression(C=c)
    #             lr.fit(X_train, y_train)
    #             print("Accuracy for C=%s: %s"
    #                   % (c, accuracy_score(y_val, lr.predict(X_val))))

    # #SAVE THE MODEL & CV
    #         pickle.dump(cv, open("cv", "wb"))
    #         final_model = LogisticRegression(C=0.25)
    #         final_model.fit(X, ratesBinary)
    #         object = final_model
    #         filehandler = open("sentiment_analysis_model", 'wb')
    #         pickle.dump(object, filehandler)
    #         print("done save. now words!")
    # #GIVES THE BEST GOOD/BAD WORDS:
    #         feature_to_coef = {
    #             word: coef for word, coef in zip(
    #                 cv.get_feature_names(), final_model.coef_[0]
    #             )
    #         }
    #         for best_positive in sorted(
    #                 feature_to_coef.items(),
    #                 key=lambda x: x[1],
    #                 reverse=True)[:5]:
    #             print(best_positive)
    #         print("---------")
    #
    #         for best_negative in sorted(
    #                 feature_to_coef.items(),
    #                 key=lambda x: x[1])[:5]:
    #             print(best_negative)

    '''
    @:param: List of reviews
    @:return: List of occurrences (1=positive, -1 negative) -- BY MODEL
    '''

    def predictReviewsList(self, reviewsList):
        ans = []
        vectorizer = pickle.load(open("cv", "rb"))
        model = pickle.load(open("sentiment_analysis_model", "rb"))
        for comment in reviewsList:
            ans.append(model.predict(vectorizer.transform([self.REPLACE_NO_SPACE.sub("", comment.lower())]))[0])
        return ans

    '''
    @:param: bussienss name to search in DataSET
    @:return: List of occurrences (1=positive, -1 negative) -- BY RATES in dataset
    '''

    def useRateToPredict(self, bussinessID):
        ans = []
        bussinessRates = self.review_Json[self.review_Json['business_id'] == bussinessID][
            'stars'].compute().tolist()
        for rate in bussinessRates:
            if rate > 3:
                ans.append(1)
            else:
                ans.append(-1)
        return ans

    '''
    @:param: bussienss name to search in DataSET
    @:return: List [list of occurrences +-, tuples of precentages of negative,positive]
    '''

    def businessSentimentAnalysis_FromDATASET(self, bussinessName):
        bussinessID = \
        self.business_Json[self.business_Json['name'] == bussinessName]['business_id'].compute().tolist()[0]
        reviewsList = self.review_Json[self.review_Json['business_id'] == bussinessID]['text'].compute().tolist()
        print("\n------------------------\n".join(reviewsList))
        ans = self.useRateToPredict(bussinessID)
        print(ans)
        # return list: [0]= shows, [1]=precentages
        counter = Counter(ans)
        print([(i, round(counter[i] / len(ans) * 100.0, 2)) for i in counter])
        return (
        [self.useRateToPredict(bussinessID), [(i, round(counter[i] / len(ans) * 100.0, 2)) for i in counter],
         reviewsList])

    '''
    @:param: csv path for reviewsFile
    @:return: List [list of occurrences +-, tuples of precentages of negative,positive]
    '''

    def businessSentimentAnalysis_FromCSV(self, csvPath):
        with open(csvPath, "rt") as file:
            reader = csv.reader(file, delimiter=',')
            reviewsList = list(reader)
        print(reviewsList[0])
        ans = self.predictReviewsList(reviewsList[0])
        # print(ans)
        # return list: [0]= shows, [1]=precentages
        counter = Counter(ans)
        print([(i, round(counter[i] / len(ans) * 100.0, 2)) for i in counter])
        return (
        [self.predictReviewsList(reviewsList[0]), [(i, round(counter[i] / len(ans) * 100.0, 2)) for i in counter],
         reviewsList])

    def preprocess_reviews_text(self, text):
        result = []
        lemmatizer = WordNetLemmatizer()

        for token in gensim.utils.simple_preprocess(text):
            lemmatized_token = lemmatizer.lemmatize(token, pos='v')
            if lemmatized_token not in self.domain_stopwords and lemmatized_token not in string.punctuation and len(
                    lemmatized_token) > 2:
                result.append(lemmatized_token)
        return result

    def preprocess_tfidf(self, text):
        return " ".join(self.preprocess_reviews_text(text))

    def get_top_keywords(self, data, clusters, labels, n_terms):
        df = pd.DataFrame(data.todense()).groupby(clusters).mean()
        dict = {}
        for i, r in df.iterrows():
            print('\nCluster {}'.format(i))
            list = ','.join([labels[t] for t in np.argsort(r)[-n_terms:]])
            print(list)
            dict[i] = list.split(",")[:6]

        with open('clusters_labels.json', 'w') as fp:
            json.dump(dict, fp)

    def create_clusters(self):

        # Prepare docs as list of words and an index per doc
        processed_reviews = self.review_Json['text'].compute().values.tolist()
        tfidf = TfidfVectorizer(
            # max_df=0.95,
            max_features=8000,
            stop_words=self.domain_stopwords,
            analyzer='word',
            token_pattern='[a-zA-Z0-9]+',
            preprocessor=self.preprocess_tfidf
        )
        print("Created vectorizer.")
        tfidf.fit(processed_reviews)
        print("Vectorizer fitted.")
        pickle.dump(tfidf.vocabulary_, open("tfidf_vocabulary", 'wb'))

        text = tfidf.transform(processed_reviews)
        print("transformed reviews")
        # # max_k = 14
        # # iters = range(2, max_k + 1, 2)
        # #
        # # print("Started training KMeans...")
        # # sse = []
        # # for k in iters:
        # #     sse.append(
        # #         KMeans(n_clusters=k, init='k-means++', max_iter=100).fit(text).inertia_)
        # #     print('Fit {} clusters'.format(k))
        # #
        # # f, ax = plt.subplots(1, 1)
        # # ax.plot(iters, sse, marker='o')
        # # ax.set_xlabel('Cluster Centers')
        # # ax.set_xticks(iters)
        # # ax.set_xticklabels(iters)
        # # ax.set_ylabel('SSE')
        # # ax.set_title('SSE by Cluster Center Plot')
        # # plt.show()

        clusters = KMeans(n_clusters=10, init='k-means++', max_iter=100)
        clusters.fit(text)
        clusters_predict = clusters.predict(text)
        pickle.dump(clusters, open("tfidf_clusters.mdl", "wb"))

        self.get_top_keywords(text, clusters_predict, tfidf.get_feature_names(), 20)

    def get_text_prediction(self, reviews_lst):
        with open('clusters_labels.json') as json_file:
            data = json.load(json_file)

        print("Load and create vectorizer")
        loaded_vec = TfidfVectorizer(vocabulary=pickle.load(open("tfidf_vocabulary", 'rb')),
            # max_df=0.95,
            max_features=8000,
            stop_words=self.domain_stopwords,
            analyzer='word',
            token_pattern='[a-zA-Z0-9]+',
            preprocessor=self.preprocess_tfidf)
        processed_reviews = self.review_Json['text'].compute().values.tolist()
        loaded_vec.fit(processed_reviews)
        text = loaded_vec.transform(reviews_lst)

        loaded_kmeans = pickle.load(open("tfidf_clusters.mdl", "rb"))

        cluster_predict = loaded_kmeans.predict(text)
        df = pd.DataFrame(reviews_lst, columns=['review'])
        df['cluster'] = cluster_predict
        top_4_clusters = df.groupby('cluster').count().reset_index().sort_values('review', ascending=0)['cluster'].head(4).tolist()

        cluster_labels = []
        for cluster in top_4_clusters:
            cluster_labels.append(data[str(cluster)])

        return cluster_labels


def makeMiniCorpusCopy():
    with open("C:\\Users\\User\\Desktop\\DATA_SET\\review_MinCorpus_500K.json", "w+", encoding="utf8") as miniFile:
        with open("C:\\Users\\User\\Desktop\\DATA_SET\\review.json", encoding="utf8") as json_file:
            for i in range(500000):
                miniFile.write(json_file.readline())
        json_file.close()
        print(str("review_MinCorpus_500K.json") + " is created! ")



if __name__ == '__main__':
    pass
     # test = DataBase("C:\\Users\\User\\Desktop\\DATA_SET")
     # test.businessSentimentAnalysis_FromDATASET("Arizona Biltmore Golf Club")
     # test.businessSentimentAnalysis_FromCSV("rev")
     # test.buildModel()
    # makeMiniCorpusCopy()

    # cwd = os.getcwd()
    # test = DataBase(cwd + "/miniCorpus/")
    # test = DataBase(cwd + "/")
    #test.getSimillar("Arizona Biltmore Golf Club",True,True,True)
    # test.build_doc2vec_model("doc2vec.mdl")
    # test.create_clusters_save_parquet(doc2vec_model_path="5k/doc2vec.mdl", kmeans_path='5k/kmeans.mdl')
    # test.explore_data()
    # test.create_clusters()
    # print(test.get_text_prediction(["crab crab fish shrimp", "bar whiskey beer night shot"]))