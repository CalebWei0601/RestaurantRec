from sentence_transformers import util
import torch

class model():
    def __init__(self, model, merged_reviews, restaurant_mapping, places):
        self.model = model
        self.merged_reviews = merged_reviews
        self.restaurant_mapping = restaurant_mapping
        self.places = places
        self.corpus_embeddings = self.model.encode(self.merged_reviews, convert_to_tensor=True)

    def predict(self, query):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        cos_scores = util.cos_sim(query_embedding, self.corpus_embeddings)[0]
        top_res = torch.topk(cos_scores, k=5)
        
        out = []
        for score, idx in zip(top_res[0], top_res[1]):
            out.append([self.merged_reviews[idx], self.places[self.restaurant_mapping[self.merged_reviews[idx]]], "(Score: {:.4f})".format(score)])

        return out
        