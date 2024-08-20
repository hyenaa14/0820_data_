import pandas as pd

header=['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS',
        'RAD','TAX','PTRATIO','B','LSTAT','MEDV']
data=pd.read_csv("./data/3.housing.csv", delim_whitespace=True, names=header)


array=data.values
#독립변수/ 종속변수
X=array[:,0:13]
Y=array[:,13]

#학습데이터/ 테스트데이터
X_train, X_test, Y_train, Y_test= train_test_split(X,Y,test_size=0.2)
mpdel=LinearRegression()
model.fit(X_train, Y_train)
y_pred= model.predict(X_test)

plt.scatter()