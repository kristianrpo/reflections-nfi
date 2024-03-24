<h1 align="center">How to Start Using the Project as a Developer?</h1>

<h2>Windows</h2>

1. Download Python.
    - Visit the official Python website at https://www.python.org/downloads/windows/.

    - Download the latest Python installer for Windows by clicking on the "Download Python X.X.X" button (X.X.X represents the Python version).

    - Click the "Install Now" button to start the installation process. The installer will copy Python files to your system.

    - Open the Command Prompt or PowerShell and type:
    ```sh
    python --version
    ```

    This should display the installed Python version, confirming a successful installation.

2. Create virtual environment

    - Once located at the root of the project, in the terminal create your venv:
    ```sh
        python -m venv venv
    ```

    - Activate your venv:
    ```sh
        ./venv/Scripts/activate
    ```

3. Install requirements of the proyect:

    - Open a terminal or command prompt and navigate to the root directory of the project.

    - Into the Command Prompt or Powershell run:
    ```sh
        pip install -r requirements/development.txt
    ```

<h2>Linux (Debian/Ubuntu)</h2>

1. Download Python.
    ```bash
        sudo apt update
        sudo apt install python3
    ```

2. Download virtual environment package
    ```bash
        sudo apt-get update  
        sudo apt-get install python3-venv
    ``` 
3. Create virtual environment
    - Once located at the root of the project, in the terminal create your venv:
    ```bash
        python3 -m venv venv
    ```

    - Activate your venv:
    ```bash
        source venv/bin/activate
    ```

4. Install requirements of the proyect:

    - Open a terminal or command prompt and navigate to the root directory of the project.

    - Into bash run:
    ```bash
        pip install -r requirements/development.txt
    ```

<h1 align="center">Visual Studio IDE</h1>

If you are using Visual Studio Code IDE, you can install the recommended libraries for a better development experience with Django and Python. You can do this through the IDE's extensions icon by searching for `@recommended`. 

Alternatively, you can also achieve this by using the following command:

```bash
python manage.py vs-extensions
```

This way, the extensions will be automatically downloaded, and thanks to the settings.json in the .vscode folder, the extensions will be configured automatically.
