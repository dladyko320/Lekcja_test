from store.products import products

orders = []


def make_order(product, quantity_ordered):
    if products[product]["quantity"] >= quantity_ordered:
        products[product]["quantity"] -= quantity_ordered
        payment = quantity_ordered * products[product]["price"]
        one_order = {"product": product, "quantity_ordered": quantity_ordered, "price": payment}
        orders.append(one_order)
        return one_order
    else:
        print(f"Niewystarczająca ilość produktu. Możesz zamowić maksymalnie {products[product]['quantity']} sztuk")
        return None
