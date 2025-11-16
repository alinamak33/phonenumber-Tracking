📱 Phone Location Tracker
This is a simple web application built with Flask that tracks the approximate location and carrier of a phone number using the phonenumbers library and displays the location on a Google Map.

✨ Features
Phone Number Validation: Uses the phonenumbers library for parsing and checking the phone number's location and carrier.

Location and Carrier Info: Displays the approximate location (country/region) and the service provider (carrier).

Google Maps Integration: Uses the Google Maps Geocoding API to get coordinates for the location and displays a marker on an embedded map.

Fallback Coordinates: Provides fallback country coordinates if the Google Maps API fails to find a specific location.

⚙️ Project Structure
The project is structured as follows:

tracking/
├── app.py              # Flask application logic
├── templates/
│   └── index.html      # Frontend HTML with map logic
├── static/
│   └── style.css       # Styling for the web page
└── locations.db        # Placeholder for an SQLite database (currently unused in app.py)
🛠️ Setup and Installation
Prerequisites
Python 3.x

A Google Maps API Key (The provided code uses a placeholder key: AIzaSyCEppTP44MCApw9vPnTH9eIIFpBt2rH9VQ).

Steps
Clone the Repository (or setup files): Ensure you have the files (app.py, templates/index.html, static/style.css, and locations.db) in a directory named tracking.

Install Dependencies:

Bash

pip install Flask phonenumbers requests
Run the Application:

Bash

python tracking/app.py
Access the App: Open your web browser and navigate to http://127.0.0.1:5000/.

💻 Technical Details
app.py
A Flask application with two routes:

/: Renders the index.html template.

/track (POST):

Takes a phone number from the form.

Prefixes with +91 if a country code is missing.

Uses phonenumbers.geocoder to get the location.

Uses phonenumbers.carrier to get the carrier name.

Makes a request to the Google Maps Geocoding API using the extracted location and a hardcoded API key (AIzaSyCEppTP44MCApw9vPnTH9eIIFpBt2rH9VQ).

If the API request is successful ('status' == 'OK'), it extracts the latitude and longitude.

If the API fails, it uses hardcoded fallback coordinates for countries like India, United States, United Kingdom, Canada, or Australia.

Returns a JSON response with the tracking information.

templates/index.html
The front-end interface for entering the phone number.

Contains a JavaScript function (document.getElementById('trackForm').onsubmit) that intercepts the form submission, makes an asynchronous POST request to /track, and updates the results.

Includes the Google Maps API script with the hardcoded API key (AIzaSyCEppTP44MCApw9vPnTH9eIIFpBt2rH9VQ).

The initMap JavaScript function initializes and displays the map with a marker at the returned coordinates.

locations.db
This is an SQLite database file. The schema includes a table named locations.

The locations table has the following columns:

id (INTEGER PRIMARY KEY AUTOINCREMENT)

user_id (TEXT)

name (TEXT)

latitude (REAL)

longitude (REAL)

timestamp (TEXT)

Note: This database is currently not used in the app.py logic but is present in the project structure.

⚠️ Important Note on API Key
The provided code contains a publicly visible Google Maps API Key (AIzaSyCEppTP44MCApw9vPnTH9eIIFpBt2rH9VQ). It is highly recommended to secure your API key by using environment variables or a configuration file and restricting its usage in the Google Cloud Console.
