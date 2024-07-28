from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        input_text = request.form['text']
        try:
            output_text = predict_sentence(input_text)[0]
        except Exception as e:
            output_text = f"An error occurred: {e}"
        return render_template("result.html", input_text=input_text, output_text=output_text)
    else:
        return render_template("index.html")

def predict_sentence(input_text):
    response = requests.post("https://mhdhrubo-quran-hadith-verse-finder.hf.space/run/predict", json={
        "data": [
            input_text
        ]
    })
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()["data"]
    return data

if __name__ == "__main__":
    app.run(debug=True)
