import dotenv
import os

dotenv.load_dotenv()

APP_LOGGER_FILE = os.getenv("APP_LOGGER_FILE", "asgi.log")

EXCEPTIONS_LOGGER_FILE = os.getenv("EXCEPTIONS_LOGGER_FILE", "exceptions.log")

WORKERS_COUNT = int(os.getenv("WORKERS_COUNT", 2))

ISSUER = os.getenv("ISSUER", "vr")
JWT_SECRET = os.getenv("JWT_SECRET")
PORT_HTTP = os.getenv("PORT_HTTP")
PORT_HTTPS = os.getenv("PORT_HTTPS")

SSL_CERT_PATH = os.getenv("SSL_CERT_PATH")
SSL_KEY_PATH = os.getenv("SSL_KEY_PATH")

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@vr.com")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

POSTGRES_URI = os.getenv("POSTGRES_URI")

# POSTGRES_DATABASE_NAME = os.getenv("POSTGRES_DATABASE_NAME", "device-manager")
POSTGRES_ENABLE_TLS = os.getenv("POSTGRES_ENABLE_TLS", "False").lower() in ("true", "1")

if POSTGRES_ENABLE_TLS:
    POSTGRES_CA_PATH = os.getenv("POSTGRES_CA_PATH")
    POSTGRES_CERT_PATH = os.getenv("POSTGRES_CERT_PATH")
    POSTGRES_KEY_PATH = os.getenv("POSTGRES_KEY_PATH")
else:
    POSTGRES_CA_PATH = None
    POSTGRES_CERT_PATH = None
    POSTGRES_KEY_PATH = None

ENVIRONMENT = os.getenv("ENVIRONMENT")