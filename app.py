from flask import Flask, request, jsonify
import oseti

import os

app = Flask(__name__)


@app.route('/score', methods=['GET'])
def calculate_score():
	sentence = request.args.get('q')
	print('Sentence', sentence)
	analyzer = oseti.Analyzer()
	score_list = analyzer.analyze(sentence)
	score = sum(score_list)/len(score_list)
	print('Score:', score)

	return(jsonify(score=score))


@app.route('/')
def index():
	return 'Hello World!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))