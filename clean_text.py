import sqlite3
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import numpy as np

# connect to db
conn = sqlite3.connect("podcast_data.db")

# create cursor to execute SQL
cursor = conn.cursor()

# retrieve transcripts from db
cursor.execute("SELECT transcript FROM episodes")

# creates a list of tuples in `data`
data = cursor.fetchall()
transcripts = [entry[0] for entry in data]

# create list of cleaned transcripts using regex
no_punc_transcripts = []
for transcript in transcripts:
    new_tran = re.sub(r'[^\w\s]', '', transcript)
    no_punc_transcripts.append(new_tran)

# stop words list - base list gotten from vectorizer itself by passing stop_words='english'
stop_words = ['be', 'five', 'mine', 'is', 'yourselves', 'who', 'would', 'side', 'find', 'namely', 'forty', 'anywhere',
              'others', 'from', 'seeming', 'thereupon', 'hasnt', 'thin', 'de', 'someone', 'anyone', 'ourselves',
              'whatever', 'seemed', 'un', 'his', 'enough', 'done', 'part', 'for', 'alone', 'fire', 'only', 'behind',
              'itself', 'once', 'herein', 'them', 'sincere', 'thereby', 'nor', 'against', 'empty', 'thus', 'cannot',
              'here', 'now', 'found', 'whoever', 'because', 'am', 'back', 'of', 'somewhere', 'everyone', 'between',
              'serious', 'hereafter', 'whereafter', 'any', 'can', 'thence', 'amount', 'after', 'system', 'eg', 'beyond',
              'when', 'before', 'same', 'rather', 'beforehand', 'full', 'about', 'thick', 'whereby', 'due',
              'themselves', 'further', 'off', 'with', 'was', 'in', 'first', 'front', 'however', 'ltd', 'cant', 'must',
              'already', 'i', 'well', 'my', 'also', 'wherein', 'out', 'detail', 'couldnt', 'indeed', 'mostly', 'call',
              'they', 'seems', 'you', 'always', 'beside', 'hereby', 'move', 'while', 'fifteen', 'more', 'less', 'last',
              'their', 'often', 'hers', 'do', 'co', 'whence', 'some', 'much', 'by', 'thereafter', 'latterly', 're',
              'are', 'these', 'but', 'this', 'and', 'on', 'hereupon', 'the', 'if', 'within', 'third', 'ours', 'our',
              'fifty', 'show', 'etc', 'down', 'something', 'almost', 'so', 'other', 'most', 'anyhow', 'sometimes',
              'none', 'nothing', 'fill', 'himself', 'otherwise', 'inc', 'six', 'your', 'everything', 'whither', 'no',
              'up', 'eleven', 'afterwards', 'both', 'together', 'twelve', 'interest', 'around', 'whom', 'as',
              'wherever', 'yours', 'been', 'many', 'becomes', 'she', 'sometime', 'whole', 'cry', 'top', 'could',
              'becoming', 'sixty', 'ever', 'nobody', 'yourself', 'we', 'us', 'keep', 'amoungst', 'toward', 'thru',
              'become', 'therefore', 'such', 'besides', 'one', 'her', 'hence', 'or', 'ie', 'noone', 'amongst', 'an',
              'next', 'whereas', 'how', 'under', 'give', 'own', 'along', 'put', 'may', 'every', 'never', 'though',
              'everywhere', 'nowhere', 'that', 'upon', 'each', 'has', 'during', 'again', 'eight', 'became', 'into',
              'bottom', 'mill', 'him', 'across', 'anyway', 'will', 'it', 'which', 'two', 'myself', 'get', 'anything',
              'still', 'at', 'through', 'even', 'seem', 'go', 'name', 'since', 'meanwhile', 'whose', 'made', 'onto',
              'perhaps', 'than', 'without', 'should', 'twenty', 'moreover', 'being', 'although', 'nevertheless', 'nine',
              'too', 'elsewhere', 'via', 'ten', 'former', 'were', 'four', 'whereupon', 'among', 'whenever', 'con',
              'then', 'yet', 'else', 'whether', 'where', 'had', 'latter', 'why', 'please', 'all', 'not', 'somehow',
              'what', 'either', 'throughout', 'he', 'until', 'very', 'might', 'a', 'except', 'herself', 'over',
              'therein', 'to', 'several', 'take', 'see', 'me', 'describe', 'above', 'those', 'there', 'towards', 'per',
              'another', 'few', 'have', 'its', 'bill', 'least', 'neither', 'three', 'hundred', 'below', 'formerly']
custom_stop_words = ['rebecca', 'nguyen', 'wynne', 'wynn', 'cxo', 'soulful', 'doctor', 'dr', 'ciso']
for word in custom_stop_words:
    stop_words.append(word)

# convert podcast transcripts to TF-IDF vectors
vectorizer = TfidfVectorizer(stop_words=stop_words)
tfidf_matrix = vectorizer.fit_transform(no_punc_transcripts)

# compute cosine similarity between podcast titles
similarity_matrix = cosine_similarity(tfidf_matrix)


def print_similarity_scores(trans: "list of transcripts" = None, thresh: float = 0):
    """Prints all similarity scores over threshold. Default threshold is 0, so prints all scores."""
    if trans is None:
        trans = no_punc_transcripts
    for i in range(len(trans)):
        for j in range(i + 1, len(trans)):
            if similarity_matrix[i, j] > thresh:
                print(f"Similarity score between transcript {i} and transcript {j}: {similarity_matrix[i, j]}")


def top_three_podcasts(podcast: "int of podcast index in matrix"):
    """Returns top 3 similar podcasts for a given podcast index"""
    # Get similarity scores for the specified podcast
    scores = similarity_matrix[podcast]
    # Exclude similarity score with itself by setting to -1
    scores[podcast] = -1
    # Find the indices of the top 3 similarity scores
    top_indices = np.argsort(scores)[::-1][:3]
    return top_indices

# # print top 3 similar podcast episode numbers for each episode
# for n in range(len(no_punc_transcripts)):
#     print(f"The top 3 similar podcasts for episode {n + 1} are: {top_three_podcasts(n) + 1}")





conn.commit()
conn.close()
