""" Post Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one,belongs_to_many,belongs_to

class Post(Model):
    """Post Model"""


    @belongs_to('categories_id')
    def categories(self):
        from app.models.Categorie import Categorie
        return Categorie
    
    @belongs_to('author_id')
    def authors(self):
        from app.models.User import User
        return User
