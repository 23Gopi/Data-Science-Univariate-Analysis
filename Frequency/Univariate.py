class Univariate():
    def quanQual(datas):
        quan=[]
        qual=[]
        for columnName in datas.columns:
            if(datas[columnName].dtypes == 'O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan, qual
    
    def frequencyTable(columnName, dataset):
        total_count = len(dataset[columnName].value_counts())
        table = pd.DataFrame(columns=["Unique_Values", "Frequency", "Relative_Frequency", "Cumulative_Requency"])
        table["Unique_Values"]=dataset[columnName].value_counts().index
        table["Frequency"]=dataset[columnName].value_counts().values
        table["Relative_Frequency"]=(table["Frequency"]/total_count)
        table["Cumulative_Requency"]=table["Relative_Frequency"].cumsum()
        return table
    
    def Univariate(dataset, quan):
        descriptive=pd.DataFrame(index=["Mean","Median","Mode","25%","50%","75%",
                                    "99%","100%","IQR", "1.5 Rule", "Lesser", "Greater", "Min", "Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["Mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descriptive[columnName]["100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["75%"] - descriptive[columnName]["25%"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["25%"] - descriptive[columnName]["1.5 Rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["75%"] + descriptive[columnName]["1.5 Rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
        return descriptive
    
    
    def replace_outliers(dataset, lesser, greater, descriptive):
        for columnName in lesser:
            dataset[columnName][dataset[columnName] < descriptive[columnName]["Lesser"]] = descriptive[columnName]["Lesser"]

        for columnName in greater:
            dataset[columnName][dataset[columnName] > descriptive[columnName]["Greater"]] = descriptive[columnName]["Greater"]

        return dataset
    
    def find_outliers(quan, descriptive):
        lesser = []
        greater = []

        for columnName in quan:
            if descriptive[columnName]["Min"] < descriptive[columnName]["Lesser"]:
                lesser.append(columnName)

            if descriptive[columnName]["Max"] > descriptive[columnName]["Greater"]:
                greater.append(columnName)

        return lesser, greater