"""Centroid"""

import numpy as np
from sklearn.neighbors.nearest_centroid import NearestCentroid
from matplotlib import pyplot as plt


train_label_final = []
test_label_final = []
train_data_final = []
test_data_final = []

def pickData(filename,class_numbers, training_instances, test_instances):


    data1 = np.genfromtxt(filename, delimiter=",")  ####  Reading File


    array = np.array(data1)
    data = array
    class_count = 0
    test_instance = test_instances
    training_instance = training_instances
    count = 1
    file_name = filename

    if (file_name == "HandWrittenLetters.txt"):
        class_count = 39
    elif (file_name == "ATNTFaceImages400.txt"):
        class_count = 10

    for i in range(len(class_numbers)):
        column_from = (class_numbers[i] - 1) * class_count
        column_to = column_from + class_count;
        training_column_end = column_to - test_instance

        train_label = data[0, column_from:training_column_end]
        train_data = data[1:, column_from:training_column_end]

        test_label = data[0, training_column_end:column_to]
        test_data = data[1:, training_column_end:column_to]

        if (count == 1):
            train_label_final = train_label
            test_label_final = test_label
            train_data_final = train_data
            test_data_final = test_data
            count = 0
        else:
            train_label_final = np.hstack((train_label_final, train_label))
            test_label_final = np.hstack((test_label_final, test_label))
            train_data_final = np.hstack((train_data_final, train_data))
            test_data_final = np.hstack((test_data_final, test_data))

    train_data_final_t = train_data_final.transpose()
    test_data_final_t = test_data_final.transpose()

    outfile(train_data_final, test_data_final, train_label_final, test_label_final)

    clf = NearestCentroid()
    clf.fit(train_data_final_t, train_label_final)
    predictions = clf.predict(test_data_final_t)
    print("Test set predictions:\n{}".format(clf.predict(test_data_final_t)))
    print("Test set accuracy: {:.2f}".format(clf.score(test_data_final_t, test_label_final)))


def outfile(train_data_final,test_data_final,train_label_final,test_label_final):
    np.savetxt('train_data_final.out',train_data_final, '%0.f')
    np.savetxt('test_data_final.out', test_data_final, '%0.f')
    np.savetxt('train_label_final.out',train_label_final, '%0.f')
    np.savetxt('test_label_final.out', test_label_final, '%0.f')


def charToInt(input):
    input = input.lower()
    output = []
    for character in input:
        number = ord(character) - 96
        output.append(number)
    return output



input = input('Which classes to be picked? Without spaces:')
pickData("HandWrittenLetters.txt",charToInt(input),30,9)


# list = (1,2,3,5,6,8,40,4,45)
# pickData("ATNTFaceImages400.txt",list,9,1)

