# mask_detection Project Repository

Copyright : 2020, May

Masks Detection


# Getting Started

**[Generic Development Tutorials by Quantmetry](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/tree/master/tutorials)**

## 0. Clone this repository

```
$ git clone <this project>
$ cd <this project>
```

## 1. Setup your virtual environment and activate it

Goal : create a local virtual environment in the folder `./.venv/`.

- First: check your python3 version:

    ```
    $ python3 --version
    # examples of outputs:
    Python 3.6.2 :: Anaconda, Inc.
    Python 3.7.2

    $ which python3
    /Users/benjamin/anaconda3/bin/python3
    /usr/bin/python3
    ```

    - If you don't have python3 and you are working on your mac: install it from [python.org](https://www.python.org/downloads/)
    - If you don't have python3 and are working on an ubuntu-like system: install from package manager:

        ```
        $ apt-get update
        $ apt-get -y install python3 python3-pip python3-venv
        ```

- Now that python3 is installed create your environment and activate it:

    ```
    $ make init
    $ source activate.sh
    ```

    You sould **allways** activate your environment when working on the project.

    If it fails with one of the following message :
    ```
    "ERROR: failed to create the .venv : do it yourself!"
    "ERROR: failed to activate virtual environment .venv! ask for advice on #dev "
    ```

    instructions on how to create an environment by yourself can be found in the
    [tutorials about virtual environments](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/blob/master/tutorials/virtualenv.md)


## 2. Install the project's requirements

```
(path/to/here/.venv)$ make install
(path/to/here/.venv)$ make install-dev
```

## 3. Check that everything is running properly. The `Makefile` comes with useful features:

```
$ make help
coverage                       run code coverage (% of code tested)
doc                            build documentation from docstring
help                           Show this help.
install-dev                    install developpment dependencies (for testing, linting etc.)
install                        install project dependencies (requirements.txt)
lint                           Check that your code follows the PEP8 standards
pipeline                       run main project pipeline
tests                          run unit tests

# start the tests:
$ make tests
```


## 4. Start coding! 

Your code will go in the folder `mask_detection/`.

You can change your settings (where data is stored, database url / passwords)
in `mask_detection/settings/`:
    - `.env` should contain **secret infos** (passwords)
    - `base.py` or `dev.py` should contain the rest of the configuration

Read [Project Structure documentation](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/blob/master/tutorials/organization.md) for more details.

## 5. Check your Continuous-Integration setup

By default this project comes equiped with a `.gitlab-ci.yml` file that
defines an ensamble of tests that are performed automatically by gitlab
every time code is pushed to the repo.

You can modify this file, remove or add steps. For more info read
[this tutorial](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/blob/master/tutorials/integration.md)

You can read [more tutorials](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/tree/master/tutorials)
for tips on git, continuous integration, linting, etc.
