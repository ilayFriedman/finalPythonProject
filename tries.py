import csv

import nltk

from dask.bag import read_text

import json



import gensim.models.doc2vec
import re
assert gensim.models.doc2vec.FAST_VERSION > -1, "This will be painfully slow otherwise"

if __name__ == '__main__':
    review_Json = read_text("C:\\Users\\User\\Desktop\\DATA_SET\\review_MinCorpus.json").map(json.loads).to_dataframe()
    business_Json = read_text("C:\\Users\\User\\Desktop\\DATA_SET\\business_MinCorpus.json").map(json.loads).to_dataframe()

    print(list(set(business_Json['business_id'].compute().tolist()) | set(review_Json['business_id'].compute().tolist())))
