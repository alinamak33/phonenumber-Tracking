from flask import Flask, render_template, request, jsonify
import phonenumbers
from phonenumbers import geocoder, carrier
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/track', methods=['POST'])
def track():
    number = request.form['number']
    try:
        # Add +91 if not present
        if not number.startswith('+'):
            number = '+91' + number

        phone_number = phonenumbers.parse(number, None)
        location = geocoder.description_for_number(phone_number, 'en')
        sim_carrier = carrier.name_for_number(phone_number, 'en')

        if not location:
            return jsonify({'success': False, 'error': 'Location not found for this number'})

        # ✅ Google Maps Geocoding API
        google_api_key = "AIzaSyCEppTP44MCApw9vPnTH9eIIFpBt2rH9VQ"
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_api_key}"
        response = requests.get(url).json()

        if response['status'] == 'OK':
            lat = response['results'][0]['geometry']['location']['lat']
            lng = response['results'][0]['geometry']['location']['lng']
        else:
            # ✅ Fallback to country-level coordinates
            fallback_coords = {
                "India": (20.5937, 78.9629),
                "United States": (37.0902, -95.7129),
                "United Kingdom": (55.3781, -3.4360),
                "Canada": (56.1304, -106.3468),
                "Australia": (-25.2744, 133.7751),
            }
            lat, lng = fallback_coords.get(location, (20.5937, 78.9629))

        return jsonify({
            'success': True,
            'number': number,
            'location': location,
            'carrier': sim_carrier if sim_carrier else "Unknown",
            'latitude': lat,
            'longitude': lng
        })

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
