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