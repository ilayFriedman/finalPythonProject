import time
import dask.bag as db
import dask.dataframe as dd
import json

class DataBase:

    def __init__(self,pathToDataSet):
        self.review_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\review.json").map(json.loads).to_dataframe()
        self.business_Json = db.read_text("C:\\Users\\User\\Desktop\\DATA_SET\\business.json").map(json.loads).to_dataframe()
        self.checkin_Json = db.read_text(pathToDataSet+"\\checkin.json").map(json.loads).to_dataframe()
        self.photo_Json = db.read_text(pathToDataSet+"\\photo.json").map(json.loads).to_dataframe()
        self.tip_Json = db.read_text(pathToDataSet+"\\tip.json").map(json.loads).to_dataframe()
        self.user_Json = db.read_text(pathToDataSet+"\\user.json").map(json.loads).to_dataframe()

    def getSimillar(self,bussinessName,categoriesSim,locationSim,hoursSim):
        print(self.business_Json[self.business_Json['name']==bussinessName].compute())


if __name__ == '__main__':
    test = DataBase("C:\\Users\\User\\Desktop\\DATA_SET")
    test.getSimillar("Arizona Biltmore Golf Club",True,True,True)