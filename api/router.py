from flask import Flask, request, jsonify

from api.services import convert_data_from_georgian, convert_data_to_georgian

app = Flask(__name__)


@app.route('/translate-to-georgian', methods=['POST'])
def translate_to_geo():
    text = request.json['input']
    return jsonify(convert_data_to_georgian(text))


@app.route('/translate-from-georgian', methods=['POST'])
def translate_from_geo():
    text = request.json['input']
    return jsonify(convert_data_from_georgian(text))
