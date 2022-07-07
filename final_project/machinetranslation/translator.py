"""
Python Project for AI course, Final assignment.
Module containing translation functions.
"""
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv
load_dotenv()
url = os.environ['{url}']
apikey = os.environ['{apikey}']
version = os.environ['{version}']

# Add code to create an instance of the IBM Watson Language translator
authenticator = IAMAuthenticator( apikey )
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)
language_translator.set_service_url( url )



def english_to_french(english_text):
    """ Function to translate English text to French """
    # Retrieve the Detailed Response object.
    translation = language_translator.translate(
        text=english_text,
        model_id='fr-en').get_result()
    # Get translation as a string.
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """ Function to translate French text to English """
    # Retrieve the Detailed Response object.
    translation_respose = language_translator.translate(
        text=french_text,
        model_id='en-fr')
    translation = translation_respose.get_result()
    # Get translation as a string.
    english_text = translation['translations'][0]['translation']
    return english_text