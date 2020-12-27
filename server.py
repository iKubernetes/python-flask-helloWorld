#!/usr/bin/env python
from flask import Flask, request, abort, Response, jsonify as flask_jsonify, make_response
import argparse 
import sys, os, getopt, socket, json, time

app = Flask(__name__)

@app.route('/')
@app.route('/hello/')
def hello_world():
    return 'Hello World!\nWebSite: http://www.magedu.com\n'

@app.route('/hello/<username>') # dynamic route
def hello_user(username):
    return 'Hello %s!\n' % username

@app.route("/user-agent")
def view_user_agent():
    # user_agent=request.headers.get('User-Agent')
    return('User-Agent: {}\n'.format(request.headers.get('user-agent'))) 

def main(argv):
    port = 80
    host = '0.0.0.0'
    debug = False

    if os.environ.get('PORT') is not None:
        port = os.environ.get('PORT')

    if os.environ.get('HOST') is not None:
        host = os.environ.get('HOST')

    try:
        opts, args = getopt.getopt(argv,"vh:p:",["verbose","host=","port="])
    except getopt.GetoptError:
        print('server.py -p <portnumber>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-p", "--port"):
            port = arg
        elif opt in ("-h", "--host"):
            host = arg
        elif opt in ("-v", "--verbose"):
            debug = True

    app.run(host=str(host), port=int(port), debug=bool(debug))


if __name__ == "__main__":
    main(sys.argv[1:])
