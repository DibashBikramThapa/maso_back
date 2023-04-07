from masonite.routes import Route
from masonite.api import Api

ROUTES = [
    Route.get("/", "WelcomeController@show"),

    # RouteGroup([
        Route.get('/show', "UserController@show").name("show"),
        Route.get('/@id', "UserController@index").name("index"),
        Route.post('/create', "UserController@create").name("create"),
        Route.put('/update/@id', "UserController@update").name("update"),
        Route.delete('/destroy/@id', "UserController@destroy").name("destroy"),
        Route.post('/login', "UserController@login"),
    # ], prefix='/users', name='users', middleware=('auth',)
    # )
    ]

ROUTES += Api.routes(auth_route="/api/auth", reauth_route="/api/reauth")
