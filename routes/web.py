from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),

    # RouteGroup([
        Route.get('/show', "UserController@show").name("show"),
        Route.get('/@id', "UserController@index").name("index"),
        Route.post('/create', "UserController@create").name("create"),
        Route.put('/update/@id', "UserController@update").name("update"),
        Route.delete('/destroy/@id', "UserController@destroy").name("destroy"),
    # ], prefix='/users', name='users', middleware=('auth',)
    # )
    ]
