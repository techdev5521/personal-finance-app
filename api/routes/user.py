from flask_restful import Resource, request
from api.models import db
from api.models.user import User, UserSchema

# An example route
class UserRoute(Resource):
	# Create
	def post(self) -> str:
		"""Returns a json object of the newly created User.

		Returns:
			str: User Json
		"""
		if request.json['first_name'] and request.json['last_name'] and request.json['email'] and request.json['password_hash'] and request.json['salt']:
			if len(request.json['password_hash']) != 32:
				return { 'message': 'Incorect password hash format' }, 400

			new_user = User(
				first_name = request.json['first_name'],
				last_name = request.json['last_name'],
				email = request.json['email'],
				password_hash = request.json['password_hash'],
				salt = request.json['salt']
			)

			query_user_count = db.session.query(User).filter_by(email=new_user.email).first()

			if query_user_count == None:
				db.session.add(new_user)
				db.session.commit()

				print("New user registered")

				user = UserSchema()
				# Can use json encoded value with dumps()
				return user.dump(new_user)
			else:
				return { 'message': 'Email already signed up' }, 400
			
		else:
			return { 'message': 'Missing user entry' }, 400

	# Read
	def get(self) -> str:
		"""Returns a json object of the user specified by the uuid parameter.

		Returns:
			str: User Json
		"""
		if request.args['uuid']:
			print("Checking for uuid: ", request.args['uuid'])

			search_uuid = request.args['uuid']

			query_user = db.session.query(User).filter_by(uuid=search_uuid).first()

			user = UserSchema()
			return user.dump(query_user)
		else:
			return { 'message': 'Missing uuid' }, 400

	# Update
	def put(self) -> str:
		"""Updates a user object given updated information

		Returns:
			str: HTTP-200 if successful, HTTP-400 on error
		"""
		if request.json['uuid']:
			search_uuid = request.json['uuid']
			query_user = db.session.query(User).filter_by(uuid=search_uuid).first()
			if request.json['first_name']:
				query_user.first_name = request.json['first_name']
			if request.json['last_name']:
				query_user.last_name = request.json['last_name']
			if request.json['email']:
				query_user.email = request.json['email']
			db.session.commit()
		else:
			return { 'message': 'No uuid specified!' }, 400
		return { 'message': 'User updated' }, 200

	# Delete
	def delete(self) -> str:
		"""Updates a user object given updated information

		Returns:
			str: HTTP-200 if successful, HTTP-400 on error
		"""
		if request.args['uuid']:
			search_uuid = request.args['uuid']
			query_user = db.session.query(User).filter_by(uuid=search_uuid).first()
			if query_user:
				db.session.delete(query_user)
				db.session.commit()
			else:
				return { 'message': 'User does not exist!' }, 400
		else:
			return { 'message': 'No uuid specified!' }, 400
		return { 'message': 'User deleted' }, 200