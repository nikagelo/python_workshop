products = {"Phone": 1200, "PC": 1800, "Laptop": 2200}


def productListPrinter(productsList):
    for key, value in products.items():
        print(f"სახელი : {key}, ფასი: {value}")
    typeOfProduct()


def typeOfProduct():
    typeOfProductInput = input("გთხოვთ შეიყვანოთ რისი ყიდვა გსურთ")
    if products.get(typeOfProductInput):
        confirm(typeOfProductInput)
    else:
        print("პროდუქტი", typeOfProductInput, "არ გვაქვს")
        typeOfProduct()


def confirm(typeOfProductInput):
    print(f"ფასი: {products[typeOfProductInput]}")
    confirmationInput = input("ნამდვილად გსურთ შეძენა?")
    if confirmationInput == "yes":
        print("მადლობა, კიდევ გვეწვიეთ")
    else:
        anythingElseInput = input("სხვა რამის შეძენა ხომ არ გსურთ?")
        anythingElseInput.lower
        if anythingElseInput == "yes":
            typeOfProduct()
        else:
            print("დროებით")


productListPrinter(products)
