from uuid import UUID
from flask_restful import Resource, request
from api.models import db
from api.models.user import User, UserSchema
from api.tokens import ta


class UserRoute(Resource):
    # Create
    def post(self) -> str:
        """Returns a json object of the newly created User.

        Returns:
            str: User Json
        """
        if request.json['first_name'] and request.json['last_name'] and request.json['email'] and request.json['password_hash'] and request.json['salt']:
            # Check that the password hash is in the correct format
            if len(request.json['password_hash']) != 32:
                return {'message': 'Incorect password hash format'}, 400

            # Create a user to add
            new_user = User(
                first_name=request.json['first_name'],
                last_name=request.json['last_name'],
                email=request.json['email'],
                password_hash=request.json['password_hash'],
                salt=request.json['salt']
            )

            # Check if the user already exists by email
            query_user_count = db.session.query(
                User).filter_by(email=new_user.email).first()

            # User does not exist, continue
            if query_user_count == None:
                db.session.add(new_user)
                db.session.commit()

                print("New user registered")

                user = UserSchema()
                # Can use json encoded value with dumps()
                return user.dump(new_user)
            else:
                return {'message': 'Email already signed up'}, 400

        else:
            return {'message': 'Missing user entry'}, 400

    # Read
    def get(self) -> str:
        """Returns a json object of the user specified by the uuid parameter.

        Returns:
                str: User Json
        """
        if request.args['uuid']:
            print("Checking for uuid: ", request.args['uuid'])

            search_uuid = request.args['uuid']

            query_user = db.session.query(
                User).filter_by(uuid=search_uuid).first()

            user = UserSchema()
            return user.dump(query_user)
        else:
            return {'message': 'Missing uuid'}, 400

    # Update
    def put(self) -> str:
        """Updates a user object given updated information

        Returns:
                str: HTTP-200 if successful, HTTP-400 on error
        """
        # Check for parameters
        if request.json['token'] and request.json['uuid']:
            search_uuid = UUID(request.json['uuid'])
            # Verify a valid token
            if not ta.verify_token(
                request.json['token'],
                uuid=search_uuid
            ):
                return {'message': 'Not logged in!'}

            # Lookup the user
            query_user = db.session.query(
                User).filter_by(uuid=search_uuid).first()

            # Make sure the user exists
            if query_user:
                # Update user information depending on what's provided
                if request.json['first_name']:
                    query_user.first_name = request.json['first_name']
                if request.json['last_name']:
                    query_user.last_name = request.json['last_name']
                if request.json['email']:
                    # Make sure the email is not already registered
                    query_check_user = db.session.query(
                        User).filter_by(email=request.json['email']).first()
                    if query_check_user:
                        return {'message': 'email already registered'}, 400
                    query_user.email = request.json['email']
                db.session.commit()
            else:
                return {'message': 'uuid not valid'}, 400
        else:
            return {'message': 'missing parameter'}, 400
        return {'message': 'User updated'}, 200

    # Delete
    def delete(self) -> str:
        """Updates a user object given updated information

        Returns:
            str: HTTP-200 if successful, HTTP-400 on error
        """
        if request.args['uuid']:
            search_uuid = request.args['uuid']
            query_user = db.session.query(
                User).filter_by(uuid=search_uuid).first()
            if query_user:
                db.session.delete(query_user)
                db.session.commit()
            else:
                return {'message': 'User does not exist!'}, 400
        else:
            return {'message': 'No uuid specified!'}, 400
        return {'message': 'User deleted'}, 200
