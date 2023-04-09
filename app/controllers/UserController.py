from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from ..models.User import User
from masonite.authentication import Auth
import json

class UserController(Controller):


    def index(self, request:Request):
        user = User.find(request.param('id'))
        return user

    def create(self, request:Request, auth: Auth):
        user = auth.register(request.only("name", "email", "password"))
        return f"{user.name if user else json.dumps(False)}"

    def store(self, request:Request):
        return view.render("")

    def show(self, request:Request):
        return User.all()

    def edit(self, request:Request):
        return view.render("")

    def update(self, view: View, request:Request):
        id = request.param('id')
        user = request.only('password','password_confirmation')
        User.find(id).update(user)
        return "Successfully updated"

    def destroy(self, view: View, request:Request):
        id = request.param("id")
        User.find(id).delete()
        return "Successfully deleted"

    # def login(self, auth:Auth, request:Request):
    #     login = auth.attempt(request.input("username"), request.input("password"))
    #     return login.name if login else False

    def logout(self, auth: Auth, response: Response, request:Request, user:User):
        token =[request.header('Authorization'), request.cookie('token'), request.user()]
        user_token=(request.header('Authorization').split()[1])
        decoded_user = user.attempt_by_token(user_token)
        decoded_user.api_token= None
        decoded_user.save()
        return True

    def get_current_user(self, auth: Auth, response: Response, request:Request, user:User):
        token =[request.header('Authorization'), request.cookie('token'), request.user()]
        user_token=(request.header('Authorization').split()[1])
        decoded_user = user.attempt_by_token(user_token)
        return decoded_user

