import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Translator Instance
authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    authenticator=authenticator,
    version='2018-05-01'
)
translator.set_service_url(url)


def english_to_french(english_text):
    # write the code here
    french_test = translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_test = french_test['translations'][0]['translation']
    return french_test


def french_to_english(french_text):
    # write the code here
    english_test = translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_test = english_test['translations'][0]['translation']
    return english_test
