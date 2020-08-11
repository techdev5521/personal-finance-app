from datetime import datetime, timedelta
from uuid import UUID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt

class TokenAuthority:
    """Creates a new token authority to handle JWTs

    Returns:
        TokenAuthority: a new instance of a TokenAuthority
    """
    __private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = __private_key.public_key()

    # TODO: Store old public keys for verification of older tokens
    # Or just make the user login again and get a new token
    # Maybe only store X days worth of keys and rotate them?
    # Then make the user login if it's after X days
    public_key_pem = public_key.public_bytes(
       encoding=serialization.Encoding.PEM,
       format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')

    timout = 15
    issuer = 'poggersmydoggers'

    def create_token(self, uuid: UUID) -> str:
        """Creates a new JWT token and returns it

        Args:
            uuid (UUID): The uuid of the user the token is being created for

        Returns:
            str: Encoded JWT token
        """
        payload = {
            'exp': datetime.utcnow() + timedelta(minutes=self.timout),
            'iss': self.issuer,
            'aud': str(uuid),
            'iat': datetime.utcnow()
        }
        # TODO: Log token to DB
        return jwt.encode(payload, self.__private_key, algorithm='PS256').decode('utf-8')

    def verify_token(self, encoded: str, uuid: UUID) -> bool:
        """Verifies a JWT token based on the UUID provided

        Args:
            encoded (str): Encoded JWT token
            uuid (UUID): UUID of the user being verified

        Returns:
            bool: Whether or not the token is valid
        """
        try:
            decoded = jwt.decode(
                encoded,
                self.public_key,
                issuer=self.issuer,
                audience=str(uuid),
                algorithms=['PS256']
            )
            return True
        except jwt.exceptions.InvalidTokenError:
            return False