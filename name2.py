import string
import dask.bag as db
import dask.dataframe as dd
import json
import os
import pandas as pd
from joblib import dump, load
import matplotlib.pyplot as plt
import nltk
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np

nltk.download('wordnet')
import gensim
from nltk.stem import WordNetLemmatizer
import multiprocessing

import gensim.models.doc2vec
assert gensim.models.doc2vec.FAST_VERSION > -1, "This will be painfully slow otherwise"

from gensim.models.doc2vec import Doc2Vec, TaggedDocument

class DataBase:


    def __init__(self,pathToDataSet):
        # self.review_Json = db.read_text(pathToDataSet + "selected_entries_reviews_30k.json").map(json.loads).to_dataframe()
        self.review_Json = db.read_text(pathToDataSet + "review.json").map(json.loads).to_dataframe()
        # self.business_Json = db.read_text(pathToDataSet + "business.json").map(json.loads).to_dataframe()
        # self.checkin_Json = db.read_text(pathToDataSet + "checkin.json").map(json.loads).to_dataframe()
        # self.photo_Json = db.read_text(pathToDataSet + "photo.json").map(json.loads).to_dataframe()
        # self.tip_Json = db.read_text(pathToDataSet + "tip.json").map(json.loads).to_dataframe()
        # self.user_Json = db.read_text(pathToDataSet + "user.json").map(json.loads).to_dataframe()
        stopwords = ["look", "amaze", "ask", "tell","know","work","think","est","les","bite","little","use","pour","leave","right","left","hot","star","que","appointment","far","felt","start","knowledgeable","actually","seen","job","day","visit","busy","local","smaller","big","neighborhood","iced","toast","morning","benedict","getting","phone","family","stay","thank","hotel","vegas","favorite","wasn","special","order","table","glad","country","joint","absolutely","wish","guys","ready","items","future","week","sitting","high","kind","major","venue","machine","extremely","moved","helpful","phoenix","lacking","especially", "like", "time","food", "super", "eat", "shop", "husband", "wife", "great", "place", "excellent", "good", "got", "nice", "come", "came", "go", "went", "best", "said", "try", "definitely", "way", "they", "love", "going", "took", "pretty", "nice","better", "amazing", "delicious", "told", "awesome", "recommend" ,"sure", "looked", "told", "friendly", "line", "best", "nice", "store", "overall", "won", "bit","thing","away","probably","want","lot","worth","point","need","gave","looking","maybe","years","house","called","having","review","remember","needed","entire","large","thought","loved","small","thing","customer","perfect"]

        lemmatized_stopwords = []
        lemmatizer = WordNetLemmatizer()

        for token in stopwords:
            lemmatized_token = lemmatizer.lemmatize(token, pos='v')
            lemmatized_stopwords.append(lemmatized_token)
        self.domain_stopwords = gensim.parsing.preprocessing.STOPWORDS.union(set(lemmatized_stopwords))

    def getSimillar(self,bussinessName,categoriesSim,locationSim,hoursSim):
        print(self.business_Json[self.business_Json['name']==bussinessName].compute())

    def preprocess_reviews_text(self, text):
        result = []
        lemmatizer = WordNetLemmatizer()

        for token in gensim.utils.simple_preprocess(text):
            lemmatized_token =  lemmatizer.lemmatize(token, pos='v')
            if lemmatized_token not in self.domain_stopwords and lemmatized_token not in string.punctuation and len(lemmatized_token) > 2:
                result.append(lemmatized_token)
            # if token not in self.domain_stopwords and token not in string.punctuation and len(token) > 2:
            #     result.append(token)
        return result

    def preprocess_tfidf(self, text):
        return " ".join(self.preprocess_reviews_text(text))

    def get_top_n_words(self, corpus, n=None):
        """
        List the top n words in a vocabulary according to occurrence in a text corpus.

        get_top_n_words(["I love Python", "Python is a language programming", "Hello world", "I love the world"]) ->
        [('python', 2),
         ('world', 2),
         ('love', 2),
         ('hello', 1),
         ('is', 1),
         ('programming', 1),
         ('the', 1),
         ('language', 1)]
        """
        vec = CountVectorizer().fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0)
        words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        return words_freq[:n]

    def build_doc2vec_model(self, model_path, data_path='data/clustered_reviews.parquet'):
        # Preprocess reviews
        self.review_Json['processed review'] = self.review_Json['text'].map(self.preprocess_reviews_text)

        # Prepare docs as list of words and an index per doc
        processed_reviews = self.review_Json['processed review'].compute().values
        tagged_data = [TaggedDocument(words=processed_reviews[i], tags=[str(i)])
                       for (i, name) in enumerate(processed_reviews)]

        # Create doc2vec model
        common_kwargs = dict(
            vector_size=300, epochs=20, min_count=20,
            sample=0, workers=multiprocessing.cpu_count(), negative=5, hs=0,
        )
        model_doc2vec = Doc2Vec(dm=1, window=10, alpha=0.1, comment='alpha=0.1', **common_kwargs)
        model_doc2vec.build_vocab(documents=tagged_data)

        # Train model
        model_doc2vec.train(tagged_data, total_examples=model_doc2vec.corpus_count, epochs=model_doc2vec.epochs,
                            start_alpha=0.002,
                            end_alpha=-0.016)

        # Save model
        model_doc2vec.save(model_path)
        # Save df with new processed review column
        self.review_Json.to_parquet(data_path, engine='pyarrow')

    def create_clusters_save_parquet(self, doc2vec_model_path=False, data_path='data/clustered_reviews.parquet', kmeans_path='kmeans.mdl'):
        # Load trained doc2vec model
        if not doc2vec_model_path:
            doc2vec_model_path = "doc2vec.mdl"
            self.build_doc2vec_model(doc2vec_model_path)

        model_doc2vec = Doc2Vec.load(doc2vec_model_path)

        # Initialize and train KMeans on documents' vectors
        # iters = range(4, 15 + 1, 2)
        #
        # sse = []
        # for k in iters:
        #     sse.append(
        #         KMeans(n_clusters=k, random_state=20, init='k-means++', max_iter=100).fit(model_doc2vec.docvecs.vectors_docs).inertia_)
        #     print('Fit {} clusters'.format(k))
        #
        # f, ax = plt.subplots(1, 1)
        # ax.plot(iters, sse, marker='o')
        # ax.set_xlabel('Cluster Centers')
        # ax.set_xticks(iters)
        # ax.set_xticklabels(iters)
        # ax.set_ylabel('SSE')
        # ax.set_title('SSE by Cluster Center Plot')
        # plt.show()

        kmeans_model = KMeans(n_clusters=10, init='k-means++', max_iter=100)
        kmeans_model.fit(model_doc2vec.docvecs.vectors_docs)

        # Save KMeans model
        dump(kmeans_model, kmeans_path)

        # Add a cluster column to reviews' data
        df = pd.DataFrame({'cluster': kmeans_model.labels_.tolist()})
        cluster_dd = dd.from_pandas(df, npartitions=1).reset_index()
        df = dd.read_parquet(data_path, engine='pyarrow')

        df['cluster'] = cluster_dd['cluster']
        df.reset_index()

        # Save to disk
        df.to_parquet(data_path, engine='pyarrow')

    def create_doc_vetor(self, doc, doc2vec_model_path="doc2vec.mdl"):
        # Load trained doc2vec model
        if not doc2vec_model_path:
            doc2vec_model_path = "doc2vec.mdl"
            self.build_doc2vec_model(doc2vec_model_path)

        model_doc2vec = Doc2Vec.load(doc2vec_model_path)
        return model_doc2vec.infer_vector(self.preprocess_reviews_text(doc))

    def get_vector_cluster(self, vector, kmeans_model_path='kmeans.mdl'):
        # Load trained KMeans model
        if not kmeans_model_path:
            return None

        model_kmeans = load(kmeans_model_path)

        return model_kmeans.predict(vector)

    def explore_data(self):
        df = dd.read_parquet('data/clustered_reviews.parquet', columns=['processed review', 'cluster'], engine='pyarrow')
        # print(df.head())
        for i in range(10):
            df_selected = (df[df['cluster'] == i]['processed review']).compute()

            tokens = []
            df_selected.map(lambda review: [tokens.append(r) for r in review])
            print("cluster " + str(i) + ":\t" + str(self.get_top_n_words([" ".join(tokens)], 100)))

    def get_top_keywords(self, data, clusters, labels, n_terms):
        df = pd.DataFrame(data.todense()).groupby(clusters).mean()

        for i, r in df.iterrows():
            print('\nCluster {}'.format(i))
            print(','.join([labels[t] for t in np.argsort(r)[-n_terms:]]))


    def test(self):
        #self.review_Json['processed review'] = self.review_Json['text'].map(self.preprocess_reviews_text)

        # Prepare docs as list of words and an index per doc
        processed_reviews = self.review_Json['text'].compute().values.tolist()
        tfidf = TfidfVectorizer(
            min_df=5,
            max_df=0.95,
            max_features=8000,
            stop_words=gensim.parsing.preprocessing.STOPWORDS,
            analyzer='word',
            token_pattern='[a-zA-Z0-9]+',
            preprocessor=self.preprocess_tfidf
        )
        print("Created vectorizer.")
        tfidf.fit(processed_reviews)
        print("Vectorizer fitted.")
        # dump(tfidf, "tfidf_vectorizer.mdl")
        text = tfidf.transform(processed_reviews)
        print("transformed reviews")
        # max_k = 14
        # iters = range(2, max_k + 1, 2)
        #
        # print("Started training KMeans...")
        # sse = []
        # for k in iters:
        #     sse.append(
        #         KMeans(n_clusters=k, init='k-means++', max_iter=100).fit(text).inertia_)
        #     print('Fit {} clusters'.format(k))
        #
        # f, ax = plt.subplots(1, 1)
        # ax.plot(iters, sse, marker='o')
        # ax.set_xlabel('Cluster Centers')
        # ax.set_xticks(iters)
        # ax.set_xticklabels(iters)
        # ax.set_ylabel('SSE')
        # ax.set_title('SSE by Cluster Center Plot')
        # plt.show()


        clusters = KMeans(n_clusters=10, init='k-means++', max_iter=100).fit_predict(text)
        # dump(clusters, "tfidf_clusters.mdl")
        self.get_top_keywords(text, clusters, tfidf.get_feature_names(), 20)

if __name__ == '__main__':

    cwd = os.getcwd()
    test = DataBase(cwd + "/miniCorpus/")
    # test = DataBase(cwd + "/")
    #test.getSimillar("Arizona Biltmore Golf Club",True,True,True)
    # test.build_doc2vec_model("doc2vec.mdl")
    # test.create_clusters_save_parquet(doc2vec_model_path="5k/doc2vec.mdl", kmeans_path='5k/kmeans.mdl')
    # test.explore_data()
    test.test()