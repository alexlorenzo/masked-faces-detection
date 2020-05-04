import pandas as pd

from mask_detection.infrastructure import technical_cleaning


def test_upper_cased_header():
    df = pd.DataFrame([
        (1, "coucou")
    ], columns=['Number', 'other_Column'])

    result = technical_cleaning.upper_cased_header(df)
    expected_result = pd.DataFrame([
        (1, "coucou")
    ], columns=['NUMBER', 'OTHER_COLUMN'])

    pd.testing.assert_frame_equal(result, expected_result)


def test_fillna_mean():
    df = pd.DataFrame([
        (1.0, 1),
        (pd.np.nan, pd.np.nan),
        (2.0, 1)
    ], columns=['number', 'other'])
    columns = ['number']
    result = technical_cleaning.fillna_mean(df, columns)
    expected_result = pd.DataFrame([
        (1.0, 1),
        (1.5, pd.np.nan),
        (2.0, 1)
    ], columns=['number', 'other'])

    pd.testing.assert_frame_equal(result, expected_result)
