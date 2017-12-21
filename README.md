data set: ATNT-face-image400.txt  :

Text file. 
1st row is cluster labels. 
2nd-end rows: each colum is a feature vectors (vector length=28x23).

Total 40 classes. each class has 10 images. Total 40*10=400 images

----------------------------------------------------------------------------------------

data set: Hand-written-26-letters.txt :

Text file. 
1st row is cluster labels. 
2nd-end rows: each colum is a feature vectors (vector length=20x16).

Total 26 classes. each class has 39 images. Total 26*39=1014 images.


-------------------------------------------------------------------------------------
I used 5-fold cross-validation (CV) assess/evaluate the classifer.
I did CV using the following two full datasets.

ATNT face images data are generally easier, i.e., I get high classification accuracy.

Hand-written-letters data are harder to classify, i.e., I get lower classification accuracy.

I ran the classifier on hand-written-letter data only after I was confident 
that my classifier works correctly.

(A)
On ATNT data, 
run 5-fold cross-validation using  each of the four classifers:
KNN, centroid, linear regression and SVM.
Reported the classification accuracy on each classifier.
Remember, each of the 5-fold CV gives one accuracy. I presented all 5 accuracy numbers
for each classifier.

(C)
I have the ability to generate a training data and test data
from the ATNT or hand-written-letter data.

For example, from ATNT data, generate a training data using the first 9 images of a class 
and the test data using the remaining 1 image of the class. Thus the training data contains 
9*40=360 images and the list of corresponding class labels. The test data contains 1*40=40 images
and the list of corresponding class labels.
(The data in ATNT50 are generated in this way)

Another example. Generate a 2-class data for the 2-class SVM classifier.
For example, pick "C" and "F" classes from the hand-written-letter data. Using the first 30 images
in "C" and in "F" to form the training data. Using the remaining 9 images in each class to form the 
test data.



