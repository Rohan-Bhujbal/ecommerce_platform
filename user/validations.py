from kanpai import Kanpai
from user import messages
from app.messages import MAX_LIMIT_IS_1000, MAX_LIMIT_IS_256, PLEASE_SELECT_STATUS, MAX_LIMIT_IS_2000

user_validation = Kanpai.Object({

        'full_name': (Kanpai.String(error=messages.PLEASE_ENTER_FULL_NAME)
                   .trim()
                   .required(error=messages.PLEASE_ENTER_FULL_NAME)
                   .max(256, error=MAX_LIMIT_IS_256)),

        'email': (Kanpai.Email(error=messages.PLEASE_PROVIDE_VALID_EMAIL)
                  .trim()
                  .required(error=messages.PLEASE_PROVIDE_VALID_EMAIL)
                  .max(256, error=MAX_LIMIT_IS_256)),
        
        'mobile': (Kanpai.String(error=messages.PLEASE_PROVIDE_VALID_MOBILE)
                  .required(error=messages.PLEASE_PROVIDE_VALID_MOBILE)
                  .min(10, error=messages.PLEASE_PROVIDE_VALID_MOBILE)
                  .max(10, error=messages.PLEASE_PROVIDE_VALID_MOBILE)),

        'address': (Kanpai.String(error=messages.PLEASE_PROVIDE_VALID_ADDRESS)
                  .trim()
                  .max(1000, error=MAX_LIMIT_IS_1000)),
     
        'password': (Kanpai.String(error=messages.PLEASE_ENTER_PASSWORD)
                  .trim()
                  .required(error=messages.PLEASE_ENTER_PASSWORD)
                  .max(256, error=MAX_LIMIT_IS_256)),

        'user_type': (Kanpai.String(error=messages.PLEASE_SELECT_USER_TYPE)
                  .trim()
                  .required(error=messages.PLEASE_SELECT_USER_TYPE)
                  .max(256, error=MAX_LIMIT_IS_256)),

        'permissions': (Kanpai.String(error=messages.PLEASE_SELECT_USER_PERMISSION)
                  .trim()
                  .required(error=messages.PLEASE_SELECT_USER_PERMISSION)
                  .max(2000, error=MAX_LIMIT_IS_2000)),

        'is_active': (Kanpai.Boolean(error=PLEASE_SELECT_STATUS)
                        .required(error=PLEASE_SELECT_STATUS)),
        
        'related_id': (Kanpai.String(error=messages.PLEASE_PROVIDE_VALID_RELATED_ID)
                .trim()
                .max(256, error=MAX_LIMIT_IS_256)),
})


login_validation = Kanpai.Object({

        'email': (Kanpai.String(error=messages.PLEASE_PROVIDE_VALID_EMAIL)
                  .trim()
                  .required(error=messages.PLEASE_PROVIDE_VALID_EMAIL)
                  .max(256, error=MAX_LIMIT_IS_256)),

        'password': (Kanpai.String(error=messages.PLEASE_ENTER_PASSWORD)
                  .trim()
                  .required(error=messages.PLEASE_ENTER_PASSWORD)
                  .max(256, error=MAX_LIMIT_IS_256)),

        'device_type': (Kanpai.String(error=messages.PLEASE_ENTER_DEVICE_TYPE)
                  .trim()
                  .required(error=messages.PLEASE_ENTER_DEVICE_TYPE)
                  .max(256, error=MAX_LIMIT_IS_256)),

        'device_id': (Kanpai.String(error=messages.PLEASE_ENTER_DEVICE_ID)
                  .trim()
                  .required(error=messages.PLEASE_ENTER_DEVICE_ID)
                  .max(256, error=MAX_LIMIT_IS_256)),

})


magic_code_validation = Kanpai.Object({


    'device_id': (Kanpai.String(error=messages.PLEASE_ENTER_DEVICE_ID)
              .trim()
              .required(error=messages.PLEASE_ENTER_DEVICE_ID)
              .max(200, error=messages.PLEASE_ENTER_DEVICE_ID)),

    'device_type': (Kanpai.String(error=messages.PLEASE_ENTER_DEVICE_TYPE)
                   .trim()
                   .required(error=messages.PLEASE_ENTER_DEVICE_TYPE)
                   .max(200, error=messages.PLEASE_ENTER_DEVICE_TYPE)),

})