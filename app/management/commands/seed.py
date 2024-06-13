# <project>/<app>/management/commands/seed.py
from user.models import User
from django.conf import settings
from app.helper import pass_validation, email_validate
from django.core.management.base import BaseCommand
from user.auth import user_pass_encode, check_user_pass
from user.messages import USER_NOT_FOUND, PLEASE_PROVIDE_VALID_EMAIL, P_CRITERIA_NOT_MATCH


# python manage.py seed --mode=refresh
# python manage.py seed --mode=clear

# docker exec -it mem_web python3 manage.py seed --mode=refresh
# docker exec -it mem_web python3 manage.py seed --mode=clear


""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    encoded_pass = user_pass_encode(settings.SYSTEM_USER_PASS)
    clear = User.objects.filter(email=settings.SYSTEM_USER_EMAIL, password=encoded_pass).delete()
    if clear:
        print("\nRecords cleared!!\n")
    else:
        print("\nPlease try after some time.\n")



def create_data():
    """Creates an data object combining different elements from the list"""
    try:
        if not email_validate(settings.SYSTEM_USER_EMAIL):
            print(f"\nerror >>>>>>>> {PLEASE_PROVIDE_VALID_EMAIL}\n")
        else:
            if not pass_validation(settings.SYSTEM_USER_PASS):
                print(f"\nerror >>>>>>>> {P_CRITERIA_NOT_MATCH}\n")
            else:
                try:
                    encoded_pass = user_pass_encode(settings.SYSTEM_USER_PASS)
                    user = User.objects.get(email=settings.SYSTEM_USER_EMAIL)
                except User.DoesNotExist:
                    user = None
                    print(f"\nerror >>>>>>>> {USER_NOT_FOUND}\n")
                if user:
                    print(f"\nSystem user already created..\n")
                else:
                    print(f"Creating system user...\n")
                    encoded_pass = user_pass_encode(settings.SYSTEM_USER_PASS)
                    user = User(
                        full_name=settings.SYSTEM_USERNAME, 
                        email=settings.SYSTEM_USER_EMAIL, 
                        password=encoded_pass,
                        user_type="admin"
                    )
                    user.save()
                    is_valid = check_user_pass(settings.SYSTEM_USER_PASS, user.password)
                    if is_valid:
                        print(f"User email >>>>>>>> {user.email}")
                        print(f"User password >>>>>>>> {settings.SYSTEM_USER_PASS}")
                        print(f"\nSystem user created!!!\n")
    except Exception as e:
        print({"error": e})


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    if mode == MODE_CLEAR:
        clear_data()

    # Creating data
    if mode == MODE_REFRESH:
        create_data()