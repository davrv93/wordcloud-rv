import pandas as pd
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from wordcloud import WordCloud


class Analysis:

    def __init__(self):
        self.max_words = 20
        self.max_font_size = 200
        self.scale = 3
        self.min_word_length = 4
        self.random_state = 4
        self.background_color = 'white'
        self.name_file = 'speech.txt'
        self.stop_words_sp = self.getStopWords()
        self.data = self.open(self.name_file)
        self.process(self.data)

    def open(self, name_file):

        f = open(name_file, "r")
        data = f.read()
        return data

    def getStopWords(self):
        stop_words_sp = set(stopwords.words('spanish'))
        return stop_words_sp

    def generateWordCloud(self, data, title):
        wordcloud = WordCloud(background_color=self.background_color,
                              stopwords=self.stop_words_sp,
                              max_words=self.max_words,
                              max_font_size=self.max_font_size,
                              scale=self.scale,
                              min_word_length=self.min_word_length,
                              random_state=self.random_state).generate(str(data))

        wordcloud.recolor(random_state=1)
        plt.figure(figsize=(20, 15))
        plt.title(title, fontsize=20, color='blue')
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()

    def process(self, data):

        first_line = data.split('\n')[0]

        datos = {"Header": [first_line, ],
                 "Body":              [data, ]
                 }
        Tablero = pd.DataFrame(datos)

        for cols in Tablero.index:
            self.generateWordCloud(Tablero.loc[cols, 'Body'],
                                   Tablero.loc[cols, 'Header'])


print('starting')
analysis = Analysis()
print('finished')
