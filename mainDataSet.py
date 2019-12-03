import pandas as pd
import dask.dataframe as dd

### import DATA-SET ###
def makeMiniCorpusCopy (dir_path,name):
    with open(dir_path+"\\"+name+"_MinCorpus.json","w+") as miniFile:
        with open(dir_path+"\\"+name+".json") as json_file:
            for i in range(850):
                miniFile.write(json_file.readline())
        json_file.close()
        print (str(name+"_MinCorpus.json") +" is created! ")

makeMiniCorpusCopy("d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset","user")
makeMiniCorpusCopy("d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset","tip")
makeMiniCorpusCopy("d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset","review")
makeMiniCorpusCopy("d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset","photo")
makeMiniCorpusCopy("d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset","checkin")
# makeMiniCorpusCopy("d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset","business")



# Import Dataset
users = pd
usersMake = pd.DataFrame('d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset\\user.json',[0,2],columns=['user_id'])
tips = pd.read_json('d:\\documents\\users\\saarzeev\\Downloads\\yelpDataset\\review_MinCorpus.json', lines=True)
# print(users.head())

