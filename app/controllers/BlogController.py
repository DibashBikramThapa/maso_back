from masonite.controllers import Controller
from masonite.views import View
from ..models.Post import Post
from ..models.User import User
from ..models.Categorie import Categorie
from masonite.request import Request
from masonite.response import Response
import json

class BlogController(Controller):
    
    def index(self, view: View, request:Request, response:Response, user:User):
        user_id = user.get_user_from_auth(request.header('Authorization'))
        posts = Post.with_('categories','authors').find(request.param('id')) if user_id.is_admin else Post.with_('categories','authors').where('author_id',user_id.id).where('id',request.param('id')).get()
        return posts[0]

    def create(self, view: View, request:Request, response:Response, user:User):
        create_param = request.only('title','body','categories_id')

        user_id = user.get_user_from_auth(request.header('Authorization'))

        create_param['author_id'] = user_id.id
        post = Post.create(create_param)
        return f"Post: {post.title} by {user_id.name}"

    def store(self, view: View):
        return view.render("")

    def show(self, view: View,request:Request, response:Response, user:User):
        user_id = user.get_user_from_auth(request.header('Authorization'))
        posts = Post.with_('categories','authors').all() if user_id.is_admin else Post.with_('categories','authors').where('author_id',user_id.id).get()
        return posts

    def edit(self, view: View):
        return view.render("")

    def update(self, view: View, request:Request, response:Response, user:User):
        user_id = user.get_user_from_auth(request.header('Authorization'))
        post = Post.find(request.param('id')).where('author_id', user_id.id)
        if post:
            update_param = request.only('title','body','categories_id')
            post.update(update_param)
        return "Post updated"

    def destroy(self, view: View, request:Request, response:Response, user:User):
        user_id = user.get_user_from_auth(request.header('Authorization'))
        post_id = request.param('id')
        post = Post.where('id',post_id).where('author_id',user_id.id).get()
        if post:
            post[0].delete()     
            return "Post deleted"
        else:
            return f"Something went wrong."
