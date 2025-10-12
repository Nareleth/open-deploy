import subprocess
from flask import Flask, jsonify

server = Flask(__name__)

@server.route('/')
def index():
    return 'OK'

@server.route('/newguest')
def newGuest():
    result = subprocess.run(["python3", "bin/opendeploy-cli.py", "-c", "-n" "Alpine", "-m", "1024", "-cpu", "2", "-i", "resources/iso/alpine-standard-3.22.2-x86_64.iso", "-v", "20G"])
    return jsonify({
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    })

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8080, debug=True)