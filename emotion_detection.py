# imports the requests libraby
import requests

#defining the function for emotion_detector

def emotion_detector(text_to_analyze): 
    # passing text_to_analyzer
    # Define the Watson Emotion Detection API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #providing the required headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # input JSON with the text to analyze
    obj = { "raw_document": { "text": text_to_analyze } }
    
    # Sendes the post request to Watson NLP Service
    response = requests.post(url , headers = header, json = obj)
    
    # returning the respons as text
    return response.text