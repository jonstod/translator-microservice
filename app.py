from flask import Flask, request
from translator import Translator
from flask_cors import CORS

# Configuration

app = Flask(__name__)
CORS(app)

# Routes

@app.route("/", methods=['GET'])
def translate_text():
    try:
        text_to_translate = request.args.get("text")
        target_lang = request.args.get("target")
        source_lang = request.args.get("source")
        if not source_lang:
            source_lang = "auto"
        new_translator = Translator(text_to_translate, target_lang, source_lang)

        translated_text = new_translator.translate()

        return translated_text
    except:
        return "<h1> Please retry with different parameters. Unable to process.</h1><p>Example usage: http://flip2.engr.oregonstate.edu:6238/?text=hello%20world&target=es</p>"

# Listener

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6238, debug=True)
