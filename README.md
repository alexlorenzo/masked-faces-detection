# mask_detection Project Repository

Copyright : 2020, May
Authors: Alexandra Lorenzo, Louise Rodriguez

Masks Detection


# Getting Started

**[Generic Development Tutorials by Quantmetry](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/tree/master/tutorials)**

## 0. Clone this repository

```
$ git clone <this project>
$ cd <this project>
```


## Getting started

### Requirements
Following tools must be install to setup this project:
* `python >= 3.7`
* `poetry >= 0.12` (poetry installation guide could be found on their website)

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


### Run script
In order to run a script, following steps could be performed:
```
$ source activate.sh
$ python3 mask_detection/application/main.py
```

## Useful poetry commands
```
$ poetry new folder --name package_name

$ poetry env use 3.7 # creates .venv with accurate version of python
$ poetry env info
```

Install from `poetry.lock` file that already exists
```
poetry install --no-root # --no-root option skips installation of the project package
```

Update the latest versions of the dependencies and update `poetry.lock` file
```
poetry update
```

```
poetry add pandas
```


## Start coding! 

Your code will go in the folder `mask_detection/`.

You can change your settings (where data is stored, database url / passwords)
in `mask_detection/settings/`:
    - `.env` should contain **secret infos** (passwords)
    - `base.py` or `dev.py` should contain the rest of the configuration

Read [Project Structure documentation](https://gitlab.com/quantmetry/qmtools/TemplateCookieCutter/blob/master/tutorials/organization.md) for more details.