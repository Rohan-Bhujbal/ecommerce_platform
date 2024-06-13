import requests
from django.conf import settings
from django.core.mail import send_mail


def send_account_created(full_name, email, password):
    content = add_line(f"Dear {full_name},")
    content += add_line(f"We are thrilled to welcome you to {str(settings.PROJECT_NAME)}! Your new account has been successfully created by a family member, and we're excited to have you join us.")
    content += add_pre2(f"""Here are your account details:\n   - Name: {full_name}\n   - Email Address: {email}\n   - Password: {password}""")
    content += add_line(f"To get started, simply log in using the link below.")
    content += add_empty_line()
    content += add_btn("LOG IN",str(settings.APP_LINK))
    content += add_empty_line()
    content += add_line("Regards,")
    content += add_line(str(settings.PROJECT_NAME))
    subject= f"Welcome to {str(settings.PROJECT_NAME)} - Your New Account Awaits!"
    return send_mail_template(email, subject, content)



############################# 1st Call End ##############################################


############################# Email sending Functions Start##############################
def send_mail_template(receiver_email, subject, content):

    html_template ="""\
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"><html xmlns="http://www.w3.org/1999/xhtml"><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body class="main-email-tempst" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; background-color: #e4e4e4; color: #74787e; height: 100%; hyphens: auto; line-height: 1.4; margin: 0; -moz-hyphens: auto; -ms-word-break: break-all; width: 100% !important; -webkit-hyphens: auto; -webkit-text-size-adjust: none; word-break: break-word; padding: 10px 5px;"><style> .full-width-row{width: 100%;} .my-row-4{ width: 29.33%;margin: 10px 2%;float: left;} .email-down-so-temp{ text-align: center; width: 100%; } @media (min-width: 768px) { .main-email-tempst{ max-width: 600px; min-width: 600px; margin: 0px auto; } .add-mobile-viewss{ max-width: 480px!important; } } @media only screen and (max-width: 600px) { .inner-body { width: 100% !important; } .content-cell.test-add-ijmeet{ padding: 20px 15px!important;} .footer { width: 100% !important; } .my-row-4{width: 100% !important;text-align: center !important;} .content-cell.test-add-ijmeet{ padding: 10px; display: block; overflow: hidden; white-space: normal; } .add-mobile-viewss{ padding: 10px; display: block; overflow: hidden; white-space: normal; } } @media only screen and (max-width: 500px) { .button { width: 100% !important; min-width: 100% !important; } .my-row-4{width: 100% !important;text-align: center !important;} } .add--tex-ijmeet{ border: none!important; padding: 0px!important; } .btn.btn-default.google-plugin-link{ text-align: center!important; width: 95%!important; display: inline-block;} .download-ijmeet-social{background-color: #fafafa; padding: 20px 15px; display: inline-block; border-radius: 10px; } .download-ijmeet-social h2{font-size: 23px; font-weight: 500; font-stretch: normal; font-style: normal;letter-spacing: normal; text-align: center; color: #40546f; } .download-ijmeet-social p{font-size: 17px; font-weight: normal;font-stretch: normal;font-style: normal;line-height: 1.57; letter-spacing: normal;text-align: center;color: #656c74; } .email-down-so-temp{display: inline-block;} .email-down-so-temp .email-icons-send{ box-sizing: border-box; width: 31.33%; margin: 10px 1%;float: left;} .email-down-so-temp .email-icons-send img{ max-width: 100%; background-repeat: no-repeat;background-size: 100% 100%; padding: 5px; } .social_icons-ijmeet{ margin: 15px 0px; text-align: center; } .social_icons-con{ display: inline-block; margin: 0px auto; text-align: center; } .co-ijmeet-facebook{ float: left; margin: 5px; } .footer-bottom-thankyou h2{ font-size: 24px; padding: 5px 0px; font-weight: 700; margin-bottom: 5px!important; font-stretch: normal; font-style: normal; letter-spacing: normal; text-align: center; color: #40546f;} .footer-bottom-thankyou p{ font-size: 13px; font-weight: normal; font-stretch: normal; font-style: normal; line-height: 1.67; letter-spacing: normal; text-align: center; color: #656c74; } .footer-copy-text{ font-size: 13px; font-weight: normal; font-stretch: normal;font-style: normal;line-height: 1.5; letter-spacing: normal; text-align: center; color: #b5b5b4; } @media (max-width: 767px) { .download-ijmeet-social h2{ font-size: 20px!important; } } .ar.add-mobile-viewss .header{ text-align: right!important; } .ar .test-add-ijmeet{ text-align: right!important; } .ar .inner-body .test-add-ijmeet p{ text-align: right!important; direction: rtl; } .ar .test-add-ijmeet .my-row-4, .ar .email-down-so-temp .email-icons-send{ float:right!important; } </style><div class="en add-mobile-viewss" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; background: #fff; padding: 15px 15px; max-width: 480px; margin: 15px auto; border-radius: 10px;"><div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"><div class="header" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; padding: 5px 0; text-align: center;"><a href=
            """
    html_template += settings.SITE_URL
    html_template +="""\
            style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; color: #bbbfc3; font-size: 19px; font-weight: bold; text-decoration: none; text-shadow: 0 1px 0 white;"><img src=
            """
    html_template += settings.SITE_LOGO_URL
    html_template +="""\
            style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; border: none; max-width: 80px;"></a></div></div><table class="wrapper" width="100%" cellpadding="0" cellspacing="0" role="presentation" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; background-color: #f8fafc; margin: 0; padding: 0; width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: 0; -premailer-width: 100%;"><tr><td align="center" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"><table class="content " width="100%" cellpadding="0" cellspacing="0" role="presentation" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; margin: 0; padding: 0; width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: 0; -premailer-width: 100%;"><tr><td class="body add--tex-ijmeet" width="100%" cellpadding="0" cellspacing="0" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; border: none!important; background-color: #ffffff; border-bottom: 1px solid #edeff2; border-top: 1px solid #edeff2; margin: 0; width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: 0; -premailer-width: 100%; padding: 0px!important;"><table class="inner-body" align="center" width="570" cellpadding="0" cellspacing="0" role="presentation" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; padding: 0; -premailer-cellpadding: 0; -premailer-cellspacing: 0; -premailer-width: 100%; -premailer-max-width: 570px; width: 100%; margin: 5px 0px; background-color: #fafafa; max-width: 100%; margin-bottom: 20px!important; border-radius: 10px;"><tr><td class="content-cell test-add-ijmeet" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; padding: 25px;">
            """
    html_template += content
    html_template += F"""\
        </td></tr></table><div class="download-ijmeet-social-comm" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; width: 100%; margin: 10px 0px; border-radius: 5px;"><div class="my-3 social_icons-ijmeet " style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; margin: 15px 0px; text-align: center; width: 100%; display: block;"><div class="footer-bottom-thankyou mt-2" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; width: 100%; display: block;"><h2 style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; margin-top: 0; font-size: 20px; padding: 5px 0px; font-weight: 700; margin-bottom: 5px!important; font-stretch: normal; font-style: normal; letter-spacing: normal; text-align: center; color: #40546f;">  Thanks! </h2><p style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; margin-top: 0; font-size: 13px; font-weight: normal; font-stretch: normal; font-style: normal; line-height: 1.67; letter-spacing: normal; text-align: center; color: #656c74;"> Please do not reply to this email.</p><div class="footer-copy-text" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; font-size: 13px; font-weight: normal; font-stretch: normal; font-style: normal; line-height: 1.5; letter-spacing: normal; text-align: center; color: #b5b5b4;"> @{str(settings.PROJECT_NAME)}. All rights reserved. </div></div></div></div></td></tr></table></td></tr></table></div></body></html>
        """
    msg     =  ""
    to      = [receiver_email]
    res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, to, html_message=html_template)  
    if(res == 1):  
        msg = "Mail Sent Successfully."  
    else:  
        msg = False  
    return msg

