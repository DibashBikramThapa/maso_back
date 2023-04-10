"""Security Related Config"""

# Cross-Origin Resource Sharing
CORS = {
    "paths": ["api/*"],
    "allowed_methods": ["POST", "PUT", "PATCH", "GET", "DELETE"],
    "allowed_origins": ["http://127.0.0.1:5173"],
    "allowed_headers": ["X-Test-1", "X-Test-2","Authorization"],
    "exposed_headers": [],
    "max_age": None,
    "supports_credentials": False,
}
