# def FeatureFunction(review: str) -> list[tuple[str, int]]:
def FeatureFunction(review: str) -> list:

    import numpy as np
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import stopwords

    # Create a set of stop words 
    STOP_WORDS = set(stopwords.words('english'))

    stop_words = set()
    for word in STOP_WORDS:
        new_word = str()                                     # create a string without punctuation
        for char in word:                                    # look at each character in the word
            if char.isalpha():                               # determine if the character is alphabetic
                new_word += char                             # if it is alphabetic, add it to the new word
        if new_word != '':
            stop_words.add(new_word)


    # instantiate important data types for storing processed data
    review_array = np.array(review.strip().lower().split())  # list of potential words from string
    dict_counts = dict()                                     # dictionary for holding word counts

    # Initialize wordnet lemmatizer
    wnl = WordNetLemmatizer()
    
    # consider each word, determine if any of its characters are not alphabetic
    for word in review_array:

        new_word = str()                                     # create a string without punctuation
        for char in word:                                    # look at each character in the word
            if char.isalpha():                               # determine if the character is alphabetic
                new_word += char                             # if it is alphabetic, add it to the new word
        if new_word != '':                                   # make sure the new string is not empty

            newer_word = wnl.lemmatize(new_word, pos="v")    # lemetize the word
            if newer_word not in stop_words:                 # check that the new word is not a common word listed in the stop words
            
                # update the word count for the new word
                if newer_word in dict_counts:                # determine if the new_word has been counted
                    dict_counts[newer_word] += 1
                else:                                        # add new words to the counts dictionary
                    dict_counts[newer_word] = 1
                
    output = list()                                          # list of (word, count) tuples
    for word in dict_counts:
        output.append((word, dict_counts[word]))
        
    return output





# type Weights = dict[str, list]
# def Score(review: str, weights: dict[str, list[float]]) -> list[float]:
def Score(review: str, weights: dict) -> list:
    ''' Calculate the positive and negative score of the given review given the weights '''

    # create the bag of words associated with the review instance
    bag_of_words = FeatureFunction(review)

    # found the positive class and negative class scores
    positive = int()
    negative = int()
    for word, count in bag_of_words:

        try:
            positive += weights[word][0]*count
            negative += weights[word][1]*count
        except:
            pass

    # create the output list
    output = list()
    output.append(positive)
    output.append(negative)
    
    return output





def check_string(text: str):
    return text.isalpha()





# def NaiveBayes(pos_reviews: list[str],
#                neg_reviews: list[str]) -> dict[str, list[float]]:

def NaiveBayes(pos_reviews: list,
               neg_reviews: list) -> dict:

    ''' Take positive and negative reviews and return a dictionary of weights for each of the unique words in the vocabulary '''
    
    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import stopwords

    # Create a set of stop words 
    STOP_WORDS = set(stopwords.words('english'))

    stop_words = set()
    for word in STOP_WORDS:
        new_word = str()                                       # create a string without punctuation
        for char in word:                                      # look at each character in the word
            if char.isalpha():                                 # determine if the character is alphabetic
                new_word += char                               # if it is alphabetic, add it to the new word
        if new_word != '':
            stop_words.add(new_word)

    # create weights dictionary
    naive_weights = dict()

    # Initialize wordnet lemmatizer
    wnl = WordNetLemmatizer()
    
    num_positive_words = 0
    for review in pos_reviews:
        review_list = review.strip().lower().split()
        
        for word in review_list:

            new_word = str()                                   # create a string without punctuation
            for char in word:                                  # look at each character in the word
                if check_string(char):                         # determine if the character is alphabetic
                    new_word += char                           # if it is alphabetic, add it to the new word
            if new_word != '':                                 # make sure the new string is not empty

                newer_word = wnl.lemmatize(new_word, pos="v")  # lemetize the word
                if newer_word not in stop_words:               # determine if the word is a stop word
            
                    num_positive_words += 1
                    if newer_word in naive_weights:
                        naive_weights[newer_word][0] += 1
                    else:
                        naive_weights[newer_word] = [1, 0]
    
    num_negative_words = 0
    for review in neg_reviews:
        review_list = review.strip().lower().split()
        
        for word in review_list:

            new_word = str()                                    # create a string without punctuation
            for char in word:                                   # look at each character in the word
                if check_string(char):                          # determine if the character is alphabetic
                    new_word += char                            # if it is alphabetic, add it to the new word
            if new_word != '':                                  # make sure the new string is not empty
                
                newer_word = wnl.lemmatize(new_word, pos="v")   # lemetize the word
                if newer_word not in stop_words:                # determine if the word is a stop word

                    num_negative_words += 1
                    if newer_word in naive_weights:
                        naive_weights[newer_word][1] += 1
                    else:
                        naive_weights[newer_word] = [0, 1]
 
            
    for item in naive_weights:
        naive_weights[item] = [naive_weights[item][0] / num_positive_words, naive_weights[item][1] / num_negative_words]
            
    return naive_weights

import math





# def LogWeights(nb_weights: dict[str, list[float]]) -> None:
def LogWeights(nb_weights: dict) -> None:
    ''' Apply the natural logarthm to each non-zero entry in the weights dictionary,
    setting zero entries to -10000 '''
    
    for item in nb_weights:
        nb_weights[item] = [math.log(num) if num != 0 else -10000 for num in nb_weights[item]]





# def PredAccuracy(pos_reviews: list[str],
#                  neg_reviews: list[str],
#                  weights: dict[str, list[float]]) -> float:

def PredAccuracy(pos_reviews: list,
                 neg_reviews: list,
                 weights: dict) -> float:

    ''' Determine the prediction accuracy of the given reviews using the indicated weights '''
    
    num_correct = int()
    
    for review in pos_reviews:
        review_scores = Score(review, weights)
        
        if review_scores[0] > review_scores[1]:
            num_correct += 1
            
    for review in neg_reviews:
        review_scores = Score(review, weights)
        
        if review_scores[0] < review_scores[1]:
            num_correct += 1
            
    prediction_accuracy = num_correct / (len(pos_reviews) + len(neg_reviews))
        
    
    return prediction_accuracy
    # return num_correct

# def trainNaiveBayes(pos_reviews: list[str],
#                     neg_reviews: list[str]) -> dict[str, list[float]]:
                 
def trainNaiveBayes(pos_reviews: list,
                    neg_reviews: list) -> dict:

    ''' Take positive and negative reviews and return a dictionary of Log weights for each of the unique words in the vocabulary '''

    weights = NaiveBayes(pos_reviews, neg_reviews) 
    LogWeights(weights)
    return weights

import itertools

def print_first_n_items(my_dict, n):
    for key, value in itertools.islice(my_dict.items(), n):
        print(f"{key}: {value}")

