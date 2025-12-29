"""
Flask server for the Emotion Detection web application.

Routes:
- /              : renders the main page.
- /emotionDetector: returns the emotion analysis for a given text.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """
    Analyze the provided text and return a formatted response.

    The text is expected in the query string parameter 'textToAnalyze'.
    If the emotion detector returns no dominant emotion, an error message is returned.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if not result or result.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )


def main():
    """Run the Flask development server on localhost:5000."""
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    main()
