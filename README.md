# Kdrama-recommendation 
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
