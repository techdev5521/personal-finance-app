from api.models import db
from api.models.example import ExampleModel, ExampleSchema
from flask_restful import Resource, request

# An example route
class ExampleRoute(Resource):
    """Flask Route for Example Model"""

    def get(self) -> ExampleModel:
        """Returns the Example record requestion/

        Returns:
            ExampleModel: Example record requested.
        """
        example = ExampleSchema(
            first_name="Justin",
            last_name="Campbell",
            email="campb303@purdue.edu",
            password_hash="urMom"
        )
        