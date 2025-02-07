# creat a configurable file

class Config: # base class - default values
    DEBUG = False                       # debug mode or not
    TESTING = False                     # testing mode or not
    DATABASE_URI = 'sqlite://:memory:'  # location of db
    LOG_LEVEL = 'DEBUG'                 # sets logging level like INFO, WARNING
    LOG_FILE_PATH = 'app.log'           # where logs are maintained
    SECRET_KEY  = 'mysecretkey'         # for security, session mgmt
    SECRET_COOKIES = 'mysecretcookies'  # secret for managing cookies
    API_ENDPOINT = 'https://api.example.com'                # external api endpoint the app communicates with
    API_TIMEOUT = 10


class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'     # MySQL db for production
    LOG_LEVEL = 'INFO'                              # logging level set to INFO - less verbose than DEBUG
    SECRET_KEY  = 'mysecretkey-prod'                # Production-specific secret key
    SECRET_COOKIES = 'mysecretcookies-prod'              # Production-specific secret for cookies
    API_ENDPOINT = 'https://api-prod.example.com'        # API endpoint remains the same
    API_TIMEOUT = 10

class DevelopmentConfig(Config):
    DEBUG = True                                    # Debugging enabled for development            
    LOG_LEVEL = 'INFO'                              # logging level set to INFO
    SECRET_KEY  = 'mysecretkey-dev'                 # Development-specific secret key
    SECRET_COOKIES = 'mysecretcookies-dev'              # Development-specific secret for cookies
    API_ENDPOINT = 'https://api-dev.example.com'        # API endpoint remains the same
    API_TIMEOUT = 20

class TestingConfig(Config):
    TESTING = True                                  # Testing mode enabled
    LOG_LEVEL = 'INFO'                              # logging level set to INFO
    SECRET_KEY  = 'mysecretkey-test'                # Testing-specific secret key
    SECRET_COOKIES = 'mysecretcookies-test'              # Testing-specific secret for cookies
    API_ENDPOINT = 'https://api-test.example.com'        # API endpoint remains the same
    API_TIMEOUT = 30