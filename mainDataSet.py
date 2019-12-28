import time
import dask.bag as db
import dask.dataframe as dd
import json


def getDetailsOnMe(businessName):
    review_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\review.json").map(json.loads).to_dataframe()
    business_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\business.json").map(json.loads).to_dataframe()
    checkin_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\checkin.json").map(json.loads).to_dataframe()
    photo_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\photo.json").map(json.loads).to_dataframe()
    tip_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\tip.json").map(json.loads).to_dataframe()
    user_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\user.json").map(json.loads).to_dataframe()
    print(tip_Json.columns)

if __name__ == '__main__':
    getDetailsOnMe("efds")
