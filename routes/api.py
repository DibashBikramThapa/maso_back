from masonite.routes import Route

ROUTES = [
    Route.get('/users', 'UserController@show'),
    Route.get('/current_user', 'UserController@get_current_user'),
    Route.get('/logout', "UserController@logout"),
]

ROUTES+= [
    Route.post('/blogs/category/create', "CategoryController@create"),
]

ROUTES+= [
    Route.get('/blogs', "BlogController@show"),
    Route.post('/blogs/create', "BlogController@create"),
    Route.get('/blogs/get/@id', "BlogController@index"),
    Route.put('/blogs/update/@id', "BlogController@update"),
    Route.delete('/blogs/delete/@id', "BlogController@destroy"),
]