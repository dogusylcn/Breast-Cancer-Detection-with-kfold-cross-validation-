# KFold-Cross-Validation-on-Breast_Cancer-Database

#Problem

Our problem in breast cancer is to be able to determine whether the tumor is benign or malignant. Our dataset is Dr. It consists of data collected by Wolberg from his own cases from 1989 to 1992. The feature in our data set is as follows. Attributes 2 through 10 were used to test the examples.


             Property - Value Range
    ---------------------------------------------
    1. Sample code number identification number 
    2. Cluster Thickness 1 - 10 
    3. Uniformity of Cell Size 1-10 
    4. Uniformity of Cell Shape 1 - 10 
    5. Marginal Adhesion 1 - 10 
    6. Single Epithelial Cell Size 1-10 
    7. Bare Nuclei 1 - 10 
    8. Soft Chromatin 1 - 10 
    9. Normal Nucleoli 1 - 10 
    10.  Mitoses 1-10 Grade 
    11.  (2 for benign, 4 for malignant)


#Application

KFold Cross Validation 10-fold technique was used in the program I wrote. The minkowski method was used for the proximity of the neighbors. Test and training data are divided into 10 equal parts, where our cross validation score (cv) is equal to 10. While I was writing the application, I added another piece of algorithm to my code that tries the neighborhood numbers from 1 to 15 to find the most suitable neighborhood number and prints it on the graph so that we can see the most appropriate number. Below you can see the most suitable k-numbers calculated for our data set. When this bar-graph code runs, it is created in the form of an image in the folder where the code is located. You can see the bars corresponding to the array value in the graphic below.
Here, the most efficient value for us is 9, as can be read from the graph and the array counterpart. (0.9664109121909632)


#Result

As a result, we reached a result of ninety-seven percent with the data we have and the kfold cv model I used. The model needs to be further developed and higher accuracy should be achieved. This study can be improved and will create more accurate data on breast cancer and positive developments for its detection.
