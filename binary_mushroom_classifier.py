import io
import numpy
import pandas
import sklearn.utils
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score

mushroom_data = pandas.read_csv(r'C:\Users\haris\PycharmProjects\challenge22S\mushrooms.csv')
#print(mushroom_data.shape)
# print(mushroom_data.head)

edibility = pandas.get_dummies(mushroom_data['class'])
attributes = pandas.get_dummies(mushroom_data.drop('class', axis=1))
edibility = edibility.e
#print(edibility.head)

attributes_train, attributes_test, edibility_train, edibility_test = model_selection.train_test_split(
    attributes,
    edibility,
    test_size=0.30)

#print(edibility_train.shape)
#print(edibility_train.head)


mushroom_classifier = SVC(kernel='linear')
mushroom_classifier.fit(attributes_train, edibility_train)

predicted_edibility = mushroom_classifier.predict(attributes_test)

print(confusion_matrix(edibility_test,predicted_edibility))
print(classification_report(edibility_test,predicted_edibility))

exit()