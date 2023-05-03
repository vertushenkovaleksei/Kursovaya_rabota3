from utils.utils import load_operations, get_new_data, filtered_data, format_data, card_number_hide


def test_load_operations():
    assert len(load_operations('test.json')) == 6


def test_get_new_data():
    operation_data = load_operations('test.json')
    assert len(get_new_data(operation_data)) == 5
    assert get_new_data(operation_data)[0]['date'] == "2021-11-29T07:18:23.941293"


def test_filtered_data():
    operation_data = load_operations('test.json')
    new_data = get_new_data(operation_data)
    assert filtered_data(new_data[0]) == """29.11.2021 Перевод с карты на карту
MasterCard 3152 47** **** 5065 -> Visa Gold 9447 34** **** 5960
3348.98 USD\n"""