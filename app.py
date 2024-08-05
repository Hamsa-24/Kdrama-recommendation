from flask import Flask, request, render_template, flash
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for the session
app.secret_key = 'b3c5d9f0b1e54c93a1c03dfd6c58a70e8c8d2f91e8a942b8b3e8a9f97b8d4937'  # Hard-coded secret key

# Load the data
try:
    df = pd.read_csv('drama_data.csv')
    df['title'] = df['title'].str.strip().str.lower()  # Normalize titles to lowercase and strip spaces
    print("Data loaded successfully.")
    print(df.head())  # Print the first few rows of the dataframe to verify data
except Exception as e:
    print(f"Error loading data: {e}")

# Function to recommend dramas based on input titles
def recommend_dramas(watched_titles):
    # Normalize input titles to lowercase and strip spaces
    watched_titles = [title.strip().lower() for title in watched_titles]
    
    # Verify input normalization
    print(f"Normalized watched titles: {watched_titles}")

    # Combine genres into a single string for TF-IDF
    df['combined_features'] = df['genres'].apply(lambda x: ' '.join(x.split(',')))

    # Initialize TF-IDF Vectorizer
    tfidf = TfidfVectorizer(stop_words='english')

    # Fit and transform the combined features
    tfidf_matrix = tfidf.fit_transform(df['combined_features'])

    # Compute the cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # Get indices of the watched titles
    indices = pd.Series(df.index, index=df['title']).drop_duplicates()

    # Debugging: Print out the indices
    print("Indices in DataFrame:", indices.head())

    # Handle titles not found in the dataset
    watched_indices = []
    missing_titles = []

    for title in watched_titles:
        if title in indices:
            watched_indices.append(indices[title])
        else:
            missing_titles.append(title)

    if missing_titles:
        flash(f"The following titles were not found in the dataset: {', '.join(missing_titles)}")
        print(f"Missing titles: {missing_titles}")

    # Return empty list if no valid titles were found
    if not watched_indices:
        print("No valid titles found in the dataset.")
        return []

    # Calculate similarity scores for the watched dramas
    sim_scores = sum(cosine_sim[watched_indices]) / len(watched_indices)

    # Sort scores and get indices of the top recommendations
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the titles of the top 5 recommendations
    recommended_indices = [i[0] for i in sim_scores if i[0] not in watched_indices][:5]

    recommendations = df['title'].iloc[recommended_indices].tolist()
    print(f"Recommendations: {recommendations}")

    return recommendations


# Route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the list of watched dramas from the form
        watched_dramas = request.form.getlist('dramas')
        print(f"Watched dramas: {watched_dramas}")
        # Get recommendations
        recommendations = recommend_dramas(watched_dramas)
        # Render the recommendations page with the recommended dramas
        return render_template('recommendations.html', recommendations=recommendations)
    return render_template('index.html')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
