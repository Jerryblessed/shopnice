"""
This file contains the main function
"""

from flask import render_template, request
from modules import (
    Log,  # Importing the Log class for logging
    timedelta,  # Importing the timedelta class for working with time differences
    terminalASCII,  # Importing the terminalASCII function for displaying ASCII art in the terminal
    currentTimeStamp,  # Importing the currentTimeStamp function for getting the current timestamp
)


# Get the start time of the app
startTime = currentTimeStamp()

# Print a line breaker and a ASCII art
Log.breaker()
print(terminalASCII())

# Print a line breaker and a message that the app is starting
Log.app("Starting...")


# Importing necessary modules and classes
from modules import (
    Flask,
)  # Importing Flask class for creating the Flask application instance

# Importing blueprints for different routes
from routes.post import postBlueprint  # Importing the blueprint for post route
from routes.user import userBlueprint  # Importing the blueprint for user route
from routes.index import (
    indexBlueprint,
)  # Importing the blueprint for index route
from routes.login import (
    loginBlueprint,
)  # Importing the blueprint for login route
from routes.about import (
    aboutBlueprint,
)  # Importing the blueprint for about route
from routes.signup import (
    signUpBlueprint,
)  # Importing the blueprint for signup route
from routes.logout import (
    logoutBlueprint,
)  # Importing the blueprint for logout route
from routes.search import (
    searchBlueprint,
)  # Importing the blueprint for search route
from routes.category import (
    categoryBlueprint,
)  # Importing the blueprint for category route
from routes.editPost import (
    editPostBlueprint,
)  # Importing the blueprint for post editing route
from routes.searchBar import (
    searchBarBlueprint,
)  # Importing the blueprint for search bar route
from routes.dashboard import (
    dashboardBlueprint,
)  # Importing the blueprint for dashboard route
from routes.verifyUser import (
    verifyUserBlueprint,
)  # Importing the blueprint for user verification route
from routes.adminPanel import (
    adminPanelBlueprint,
)  # Importing the blueprint for admin panel route
from routes.createPost import (
    createPostBlueprint,
)  # Importing the blueprint for creating post route
from routes.privacyPolicy import (
    privacyPolicyBlueprint,
)  # Importing the blueprint for privacy policy route
from routes.passwordReset import (
    passwordResetBlueprint,
)  # Importing the blueprint for password reset route
from routes.changeUserName import (
    changeUserNameBlueprint,
)  # Importing the blueprint for changing username route
from routes.changePassword import (
    changePasswordBlueprint,
)  # Importing the blueprint for changing password route
from routes.adminPanelUsers import (
    adminPanelUsersBlueprint,
)  # Importing the blueprint for admin panel users route
from routes.adminPanelPosts import (
    adminPanelPostsBlueprint,
)  # Importing the blueprint for admin panel posts route
from routes.accountSettings import (
    accountSettingsBlueprint,
)  # Importing the blueprint for account settings route
from routes.returnPostBanner import (
    returnPostBannerBlueprint,
)  # Importing the blueprint for returning post banners
from routes.adminPanelComments import (
    adminPanelCommentsBlueprint,
)  # Importing the blueprint for admin panel comments route
from routes.changeProfilePicture import (
    changeProfilePictureBlueprint,
)  # Importing the blueprint for changing profile picture route

from flask_wtf.csrf import (
    CSRFProtect,
    CSRFError,
)  # Importing CSRF protection for Flask forms

# Importing database related utilities
from utils.dbChecker import dbFolder, usersTable, postsTable, commentsTable

