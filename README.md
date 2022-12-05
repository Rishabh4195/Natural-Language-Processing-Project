# Natural-Language-Processing-Project
In this project I predicted hotel reviews positive or negative on the basis of ratings.
I performed different stpels like importing libraries and dataset, EDA, Visualization, data cleaning and Pre-Processing(tokenization, stemming, Lamnatiztion, wordcloud etc), Sentimental analysis, vectorization and model building with deployment.

Name of libraries are pandas, numpy, seaborn, matplolib, sklearn, textblob for sentimental analysis, nltk for removing stop words, stemming, lemnatization, wordcloud etc.

### EDA & Visualization
In step of EDA and visualization creating bixplot, lineplot, barplot, density plot, countplot, etc and checking statastical values, null values if availalbe in data set, removing duplicates etc.

### data cleaning and pre-processing-
(1) cleaning - removing numerical values, sysmobls etc
(2) pre-processing - lowering words, stemming on words and lamnatization of words, also removing stop words in given dataset.

### Model Building-
In this step created different models by use of sklearn library.
* List of Models
  (1) Logistic regression
  (2) Random Forest
  (3) Naive Bayes
  (4) MultinomialNB
  (5) LinearSVC
Also checked model accuracy by accuracy score, create confusion matrix and classification report of each models.

### Deployment
In this step use of Pandas pipeline feature allows us to string together various user-defined Python functions in order to build a pipeline of data processing. In pipeline use Logistic Regression.
I used LinearSVC for deplotment because it gives higher accuracy.
Run the model and checked model accuracy with unknown data and gives very nice accuracy and my model worked good.
After that creating PKL file for use in deployment.
Final step of deployment did in PyCharm IDE by use of \stramlit\.
