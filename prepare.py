# This is my Data Preparation Module for NLP

# imports
from requests import get
from bs4 import BeautifulSoup
import os
import unicodedata
import re
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from markdown import markdown
from sklearn.model_selection import train_test_split

def basic_clean(string):
    '''
    This funtion will take in a single string, 
    - lowercase all of the characters, 
    - normalize unicode characters, 
    - replace anything that is not a letter/number/whitespace/single quote.
    '''
    
    #lowercase all letters in the text
    string = string.lower()
    
    # Normalizaton: Remove inconsistencies in unicode charater encoding.
    # encode the strings into ASCII byte-strings (ignore non-ASCII characters)
    # decode the byte-string back into a string
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    
    # remove anything that is not a through z, a number, a single quote, or whitespace
    string = re.sub(r'[^\w\s]', '', string)
    return string

def remove_html(value):
    ''' Takes in one cell of a dataframe and returns it with html and markdown removed.'''
    # uses markdown to take in the value
    html = markdown(value)
    # remove html/markdown tags
    html = re.sub(r'<pre>(.*?)</pre>', ' ', html)
    html = re.sub(r'<code>(.*?)</code >', ' ', html)
    # make it into readable text with beautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # use the soup to find only the text
    text = ''.join(soup.findAll(text=True))
    # replace linebreaks
    text = text.strip().replace('\n', ' ')
    return text

def remove_all_html(df):
    #Apply remove_html to each cell in the column. Maybe iterate? Need to figure out how to use .loc for it
    # Then we need to replace each value in the cell with markdown removed
    # return the cleaned df.
    return df

def tokenize(string):
    '''
    This function takes in the result of my basic_clean function (a single, cleaned string) and tokenizes all the words in the string.
    It returns the tokenized string as a list
    '''
    
    # Create the tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()

    # Use the tokenizer
    string = tokenizer.tokenize(string, return_str=True)
    
    return string

def re_tokenize(string):
    '''uses regex expression to tokenize string, ignore any non-alpha/numeric strings'''
    tokenizer = RegexpTokenizer('\w+')

    # use tokenizer
    string = tokenizer.tokenize(string)

    string = ' '.join(string)

    return string

def stem(string):
    '''
    This function will take in a single string, perform a PorterStemmer, and return the stemmed string.
    '''
    
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Apply the stemmer to each word in our string.
    stems = [ps.stem(word) for word in string.split()]
    
    string = ' '.join(stems)

    
    return string

def lemmatize(string):
    '''
    This function will take in a single string, perform lemmatization, and return the lemmatized string.
    '''
    
    
    # Create the Lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of tokenized words.
    lemmas = [wnl.lemmatize(word) for word in string.split()] 
    
    # Join our list of words into a string again; assign to a variable to save changes.
    string = ' '.join(lemmas)
    
    return string

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    '''
    This function will take in a single string ('input_string') that has already been prepped, 
    remove all stop words, and return the string minus the stopwords.
    '''

    # define stopwords
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add 'extra_words' to stopword_list
    stopword_list = stopword_list.union(set(extra_words))
    
    # split words in string
    words = string.split()
        
    # create a list of words from my string with stopwords removed
    filtered_words = [word for word in words if word not in stopword_list]
    
    # join words in list back into strings
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

def drop_foreign_language(df):
    '''
    This function takes in a pandas DataFrame, along with an index list of observations to drop.
    It returns a pandas DataFrame with foreign language files removed.
    '''
    df = df.drop(labels=[1,4,12,18,19,28,31,44,54,67,68,72,74,79,81,87,95], axis=0)
    
    return df


def prep_article_data(df, column, tokenizer=tokenize, extra_words=[], exclude_words=[]):
    '''
    This function take in a df and the string name for a text column with 
    option to pass lists for extra_words and exclude_words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed.
    '''
    df = df.dropna()
    
    df = drop_foreign_language(df)
    
    df[f'cleaned_{column}'] = df[column].copy()\
                            .apply(remove_html)\
                            .apply(basic_clean)\
                            .apply(tokenizer)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df[f'stemmed_{column}'] = df[column].copy()\
                            .apply(remove_html)\
                            .apply(basic_clean)\
                            .apply(tokenizer)\
                            .apply(stem)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    df[f'lemmatized_{column}'] = df[column].copy()\
                            .apply(remove_html)\
                            .apply(basic_clean)\
                            .apply(tokenizer)\
                            .apply(lemmatize)\
                            .apply(remove_stopwords, 
                                   extra_words=extra_words, 
                                   exclude_words=exclude_words)
    
    return df

def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test