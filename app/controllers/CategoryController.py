from masonite.controllers import Controller
from masonite.views import View
from ..models.Categorie import Categorie
from masonite.request import Request
from masonite.response import Response
from ..models.User import User
from ..models.Categorie import Categorie


class CategoryController(Controller):
    def create(self, view: View, request:Request, response:Response):
        category = Categorie.create(request.only('title'))
        return category
    
    def destroy(self, view: View, request:Request, response:Response):
        category = Category.find(request.param('id'))
        # user_id = user.get_user_from_auth(request.header('Authorization'))
        category.delete()
        return "category deleted"
    
    def show(self, view: View, request:Request, response:Response):
        category = Categorie.all()
        param = []
        for each in category:
            param.append({
                'id':each.id,
                'title': each.title
            })
        return param
        
