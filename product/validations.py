from kanpai import Kanpai
from product import messages
from app.messages import MAX_LIMIT_IS_256

product_validation = Kanpai.Object({
    'product_name': (Kanpai.String(error=messages.PLEASE_ENTER_PRODUCT_NAME)
                .trim()
                .required(error=messages.PLEASE_ENTER_PRODUCT_NAME)
                .max(256, error=MAX_LIMIT_IS_256)),

    'short_description': (Kanpai.String(error=messages.PLEASE_ENTER_SHORT_DESCRIPTION)
        .trim()
        .max(256, error=MAX_LIMIT_IS_256)),

    # 'product_image': (Kanpai.String(error=messages.PLEASE_UPLOAD_VALID_IMAGE)
    #     .trim()
    #     .max(1000, error=MAX_LIMIT_IS_256)),
    
    'mrp': (Kanpai.String(error=messages.PLEASE_ENTER_MRP)
                        .trim()
                        .required(error=messages.PLEASE_ENTER_MRP)
                        .max(256, error=MAX_LIMIT_IS_256)),
})