############################# Email sending Functions End################################

############################# Common Functions Start ####################################
def get_base_url():
    aurl = requests.base_url.split("/")
    surl = aurl[0]+"//"+aurl[2]
    return surl


def add_pre(title):
    content = """\
                <pre style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;">"""+title+"""</pre>
                """
    return content


def add_heading(title,url):
    content = """\
                <p style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; color: #3d4852; font-size: 16px; line-height: 1.5em; margin-top: 0; text-align: left;"><a style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; color: #472811; font-size: 20px; text-decoration: none;" href='"""+url+"""'>"""+title+"""</a></p>
                """
    return content


def add_line(title):
    content = """\
                <p style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; color: #3d4852; font-size: 16px; line-height: 1.5em; margin-top: 0; text-align: left;">"""+title+"""</p>
                """
    return content


def add_empty_line():
    content = """\
                <p><br></p>
                """
    return content

def add_btn(title,url):
    content = """\
                <table class="action" align="center" width="100%" cellpadding="0" cellspacing="0" role="presentation" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; padding: 0; text-align: center; width: 100%; -premailer-cellpadding: 0; -premailer-cellspacing: 0; -premailer-width: 100%; margin: 15px auto; margin-bottom: 5px!important;"><tr><td align="center" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"><table width="100%" border="0" cellpadding="0" cellspacing="0" role="presentation" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"><tr><td align="center" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"><table border="0" cellpadding="0" cellspacing="0" role="presentation" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"><tr><td style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box;"> <a href='"""+url+"""' class="button button-primary" target="_blank" style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; border-radius: 3px; box-shadow: 0 2px 3px rgba(0, 0, 0, 0.16); color: #fff; display: inline-block; text-decoration: none; -webkit-text-size-adjust: none; min-width: 200px; font-size: 18px; text-align: center; background-color: #3490dc; border-top: 10px solid #3490dc; border-right: 18px solid #3490dc; border-bottom: 10px solid #3490dc; border-left: 18px solid #3490dc;">"""+title+"""</a></td></tr></table></td></tr></table></td></tr></table>
                """
    return content

def add_pre2(title):
    content = """\
                <pre style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol'; box-sizing: border-box; color: #3d4852; font-size: 16px; line-height: 1.5em; margin-top: 0; text-align: left;">"""+title+"""</pre>
                """
    return content

############################# Common Functions End ########################################