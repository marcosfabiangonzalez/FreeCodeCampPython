import pytest

from arithmetic_arranger import arithmetic_arranger

test_cases = [
    pytest.param(
        [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']],
        'Error: Numbers must only contain digits.',
        'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."',
        id='test_only_digits')
]

@pytest.mark.parametrize('arguments,expected_output,fail_message', test_cases)
def test_successful_no_result(arguments, expected_output, fail_message):
    result = arithmetic_arranger(*arguments)
    assert result == expected_output, fail_message
