from kanpai import Kanpai
from order import messages
from app.messages import MAX_LIMIT_IS_256, MAX_LIMIT_IS_100
from user.messages import PLEASE_PROVIDE_VALID_EMAIL


order_validation = Kanpai.Object({
    'customer_name': (Kanpai.String(error=messages.PLEASE_ENTER_CUSTOMER_NAME)
        .trim()
        .required(error=messages.PLEASE_ENTER_CUSTOMER_NAME)
        .max(256, error=MAX_LIMIT_IS_256)),
    'mobile': (Kanpai.String(error=messages.PLEASE_ENTER_MOBILE)
        .trim()
        .required(error=messages.PLEASE_ENTER_MOBILE)
        .max(256, error=MAX_LIMIT_IS_256)),
    'email': (Kanpai.Email(error=PLEASE_PROVIDE_VALID_EMAIL)
        .trim()
        .required(error=PLEASE_PROVIDE_VALID_EMAIL)
        .max(256, error=MAX_LIMIT_IS_256)),
    'address': (Kanpai.String(error=messages.PLEASE_ENTER_ADDRESS)
        .trim()
        .required(error=messages.PLEASE_ENTER_ADDRESS)
        .max(100, error=MAX_LIMIT_IS_100)),
    'address2': (Kanpai.String(error=messages.PLEASE_ENTER_ADDRESS)
        .trim()
        .max(100, error=MAX_LIMIT_IS_100)),
})