# Importing various configuration variables from the modules
from modules import (
    LOG_IN,  # Importing the log-in configuration
    UI_NAME,  # Importing the UI name configuration
    APP_HOST,  # Importing the application host configuration
    APP_NAME,  # Importing the application name configuration
    APP_PORT,  # Importing the application port configuration
    SMTP_MAIL,  # Importing the SMTP mail configuration
    SMTP_PORT,  # Importing the SMTP port configuration
    DEBUG_MODE,  # Importing the debug mode configuration
    APP_VERSION,  # Importing the application version configuration
    SMTP_SERVER,  # Importing the SMTP server configuration
    REGISTRATION,  # Importing the registration configuration
    SMTP_PASSWORD,  # Importing the SMTP password configuration
    DEFAULT_ADMIN,  # Importing the default admin configuration
    LOG_FILE_ROOT,  # Importing the log file root configuration
    APP_ROOT_PATH,  # Importing the application root path configuration
    STATIC_FOLDER,  # Importing the static folder configuration
    CUSTOM_LOGGER,  # Importing the custom logger configuration
    APP_SECRET_KEY,  # Importing the application secret key configuration
    RECAPTCHA_BADGE,  # Flag for enabling/disabling reCAPTCHA for badge configuration
    TEMPLATE_FOLDER,  # Importing the template folder configuration
    LOG_FOLDER_ROOT,  # Importing the log folder root configuration
    WERKZEUG_LOGGER,  # Importing the werkzeug logger configuration
    LOG_APP_FILE_ROOT,  # Importing the app log file root configuration
    SESSION_PERMANENT,  # Importing the session permanence configuration
    LOG_INFO_FILE_ROOT,  # Importing the info log file root configuration
    DEFAULT_ADMIN_POINT,  # Importing the default admin point configuration
    DEFAULT_ADMIN_EMAIL,  # Importing the default admin email configuration
    LOG_DANGER_FILE_ROOT,  # Importing the danger log file root configuration
    LOG_SUCCESS_FILE_ROOT,  # Importing the success log file root configuration
    LOG_WARNING_FILE_ROOT,  # Importing the warning log file root configuration
    DEFAULT_ADMIN_USERNAME,  # Importing the default admin username configuration
    DEFAULT_ADMIN_PASSWORD,  # Importing the default admin password configuration
    DEFAULT_ADMIN_PROFILE_PICTURE,  # Importing the default admin profile picture configuration
)

# Importing reCAPTCHA configurations
from modules import (
    RECAPTCHA,  # Flag for enabling/disabling reCAPTCHA
    RECAPTCHA_LOGIN,  # Flag for enabling/disabling reCAPTCHA for login
    RECAPTCHA_COMMENT,  # Flag for enabling/disabling reCAPTCHA for comment
    RECAPTCHA_SIGN_UP,  # Flag for enabling/disabling reCAPTCHA for sign-up
    RECAPTCHA_SITE_KEY,  # Flag for enabling/disabling reCAPTCHA for site key
    RECAPTCHA_POST_EDIT,  # Flag for enabling/disabling reCAPTCHA for post edit
    RECAPTCHA_SECRET_KEY,  # Flag for enabling/disabling reCAPTCHA for secret key
    RECAPTCHA_VERIFY_URL,  # Flag for enabling/disabling reCAPTCHA for verify URL
    RECAPTCHA_DELETE_USER,  # Flag for enabling/disabling reCAPTCHA for delete user
    RECAPTCHA_POST_DELETE,  # Flag for enabling/disabling reCAPTCHA for post delete
    RECAPTCHA_VERIFY_USER,  # Flag for enabling/disabling reCAPTCHA for verify user
    RECAPTCHA_POST_CREATE,  # Flag for enabling/disabling reCAPTCHA for post create
    RECAPTCHA_COMMENT_DELETE,  # Flag for enabling/disabling reCAPTCHA for comment delete
    RECAPTCHA_PASSWORD_RESET,  # Flag for enabling/disabling reCAPTCHA for password reset
    RECAPTCHA_PASSWORD_CHANGE,  # Flag for enabling/disabling reCAPTCHA for password change
    RECAPTCHA_USERNAME_CHANGE,  # Flag for enabling/disabling reCAPTCHA for username change
    RECAPTCHA_PROFILE_PICTURE_CHANGE,  # Flag for enabling/disabling reCAPTCHA for profile picture change
)

