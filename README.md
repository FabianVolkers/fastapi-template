# windbox-config-service

Config service as RESTful API for the WindBox project. Built with FastAPI

## Running the development environment

### Setup virtual environment

Setup a virtual environment using your preferred tool.

```zsh
# Install requirements
pip install -r requirements.txt

```

### Create the development database


### Run the app

```zsh
# Start development server
uvicorn main:app --reload
```

The API will be accessible at http://127.0.0.1:8000, with the autogenerated docs available at http://127.0.0.1:8000/docs.

### Development tools

For this project, we employ the following tools to streamline development.

#### flake8

A python linter enforcing the pep8 style guide

Usage:

```zsh
flake8 /path/to/file/or/directory
```

#### autopep8

 A python code formatting tool

Usage:

```zsh
autopep8 --in-place --aggressive /path/to/file
```
 
#### Python refactor

 A vscode extension for refactoring python code

Usage:

- Sorting imports: `shift` + `command` + `p`: python refactor: sort imports
