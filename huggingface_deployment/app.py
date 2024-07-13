import pickle
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors
import gradio as gr

# Load the embeddings from the file
with open('embeddings.pkl', 'rb') as f:
    embeddings = pickle.load(f)

# Initialize the Nearest Neighbors model with cosine similarity
nbrs = NearestNeighbors(n_neighbors=10, metric='cosine').fit(embeddings)

# Load the dataset
df = pd.read_csv('quran_hadith.csv')

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def semantic_search(query, model, embeddings, nbrs):
    query_embedding = model.encode([query])[0]
    distances, indices = nbrs.kneighbors([query_embedding])
    similar_sentences = [(df['text'].iloc[idx], dist) for idx, dist in zip(indices[:10], distances)]
    return similar_sentences

# Gradio function
def search_interface(query):
    similar_sentences = semantic_search(query, model, embeddings, nbrs)
    sentences = [sentence for sentence, distance in similar_sentences]
    return sentences

pd.set_option('display.max_colwidth', None)


# Create Gradio interface
iface = gr.Interface(
    fn=search_interface,
    inputs=gr.Textbox(lines=2, placeholder="Enter your query here..."),
    outputs=gr.Textbox(label="Similar Sentences")
)

# Launch the interface
iface.launch(share=True)
