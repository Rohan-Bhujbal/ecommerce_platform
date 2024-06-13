# STATUS CODE
OK_CODE=200
BAD_CODE=400
AUTH_CODE=403

# FILES
VAR_350 = "350"
VAR_FILE = "file"
VAR_THUMBNAIL = "thumbnail"
VAR_FILES = "files"
VAR_MEDIA = "media"
VAR_AVATAR = "avatar"
VAR_PNG = '.png'
VAR_JPG = '.jpg'
VAR_JPEG = '.jpeg'
IMAGE_EXTENSION_LIST = [VAR_PNG, VAR_JPG, VAR_JPEG]
FILE_TYPE = [VAR_FILE, VAR_THUMBNAIL]

# Magic URL
VAR_MINUTES =15

# Database
TABLE_PREFIX='em_'
MAX_LIMIT = 5000
USER_TYPE = ['admin', 'manager', 'user']
USER_IS_NOT_AUTHORIZED = "User is not authorized."
SEARCH_START_TIME=" 00:00:00"
SEARCH_END_TIME=" 23:59:59"
# CONSUMERS
WITHOUT_LOGIN_URLS = ['test']
VAR_SINGLE = "single"
VAR_URLS = {}


# USER
VAR_URLS['user_add'] = {"class" : "UserController", "function" : "user_add"}
VAR_URLS['user_edit'] = {"class" : "UserController", "function" : "user_edit"}
VAR_URLS['user_list'] = {"class" : "UserController", "function" : "user_list"}
