from app import converter_dolar

def test_converter_dolar():
    assert converter_dolar(10, 5.0) == 50.0
