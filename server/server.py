import subprocess
from api import endpoints
from flask import Flask, request, jsonify

server = Flask(__name__)


# Default
@server.route('/')
def index():
    return 'OK'


# API
@server.route('/api', methods=['GET'])
def getAPI():
    # Init empty dictionary for response
    api_list = {}

    # Loop through endpoints and append to list
    for name, endpoint in endpoints.items():
        api_list[name] = {
            "name":         endpoint.name,
            "description":  endpoint.description,
            "methods":      endpoint.methods,
            "url":          endpoint.url,
            "parameters":   endpoint.parameters
        }

    # Generate a response
    response = {
        "version":  "1.0",
        "base_url": request.url_root,
        "api_list": api_list
    }

    # Return response
    return jsonify(response)


# Create Guest VM
@server.route('/api/createguest', methods=["POST"])
def createGuest():
    # Get request data
    data = request.get_json()

    name    = data.get('name'),
    memory  = data.get('memory'),
    cores   = data.get('cores'),
    cdrom   = data.get('cdrom'),
    volume   = data.get('volume')

    response = {
        'name':     name,
        'memory':   memory,
        'cores':    cores,
        'cdrom':    cdrom,
        'volume':   volume
    }

    return jsonify(response)


# Create Guest VM
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