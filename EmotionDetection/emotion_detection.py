import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=payload, headers=headers)

    # Convert response text (JSON string) to a Python dictionary
    response_dict = json.loads(response.text)

    # Extract the emotion scores dictionary
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    # Extract required emotions
    anger_score   = emotions["anger"]
    disgust_score = emotions["disgust"]
    fear_score    = emotions["fear"]
    joy_score     = emotions["joy"]
    sadness_score = emotions["sadness"]

    # Find dominant emotion (highest score)
    dominant_emotion = max(emotions, key=emotions.get)

    # Return the required output format
    return {
        "anger": anger_score,
        "disgust": disgust_score,
        "fear": fear_score,
        "joy": joy_score,
        "sadness": sadness_score,
        "dominant_emotion": dominant_emotion
    }