from app import get_exchange_rate


def test_get_exchange_rate():
    taxa = get_exchange_rate()
    assert taxa is None or taxa > 0

