from flask import Blueprint, Flask, request, jsonify, send_from_directory

transcript_blueprint = Blueprint('transcript', __name__)

@transcript_blueprint.route('/transcript')
def transcript():
    return send_from_directory('static', 'transcript.html')

app = Flask(__name__)


@app.route('/save_transcript', methods=['POST'])
def save_transcript():
    data = request.json
    text = data.get('text', '')
    
    if text:
        with open("output.txt", "a") as f:
            f.write(text)
            f.write("\n")
    
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)