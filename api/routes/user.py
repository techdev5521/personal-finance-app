"""Routing for User"""
from uuid import UUID
from flask_restful import Resource, request
from api.models import db
from api.models.user import UserModel, UserSchema
from api.security import ta, ph

def uuid_is_valid(uuid: str) -> bool:
    """Returns true is given string is a valid UUID

    Args:
        uuid (str): String to test.

    Returns:
        bool: Is UUID valid.
    """
    try:
        UUID(uuid)
    except ValueError:
        return False

    return True

class UserRoute(Resource):
    """Routing for User"""

    def post(self) -> tuple:
        """Creates a new user in the database.

        Creates a user with provided information, auto generated uuid and hashed password.

        Returns:
            tuple: (User Info | Error Message, HTTP Return Code)
        """
        # Check for JSON content
        new_user_json = request.get_json(silent=True)
        if new_user_json is None:
            return {"message": "Could not parse JSON"}, 500

        # Check for missing keys
        keys_to_look_for = ["first_name", "last_name", "email", "password"]
        for key in keys_to_look_for:
            if key not in new_user_json:
                return {"message": "Missing key: {key}".format(key=key)}, 422

        # Check for existing user by email
        existing_user = db.session.query(UserModel).filter_by(
            email=new_user_json["email"]).first()
        if existing_user is not None:
            return {"message": "A user with email address {email} already exists.".format(
                email=new_user_json["email"])}, 409

        # Create argon2 Password Hash
        password_hash = ph.hash(new_user_json["password"])

        # Create New User
        new_user = UserModel(
            first_name=new_user_json["first_name"],
            last_name=new_user_json["last_name"],
            email=new_user_json["email"],
            password_hash=password_hash
        )

        # Add User to Database
        db.session.add(new_user)
        db.session.commit()

        # Return Created User w/o ID or Password info
        user_schema = UserSchema(exclude=["id", "password_hash"])
        return user_schema.dump(new_user), 200

    def get(self, uuid: str) -> tuple:
        """Returns user info for given UUID.

        Args:
            uuid (str): UUID of user to lookup.

        Returns:
            tuple: (User Info | Error Message, HTTP Return Code)
        """
        # Confirm UUID is valid
        if not uuid_is_valid(uuid):
            return {"message": "{uuid} is not a valid UUID".format(uuid=uuid)}, 400

        # Confirm user exists
        existing_user = db.session.query(UserModel).filter_by(uuid=uuid).first()
        if existing_user is None:
            return {"message": "No user with uuid {uuid} found.".format(uuid=uuid)}, 404

        # Return User w/o ID or Password info
        user = UserSchema(exclude=["id", "password_hash"])
        return user.dump(existing_user), 200

    def put(self, uuid: str) -> tuple:
        """Updates user information.

        Args:
            uuid (str): UUID of user to update.

        Returns:
            tuple: (User Info | Error Message, HTTP Return Code)
        """
        # Confirm UUID is valid
        if not uuid_is_valid(uuid):
            return {"message": "{uuid} is not a valid UUID".format(uuid=uuid)}, 400

        # Check for JSON content
        update_json = request.get_json(silent=True)
        if update_json is None:
            return {"message": "Could not parse JSON"}, 500

        # Confirm user exists
        existing_user = db.session.query(UserModel).filter_by(uuid=uuid).first()
        if existing_user is None:
            return {"message": "No user with uuid {uuid} found.".format(uuid=uuid)}, 404

        # Update first name if it exists
        if "first_name" in update_json:
            existing_user.first_name = update_json["first_name"]

        # Update last name if it exists
        if "last_name" in update_json:
            existing_user.last_name = update_json["last_name"]

        # Update email if it exists
        if "email" in update_json:
            email_to_check = update_json["email"]
            email_exists = db.session.query(UserModel).filter_by(email=email_to_check).first()
            if email_exists:
                return {"message": "A user with email address {email} already exists.".format(
                    email=email_to_check)}, 409
            else:
                existing_user.email = email_to_check

        # Update password if it exists
        if "password" in update_json:
            password_hash = ph.hash(update_json["password"])
            existing_user.password = password_hash

        # Commit changes to database
        db.session.commit()

        return {"message": "Update successful."}, 200

    def delete(self, uuid: str) -> tuple:
        """Delete a user from the database.

        Delete a user with provided UUID and returns user info.

        Args:
            uuid (str): UUID of user to delete.

        Returns:
            tuple: (User Info | Error Message, HTTP Return Code)
        """
        # Confirm UUID is valid
        if not uuid_is_valid(uuid):
            return {"message": "{uuid} is not a valid UUID".format(uuid=uuid)}, 400

        # Confirm user exists
        existing_user = db.session.query(UserModel).filter_by(uuid=uuid).first()
        if existing_user is None:
            return {"message": "No user with uuid {uuid} found.".format(uuid=uuid)}, 404

        # Confirm user exists
        existing_user = db.session.query(UserModel).filter_by(uuid=uuid).first()
        if existing_user is None:
            return {"message": "User with uuid {uuid} not found.".format(uuid=uuid)}, 404

        # Delete user
        db.session.delete(existing_user)
        db.session.commit()

        # Return Deleted User w/o ID or Password info
        user_schema = UserSchema(exclude=["id", "password_hash"])
        return user_schema.dump(existing_user), 200
