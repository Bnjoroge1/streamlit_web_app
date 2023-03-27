import streamlit as st
import requests

LANGUAGES = {'AutoDetect': 'auto', 'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar',
             'Armenian': 'hy',
             'Azerbaijani': 'az',
             'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 'Catalan': 'ca',
             'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (Simplified)': 'zh', 'Chinese (Traditional)': 'zh-TW',
             'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en',
             'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy',
             'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu',
             'Haitian Creole': 'ht',
             'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'he', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu',
             'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja',
             'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Kinyarwanda': 'rw', 'Korean': 'ko',
             'Kurdish (Kurmanji)': 'ku', 'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv',
             'Lithuanian': 'lt',
             'Luxembourgish': 'lb', 'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml',
             'Maltese': 'mt', 'Maori': 'mi', 'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (Burmese)': 'my',
             'Nepali': 'ne', 'Norwegian': 'no', 'Odia (Oriya)': 'or', 'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl',
             'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 'Russian': 'ru', 'Samoan': 'sm',
             'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 'Sindhi': 'sd', 'Sinhala': 'si',
             'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 'Sundanese': 'su', 'Swahili': 'sw',
             'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Tatar': 'tt', 'Telugu': 'te', 'Thai': 'th',
             'Turkish': 'tr',
             'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi',
             'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'}
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "92e0b3f2b4msh3c165a5b3bb5840p12dc96jsn4368636b3287",
    "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}


def translate_text(text, source_lang, target_lang):
    url = "https://text-translator2.p.rapidapi.com/translate"
    payload = f"source_language={source_lang}&target_language={target_lang}&text={text}"
    response = requests.request("POST", url, headers=headers, data=payload)
    content = response.json()
    return content['data']['translatedText'], content['data']['detectedSourceLanguage']['name']


# FrontEnd

st.title('Text Translator')

text = st.text_area('Enter text to translate:')
source_lang = st.selectbox('Source language:', options=list(LANGUAGES.keys()))
target_lang = st.selectbox('Target language:', options=list(LANGUAGES.keys()), index=1)

if st.button('Translate'):
    translation, detected_lang = translate_text(text, LANGUAGES[source_lang], LANGUAGES[target_lang])
    st.subheader(f'Translation: From {detected_lang} to {target_lang}')
    st.info(translation)
