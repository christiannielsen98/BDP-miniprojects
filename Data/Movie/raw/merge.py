import pandas as pd
import numpy as np

imdb = pd.read_csv('imdb.csv')
tmdb = pd.read_csv('tmdb.csv')

imdb = imdb[['movie_title', 'genres', 'budget', 'language', 'duration', 'title_year', 'num_voted_users', 'imdb_score']]
tmdb = tmdb[['title', 'genres', 'budget', 'original_language', 'runtime', 'release_date', 'vote_count', 'vote_average']]

merge_column = ['title', 'genres', 'budget', 'language', 'duration', 'year', 'vote_count','score']
imdb.columns = merge_column
tmdb.columns = merge_column

tmdb = tmdb.dropna().reset_index(drop=True)
imdb = imdb.dropna().reset_index(drop=True)

# tmdb preprocess
N = tmdb.shape[0]
is_comedy_tmdb = np.zeros((N, 1)).astype(int)

for i in range(N):
    gen = pd.read_json(tmdb.loc[i, 'genres'])
    if 'name' in gen.keys():
        name_list = gen.name.tolist()
        if "Comedy" in name_list:
            is_comedy_tmdb[i] = 1

    tmdb.loc[i, 'year'] = tmdb.loc[i, 'year'][0:4]
tmdb.loc[:, "genres"] = is_comedy_tmdb

# imdb preprocess
imdb['title'] = imdb['title'].str.strip()
N = imdb.shape[0]
is_comedy_imdb = np.zeros((N, 1))
for i in range(N):
    gen = imdb.loc[i, 'genres'].split('|')
    if "Comedy" in gen:
            is_comedy_imdb[i] = 1

imdb.loc[:, "genres"] = is_comedy_imdb

merge = pd.concat([imdb, tmdb])

print(merge.title.duplicated(keep=False).sum())
print(merge.duplicated(keep=False).sum())

merge.to_csv('raw.csv', index=False)