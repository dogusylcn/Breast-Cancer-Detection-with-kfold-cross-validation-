import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt

# reading data
data = pd.read_csv('breast-cancer-wisconsin.data')
#we need columns between 2 and 10 in breast_cancer database
X = data.iloc[:,2:10]
#column of results
y = data.iloc[:,-1].values

#We used the minkowski method to determine the proximity of neighbors.
knn = KNeighborsClassifier(n_neighbors=9,metric='minkowski')

skor = cross_val_score(knn, X, y, cv=10, scoring='accuracy')

#calculation of sensitivity 
Rscores= cross_val_score(knn, X, y, cv=10, scoring='recall_weighted')
sensitivity=round((Rscores.mean()*100),3)


#calculation of balanced_accuracy 
Sscores= cross_val_score(knn, X, y, cv=10, scoring='balanced_accuracy')
balanced_accuracy=round((Sscores.mean()*100),3)


print("\n----------------------------------------------------------------")
print("\nCalculated Scores for K neighborhood value 10, KFold (cv) value 10 :\n\n ",skor)
print("\n----------------------------------------------------------------")
print("\nAvarage Trust :", skor.mean())
print("\n----------------------------------------------------------------")
print("\nAverage error rate: ",1-skor.mean())
print("\n----------------------------------------------------------------")
print("\nSensitivity : ",sensitivity)
print("\n----------------------------------------------------------------")
print("\nSpecificity : ",balanced_accuracy*2-sensitivity )
print("\n----------------------------------------------------------------")
print("\nFor the most efficient K number, examine the plot of knn_trust.png where the code is located.\n")
print("\n----------------------------------------------------------------")


# We compute the values for the k values in the range
k_range = range(1, 15)
k_scores = []

for k in k_range:
	knn = KNeighborsClassifier(n_neighbors=k,metric='minkowski')
	#Up to 10 kfold is applied
 #The average value in each fold operation is kept in k_scores
	skor = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
	k_scores.append(skor.mean())
print("\nAverage scores achieved for K between 1 and 20: \n\n ",k_scores)

# To display the best K number, we give K values from 1 to 10 and plot the results on the graph.
plt.bar(k_range,k_scores,color='blue',align='center', alpha=0.5)
plt.xlabel('K value')
plt.ylabel('Cross Validity Accuracy')
plt.title('Observing the best value for K')
plt.savefig("knn_trust.png")
