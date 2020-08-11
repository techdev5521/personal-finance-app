from api.tokens import ta
from api.models import db, User
from flask_restful import Resource, request

class LoginRoute(Resource):
    def post(self) -> str:
        """Login a user based on email and password

        Returns:
            str: Valid token on successful login
        """
        # TODO: Check for previous tokens and time, create a token expiry check
        # Then issue a new token if it's expired but valid? 
        # Create a new key no matter what after X days?
        if request.json['email'] and request.json['password_hash']:
            email = request.json['email']
            password = request.json['password_hash']
            query_user = db.session.query(
                User).filter_by(email=email).first()
            if password == query_user.password_hash:
                return { 
                    'token': ta.create_token(query_user.uuid),
                    'uuid': str(query_user.uuid),
                    'public_key': ta.public_key_pem
                }
            else:
                return { 'message': 'login failed' }, 400
        else:
            return { 'message': 'invalid parameters' }, 400