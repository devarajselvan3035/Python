class Customer:
    customerId = 100
    def __init__(self, name, phone):
        Customer.customerId += 1
        self.customer_id = Customer.customerId
        self.name = name
        self.phone = phone
        
        
class Items:
    itemsId = 0
    
    def __init__(self, item_name, quantity, price):
        Items.itemsId += 1
        self.item_id = Items.itemsId
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        
    def totol_price(self):
        return self.quantity * self.price
    
class Invoice:
    invoiceId = 0
    
    def __init__(self, customer_id: int, item_list:list = []):
        Invoice.invoiceId += 1
        self.invoice_id = Invoice.invoiceId
        self.item_list = item_list
        self.customer_id = customer_id
        
        
class Inventory:
    def __init__(self):
        self.list_customers: dict[int, Customer] = {}
        self.list_invoice: dict[int, Invoice] = {}
    
    def all_invoice_of_customer(self, customer_id) -> list[Invoice]:
        result = []
        for key, val in self.list_invoice.items():
            if val.customer_id == customer_id:
                result.append(val)
        return result
                
class InvoiceManagement:
    
    def __init__(self):
        self.inventory = Inventory()
    
    def addCustomer(self, name, phone):
        customer = Customer(name, phone)
        self.inventory.list_customers[customer.customer_id] = customer
        
    def addInvoice(self, customer_id):
        invoice = Invoice(customer_id)
        self.inventory.list_invoice[invoice.invoice_id] = invoice
        
    def addItemsToInvoice(self, invoice_id: int, items: list[Items] = []):
        invoice = self.inventory.list_invoice[invoice_id]
        invoice.item_list = items
    
    def listAllCustomer(self):
        return self.inventory.list_customers
        
    def listAllInvoice(self):
        return self.inventory.list_invoice
    
    def listAllInvoiceCustomer(self, customer_id):
        return self.inventory.all_invoice_of_customer(customer_id)
        
        
if __name__ == "__main__":
    management = InvoiceManagement()
    management.addCustomer("devaraj", "6379421146")
    management.addCustomer("Kavi", "9500913035")
    management.addInvoice(101)
    management.addInvoice(101)
    inlist = management.listAllInvoice()
    item1 = Items("mango", 1, 30)
    item2 = Items("apple", 1, 20)
    management.addItemsToInvoice(1, [item1, item2])
    print(management.listAllInvoiceCustomer(101))
    
    