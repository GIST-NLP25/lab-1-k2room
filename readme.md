[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/hSwLlYWm)
#  Sequential Labeling Input Transform

Sequential labeling is a form of most of the problems to obtain special information in natural languages we use, such as Korean and English, and is a representative problem to solve symbols with abstract meaning in machine learning.

Data consisting of arbitrary symbols and labels are provided to verify the ability to construct a model for the format of the problem, rather than solving it with analysis of special domain-specific knowledge or qualities.

It verifies the ability to implement a method of configuring a model to receive sequential input of symbols.

1. One-Hot Representation
2. Trainable Word Embedding

## Method
1. The one-hot representation gives one symbol the only numeric ID, has only 1 value corresponding to that ID, and the rest is expressed as a vector with 0. The maximum length per symbol has a set maximum length that is used in the training set or larger in dimensions.

2. One-hot consists of vectors with continuous values in small dimensions, as the maximum length increases with more vocabulary. In addition, inputs with similar information are learned so that they can be gathered. For learning, we put vectors representing symbols as a set of model parameters and learn dictionaries like network parameters by connecting parameters according to the symbol's ID.

## Train Dataset

In this problem, test data is used the same as learning data to exclude verification of the model's generalization technology.
 * train set: simple_seq.train.csv
 * test set: simple_seq.test.csv

Input: Sequential Symbol (sequence, different length.)
Output: Class label

Input and output refer to objects that should be put in observational information from the perspective of the model and objects that should be predicted.

Fixed hyper-parameters.
* Number of class label : 19
* Input max length : 20

### Example
Each line of the learning data file represents one input observation information and output label information.

For example, all symbols starting with 'W' in the following samples are inputs. Class label that symbol starting with 'D' should predict.

W25,W26,W27,W19,W28,W29,W30,W31,W32,W33,W34,W35,W36,W37,W38,W39,W24,W40,D11

Input: W25,W26,W27,W19,W28,W29,W30,W31,W32,W33,W34,W35,W36,W37,W38,W39,W24,W40

Output: D11

## Problems and Submission Files

The purpose of this problem is to verify the ability to implement the part of connecting variable symbol sequences to the model after the vectorization process from basic file input to use them in neural network models.

To simplify the verification environment, the model implements a 3-layer feedforward network consisting of the following techniques:

An input is a long vector with vectors representing symbols attached (concatenate).

Model Details:
- batch normalization
- Xavier or He initialization
- cross-entropy loss
- sigmoid activation function
- learning rate scheduling
- stochastic gradient descent

Example of Model Setting:
- learning rate : 0.1
- weight decay : 0.99
- (data_input, hidden layer 1, hidden layer 2, output) = (vocabulary size x maximum length, 1000, 100, 19)
- (data_input, hidden layer 1, hidden layer 2, output) = (embedding vector dimension x maximum length, 1000, 100, 19)



### Problem 1 - symbol sequence input by one-hot representation

1. Load input symbol sequence
2. Generate dictionary and transform all the symbols of symbol sequence into One-hot representation
3. Vactorize symbol sequence
4. Padding (set different input length being same: add zero vector)
5. Design 3-layer feedforward network

### Problem 2 - symbol sequence input by trainable embedding

1. Load input symbol sequence
2. Replace generated dictionary into trainable word embedding
3. Vactorize symbol sequence
4. Padding (set different input length being same: add zero vector)
5. Design 3-layer feedforward network


### Score
If you show 100% accuracy based on the test set, you pass.
(Without the need for special generalization skills, 100% of the learning set is achievable.)


## Result

For scoring, please save the data obtained above under the name 'student ID_name_simple_seq.p#.answer.csv' in the same directory as the current file (directory where the .md file is located).
