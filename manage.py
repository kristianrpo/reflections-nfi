import os
import sys
import subprocess
import json
from django.core.management import execute_from_command_line


def app_exists(app_name):
    """
    Check if the given Django app exists in the specified directory.
    """
    apps_folder = 'src/applications'
    return os.path.exists(os.path.join(os.getcwd(), apps_folder, app_name))


def change_destination_path(app_name):
    """
    Change the destination path for a Django app and move it to a specified folder.
    """
    default_destination_path = 'src/applications'
    execute_from_command_line(['manage.py', 'startapp', app_name])
    source_path = os.path.join(os.getcwd(), app_name)
    destination_path = os.path.join(os.getcwd(), default_destination_path, app_name)
    os.rename(source_path, destination_path)

    return destination_path

def create_app_folders(destination_path):
    """
    Create necessary folders for a Django app within the specified destination path.
    """
    folders_to_create = ['middlewares', 'decorators', 'docs', 'validators', 'tests','models', 'views']
    for folder in folders_to_create:
        os.makedirs(os.path.join(destination_path, folder))

def delete_app_files(destination_path):
    """
    Delete specific files from a Django app within the specified destination path.
    """
    files_to_delete = ['models.py','views.py','tests.py']
    for file in files_to_delete:
        os.remove(os.path.join(destination_path, file))

def create_urls_file(destination_path):
    """
    Create a Django 'urls.py' file within the specified destination path.
    """
    with open(os.path.join(destination_path, 'urls.py'), 'w', encoding='utf-8') as line:
        line.write('from django.urls import path')
        line.write('\n')
        line.write('urlpatterns = []')

def edit_apps_file(destination_path,app_name):
    """
    Edit the 'apps.py' file of a Django app within the specified destination path.
    """
    with open(os.path.join(destination_path, 'apps.py'), 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines.pop()
    lines.pop()
    with open(os.path.join(destination_path, 'apps.py'), 'w', encoding='utf-8') as file:
        file.writelines(lines)
        file.write(f"    name = 'src.applications.{app_name}'")

def create_user_interface_folders(app_name):
    """
    Create necessary folders for the user interface of a Django app.
    """
    path_folders = [
        'src/user_interface/templates', 
        'src/user_interface/static_files/CSS', 
        'src/user_interface/static_files/JS', 
        'src/user_interface/static_files/img'
        ]
    for path in path_folders:
        destination_path = os.path.join(os.getcwd(),path, app_name)
        os.makedirs(destination_path)

def edit_settings_file(app_name):
    """
    Edit the 'base.py' settings file of a Django app.
    """
    settings_file_path = 'config/settings/base.py'
    with open(settings_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith("    'django_neomodel'"):
            index = line.index(',')
            lines[i] = line[:index + 1] + '\n' + f"    'src.applications.{app_name}'," +line[index + 1:]

    with open(settings_file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def custom_startapp(app_name):
    """Custom implementation of Django's 'startapp' command with additional setup.

    Args:
        app_name (str): The name of the Django app.
    """
    if app_exists(app_name):
        pass
    else:
        destination_path = change_destination_path(app_name)
        create_app_folders(destination_path)
        delete_app_files(destination_path)
        create_urls_file(destination_path)
        edit_apps_file(destination_path,app_name)
        create_user_interface_folders(app_name)
        edit_settings_file(app_name)

def install_extensions():
    """Install recommended VS Code extensions."""
    with open('.vscode/extensions.json', encoding='utf-8') as f:
        extensions = json.load(f)['recommendations']

    for extension in extensions:
        subprocess.run(['code', '--install-extension', extension], check=True)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    if sys.argv[1] == 'startapp':
        custom_startapp(sys.argv[2])
    elif sys.argv[1] == 'vs-extensions':
        install_extensions()
    else:
        main()
        