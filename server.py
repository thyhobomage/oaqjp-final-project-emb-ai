from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    dominant_emotion = emotion_detector(text_to_analyze)

    if ['dominant_emotion'] == None:
        return "Invalid text! Please try again."

    anger = dominant_emotion['anger']
    disgust = dominant_emotion['disgust']
    fear = dominant_emotion['fear']
    joy = dominant_emotion['joy']
    sad = dominant_emotion['sadness']

    return (f"For the given statement, the system response is "
            f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, "
            f"'sadness': {sad}. "
            f"The dominant emotion is {dominant_emotion}")

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2998)