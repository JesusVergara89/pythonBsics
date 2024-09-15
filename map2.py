items = [
    {
        'product': 'apple',
        'price': 0.5,
    },
    {
        'product': 'banana',
        'price': 0.4,
    },
    {
        'product': 'orange',
        'price': 0.3,
    }
]

prices = list(map(lambda x: x['price'], items))

print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))

print(new_items)

