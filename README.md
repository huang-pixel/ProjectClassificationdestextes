# Classificationdestextes
## Corpus
Web pages in Chinese, English, French, Japanese, Korean and Turkish (25 texts each)


## References : Google scholar
[Language Identification from Text Using N-gram Based Cumulative Frequency Addition](https://www.researchgate.net/profile/Charles-Tappert/publication/265405649_Language_Identification_from_Text_Using_N-gram_Based_Cumulative_Frequency_Addition/links/54ac4c110cf2479c2ee7b15e/Language-Identification-from-Text-Using-N-gram-Based-Cumulative-Frequency-Addition.pdf)  

-> Language classifier using an ad-hoc Cumulative Frequency Addition of N-gram 
(in comparison with 2 other methods: rank-order statistics and Naïve Bayesian classifier)

[Automatic Language Identification in Texts: A Survey](https://www.jair.org/index.php/jair/article/view/11675)  

[Language Identification of Short Text Segments with N-gram Models](https://aclanthology.org/L10-1193/)
-> to complement some missing information

## State of the art 
### Statistical approach :  

- N-gram Based Cumulative Frequency Addition
- Rank-Order Statistics  

### Naïve Bayesian classification
- Retrieve the labeled corpus
- Cleaning the text to remove symbols
- Build a dataset
- Vectorization 
- Prediction 
- Get the result


## Testing Procedures 
●	Classification by Rank-Order Statistics 
-	tokenize each test string using N-grams of sizes 2, 3, 4, 5, 6 and 7 
-	no preprocessing of the string 
-	to classify the string using the rank-order statistical method, while tokenizing, count each N-gram and increment the counter if it occurred multiple times 
-	sort the N-grams and create the rank ordered lists
-	by issuing a simple SQL and joining the test N-grams and the Training N-grams table, create a candidate N-grams list <- use these to perform the distant measurement 
-	a default maximum distance of 1000 to a test N-gram without a match in the training database for any language
-	sum and sort the rank ordered distances from lowest to highest -> the language with the lowest number as the language category 

●	Classification using Cumulative Frequency Addition:
-	tokenize each test string using N-grams of sizes 2, 3, 4, 5, 6 and 7 and build an N-gram list 
-	no preprocessing of string
-	provide the N-grams participating in the classification of both the training and test N-grams
-	delete from the calculation any test N-gram with no match in the training database for any language

● Classification using Naïve Bayesian Classifier
-	use the same set of candidate N-grams from above for the NBC method
-	instead of addition, multiply the normalized frequencies of all candidate N-grams from each language of the training set
-	the language that produced the highest number = identified as the correct one

## Results 
### 3-grammes (ENG, TRK, FRA)
![image](https://user-images.githubusercontent.com/106084825/205982212-07d8453b-75b8-4d56-a6f9-633f160a3042.png)  

### Naïve Bayesien
![image](https://user-images.githubusercontent.com/106084825/205983292-722178cb-0eb1-448a-a2ba-167c23107ec4.png)

## Problems and Reflection 
● Script optimization is necessary to improve detection accuracy. Let's say we run with strange results, but we can't find a more reasonable solution for the moment
● For corpus preprocessing. We followed the experimental approach of the N gram papers (the authors did not perform this preprocessing process), but in practice we found that not performing this step would have had some impact on the subsequent results.
● We lack the time to perform each task in the project in more detail.