from utils.errorHandlers.notFoundErrorHandler import (
    notFoundErrorHandler,
)  # This function handles 404 errors

from utils.errorHandlers.csrfErrorHandler import (
    csrfErrorHandler,
)  # This function handles CSRF errors

from utils.errorHandlers.unauthorizedErrorHandler import (
    unauthorizedErrorHandler,
)  # This function handles unauthorized access errors


from utils.afterRequest import (
    afterRequestLogger,
)  # This function handles loggins of every request


# Import the contextProcessor module that contains custom functions for the app
from modules import (
    isLogin,  # A function that checks LOG_IN constant
    recaptchaBadge,  # A function that checks RECAPTCHA_BADGE constant
    isRegistration,  # A function that checks REGISTRATION constant
    returnUserProfilePicture,  # A function that returns the user's profile picture
)

from square.client import Client
from dotenv import load_dotenv
import os;


environment_test = os.getenv('SQ_ENVIRONMENT_TEST')
clienttest = Client(
  environment = environment_test,
  user_agent_detail = "sandbox" # Remove or replace this detail when building your own app
)
obtain_token_test = clienttest.o_auth.obtain_token


environment = os.getenv('SQ_ENVIRONMENT').lower()
client = Client(
  environment = 'production',
  user_agent_detail = "sample_app_oauth_python" # Remove or replace this detail when building your own app
)
obtain_token = client.o_auth.obtain_token




# Create a Flask app object with the app name, root path, static folder and template folder
app = Flask(
    import_name=APP_NAME,  # The name of the app
    root_path=APP_ROOT_PATH,  # The root path of the app
    static_folder=STATIC_FOLDER,  # The folder where the static files(*.js/*.css) are stored
    template_folder=TEMPLATE_FOLDER,  # The folder where the Jinja(*.html.jinja) templates are stored
)


# Your application's ID and secret, available from your application dashboard.
application_id = os.getenv('SQ_APPLICATION_ID')
application_secret = os.getenv('SQ_APPLICATION_SECRET')


application_id_sandbox = os.getenv('SQ_APPLICATION_ID_TEST')
application_secret_sandbox = os.getenv('SQ_APPLICATION_SECRET_TEST')

base_url_test = "https://connect.squareup.com" if environment == "production" else "https://connect.squareupsandbox.com"

base_url = "https://connect.squareup.com" if environment_test == "sandbox" else "https://connect.squareupsandbox.com"

# Set the secret key and the session permanent flag for the app
app.secret_key = APP_SECRET_KEY  # The secret key for the app
app.config["SESSION_PERMANENT"] = (
    SESSION_PERMANENT  # A flag that determines if the session is permanent or not
)

# Create a CSRFProtect object for the app
csrf = CSRFProtect(app)  # A CSRF protection mechanism for the app

# Register the custom functions from the contextProcessor module as context processors for the app
# Context processors are functions that run before rendering a template and add variables to the template context
app.context_processor(
    isLogin
)  # A context processor that adds the isLogin variable to the template context
app.context_processor(
    recaptchaBadge
)  # A context processor that adds the recaptchaBadge variable to the template context
app.context_processor(
    isRegistration
)  # A context processor that adds the isRegistration variable to the template context
app.context_processor(
    returnUserProfilePicture
)  # A context processor that adds the getProfilePicture variable to the template context


# Match WERKZEUG_LOGGER status
match WERKZEUG_LOGGER:
    # If Werkzeug default logger is enabled
    case True:
        # Log that Werkzeug default logger is enabled
        Log.app("Werkzeug default logger is enabled")
    # If Werkzeug default logger is disabled
    case False:
        # Import getLogger from logging module
        from logging import getLogger

        # Log that Werkzeug default logger is disabled
        Log.app("Werkzeug default logger is disabled")
        # Disable the Werkzeug default logger
        getLogger("werkzeug").disabled = True

