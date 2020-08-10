from flask_restful import Resource, request
from api.models import db
from api.models.user import User, UserSchema

# An example route
class UserRoute(Resource):
	def post(self) -> str:
		"""Returns a json object of the newly created User.

		Returns:
			str: User Json
		"""
		new_user = User(
			first_name = request.json['first_name'],
			last_name = request.json['last_name'],
			email = request.json['email'],
			salt = request.json['salt']
		)

		db.session.add(new_user)
		db.session.commit()

		print("New user registered")

		user = UserSchema()
		# Can use json encoded value with dumps()
		return user.dump(new_user)