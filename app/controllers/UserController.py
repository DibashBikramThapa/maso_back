from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from ..models.User import User

class UserController(Controller):


    def index(self, request:Request):
        user = User.find(request.param('id'))
        return user

    def create(self, request:Request):
        user = request.only('name', 'email', 'password', 'second_password')
        new_user = User.create(user)
        return f"User created {new_user.name}"

    def store(self, request:Request,):
        return view.render("")

    def show(self, request:Request,):
        return User.all()

    def edit(self, request:Request,):
        return view.render("")

    def update(self, view: View, request:Request,):
        id = request.param('id')
        user = request.only('password','second_password')
        User.find(id).update(user)
        return "Successfully updated"

    def destroy(self, view: View, request:Request,):
        id = request.param("id")
        User.find(id).delete()
        return "Successfully deleted"
