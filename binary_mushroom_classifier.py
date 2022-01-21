import io
import numpy
import pandas
from sklearn.svm import SVC
from sklearn import model_selection
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, precision_score, recall_score

mushroom_data = pandas.read_csv(r'C:\Users\haris\Coding-Challenge-S22\mushrooms.csv')
# print(mushroom_data.shape)
# print(mushroom_data.head)

# get_dummies converts the string data in the csv to one hot encoding so that sk can use it,
# drop_first = True drops the first column ('e' for edibility status), leaving us with a column-vector
edibility = pandas.get_dummies(mushroom_data['class'], drop_first = True)
attributes = pandas.get_dummies(mushroom_data.drop('class', axis=1))
# print(edibility.head)

# split into 30% test 70% train. experimenting with ratios didn't yield a significant difference
attributes_train, attributes_test, edibility_train, edibility_test = model_selection.train_test_split(
    attributes,
    edibility,
    test_size=0.30)

# print(edibility_train.shape)
# print(edibility_train.head)

# can choose linear, gaussian, polynomial, sigmoid kernels. there is a drop in accuracy when using sigmoid
mushroom_classifier = SVC(kernel='linear')
mushroom_classifier.fit(attributes_train, numpy.ravel(edibility_train))

# test model
predicted_edibility = mushroom_classifier.predict(attributes_test)

print(confusion_matrix(edibility_test,predicted_edibility))
print(classification_report(edibility_test,predicted_edibility))

exit()