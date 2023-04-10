"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
from masonite.api.authentication import AuthenticatesTokens


class User(Model, SoftDeletesMixin, Authenticates, AuthenticatesTokens):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"
    
    
    def get_user_from_auth(self, token):
        user_token=token.split()[1]
        user_id = self.attempt_by_token(user_token)
        return user_id
