def _get_settings_module():
    import importlib
    import os
    import shutil
    import dotenv

    default_settings_module = 'mask_detection.settings.dev'
    this_folder = os.path.abspath(os.path.dirname(__file__))
    env_path = os.path.join(this_folder, '.env')

    def create_env_file_if_missing():
        
        env_template_path = os.path.join(this_folder, '.env_template')
        if not os.path.exists(env_path):
            shutil.copy(env_template_path, env_path)
            os.chmod(env_path, 0o700)

    def get_settings_module_from_environment_variable():
        variable_name = "MASK_DETECTION_SETTINGS_MODULE"
        try:
            settings_module = os.environ[variable_name]
        except KeyError:
            print('***' * 20)
            print('WARNING: variable {} must be defined in {}'.format(
                variable_name, env_path
            ))
            print('USING default value : {}'.format(default_settings_module))
            print('***' * 20)
            settings_module = default_settings_module
        return settings_module

    create_env_file_if_missing()
    dotenv.load_dotenv(env_path)
    settings_module = get_settings_module_from_environment_variable()
    
    return settings_module

exec("from {} import *".format(_get_settings_module()))