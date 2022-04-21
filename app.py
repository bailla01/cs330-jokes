#!/usr/bin/env python3
"""
jokes api
"""

import json
from flask import Flask, Response, jsonify, request, abort
import pyjokes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/v1/jokes", methods=['GET', 'POST'])
def get_any():
    language=request.args.get('language')
    category=request.args.get('category')
    number=request.args.get('number')
    id=request.args.get('id')
    if id:
        alljokes = pyjokes.get_jokes(language, category)
        id = int(id)
        if id < len(alljokes):
            joke = alljokes[id]
        else:
            # TODO: make this an error
            joke = alljokes[0]
    elif number:
        alljokes = pyjokes.get_jokes(language, category)
        number = int(number)
        joke = alljokes[:number]
    else:
        try:
            joke = pyjokes.get_joke(language, category)
        except:
            abort(404)
    return jsonify(joke=joke)


if __name__ == "__main__":
    app.run("0.0.0.0")