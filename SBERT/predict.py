from sentence_transformers import SentenceTransformer, util
import torch
from model import model, corpus_embeddings, merged_reviews, restaurant_mapping
import time

start = time.time()

query = 'I would like to eat some good salmon sashimi and sushi.  Preferably not too expensive.'

# Embed the query
query_embedding = model.encode(query, convert_to_tensor=True)

# compute cosine similarity between embeddings and find the top 5
cos_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]
top_res = torch.topk(cos_scores, k=5)

for score, idx in zip(top_res[0], top_res[1]):
    print(merged_reviews[idx], restaurant_mapping[merged_reviews[idx]], "(Score: {:.4f})".format(score))

end = time.time()
print(end-start)