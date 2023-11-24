from arithmetic_arranger import arithmetic_arranger

def test_successful_no_result(mocker):
    test_class = arithmetic_arranger()
    operation = ["32+8"]
    show_result = False
    printer_calls = mocker.patch('builtins.print')
    test_class.arithmetic_arranger(operation, show_result)
    assert printer_calls.call_count == 5
