def addToCart(userIds, name, productName, addTOCart, groceries, productQuantity):
    try:
        if name not in userIds:
            raise Exception("User not found, please register with us")
        else:
            if productName not in groceries:
                raise Exception("Product not present in our inventory")
            if productName not in productQuantity:
                raise Exception("Need to add more products to obtain")
            else:
                addTOCart.append(productName)
                addTOCart.append(productQuantity[productName])
                return {
                    "message":  f"{productName} is added by user {name}, Quantity: {productQuantity[productName]}",
                    "data": addTOCart
                }
    except Exception as ex:
        return {
            "message": str(ex),
            "data": None
        }

db = {
    1: "raja",
    2: "Sandhya",
    3: "Vamshi",
    4: "bhargava",
    5: "gopi",
    6: "pusgpavati"
}

addTOCart = []
groceries = ["apples", "bananas", "carrots", "eggs", 
                  "milk", "bread", "chicken", "rice", "pasta", "onions"]
productQuantity = {"apples": 50, "bananas": 50, "carrots": 40, "eggs": 24,
                   "milk": 50, "bread": 40, "chicken": 30, "rice": 100, "pasta": 20, "onions": 30}

userNamesList = list(db.values())
currentCustomerUserName = "Sandhya"
productName = "bread"
ProductQuantity = ""
res = addToCart(userNamesList, currentCustomerUserName, productName, addTOCart, groceries, productQuantity)
print(res)