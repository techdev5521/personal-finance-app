""" Utility functions for various security tasks """
from uuid import UUID

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