import logging
from http import HTTPStatus as HTTP

from flask import Blueprint, jsonify, request, url_for

from core.config import settings
from services.oauth_serv import OauthServ

oauth = Blueprint('oauth', __name__)
@oauth.route('/oauth_login', methods=['GET'])
def oauth_login():
    oauth_provider = OauthServ.check_source()
    redirect_uri = url_for('.oauth_authorize', provider=oauth_provider.name, _external=True)
    logging.error('redirect_uri ---------- %s', redirect_uri)
    return oauth_provider.authorize_redirect(redirect_uri=redirect_uri)

@oauth.route('/oauth_authorize', methods=['GET'])
def oauth_authorize():
    oauth_provider = OauthServ.check_source()
    logging.error('------oauth_provider ---------- %s', oauth_provider)
    oauth_provider.authorize_access_token()
    access_token, refresh_token = OauthServ.check_and_create_account(oauth_provider)
    return jsonify(access_token=access_token, refresh_token=refresh_token), HTTP.OK
