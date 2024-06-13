import re
import jwt
from django.conf import settings
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from app.globals import MAX_LIMIT
from datetime import datetime, timedelta
from pytz import timezone, utc


def ws_response(status, msg, data):
    result = {"status" : status, "msg" : msg, "data" : data}
    return result


def get_paginated_response(page_no, limit, counts):
    return {"total_records" : str(counts),"record_limit" : str(limit),"current_page" : str(page_no)}


def pagination_validation(page_no, limit):
    """
    Args:
        page_no (int): Positive integer representing the page number.
        limit (int): Positive integer representing the limit per page.

    Returns:
        dict: Returns page number and offset value in key pair if validated.
    """
    obj = {}
    page_no = int(page_no)
    limit = int(limit)
    page_condition = isinstance(page_no, int) and page_no > 0
    limit_condition = isinstance(limit, int) and limit > 0
    if limit > MAX_LIMIT :
        limit = MAX_LIMIT
    if page_condition and limit_condition:
        obj["page_result"] = page_no * limit
        obj["offset"] = (page_no - 1) * limit
        return obj
    else:
        return {}



def email_validate(email):
    """
    Args:
        email (_type_): string

    Returns:
        Returns email for successful validation.
    """
    try:
        validate_email(email)
        return email
    except ValidationError:
        return False


def pass_validation(passw):
    """
        Minimum 8 characters.\n
        1.The alphabet must be between [a-z]\n
        2.At least one alphabet should be of Upper Case [A-Z]\n
        3.At least 1 number or digit between [0-9].\n
        4.At least 1 character from [ @ $ ! % * ? & ].\n 
    """
    if passw:
        if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}', passw):
            return passw
        else:
            return False


def minus_days(input_date_string, days=1):
    input_date = datetime.strptime(input_date_string, "%Y-%m-%d")
    next_day = input_date + timedelta(days=days)
    next_day_string = next_day.strftime("%Y-%m-%d")
    return next_day_string

def get_utc_time(local_time_str,timezone_str='Asia/Kolkata'):
    local_time = datetime.strptime(local_time_str, "%Y-%m-%d %H:%M:%S")
    local_time = timezone(timezone_str).localize(local_time)
    utc_time = local_time.astimezone(utc)
    return utc_time.strftime("%Y-%m-%d %H:%M:%S")