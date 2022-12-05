import pandas as pd
import numpy as np

dirty = pd.read_csv("./raw.csv")

N, m = dirty.shape

incon_dict = {
    "en":"English",
    "fr":"French",
    "de":"German",
    "da":"Danish",
    "ar":"Arabic",
    "cn":"Chinese",
    "he":"Hebrew",
    "hi":"Hindi",
    "hu":"Hungarian",
    "it":"Italian",
    "ko":"Korean",
    "ru":"Russian",
    "th":"Thai",
    "vi":"Vietnamese",
    "ro":"Romanian",
    "id":"Indonesian",
    "es":"Spanish",
    "pt":"Portuguese",
    "zh":"Chinese",
    "ja":"Japanese",
    "ru":"Russian"
}

for i in range(N):
    if dirty.loc[i, "language"] in incon_dict.keys():
        dirty.loc[i, "language"] = incon_dict[dirty.loc[i, "language"]]
dirty.to_csv("./inconsistency_clean_raw.csv", index=False)




