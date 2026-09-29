from datetime import datetime
import json
products = []
# Load saved products
try:
    with open("products.json", "r") as file:
        products = json.load(file)

    for product in products:
        product["purchase_date"] = datetime.strptime(
            product["purchase_date"], "%d-%m-%Y"
        )

        product["expiry"] = datetime.strptime(
            product["expiry"], "%d-%m-%Y"
        )

        if "service_details" not in product:
            product["service_details"] = "No service recorded."

except FileNotFoundError:
    products = []


# Main Menu
while True:

    print()
    print("===========================================")
    print("          SMART WARRANTY CHECKER")
    print("===========================================")

    print("1. Add Product")
    print("2. View Products")
    print("3. Check Warranty")
    print("4. Search Product")
    print("5. Add Service / Repair")
    print("6. Delete Product")
    print("7. Exit")

    choice = input("Enter your choice: ")

    # ADD PRODUCT
    if choice == "1":

        print()
        print("----------- ADD PRODUCT -----------")

        product_name = input("Enter Product Name: ")
        product_brand = input("Enter Brand: ")

        purchase_date_input = input(
            "Enter purchase date (DD-MM-YYYY): "
        )

        purchase_price = input("Enter price: ")

        warranty_period = int(
            input("Enter warranty period (years): ")
        )

        purchase_date = datetime.strptime(
            purchase_date_input,
            "%d-%m-%Y"
        )

        warranty_expiry = purchase_date.replace(
            year=purchase_date.year + warranty_period
        )

        today = datetime.today()

        if today <= warranty_expiry:
            status = "ACTIVE"
            remaining_days = (
                warranty_expiry - today
            ).days
        else:
            status = "EXPIRED"
            remaining_days = 0

        print()
        print("Product Details:")
        print("------------------")

        print("Product:", product_name)
        print("Brand:", product_brand)

        print(
            "Purchase Date:",
            purchase_date.strftime("%d-%m-%Y")
        )

        print("Price:", purchase_price)

        print(
            "Warranty:",
            warranty_period,
            "years"
        )

        print(
            "Warranty Expiry:",
            warranty_expiry.strftime("%d-%m-%Y")
        )

        print("Status:", status)

        print(
            "Remaining Days:",
            remaining_days
        )

        # Create product dictionary
        product = {
            "name": product_name,
            "brand": product_brand,
            "purchase_date": purchase_date,
            "price": purchase_price,
            "warranty": warranty_period,
            "expiry": warranty_expiry,
            "status": status,
            "service_details": "No service recorded."
        }

        products.append(product)

        # Save products to JSON
        data_to_save = []

        for item in products:

            data_to_save.append({
                "name": item["name"],
                "brand": item["brand"],
                "purchase_date": item["purchase_date"].strftime(
                    "%d-%m-%Y"
                ),
                "price": item["price"],
                "warranty": item["warranty"],
                "expiry": item["expiry"].strftime(
                    "%d-%m-%Y"
                ),
                "status": item["status"],
                "service_details": item.get(
                    "service_details",
                    "No service recorded."
                )
            })

        with open("products.json", "w") as file:
            json.dump(
                data_to_save,
                file,
                indent=4
            )

        print()
        print("Product saved successfully!")


    # VIEW PRODUCTS
    elif choice == "2":

        print()
        print("----------- SAVED PRODUCTS -----------")

        if len(products) == 0:

            print("No products saved.")

        else:

            for product in products:

                print()
                print("Product:", product["name"])
                print("Brand:", product["brand"])
                print("Price:", product["price"])

                print(
                    "Warranty:",
                    product["warranty"],
                    "years"
                )

                print(
                    "Expiry:",
                    product["expiry"].strftime(
                        "%d-%m-%Y"
                    )
                )

                print(
                    "Status:",
                    product["status"]
                )

                print(
                    "Service:",
                    product.get(
                        "service_details",
                        "No service recorded."
                    )
                )

                print("-------------------------")


    # CHECK WARRANTY
    elif choice == "3":

        print()
        print("----------- WARRANTY CHECK -----------")

        if len(products) == 0:

            print("No products available.")

        else:

            today = datetime.today()

            for product in products:

                remaining_days = (
                    product["expiry"] - today
                ).days

                if remaining_days < 0:

                    print(
                        product["name"],
                        "-> WARRANTY EXPIRED"
                    )

                elif remaining_days <= 30:

                    print(
                        product["name"],
                        "-> WARRANTY EXPIRING SOON"
                    )

                    print(
                        "Remaining Days:",
                        remaining_days
                    )

                else:

                    print(
                        product["name"],
                        "-> WARRANTY ACTIVE"
                    )

                    print(
                        "Remaining Days:",
                        remaining_days
                    )


    # SEARCH PRODUCT
    elif choice == "4":

        print()
        print("----------- SEARCH PRODUCT -----------")

        search_name = input(
            "Enter product name to search: "
        )

        found = False

        for product in products:

            if (
                product["name"].lower()
                == search_name.lower()
            ):

                print()
                print("Product Found")
                print("---------------------")

                print(
                    "Product:",
                    product["name"]
                )

                print(
                    "Brand:",
                    product["brand"]
                )

                print(
                    "Price:",
                    product["price"]
                )

                print(
                    "Warranty:",
                    product["warranty"],
                    "years"
                )

                print(
                    "Expiry:",
                    product["expiry"].strftime(
                        "%d-%m-%Y"
                    )
                )

                print(
                    "Status:",
                    product["status"]
                )

                print(
                    "Service:",
                    product.get(
                        "service_details",
                        "No service recorded."
                    )
                )

                found = True

        if found == False:

            print("Product not found.")


    # SERVICE / REPAIR
    elif choice == "5":

        print()
        print("----------- SERVICE / REPAIR -----------")

        product_name = input(
            "Enter product name: "
        )

        found = False

        for product in products:

            if (
                product["name"].lower()
                == product_name.lower()
            ):

                service = input(
                    "Enter service / repair details: "
                )

                product["service_details"] = service

                # Save updated data
                data_to_save = []

                for item in products:

                    data_to_save.append({
                        "name": item["name"],
                        "brand": item["brand"],
                        "purchase_date": item["purchase_date"].strftime(
                            "%d-%m-%Y"
                        ),
                        "price": item["price"],
                        "warranty": item["warranty"],
                        "expiry": item["expiry"].strftime(
                            "%d-%m-%Y"
                        ),
                        "status": item["status"],
                        "service_details": item.get(
                            "service_details",
                            "No service recorded."
                        )
                    })

                with open("products.json", "w") as file:

                    json.dump(
                        data_to_save,
                        file,
                        indent=4
                    )

                print()
                print(
                    "Service details saved successfully!"
                )

                found = True

        if found == False:

            print("Product not found.")


    # DELETE PRODUCT
    elif choice == "6":

        print()
        print("----------- DELETE PRODUCT -----------")

        product_name = input(
            "Enter product name to delete: "
        )

        found = False

        for product in products:

            if (
                product["name"].lower()
                == product_name.lower()
            ):

                products.remove(product)

                data_to_save = []

                for item in products:

                    data_to_save.append({
                        "name": item["name"],
                        "brand": item["brand"],
                        "purchase_date": item["purchase_date"].strftime(
                            "%d-%m-%Y"
                        ),
                        "price": item["price"],
                        "warranty": item["warranty"],
                        "expiry": item["expiry"].strftime(
                            "%d-%m-%Y"
                        ),
                        "status": item["status"],
                        "service_details": item.get(
                            "service_details",
                            "No service recorded."
                        )
                    })

                with open("products.json", "w") as file:

                    json.dump(
                        data_to_save,
                        file,
                        indent=4
                    )

                print()
                print(
                    "Product deleted successfully!"
                )

                found = True
                break

        if found == False:

            print("Product not found.")


    # EXIT
    elif choice == "7":

        print()
        print(
            "Thank you for using "
            "Smart Warranty Checker!"
        )

        break


    # INVALID CHOICE
    else:

        print()
        print(
            "Invalid choice. "
            "Please enter a number from 1 to 7."
        )