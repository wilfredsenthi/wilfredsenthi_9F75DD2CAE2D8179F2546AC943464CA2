def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

products = ["Apple", "Banana", "Apple", "Orange", "Apple", "Mango", "Apple"]
target = "Apple"
result = linear_search_product(products, target)
print(f"The product '{target}' was found at indices: {result}")
