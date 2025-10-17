import subprocess
from api import endpoints
from flask import Flask, render_template, redirect, url_for, request, jsonify

server = Flask(__name__)


# Default
@server.route('/')
def index():
    return redirect(url_for('login'))


# Login
@server.route('/login')
def login():
    return render_template('login.html')


# Dashboard
@server.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


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

    name    = data.get('name')
    memory  = data.get('memory')
    cores   = data.get('cores')
    cdrom   = data.get('cdrom')
    volume  = data.get('volume')

    # Run subprocess
    result = subprocess.run(["python3", "bin/opendeploy-cli.py", "-c", "-n", str(name), "-m", str(memory), "-cpu", str(cores), "-i", str(cdrom), "-v", str(volume)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Generate response message
    response = {
        'api_name':     name,
        'api_memory':   memory,
        'api_cores':    cores,
        'api_cdrom':    cdrom,
        'api_volume':   volume,
        'stdout':       result.stdout,
        'stderr':       result.stderr,
        'returncode':   result.returncode
    }

    # Return response
    return jsonify(response)


# Boot Guest VM
@server.route('/api/bootguest', methods=["POST"])
def bootGuest():
    # Get request data
    data = request.get_json()
    name = data.get('name')

    # Run subprocess
    result = subprocess.run(["python3", "bin/opendeploy-cli.py", "-b", str(name)])

    # Generate response message
    response = {
        'api_name':     name,
        'stdout':       result.stdout,
        'stderr':       result.stderr,
        'returncode':   result.returncode
    }

    # Return response
    return jsonify(response)




# Main Handler
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8080, debug=True)