# Match CUSTOM_LOGGER status
match CUSTOM_LOGGER:
    # If Custom logger is enabled
    case True:
        # Log that Custom logger is enabled
        Log.app("Custom logger is enabled")
    # If Custom logger is disabled
    case False:
        # Log that Custom logger is disabled
        Log.app("Custom logger is disabled")


# Log app settings
Log.app(f"Debug mode: {DEBUG_MODE}")
Log.app(f"Name: {APP_NAME}")
Log.app(f"Version: {APP_VERSION}")
Log.app(f"Host: {APP_HOST}")
Log.app(f"Port: {APP_PORT}")
Log.app(f"Secret key: {APP_SECRET_KEY}")
Log.app(f"Session permanent: {SESSION_PERMANENT}")
Log.app(f"Root path: {APP_ROOT_PATH}")
Log.app(f"Log folder root: {LOG_FOLDER_ROOT}")
Log.app(f"Log file root: {LOG_FILE_ROOT}")
Log.app(f"Log app file root: {LOG_APP_FILE_ROOT}")
Log.app(f"Log danger file root: {LOG_DANGER_FILE_ROOT}")
Log.app(f"Log success file root: {LOG_SUCCESS_FILE_ROOT}")
Log.app(f"Log info file root: {LOG_INFO_FILE_ROOT}")
Log.app(f"Log warning file root: {LOG_WARNING_FILE_ROOT}")
Log.app(f"Log in: {LOG_IN}")
Log.app(f"Registration: {REGISTRATION}")
# Log the UI name, template folder and the static folder
Log.app(f"UI: {UI_NAME}")
Log.app(f"Template folder: {TEMPLATE_FOLDER}")
Log.app(f"Static folder: {STATIC_FOLDER}")
# Log the SMTP server settings
Log.app(f"SMTP server: {SMTP_SERVER}")
Log.app(f"SMTP port: {SMTP_PORT}")
Log.app(f"SMTP mail: {SMTP_MAIL}")
Log.app(f"SMTP password: {SMTP_PASSWORD}")

# Check if recaptcha is enabled
match RECAPTCHA:
    case True:
        # Check if the recaptcha site key and secret key are valid
        match RECAPTCHA_SITE_KEY == "" or RECAPTCHA_SECRET_KEY == "":
            case True:
                # Log a warning message that the recaptcha keys are invalid and may cause the app to crash
                Log.danger(
                    f"reCAPTCHA keys is unvalid this may cause the application to crash",
                )
                Log.danger(
                    f"Please check your recaptcha keys or set recaptcha to false from true in 'constants.py'",
                )
            case False:
                # Log a success message that recaptcha is on and print the recaptcha keys, url and badge status
                Log.app("reCAPTCHA is on")
                Log.app(f"reCAPTCHA recaptcha site key: {RECAPTCHA_SITE_KEY}")
                Log.app(f"reCAPTCHA secret key: {RECAPTCHA_SECRET_KEY}")
                Log.app(f"reCAPTCHA verify url: {RECAPTCHA_VERIFY_URL}")
                Log.app(f"reCAPTCHA badge: {RECAPTCHA_BADGE}")
                # Log the recaptcha settings for different actions
                Log.app(f"reCAPTCHA login: {RECAPTCHA_LOGIN}")
                Log.app(f"reCAPTCHA sign up: {RECAPTCHA_SIGN_UP }")
                Log.app(f"reCAPTCHA post create: {RECAPTCHA_POST_CREATE}")
                Log.app(f"reCAPTCHA post edit: {RECAPTCHA_POST_EDIT }")
                Log.app(f"reCAPTCHA post delete: {RECAPTCHA_POST_DELETE}")
                Log.app(f"reCAPTCHA comment: {RECAPTCHA_COMMENT}")
                Log.app(f"reCAPTCHA comment delete: {RECAPTCHA_COMMENT_DELETE}")
                Log.app(f"reCAPTCHA password reset: {RECAPTCHA_PASSWORD_RESET}")
                Log.app(f"reCAPTCHA password change: {RECAPTCHA_PASSWORD_CHANGE}")
                Log.app(f"reCAPTCHA username change: {RECAPTCHA_USERNAME_CHANGE}")
                Log.app(f"reCAPTCHA verify user: {RECAPTCHA_VERIFY_USER}")
                Log.app(f"reCAPTCHA delete user: {RECAPTCHA_DELETE_USER}")
                Log.app(
                    f"reCAPTCHA user profile picture change: {RECAPTCHA_PROFILE_PICTURE_CHANGE}",
                )
                Log.app(
                    f"reCAPTCHA profile picture change: {RECAPTCHA_PROFILE_PICTURE_CHANGE}",
                )
    case False:
        # Log a warning message that recaptcha is off
        Log.app(f"reCAPTCHA is off")

