'''Functions in this notebook

1. cleanFile - clean a single file
2. sentTokenizer - sentence tokenize a clean file
3. remove_punctuation - remove punctuation from a single word (used in the `clean_document` function)
4. lemmatize - lemmatize a single word (used in the `clean_document` function)
5. create_lemmatized_stopwords - create a lemmatized set of stop words (used in the `clean_document` function)
6. clean_document - create the final document, ready to be tokenized for model creation

'''


# clean a single file
def cleanFile(fname: str) -> str:
    '''Input: Single text file
       Output: String
       Transformations: 
           1. Remove lines containing specific strings that were found by inspecting a random set of the documents.
           2. Replace a few strings that were found by inspecting a random set of the documents.
           3. Remove all punctuation except commas and standard end of line punctuation.
    '''
    
    clean_file_text = ''
    fhand = open(fname)
    for line in fhand:
        new_line = ''
        if line.find('@') != -1: continue 
        elif line.find('Host') != -1: continue 
        elif line.find('User') != -1: continue
        elif line.find('VAX') != -1: continue
        elif line.find('USPS Mail:') != -1: continue 
        elif line.find('UUCP:') != -1: continue
        elif line.find('P.O. Box') != -1: continue
        # Added from Science documents
        elif line.find('Archive-name') != -1: continue
        elif line.find('Last-update') != -1: continue
        elif line.find('Distribution:') != -1: continue

        else: 
            new_line = line.replace('[IC]', '').replace('\n', ' ').replace('e.g.', ' ')
            
    # clean each string of all non-alphabetic characters except common punctuation
        clean_line = str()
        for char in new_line:
            if char in ['.', '!', '?', ',']:
                clean_line += char
            elif char == "'":
                clean_line += ''
            elif char.isalpha():
                clean_line += char
            else:
                clean_line += ' '
        clean_file_text += clean_line
        
    return clean_file_text


# sentence tokenize a clean file
# def sentTokenizer(cleanFile: str) -> list[str]:
def sentTokenizer(cleanFile: str) -> list:
    '''Input: string
       Output: list of strings, each being a sentence
       Transformations:
           1. Strip all white space from the front and back of the file
           2. Apply nltk.tokenize.sent_tokenize() to the entire document
    '''
    
    from nltk.tokenize import sent_tokenize
    
    sentences = sent_tokenize(cleanFile.strip())
    return sentences


# remove punctuation from a single word
def remove_punctuation(word: str) -> str:

    from nltk.stem import WordNetLemmatizer
    from nltk.corpus import stopwords    
    
    new_word = str()                                     # create a string without punctuation
    for char in word:                                    # look at each character in the word
        if char.isalpha():                               # determine if the character is alphabetic
            new_word += char                             # if it is alphabetic, add it to the new word
        else:
            new_word += ' '

    return new_word


# lemmatize a single word
def lemmatize(word: str) -> str:
    from nltk.stem import WordNetLemmatizer
    wnl = WordNetLemmatizer()
    new_word = wnl.lemmatize(word, pos="v")
    return new_word


# create a lemmatized set of stop words
def create_lemmatized_stopwords() -> str:
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

    return stop_words


# create the final document, ready to be tokenized for model creation
# def clean_document(sentTokenizer: list[str]) -> str:
def clean_document(sentTokenizer: list) -> str:
    '''Input: list of sentences associated with a single docuemtn
       Output: string, cleaned document
       Transformations:
           1. Remove Part of Speech Tags
           2. create lowercase
           3. remove punctuation
           4. lemmatize
           5. remove stop words
           6. strip away white space from the front and back of final string
    '''

    import nltk
    sentences = sentTokenizer
    tagged_word_sentences = nltk.pos_tag_sents([sent.split() for sent in sentences])
    stopwords = create_lemmatized_stopwords()
    new_document = str()
    for sentence in tagged_word_sentences:
        # print(sentence)
        new_sentence = str()
        for word, tag in sentence:
            # print(word, tag)
            if tag not in ['IN', 'NNP', 'NNPS', 'PRP', 'PRP$', 'WP', 'WP$', 'WRB']:
                # new_sentence += ' '+remove_punctuation(word.lower()).strip()
                new_word = lemmatize(remove_punctuation(word.lower()).strip())
                # print(new_word)
                if new_word not in stopwords:
                    new_sentence += ' '+new_word
        if new_sentence != '':
            new_document += ' '+new_sentence.strip()
        # print(new_sentence.lstrip())
        # print(new_sentence)
    
    return new_document.strip()

