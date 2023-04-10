from masonite.middleware import VerifyCsrfToken as Middleware


class VerifyCsrfToken(Middleware):

    exempt = [
        "/create", "/update", "/destroy","/login", "api/auth", "api/blogs/category/create"
        ]
