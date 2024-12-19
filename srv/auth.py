from http import HTTPStatus
from dotenv import load_dotenv

import os
import flask

load_dotenv()

proposal_key = os.getenv('PROPOSAL_KEY')

keys = {
    'proposal_key' : 'root',
}


def isValid(request):
    """
    returns {dict, user-obj} if authorized else None
    """

    auth = request.headers.get('Authorization')
    if auth is None:
        return False

    uname = keys.get(auth)
    if uname is not None:
        return uname


def respondInValid():
    status = HTTPStatus.UNAUTHORIZED
    response = flask.make_response(status.description, status.value)
    response.headers['WWW-Authenticate'] = 'Basic'
    return response
