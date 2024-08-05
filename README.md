# Kdrama-recommendation System

# Part 1

The part 1 of this project is a Kdrama Recommendation System that leverages collaborative filtering and content-based filtering techniques to provide personalized drama recommendations. Users can input their watched dramas, and the system will suggest new Kdramas that align with their tastes.

The recommendation system is built using Python and popular libraries such as Pandas, BeautifulSoup, Surprise, and Scikit-learn. It uses web scraping to collect data from MyDramaList, simulates user interactions for collaborative filtering, and calculates genre-based similarities for content-based recommendations.

### Features
Collaborative Filtering: Uses simulated user interactions to provide recommendations based on similar users' preferences.
Content-Based Filtering: Recommends dramas similar to a user's favorite titles based on genre and content similarity.
Hybrid Approach: Combines collaborative and content-based filtering for robust recommendations.
Web Scraping: Automatically collects Kdrama data from MyDramaList, including titles, genres, and ratings.
Dynamic User Data Simulation: Generates dummy user ratings to enable collaborative filtering.

### Installation
**Clone the Repository**
git clone https://github.com/Hamsa-24/Kdrama-recommendation/
cd kdrama-recommendation-system

**Set Up a Virtual Environment** 
python -m venv venv
source venv/bin/activate  #On Windows: venv\Scripts\activate

**Install Required Packages**
pip install -r requirements.txt

**Install Additional Packages in Google Colab**
If running in Google Colab, install the following packages:
!pip install beautifulsoup4 requests pandas scikit-surprise

### Future Enhancements:
Web Application:

Considering deploying a web application using Flask or Django.

Allow users to input watched dramas and receive recommendations in real-time.

Cloud Hosting:

Deploying the application on cloud platforms like Heroku, AWS, or Google Cloud.

Integration with Real User Data:

Incorporating real user interactions to enhance recommendation accuracy.

Advanced Algorithms:

Exploring other deep learning models for improved predictions.

User Interface Improvements:

Developing a more interactive and user-friendly web or mobile interface.

Localization and Multilingual Support:

Implementing support for multiple languages to reach a broader audience.

# Part 2
Recommend Kdramas to users based on five previously watched dramas.

This repository contains a Kdrama recommendation system that suggests Korean dramas to users based on their previously watched 5 series. The system leverages a dataset of popular Kdramas to make personalized recommendations.

### Features:
Personalized Recommendations: Users receive Kdrama suggestions tailored to their viewing history.

Easy to Use Interface: The web app features a simple and intuitive design for easy navigation.

Extensive Dataset: Includes a comprehensive collection of Kdramas for diverse recommendations.

### Project Structure
app.py: The main application file for executing the recommendation system.

drama_data.csv: A dataset containing information on various Kdramas, including genres. (Has to be improved)

index.html: The landing page for the web application, where users can input their previously watched dramas.

recommendations.html: The page displaying the recommended Kdramas to the user.

### How It Works
Input: Users enter five Kdramas they have previously watched and enjoyed.

Processing: The system analyzes the input and searches the dataset for similar dramas based on genres, ratings, and other features.

Output: The app displays a list of recommended Kdramas that align with the user's tastes.

### Getting Started
**Clone the Repository:**

git clone https://github.com/yourusername/kdrama-recommendation-system.git

**Navigate to the Directory:**

cd kdrama-recommendation-system

**Install Dependencies:**

pip install -r requirements.txt

**Run the Application:**

python app.py

**Access the App:**

Open your browser and go to http://localhost:5000.

### Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

### License
This project is licensed under the MIT License. See the LICENSE file for details.
