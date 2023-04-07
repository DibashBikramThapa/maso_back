from masonite.routes import Route

ROUTES = [
    Route.get('/users', 'UserController@show'),
    Route.get('/current_user', 'UserController@get_current_user'),
    Route.get('/logout', "UserController@logout"),
]