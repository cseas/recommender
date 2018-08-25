import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # statistical graphics
from scipy import stats
from ast import literal_eval # abstract syntax trees
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
# Singular Value Decomposition algorithm
from surprise import Reader, Dataset, SVD, evaluate

import warnings
warnings.simplefilter('ignore')

model = pd.read_csv('../input/movies_metadata.csv')
print(model.head())