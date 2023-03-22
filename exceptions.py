class BaseError(Exception):
    message = NotImplemented


class RequestError(BaseError):
    message = NotImplemented


class LogisticError(BaseError):
    message = NotImplemented


class NotEnoughSpace(LogisticError):
    message = 'Недостаточно места на складе или магазине'


class NotEnoughProduct(LogisticError):
    message = 'Недостаточно товара на складе или магазине'


class UnknownProduct(LogisticError):
    message = 'Неизвестный товар'


class TooManyDifferentProducts(LogisticError):
    message = 'Слишком много разных товаров'


class InvalidRequest(RequestError):
    message = 'Неправильный запрос'


class InvalidStorageName(RequestError):
    message = 'Выбран несуществующий склад или магазин'
