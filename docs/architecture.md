<h1 align="center">Architecture Explanation</h1>

A comprehensive and organized overview of the project's source code, configuration files, and other key components.

- **.vscode/:** This folder contains specific configurations for Visual Studio Code.

    - **extensions.json**: Recommended extensions for enhanced IDE practices and development time optimization.

    - **settings.json**: IDE extension configurations for proper functionality.

- **config/:** This folder holds the initial configuration of the Django project, emphasizing:

    - **settings/:** Global project configurations, such as the database, installed applications, and other Django options. These configurations are divided and specified for different environments: **base.py** (shared configurations), **local.py** (specific configurations for the development environment), and **production.py** (specific configurations for the production environment).
    - **routers_databases/**: In this folder, each application will establish which specific database it will point to 

    - **urls.py:** The main router that directs HTTP requests to the corresponding views of the applications.

- **docs/:** This folder stores information related to the overall project.

- **requirements/:** This folder contains necessary dependencies for project execution.

    - **development.txt:** Dependencies required in the development environment.

    - **production.txt:** Dependencies required in the production environment.

- **src/:** A folder that contains the source code of the project.

    - **applications/:** Contains specific Django applications for the project. Each application includes:

        - **middlewares/:** Folder defining application-specific custom middlewares that process HTTP requests before reaching views.

        - **decorators/:** Folder containing application-specific custom decorators that allow adding additional functionality to views.

        - **docs/:** Folder storing documentation related to the specific application.

        - **validators/:** Folder holding custom validators for Django models, evaluating certain criteria before being stored in the database.

        - **tests/:** Folder containing unit test files for the specific application, evaluating the functionality of specific code parts.

    - **user_interface/:** Contains the visual part of the software that interacts directly with the user.

        - **CSS/:** Style sheets used for web design and appearance, grouped according to the application that uses them.

        - **img/:** Static images used on the website, grouped according to the application that uses them.

        - **JS/:** JavaScript files used to enhance website functionality, grouped according to the application that uses them.

    - **utils/:** Shared functions used in various parts of the project.

- **.env:** Environment variable for protecting sensitive data.

- **.env.example:** Explanation of how to structure the environment variable (as the original .env is not uploaded to the remote repository).

- **.gitignore:** Folders and files that will not be considered for version control.

- **.pylint:** Configuration file for static code analysis of the project.

    - Inherits recommendations provided by the pylint library for good coding practices.

    - Sets a maximum line length of 120 characters.

    - Marks the usage of print() functions as a warning.

    - Marks the lack of use of defined variables as a warning.

    - Deactivates the warning for the use of undefined variables to address false positives identified by the library.

    - Deactivates the warning for the lack of docstring documentation for libraries.

    - Allows the use of continued blank lines.

    - Deactivates the warning for non-existent modules to address false positives identified by the library.
    
- **manage.py:** A script providing a command-line interface for various administrative and management tasks of the project.
