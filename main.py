from store.create_order import make_order
from store.products import products

def main():
    print("Witamy w sklepie!")
    print("Dostepne produkty:")
    print(list(products.keys()))
    print("Złóż zamówienie podając")

    order_summary = ()

    while True:
        order = ()
        while True:
            product_ordered = input("Produkt: ")
            if product_ordered in products:
                quantity_ordered = int(input("Ilość: "))
                order = make_order(product_ordered, quantity_ordered)
                if order is None:
                    break
                print(
                    f"Zamówienie"
                 f'\nProdukt: {order["product"]}'
                 f'\nIlość sztuk: {order["quantity_ordered"]}'
                 f'\nCałkowity koszt: {order["price"]}')
                is_order_in_summary = any(position['product'] == order["product"] for position in order_summary)
                if is_order_in_summary:
                    for position in order_summary:
                        if position['product'] == order["product"] :
                            position['price'] = position['price'] + order['price']
                            position['quantity_ordered'] = position['quantity_ordered'] + order['quantity_ordered']
                            break
                else:
                    order_summary = order_summary + (order,)
                break
            else:
                print(
                    'Nie ma takiego produktu w sklepie, poniżej dostępne produkty:'
                    f'\n {list(products.keys())}')

        next_order = input("Chcesz złożyć ponowne zamówienie? (t/n): ")
        if next_order == "n":
            break

    print('Podsumowanie zamówienia:')
    order_price_summary = 0
    for position in order_summary:
        print(f'Produkt: {position["product"]}, Ilość: {position["quantity_ordered"]}, Koszt: {position["price"]}')
        order_price_summary = order_price_summary + position['price']

    print(f'Łączna kwota zamówienia: {order_price_summary}')

if __name__ == "__main__":
    main()