# Check if default admin is enabled
match DEFAULT_ADMIN:
    case True:
        # Log a success message that admin is on and print the default admin settings
        Log.app(f"Default admin is on")
        Log.app(f"Default admin username: {DEFAULT_ADMIN_USERNAME}")
        Log.app(f"Default admin email: {DEFAULT_ADMIN_EMAIL}")
        Log.app(f"Default admin password: {DEFAULT_ADMIN_PASSWORD}")
        Log.app(f"Default admin point: {DEFAULT_ADMIN_POINT}")
        Log.app(f"Default admin profile picture: {DEFAULT_ADMIN_PROFILE_PICTURE}")
    case False:
        # Log a danger message that admin is off
        Log.app(f"Default admin is off")

# Call the dbFolder, usersTable, postsTable and commentsTable functions to check the database status
dbFolder()
usersTable()
postsTable()
commentsTable()


# Serves the link that merchants click to authorize your application
@app.route('/square', methods=['GET'])
def authorize():
  url = "{0}/oauth2/authorize?client_id={1}".format(base_url, application_id)
  content = """
  <div class='wrapper'>
  
    <a class='btn'
     href='{}'>
       <strong>Authorize Square Main Account</strong>
    </a>
  </div>""".format(url)
  return render_template("base.html", content=content)


# Serves requests from Square to your application's redirect URL
# Note that you need to set your application's Redirect URL to
# http://localhost:8080/callback from your application dashboard
@app.route('/callback', methods=['GET'])
def callback():

  # Extract the returned authorization code from the URL
  authorization_code = request.args.get('code')
  if authorization_code:

    # Provide the code in a request to the Obtain Token endpoint
    body = {}
    body['client_id'] = application_id
    body['client_secret'] = application_secret
    body['code'] = authorization_code
    body['grant_type'] = 'authorization_code'

    response = obtain_token(body)
    
    ACCESS_TOKEN = response.body['access_token']
    
    client = Client(
    access_token=ACCESS_TOKEN,
    environment="production",
    user_agent_detail="sample_app_python_payment", # Remove or replace this detail when building your own app
)


    result = client.merchants.list_merchants()

    if result.is_success():
        print(result.body)
        print(response.body)
    elif result.is_error():
        print(result.errors)
    if response.body:

      # Here, instead of printing the access token, your application server should store it securely
      # and use it in subsequent requests to the Connect API on behalf of the merchant.
      # business_name = result.body[0]['business_name']
      # business_name = result['merchant'][0]['business_name']
      # business_name = result
      business_name = result.body['merchant'][0]['business_name']
      
      #   print (response.body)
      content = """
      <div class='wrapper'>
        <div class='messages'>
          <h1>Business name obtained</h1>
            <div style='color:rgba(0, 204, 35, 1)'><strong></strong>Welcome to shop-nice
            </div>
            <br/>
            <div><strong>Business Name:</strong> {} </div>

            <div><p>Please proceed to shop setup</p>
            <p>Proceed <a href='/signup' target='_blank'>to store setup</a>.</p>
            <div> or </div>
            <p><a href='/login/redirect=&' target='_blank'>Login shop</a>.</p>
          </div>
        </div>
      </div>
      """.format(result.body['merchant'][0]['business_name'])
      return render_template("base.html", content=content)
      #return render_template("login3.html", content=content, business_name=business_name)

    # The response from the Obtain Token endpoint did not include an access token. Something went wrong.
    else:
      content = """
      <link type='text/css' rel='stylesheet' href='static/style.css'>
      <meta name='viewport' content='width=device-width'>
      <div class='wrapper'>
        <div class='messages'>
          <h1>Code exchange failed</h1>
        </div>
      </div>"""
      return render_template("base.html", content=content)

  # The request to the Redirect URL did not include an authorization code. Something went wrong.
  else:
    content = """
    <link type='text/css' rel='stylesheet' href='static/style.css'>
    <meta name='viewport' content='width=device-width'>
    <div class='wrapper'>
      <div class='messages'>
        <h1>Authorization failed</h1>
      </div>
    </div>"""
    return render_template("base.html", content=content)

