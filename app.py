from flask import Flask, request, jsonify
import oseti

app = Flask(__name__)

@app.route('/api/score', methods=['GET'])
def calculateScore():
	sentence = request.args.get('q')
	print('Sentence', sentence)
	analyzer = oseti.Analyzer()
	score_list = analyzer.analyze(sentence)
	score = sum(score_list)/len(score_list)
	print('Score:', score)

	return(jsonify(score=score))

if __name__ == '__main__':
	app.run()
	#app.run(host='0.0.0.0', port=80)