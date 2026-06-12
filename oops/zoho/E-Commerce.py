class Product:
    productId = 0
    
    def __init__(self, name:str, category:str, price:float, stock: int):
        Product.productId += 1
        self.product_id = Product.productId
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock
        
    def check_stock_quantity(self, wanted) -> bool:
        if wanted > self.stock_quantity:
            return False
        return True
        
class Customer:
    customerId = 1000
    
    def __init__(self, name):
        Customer.customerId += 1
        self.customer_id = Customer.customerId
        self.customer_name = name
        self.cart: dict[int, Product] = {}
        
    def add_prodct(self,new_product, product_id, quantity):
        if product_id in self.cart:
            self.cart[product_id].stock_quantity += quantity
        else:
            self.cart[product_id] = new_product
            
    def _invoice(self):
        for val in self.cart.values():
            inner = [val.name, val.product_id, val.stock_quantity, val.price, val.stock_quantity*val.price]
            print(f"{inner[0]:10} {inner[1]} {inner[2]} x {inner[3]} = {inner[4]}")
      
        
class Order:
    orderId = 100
    def __init__(self, customer):
        Order.orderId += 1
        self.order_id = Order.orderId
        self.customer: Customer = customer
        self.order_status: str | None = None
        
      
class Inventory:
    
    def __init__(self):
        self.product_list: dict[int, Product] = {}
        self.customer_list: dict[int, Customer] = {}
        self.order_list: dict[int, Order] = {}
        
        
class E_Commerce:
    
    def __init__(self):
        self.inventory = Inventory()
        self.product_list = self.inventory.product_list
        self.customer_list = self.inventory.customer_list
        self.order_list = self.inventory.order_list
    
    def add_product(self, name, category, price, stock, prd_id=None):
        if self.product_list and prd_id in self.product_list:
            self.product_list[prd_id].stock_quantity += stock
            return None
        
        product = Product(name, category, price, stock)
        self.product_list[product.product_id] = product
        
    def browseProducts(self, products=None):
        products = self.product_list.values() if not products else products
        head = ["Poduct ID", "Product Name", "Category", "Price", "Quantity"]
        print(f"{head[0]:15} {head[1]:15} {head[2]:15} {head[3]:15} {head[4]:15}")
        print("-" * 100)
        for product in products:
            print(f"{product.product_id:<15} {product.name:<15} {product.category:<15} {product.price:<15} {product.stock_quantity:<15}")
            
    def createCustomer(self, name):
        customer = Customer(name)
        self.customer_list[customer.customer_id] = customer
        print(f"[SUCCESS] {name} : {customer.customer_id}")
            
    def addItemToCart(self,customer_id, product_id: int, quantity: int):
        product = self.product_list[product_id]
        new_product = Product(product.name, product.category, product.price, quantity)
        
        customer = self.customer_list[customer_id]
        original_quantity = product.stock_quantity
        
        if product.check_stock_quantity(quantity):
            customer.add_prodct(new_product, product_id, quantity)
            product.stock_quantity -= quantity
            self.browseProducts(customer.cart.values())
            
        else:
            print(f"[ERROR] we have only {original_quantity} but you have given {quantity}")
            
    def viewCartAndCheckout(self, customer_id):
        customer = self.customer_list[customer_id]
        order: Order = Order(customer)
        order.order_status = "Successful"
        self.order_list[order.order_id] = order
        
        
            
if __name__ == "__main__":
    ec = E_Commerce()
    
    ec.add_product("Mouse", "Electronics", 600.00, 3)
    ec.add_product("Mug", "Kitchen", 200.00, 5)
    ec.add_product("Mouse", "Electronics", 600.00, 3, 1)
    
    while True:
        option= int(input("""
              1. Browse products
              2. Add Items to cart
              3. View cart & Checkout
              4. Cancel Order
              5. View Order Histroy
              6. Create Customer
              7. Exit
              Enter your choice (1-6) : """))

        if option == 1:
            ec.browseProducts()

        elif option == 2:
            ec.browseProducts()
            cus_id = int(input("Enter the customer ID : "))
            if cus_id in ec.customer_list:
                prd_id = int(input("Enter the product ID : "))
                if prd_id in ec.product_list:
                    quantity = int(input("Enter the quantity of the prodcut : "))
                    ec.addItemToCart(cus_id, prd_id, quantity)
                else:
                    print("Given product id invalid")
            else:
                print("Given Customer id in invalid")
                
        elif option == 3:
            cus_id = int(input("Enter the Customer ID : "))
            if cus_id in ec.customer_list:
                cus = ec.customer_list[cus_id]
                cus._invoice()
                ans = input("Please enter yes / no for book order : ")
                if ans == "yes":
                    ec.viewCartAndCheckout(cus_id)
                else:
                    print("Order not created")
            else:
                print("Given custome ID invalid")
                
        elif option == 6:
            name = input("Enter the customer name : ")
            ec.createCustomer(name)
        else:
            break

        
    
