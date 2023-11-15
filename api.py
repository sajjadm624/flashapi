from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route('/trigger_script', methods=['GET'])
def trigger_script():
    try:
        result = subprocess.run(['/data/backup/sbicloud/script/db-server-info-sazzad.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode('utf-8') if result.returncode == 0 else result.stderr.decode('utf-8')
        response_data = {'status': 'success', 'output': output}
        return jsonify(response_data)
    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
        return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
