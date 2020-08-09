from flask_restful import Resource

# An example route
class Example(Resource):
	def get(self, name: str) -> str:
		"""Returns a greeting for the given name.

		Args:
			name (str): The name to be greeted.

		Returns:
			str: A greeting for the given name.
		"""

		return "Hello, " + name + "!"