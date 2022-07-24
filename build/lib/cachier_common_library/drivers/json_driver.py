import json

from datetime import datetime, timedelta


class JsonDriver:
    def __init__(self: 'JsonDriver', filename: str) -> None:
        self.filename = filename

    def read_data(self: 'JsonDriver', key: str) -> object | None:
        if not key:
            print('no key to read')
            return None

        with open(self.filename, 'r') as f:
            data: dict = json.load(f)

        cache_metadata = data.get(key, None)

        if not cache_metadata: return None

        cache_value = cache_metadata.get('value', None)
        cache_expiry = cache_metadata.get('expiry', None)

        if not cache_value: return None
        if not cache_expiry: return cache_value

        expiry_date: datetime = datetime.fromisoformat(cache_expiry)
        current_date: datetime = datetime.utcnow()

        cache_expired: bool = current_date > expiry_date
        if cache_expired: return None

        return cache_value

    def write_data(self: 'JsonDriver', key: str, value: object, cache_expiry: int | None = None) -> bool:
        try:
            with open(self.filename, 'r') as f:
                data: dict = json.load(f)

            if not cache_expiry:
                encoded_expiry = ''
            else:
                expiry_date: datetime = datetime.utcnow() + timedelta(seconds=cache_expiry)
                encoded_expiry: str = expiry_date.isoformat()

            # update the data
            data[key] = {
                'value': value,
                'expiry': encoded_expiry,
            }

            with open(self.filename, 'w') as f:
                json.dump(data, f)
        except Exception as error:
            print(error)
            return False

        return True
