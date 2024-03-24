#pylint: disable=wildcard-import,unused-wildcard-import
import os
import glob
import subprocess
from decouple import config, Csv
from config.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default=[], cast=Csv())

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


NEOMODEL_NEO4J_BOLT_URL = config('NEO4J_BOLT_URL', default = '')
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },

}

STATIC_URL = 'src/user_interface/static_files/'
STATICFILES_DIRS = [STATIC_URL]

# pylint: disable=bad-builtin
def run_pylint(directory,folder_to_exclude):
    """
    Run pylint on specific files when the django project is running

    Args:
        directory (str): The root directory where Pylint will analyze Python files recursively.
        folder_to_exclude (str): The name of the folder to exclude from Pylint analysis.

    Raises:
        subprocess.CalledProcessError: If an error occurs while running Pylint.

    """
    try:
        all_elements = glob.glob(os.path.join(directory, '**'),recursive=True)
        
        python_files = [file for file in all_elements if file.endswith('.py') and folder_to_exclude not in file]
        
        subprocess.run(['pylint'] + python_files, check=True)
    except subprocess.CalledProcessError as error:
        print(f'Error running pylint: {error}')

if 'RUN_MAIN' not in os.environ:
    project_directory = os.getcwd()

    FOLDER_TO_EXCLUDE = 'venv'

    run_pylint(project_directory,FOLDER_TO_EXCLUDE)
