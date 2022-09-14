# Repository description
This repository contains workflow and results of my bachelor research investigating
impact of information about all items in ranking list on point-wise ranking model.

Key points:
1. <b>Task statement.</b> NER task is a very important in NLP field. If target entity is:
   1. Date
   2. Number (currency)
   3. Entire sentence
   
    Then we can find entity-candidate in text by algorithm and rank all candidates to find
the best one to be our target entity.

    So, we have a <b>Ranking task</b>.
2. <b>Classic approaches</b> to solve task of list ranking:
   1. <b>Point-wise</b> - for each item in list calculate scalar <b>score</b> 
and use item with maximal score as an answer
   2. <b>Pair-wise</b> - take pair of items from the list, decide which item is the best.
Sort list based on that comparisons and return first item as an answer.
   3. <b>List-wise</b> - take entire list and select the best item using complicated 
error function or tricky model architecture.
3. <b>Proposed approach</b> is to use point-wise model, but for each item in list
input other items from the list in model too.
4. <b>Data</b>. To compare performance of proposed approach to classic one, 
2 datasets were used:
   1. `CUAD V1` (https://www.atticusprojectai.org/cuad) - open-source dataset of commercial
legal contracts. `Governing-Law` label was chosen as a target entity and
all sentences in document containing name of any state of USA were selected as entity-candidates.
   2. User reviews scrapped from Google Play. Most positive word in comment was chosen
as a target entity. 'Positiveness' of each word in corpus was estimated using model
`MultinominalNB` from scikit-learn library. All words from review were selected as
entity-candidates.
5. <b>Models tested:</b>
   1. MultinominalNB
   2. LogisticRegression
   3. KNeighboursClassifier
   4. SVC
   5. DecisionTreeClassifier
   6. XGBClassifier
6. <b>Results.</b> 
   1. Proposed approach has improved results of LogisticRegression on both
   datasets.
   2. Results of XGBClassifier has improved only for dataset of Google Play reviews. 
   3. Results of other models worsened on both datasets.
   
    Possible reasons:
   1. Curse of dimensionality (proposed approach increases number of features by 2 times,
but number of items in dataset doesn't change)
   2. Analysis of LogisticRegression's coefficients showed difficult structure of 
new information given by proposed approach
7. The possible directions of further researches:
   1. Dimension reduction techniques
   2. Test most popular architectures on neural networks: FCNN, 
CNN, RNN, Fully Convolutional Neural Network
   3. Use other metrics
   4. Use other datasets

More detailed description you could find in documentation and presentation included in this repository.

