from .token_authority import TokenAuthority
from argon2 import PasswordHasher

# Initialize token authority
ta = TokenAuthority()
ph = PasswordHasher()