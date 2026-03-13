from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/alert', methods=['POST','GET'])
def alert():

    data = request.get_json() or request.args.to_dict()

    ts = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"[{ts}] ALERT RECEIVED:", data)

    return jsonify({
        "status":"ok",
        "received":data,
        "timestamp":ts
    })

if __name__ == '__main__':
    print("Webhook listening on http://0.0.0.0:5000/alert")
    app.run(host='0.0.0.0', port=5000)