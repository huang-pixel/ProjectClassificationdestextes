# Classificationdestextes
## Corpus
Web pages in Chinese, English, French, Japanese, Korean and Turkish (25 texts each)


## References 
“Language Identification from Text Using N-gram Based Cumulative Frequency Addition” 
-> Language classifier using an ad-hoc Cumulative Frequency Addition of N-gram 
(in comparison with 2 other methods: rank-order statistics and Naïve Bayesian classifier)

“Automatic Language Identification in Texts: A Survey”
“Language Identification of Short Text Segments with N-gram Models “
-> to complement some missing information

## Testing Procedures 
•	Classification by Rank-Order Statistics 
-	tokenize each test string using N-grams of sizes 2, 3, 4, 5, 6 and 7 
-	no preprocessing of the string 
-	to classify the string using the rank-order statistical method, while tokenizing, count each N-gram and increment the counter if it occurred multiple times 
-	sort the N-grams and create the rank ordered lists
-	by issuing a simple SQL and joining the test N-grams and the Training N-grams table, create a candidate N-grams list <- use these to perform the distant measurement 
-	a default maximum distance of 1000 to a test N-gram without a match in the training database for any language
-	sum and sort the rank ordered distances from lowest to highest -> the language with the lowest number as the language category 

•	Classification using Cumulative Frequency Addition:
-	tokenize each test string using N-grams of sizes 2, 3, 4, 5, 6 and 7 and build an N-gram list 
-	no preprocessing of string
-	provide the N-grams participating in the classification of both the training and test N-grams
-	delete from the calculation any test N-gram with no match in the training database for any language

•	Classification using Naïve Bayesian Classifier
-	use the same set of candidate N-grams from above for the NBC method
-	instead of addition, multiply the normalized frequencies of all candidate N-grams from each language of the training set
-	the language that produced the highest number = identified as the correct one

