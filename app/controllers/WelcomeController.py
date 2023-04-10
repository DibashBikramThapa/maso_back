"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller
from ..models.Post import Post
from ..models.Categorie import Categorie


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    def show(self, view: View):
        return view.render("welcome")