@app.route('/sandboxsquare', methods=['GET'])
def authorize_test():
  url = "{0}/oauth2/authorize?client_id={1}".format(base_url_test, application_id_sandbox)
  content = """
  <div class='wrapper'>
  
    <a class='btn'
     href='{}'>
       <strong>Authorize Square Sandbox Account</strong>
    </a>
  </div>""".format(url)
  return render_template("basesandbox.html", content=content)

# Sandbox
@app.route('/testcallback', methods=['GET'])
def callback_test():

  # Extract the returned authorization code from the URL
  authorization_code = request.args.get('code')
  if authorization_code:

    # Provide the code in a request to the Obtain Token endpoint
    body = {}
    body['client_id'] = application_id_sandbox
    body['client_secret'] = application_secret_sandbox
    body['code'] = authorization_code
    body['grant_type'] = 'authorization_code'

    response = obtain_token_test(body)

    ACCESS_TOKEN = response.body['access_token']
    
    client = Client(
    access_token=ACCESS_TOKEN,
    environment="production",
    user_agent_detail="sample_app_python_payment", # Remove or replace this detail when building your own app
)


    result = client.merchants.list_merchants()

    if result.is_success():
        print(result.body)
        print(response.body)
    elif result.is_error():
        print(result.errors)

    if response.body:

      # Here, instead of printing the access token, your application server should store it securely
      # and use it in subsequent requests to the Connect API on behalf of the merchant.
      print (response.body)
      content = """
      <div class='wrapper'>
        <div class='messages'>
          <h1>Authorization Succeeded</h1>
            <div style='color:rgba(0, 204, 35, 1)'><strong></strong>Welcome to shop-nice
            </div>
            <br/>
            <div><strong>Business Name:</strong> {} </div>

            <div><p>Please proceed to shop setup</p>
            <p>Proceed <a href='/signup' target='_blank'>to store setup</a>.</p>
            <div> or </div>
            <p><a href='/login/redirect=&' target='_blank'>Login shop</a>.</p>
          </div>
        </div>
      </div>
      """.format(result.body['merchant'][0]['business_name'])
      return render_template("basesandbox.html", content=content)
    # The response from the Obtain Token endpoint did not include an access token. Something went wrong.
    else:
      content = """
      <link type='text/css' rel='stylesheet' href='static/style.css'>
      <meta name='viewport' content='width=device-width'>
      <div class='wrapper'>
        <div class='messages'>
          <h1>Code exchange failed</h1>
        </div>
      </div>"""
      return render_template("basesandbox.html", content=content)

  # The request to the Redirect URL did not include an authorization code. Something went wrong.
  else:
    content = """
    <link type='text/css' rel='stylesheet' href='static/style.css'>
    <meta name='viewport' content='width=device-width'>
    <div class='wrapper'>
      <div class='messages'>
        <h1>Authorization failed</h1>
      </div>
    </div>"""
    return render_template("basesandbox.html", content=content)


