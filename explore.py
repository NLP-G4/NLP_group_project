import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import nltk
from wordcloud import WordCloud

def random_color_func(word=None, font_size=None, position=None,  orientation=None, font_path=None, random_state=None):
    h = 140
    s = int(100.0 * 255.0 / 255.0)
    l = int(100.0 * float(random_state.randint(80, 200)) / 255.0)
    return "hsl({}, {}%, {}%)".format(h, s, l)



def word_count_word_cloud(series_list, title_names, n = 1, x=10, title_name = None):
    '''
    This function takes in a words_list
    Creates bigrams
    Plots the counts on a bar chart and a wordcloud 
    Optional arguements to change customization
    - top_num: default 20, shows most common number of bigrams
    '''
    for i in range (0, len(series_list)):
    
        # create bigrams
        ngrams = pd.Series(nltk.ngrams(series_list[i].split(), n=n)).value_counts().head(x)

        # set up figuresize
        plt.figure(figsize = (20, x/2.5))

        # plot bigrams on left subplot
        plt.subplot(1, 2, 1)
        ngrams.sort_values(ascending = True).plot.barh(color = '#29af7f', alpha = .7, width = .9)
        plt.title(f'Top {x}: {n}_ngrams: {title_names[i]}')

        # create dictionary of words from the bigrams
        data = {k[0] : v for k, v in ngrams.to_dict().items()}

        # create wordcloud image
        img = WordCloud(background_color= None, 
                    width=800, 
                    height=400, 
                    mode = 'RGBA', 
                    color_func = random_color_func,
                    max_words = 20).generate_from_frequencies(data)

        # plot worcloud on right subplot
        plt.subplot(1, 2, 2)
        # show image
        plt.imshow(img)
        plt.axis('off')
        plt.title("Word Cloud", font = 'Arial', fontsize= 20)
        plt.show()




