from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")


@app.route("/englishToFrench")
def english_to_french():
    text = request.args.get('textToTranslate')
    # Write your code here
    return translator.english_to_french(text)


@app.route("/frenchToEnglish")
def french_to_english():
    text = request.args.get('textToTranslate')
    # Write your code here
    return translator.french_to_english(text)


@app.route("/")
def render_index_page():
    # Write the code to render template
    render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
