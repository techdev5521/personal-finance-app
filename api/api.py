from flask import Flask
from flask_restful import Api, Resource

# Create Flask App
app = Flask(__name__)

# Create API Interface
api = Api(app)



class Example(Resource):
	def get(self, name: str) -> str:
		"""Returns a greeting for the given name.

		Args:
			name (str): The name to be greeted.

		Returns:
			str: A greeting for the given name.
		"""

		return "Hello, " + name + "!"



api.add_resource(Example, "/api/<string:name>")



if __name__ == "__main__":
	app.run()