from exceptions import RequestError, LogisticError, NotEnoughSpace
from project.request import Request
from project.store import Store
from project.shop import Shop

store = Store(
    items={
        'печенька': 25,
        'собачка': 20,
        'коробки': 25,
        'чай': 15,
        'стул': 5,
        'картина': 1,
    }
)

shop = Shop(
    items={
        'печенька': 15,
        'собачка': 5,
        'коробки': 2,
        'чай': 10,
        'стул': 1,
    }
)

storages = {
    'магазин': shop,
    'склад': store,
}


def main():
    print('\nДобрый день!\n')

    while True:

        for storage_name in storages:
            print(f'Сейчас в {storage_name}:\n {storages[storage_name].get_items}')

        user_input = input(
            'Введите запрос в формате "Доставить 3 печеньки из склад в магазин"\n'
            'Введите "стоп" или "stop", если хотите закончить:\n'
        )
        if user_input in ['stop', 'стоп']:
            break

        try:
            request = Request(request=user_input, storages=storages)
        except RequestError as error:
            print(error.message)
            continue

        try:
            storages[request.departure].remove(request.product, request.amount)
        except LogisticError as error:
            print(error.message)
            continue
        print(f'Курьер забрал {request.amount} {request.product} из {request.departure}')

        try:
            storages[request.destination].add(request.product, request.amount)
        except NotEnoughSpace as error:
            print(error.message)
            storages[request.departure].add(request.product, request.amount)
            print(f'курьер вернул {request.amount} {request.product} в {request.departure}')
            continue
        print(f'Курьер доставил {request.amount} {request.product} в {request.destination}')


if __name__ == '__main__':
    main()