# Use the app.errorhandler decorator to register error handler functions for app
@app.errorhandler(404)
def notFound(e):
    # Call the notFoundErrorHandler function and return its result
    return notFoundErrorHandler(e)


# Use the app.errorhandler decorator to register error handler functions for app
@app.errorhandler(401)
def unauthorized(e):
    # Call the unauthorizedErrorHandler function and return its result
    return unauthorizedErrorHandler(e)


# Use the app.errorhandler decorator to register error handler functions for app
@app.errorhandler(CSRFError)
def csrfError(e):
    # Call the csrfErrorHandler function and return its result
    return csrfErrorHandler(e)


# Use the app.after_request decorator to handle every request
@app.after_request
def afterRequest(response):
    # Call the afterRequestLogger function and return its result
    return afterRequestLogger(response)

@app.route('/test')
def landing():
    return render_template('test.html')

@app.route('/logon')
def logon():
    return render_template('login.html')

@app.route('/aichat')
def aichat():
    return render_template('aichat.html')

@app.route('/apoint')
def apoint():
    return render_template('apoint.html')

@app.route('/giftcard')
def giftcard():
    return render_template('giftcard.html')

@app.route('/invoice')
def invoice():
    return render_template('invoice.html')
@app.route('/subs')
def subs():
    return render_template('subscription.html')

@app.route('/sproduct')
def sproduct():
    return render_template('sproduct.html')

@app.route('/register')
def signup():
    return render_template('signup.html')



# Registering blueprints for different routes with the Flask application instance
app.register_blueprint(
    postBlueprint
)  # Registering the blueprint for handling post routes
app.register_blueprint(
    userBlueprint
)  # Registering the blueprint for handling user routes
app.register_blueprint(indexBlueprint)  # Registering the blueprint for the index route
app.register_blueprint(aboutBlueprint)  # Registering the blueprint for the about route
app.register_blueprint(loginBlueprint)  # Registering the blueprint for the login route
app.register_blueprint(
    signUpBlueprint
)  # Registering the blueprint for the sign-up route
app.register_blueprint(
    logoutBlueprint
)  # Registering the blueprint for the logout route
app.register_blueprint(
    searchBlueprint
)  # Registering the blueprint for the search route
app.register_blueprint(
    categoryBlueprint
)  # Registering the blueprint for the category route
app.register_blueprint(
    editPostBlueprint
)  # Registering the blueprint for the edit post route
app.register_blueprint(
    dashboardBlueprint
)  # Registering the blueprint for the dashboard route
app.register_blueprint(
    searchBarBlueprint
)  # Registering the blueprint for the search bar route
app.register_blueprint(
    adminPanelBlueprint
)  # Registering the blueprint for the admin panel route
app.register_blueprint(
    createPostBlueprint
)  # Registering the blueprint for the create post route
app.register_blueprint(
    verifyUserBlueprint
)  # Registering the blueprint for the verify user route
app.register_blueprint(
    privacyPolicyBlueprint
)  # Registering the blueprint for the privacy policy route
app.register_blueprint(
    passwordResetBlueprint
)  # Registering the blueprint for the password reset route
app.register_blueprint(
    changeUserNameBlueprint
)  # Registering the blueprint for the change username route
app.register_blueprint(
    changePasswordBlueprint
)  # Registering the blueprint for the change password route
app.register_blueprint(
    adminPanelUsersBlueprint
)  # Registering the blueprint for the admin panel users route
app.register_blueprint(
    adminPanelPostsBlueprint
)  # Registering the blueprint for the admin panel posts route
app.register_blueprint(
    accountSettingsBlueprint
)  # Registering the blueprint for the account settings route
app.register_blueprint(
    returnPostBannerBlueprint
)  # Registering the blueprint for the return post banner route
app.register_blueprint(
    adminPanelCommentsBlueprint
)  # Registering the blueprint for the admin panel comments route
app.register_blueprint(
    changeProfilePictureBlueprint
)  # Registering the blueprint for the change profile picture route


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=5000)
