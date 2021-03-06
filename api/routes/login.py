""" Routing for Login """
from flask_restful import Resource, request
import argon2
from api.models import db, UserModel
from api.security import ta, ph


class LoginRoute(Resource):
    """ Routing for Login """

    def post(self) -> str:
        """Login a user based on email and password

        Returns:
            str: Valid token on successful login
        """
        # TODO: Check for previous tokens and time, create a token expiry check
        # Then issue a new token if it's expired but valid?
        # Create a new key no matter what after X days?
        if ('email' in request.json) and ('password' in request.json):
            email = request.json['email']
            password = request.json['password']

            query_user = db.session.query(
                UserModel).filter_by(email=email).first()

            # Check that the user exists
            if query_user is None:
                return {'message': 'login failed'}, 400

            # TODO: Move password verification to separate function?
            try:
                # Check the password against the hash
                ph.verify(query_user.password_hash, password)

                # Argon2 has hash refreshing functionality as well
                # If the password has been verified, check if the hash
                # should be recalculated and update it
                if ph.check_needs_rehash(query_user.password_hash):
                    query_user.password_hash = ph.hash(password)
                    db.session.commit()
                return {
                    'token': ta.create_token(query_user.uuid),
                    'uuid': str(query_user.uuid),
                    'public_key': ta.public_key_pem
                }
            except argon2.exceptions.VerifyMismatchError:
                return {'message': 'login failed'}, 400
        else:
            return {'message': 'invalid parameters'}, 400
