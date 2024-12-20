from http import HTTPStatus
from dotenv import load_dotenv
from base64 import b64decode

import os
import flask

load_dotenv()

proposal_key = os.getenv('PROPOSAL_KEY')

keys = {
    proposal_key : 'root',
}


def isValid(request):
    """
    returns {dict, user-obj} if authorized else None
    """

    auth = request.headers.get('Authorization')
    if auth is None:
        return False

    auth = auth.strip()
    if not auth.lower().startswith('basic'):
        return False

    try:
        encoded_credentials = auth[6:].strip()
        decoded_credentials = b64decode(encoded_credentials).decode('utf-8')

        # Splitting the decoded string into username and password
        username, password = decoded_credentials.split(":", 1)

        # Checking if the password matched the proposal key
        if password == proposal_key and username == keys.get(password):
            # Returning user object
            return {"username": username, "role": "root"}
    
    except Exception as e:
        return False
    
    return False


def respondInValid():
    status = HTTPStatus.UNAUTHORIZED
    response = flask.make_response(status.description, status.value)
    response.headers['WWW-Authenticate'] = 'Basic realm="Authorization Required"'
    return response

