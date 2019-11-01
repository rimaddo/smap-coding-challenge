from django.core.management.base import BaseCommand

from consumption.operations.import_data import import_data

OPTIONAL_PREFIX = '--'
USER_FILEPATH = 'user_filepath'
CONSUMPTION_FOLDERPATH = 'consumption_folderpath'

HELP_MESSAGE = f'\nTo run use the command `python manage.py import` and then specify the ' \
               f'inputs and filepaths to inputs that you want to import. Options are; ' \
               f'\n{OPTIONAL_PREFIX}{USER_FILEPATH}: followed by the path to a user upload csv file' \
               f'to import users. \n{OPTIONAL_PREFIX}{CONSUMPTION_FOLDERPATH}: to a folder-path ' \
               f'in which consumption data is stored. Consimption files are expected to be named with the ' \
               f'external_id of the user to which they belong.\n'


class Command(BaseCommand):
    help = HELP_MESSAGE

    def add_arguments(self, parser):
        parser.add_argument(
            f"{OPTIONAL_PREFIX}{USER_FILEPATH}",
            type=str,
            help="Specify path to the user filepath",
        )
        parser.add_argument(
            f"{OPTIONAL_PREFIX}{CONSUMPTION_FOLDERPATH}",
            type=str,
            help="Specify path to consumption data folder",
        )

    def handle(self, *args, **options):
        if options[USER_FILEPATH] is None and options[CONSUMPTION_FOLDERPATH] is None:
            print(HELP_MESSAGE)
        else:
            import_data(
                user_filepath=options[USER_FILEPATH],
                consumption_folderpath=options[CONSUMPTION_FOLDERPATH],
            )
