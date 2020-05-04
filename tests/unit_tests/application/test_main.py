from unittest.mock import patch

from mask_detection.application import main

@patch('mask_detection.application.main.do_cleaning')
def test_main_script_calls_other_functions(do_cleaning):
    main.run()
    assert do_cleaning.called

