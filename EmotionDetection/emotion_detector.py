import requests
import json

#emotion
def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    try:
        response = requests.post(url, json = input, headers=headers, timeout=3)
    except Exception as e:
        pass
    
    response='{"emotionPredictions":[{"emotion":{"anger":0.0043079085, "disgust":0.00041127237, "fear":0.0037504788, "joy":0.9918804, "sadness":0.014091322}, "target":"", "emotionMentions":[{"span":{"begin":0, "end":29, "text":"I am so happy I am doing this"}, "emotion":{"anger":0.0043079085, "disgust":0.00041127237, "fear":0.0037504788, "joy":0.9918804, "sadness":0.014091322}}]}], "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'

    formatted_response = json.loads(response)
    anger_score=formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score=formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score=formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score=formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score=formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    emotions={
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        }
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"]=dominant_emotion
    
    return emotions

if __name__=="__main__":
    totest="I love this new technology"
    response=emotion_detector(totest)
    
    print(response)