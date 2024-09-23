from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']
        
        # Fetch Quran verses
        quran_results = []
        try:
            quran_results = predict_quran(input_text)
        except Exception as e:
            quran_results = [f"Error fetching Quran results: {e}"]
        
        # Fetch Hadith verses
        hadith_results = []
        try:
            hadith_results = predict_hadith(input_text)
        except Exception as e:
            hadith_results = [f"Error fetching Hadith results: {e}"]
        
        return render_template("result.html", 
                               input_text=input_text, 
                               quran_results=format_results(quran_results), 
                               hadith_results=format_results(hadith_results))
    
    return render_template("index.html")

def predict_quran(input_text):
    """Fetches Quran verse predictions based on input_text."""
    response = requests.post(
        "https://mhdhrubo-quran-verse-finder.hf.space/run/predict", 
        json={"data": [input_text]}
    )
    response.raise_for_status()  # Ensure the request was successful
    data = response.json().get("data", [])
    
    if data:
        return data[0].split('\n')  # Split by new lines if results are joined
    return ["No Quran verses found."]

def predict_hadith(input_text):
    """Fetches Hadith verse predictions based on input_text."""
    response = requests.post(
        "https://mhdhrubo-hadith-verse-finder.hf.space/run/predict", 
        json={"data": [input_text]}
    )
    response.raise_for_status()  # Ensure the request was successful
    data = response.json().get("data", [])
    
    if data:
        return data[0].split('\n')  # Split by new lines if results are joined
    return ["No Hadith verses found."]

def format_results(results):
    """Ensures results are split into proper lines for display."""
    return [result.strip() for result in results if result.strip()]  # Strips empty or excess spaces

if __name__ == "__main__":
    app.run(debug=True)
