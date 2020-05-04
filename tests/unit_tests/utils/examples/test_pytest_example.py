import pytest

@pytest.fixture
def fake_data():
    return True


def test_a_function(fake_data):
    results_of_function = fake_data  # you may operate on fake data
    expected_results = True
    assert results_of_function == expected_results
