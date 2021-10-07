import pandas as pd
from pandas.core.indexes.timedeltas import TimedeltaDelegateMixin
from scipy import sparse
from sklearn.metrics.pairwise import pairwise_distances, cosine_similarity
import sys

gyms = pd.read_csv('usaClimbingGyms.csv')

pivot = pd.picot_table(gyms, index='gymName', columns='city', values='rating')

sparse_pivot = sparse.csr_matrix(pivot.fillna(0))
print(sparse_pivot)
sys.getsizeof(sparse_pivot)

recommender = cosine_similarity(sparse_pivot)
recommender_df = pd.DataFrame(recommender, columns = pivot.index, index=pivot.index)

Search = 'California'

for title in gyms.loc[gymName['title'].str.contains(search), 'title']:
    print(title)
    print(f'Average Rating: {pivot.loc[title, :].mean()}')
    print(f'Number of Ratings: {pivot.T[title].count()}')
    print('')
    print('2 Similar gyms:')
    print(recommender_df[title].sort_values(ascending=False)[1:6])
    print('------------------------------')
    print('')
