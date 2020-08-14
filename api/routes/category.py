"""Routing for Category"""
from uuid import UUID
from flask_restful import Resource, request
from api.models import db
from api.models.category import CategoryModel, CategorySchema
from api.security import ta, ph
from api.security.util import uuid_is_valid


class CategoryRoute(Resource):
    """Routing for Category"""

    def post(self) -> tuple:
        """Creates a new category in the database.

        Creates a category with provided information, auto generated uuid and hashed password.

        Returns:
            tuple: (Category Info | Error Message, HTTP Return Code)
        """

        new_category_json = request.get_json(silent=True)

        # Check for JSON content
        if new_category_json is None:
            return {"message": "Could not parse JSON"}, 500

        # Check for missing keys
        keys_to_look_for = ["user_uuid", "token", "name"]
        for key in keys_to_look_for:
            if key not in new_category_json:
                return {"message": "Missing key: {key}".format(key=key)}, 422

        # Retreive JSON data
        token = new_category_json['token']
        user_uuid = new_category_json['user_uuid']
        cat_name = new_category_json['name']

        # Check if token is valid
        if not ta.verify_token(token, user_uuid):
            return {"message": "Please login"}, 500

        # Check for existing Category
        existing_cat = db.session.query(CategoryModel).filter_by(name=cat_name).first()

        if existing_cat is not None:
            return {"message": "A category with this name: {category} already exists.".format(
                category=cat_name)}, 409

        # Add new Category
        new_category = CategoryModel(name=cat_name)

        db.session.add(new_category)
        db.session.commit()

        # Return Created Category
        category_schema = CategorySchema()
        return category_schema.dump(new_category), 200

    def get(self, uuid: str) -> tuple:
        """Returns category info for given UUID.

        Args:
            uuid (str): UUID of category to lookup.

        Returns:
            tuple: (Category Info | Error Message, HTTP Return Code)
        """
        # Confirm UUID is valid
        if not uuid_is_valid(uuid):
            return {"message": "{uuid} is not a valid UUID".format(uuid=uuid)}, 400

        # Confirm Category exists
        existing_cat = db.session.query(CategoryModel).filter_by(uuid=uuid).first()
        if existing_cat is None:
            return {"message": "No category with uuid {uuid} found.".format(uuid=uuid)}, 404

        # Return Category
        category = CategorySchema()
        return category.dump(existing_cat), 200

    def put(self, uuid: str) -> tuple:
        """Updates category name.

        Args:
            uuid (str): UUID of category to update.

        Returns:
            tuple: (Category Info | Error Message, HTTP Return Code)
        """
        # Confirm UUID is valid
        if not uuid_is_valid(uuid):
            return {"message": "{uuid} is not a valid UUID".format(uuid=uuid)}, 400

        # Check for JSON content
        update_json = request.get_json(silent=True)
        if update_json is None:
            return {"message": "Could not parse JSON"}, 500

        # Confirm category exists
        existing_cat = db.session.query(CategoryModel).filter_by(uuid=uuid).first()
        if existing_cat is None:
            return {"message": "No category with uuid {uuid} found.".format(uuid=uuid)}, 404

        # Update name if it exists
        if "name" in update_json:
            name_to_check = update_json["name"]
            name_exists = db.session.query(CategoryModel).filter_by(name=name_to_check).first()
            if name_exists:
                return {"message": "A category with name address {name} already exists.".format(
                    name=name_to_check)}, 409
            else:
                existing_cat.name = name_to_check

        # Commit changes to database
        db.session.commit()

        return {"message": "Update successful."}, 200

    def delete(self, uuid: str) -> tuple:
        """Delete a category from the database.

        Delete a category with provided UUID and returns category info.

        Args:
            uuid (str): UUID of category to delete.

        Returns:
            tuple: (Category Info | Error Message, HTTP Return Code)
        """
        # Confirm UUID is valid
        if not uuid_is_valid(uuid):
            return {"message": "{uuid} is not a valid UUID".format(uuid=uuid)}, 400

        # Confirm category exists
        existing_category = db.session.query(CategoryModel).filter_by(uuid=uuid).first()
        if existing_category is None:
            return {"message": "No category with uuid {uuid} found.".format(uuid=uuid)}, 404

        # Confirm category exists
        existing_category = db.session.query(CategoryModel).filter_by(uuid=uuid).first()
        if existing_category is None:
            return {"message": "Category with uuid {uuid} not found.".format(uuid=uuid)}, 404

        # Delete category
        db.session.delete(existing_category)
        db.session.commit()

        # Return Deleted Category w/o ID or Password info
        category_schema = CategorySchema()
        return category_schema.dump(existing_category), 200
        