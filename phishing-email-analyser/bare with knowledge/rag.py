from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

KNOWLEDGE_DIR = Path(__file__).resolve().parent / "knowledge" #you can use whatever file directory you want,I use knowledge for this


def load_knowledge():
    chunks = []

    for file in KNOWLEDGE_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        # Split documents into paragraph-sized chunks
        paragraphs = [
            paragraph.strip()
            for paragraph in text.split("\n\n")
            if paragraph.strip()
        ]

        for paragraph in paragraphs:
            chunks.append({
                "text": paragraph,
                "source": file.name
            })

    return chunks


def build_index(chunks):
    if not chunks:
        raise ValueError("No knowledge found in the knowledge folder.")

    vectorizer = TfidfVectorizer(stop_words="english")

    documents = [chunk["text"] for chunk in chunks]
    matrix = vectorizer.fit_transform(documents)

    return vectorizer, matrix


def retrieve_knowledge(query, chunks, vectorizer, matrix, top_k=3):
    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(query_vector, matrix)[0]

    best_indices = scores.argsort()[::-1][:top_k]

    results = []

    for index in best_indices:
        if scores[index] > 0:
            results.append({
                "text": chunks[index]["text"],
                "source": chunks[index]["source"],
                "score": float(scores[index])
            })

    return results
