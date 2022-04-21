#!/usr/bin/env python3
"""
jokes api
"""

import json
from flask import Flask, Response, jsonify, request, abort
import pyjokes

app = Flask(__name__)

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
            abort(404)
    elif number:
        alljokes = pyjokes.get_jokes(language, category)
        number = int(number)
        if number < len(alljokes):
            joke = alljokes[:number]
        else:
            abort(404)
    else:
        try:
            joke = pyjokes.get_joke(language, category)
        except:
            abort(404)
    return jsonify(joke=joke)


if __name__ == "__main__":
    app.run("0.0.0.0")