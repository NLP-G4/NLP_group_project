import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import nltk
from wordcloud import WordCloud

def word_count_word_cloud(series, n = 1, x=10, title_name = None):
    '''
    This function takes in a words_list
    Creates bigrams
    Plots the counts on a bar chart and a wordcloud 
    Optional arguements to change customization
    - top_num: default 20, shows most common number of bigrams
    '''

    # create bigrams
    ngrams = pd.Series(nltk.ngrams(series.split(), n=n)).value_counts().head(x)
    
    # set up figuresize
    plt.figure(figsize = (20, x/2.5))
    
    # plot bigrams on left subplot
    plt.subplot(1, 2, 1)
    ngrams.sort_values(ascending = True).plot.barh(color = '#29af7f', alpha = .7, width = .9)
    plt.title(f'Top {x} ngrams: {title_name}')
    
    # create dictionary of words from the bigrams
    data = {k[0] : v for k, v in ngrams.to_dict().items()}
    
    # create wordcloud image
    img = WordCloud(background_color='white', width=400, height=400).generate_from_frequencies(data)
    
    # plot worcloud on right subplot
    plt.subplot(1, 2, 2)
    # show image
    plt.imshow(img)
    plt.axis('off')
    plt.title("Word Cloud", font = 'Arial', fontsize= 20)
    plt.show()

def plot_bigrams(series, n=2, x=10):
    '''
    This function will take in a pandas Series, and return a side-by-side plot of:
    - horizontal barchart
    - wordcloud
    '''
    
    plt.figure(figsize=(20,8))
    plt.subplot(1,2,1)
    ngrams = pd.Series(nltk.ngrams(series.split(), n=n)).value_counts().head(x)
    pd.Series(nltk.ngrams(series.split(), n=n)).value_counts().head(x).plot.barh()
    plt.title('Top 10 most common spam bigrams')
    plt.subplot(1,2,2)
    img = WordCloud(background_color='white', width=800, height=600).generate(series)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def ngrams_bar_wordcloud (text_list, title_list, n=2, x=10):
    '''
    - This function takes in 'text_list' = predefined list of predefined variables (each is a series)
    - 'title_list' is a list of strings to be used to label each series in the 'text_list'
    - 'n' is the number of ngrams, default is 2, making it a bigram
    - 'x' is the number of values you want returned, default to 10
    
    '''
        
    for i in  range (0, len(text_list)):
        plt.figure(figsize=(20,16))
        plt.subplot(1,2,1)
        ngrams = pd.Series(nltk.ngrams(text_list[i].split(), n=n)).value_counts().head(x).plot.barh()
        plt.title(f'{x} most common {title_list[i]} ngrams where n={n}')
        plt.subplot(1,2,2)
        img = WordCloud(background_color='white', width=800, height=600, max_words=x).generate(series)
        plt.imshow(img)
        plt.axis('off')
        plt.title(f'{x} most common {title_list[i]} ngrams where n={n}')
        #plt.tight_layout()
        plt.show()
