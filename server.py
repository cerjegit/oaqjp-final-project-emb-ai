"""
Emotion Detection Server
"""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection Web App Using Flask")

def run_emotion_detection():
    """
    Main function to run the Emotion Detection application.
    """
    app.run(host="0.0.0.0", port=5000)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    text_to_detect = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_detect)
    formated_response = emotion_predictor(response)

    if formated_response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    return jsonify({
        'anger': formated_response['anger'],
        'disgust': formated_response['disgust'],
        'fear': formated_response['fear'],
        'joy': formated_response['joy'],
        'sadness': formated_response['sadness'],
        'dominant_emotion': formated_response['dominant_emotion']
    })

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    run_emotion_detection()
