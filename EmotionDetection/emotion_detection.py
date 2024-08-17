import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=input_json, headers=headers)
    response_data = response.json()

    # Extract emotions and their scores from the 'emotionPredictions' list
    emotion_predictions = response_data.get('emotionPredictions', [])
    if emotion_predictions:
        emotions = emotion_predictions[0].get('emotion', {})

        # Extract and return the result
        result = {
            'anger': emotions.get('anger', None),
            'disgust': emotions.get('disgust', None),
            'fear': emotions.get('fear', None),
            'joy': emotions.get('joy', None),
            'sadness': emotions.get('sadness', None),
            'dominant_emotion': max(emotions, key=emotions.get)
        }
        return result
    else:
        return "No emotion predictions found in response"