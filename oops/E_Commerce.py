import datetime
from abc import ABC, abstractmethod
from typing import Dict, List, Optional


# ==========================================
# 1. DOMAIN MODELS (ENCAPSULATION)
# ==========================================

class Product:
    """Encapsulates properties and mutation logic for marketplace merchandise."""
    def __init__(self, product_id: str, name: str, category: str, unit_price: float, stock: int):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__category: str = category
        self.__unit_price: float = unit_price
        self.__stock: int = stock

    # Getters
    def get_product_id(self) -> str: return self.__product_id
    def get_name(self) -> str: return self.__name
    def get_category(self) -> str: return self.__category
    def get_unit_price(self) -> float: return self.__unit_price
    def get_stock(self) -> int: return self.__stock

    # Business Logic Mutations
    def reduce_stock(self, quantity: int) -> bool:
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        return False

    def replenish_stock(self, quantity: int) -> None:
        if quantity > 0:
            self.__stock += quantity


class Customer:
    """Encapsulates account metrics and financial balance transitions for a Buyer."""
    def __init__(self, customer_id: str, name: str, initial_wallet: float):
        self.__customer_id: str = customer_id
        self.__name: str = name
        self.__wallet_balance: float = initial_wallet

    # Getters
    def get_customer_id(self) -> str: return self.__customer_id
    def get_name(self) -> str: return self.__name
    def get_wallet_balance(self) -> float: return self.__wallet_balance

    # Financial Operations
    def deduct_balance(self, amount: float) -> bool:
        if amount <= self.__wallet_balance:
            self.__wallet_balance -= amount
            return True
        return False

    def refund_balance(self, amount: float) -> None:
        if amount > 0:
            self.__wallet_balance += amount


class CartItem:
    """Represents a discrete product reservation intent within a shopping cart."""
    def __init__(self, product: Product, quantity: int):
        self.__product: Product = product
        self.__quantity: int = quantity

    def get_product(self) -> Product: return self.__product
    def get_quantity(self) -> int: return self.__quantity
    
    def set_quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    def calculate_item_total(self) -> float:
        return self.__product.get_unit_price() * self.__quantity


class ShoppingCart:
    """Manages the volatile stage of a customer's requested line-items."""
    def __init__(self, customer_id: str):
        self.__customer_id: str = customer_id
        self.__items: Dict[str, CartItem] = {}  # Map Product_ID -> CartItem for O(1) mutations

    def get_customer_id(self) -> str: return self.__customer_id
    def get_items(self) -> List[CartItem]: return list(self.__items.values())

    def add_or_update_item(self, product: Product, quantity: int) -> None:
        p_id = product.get_product_id()
        if p_id in self.__items:
            current_qty = self.__items[p_id].get_quantity()
            self.__items[p_id].set_quantity(current_qty + quantity)
        else:
            self.__items[p_id] = CartItem(product, quantity)

    def clear_cart(self) -> None:
        self.__items.clear()

    def calculate_subtotal(self) -> float:
        return sum(item.calculate_item_total() for item in self.__items.values())


class Order:
    """Represents an unalterable processing record of a financial checkout transaction."""
    def __init__(self, order_id: str, customer_id: str, items: List[CartItem], discount_applied: float, grand_total: float):
        self.__order_id: str = order_id
        self.__customer_id: str = customer_id
        self.__timestamp: datetime.datetime = datetime.datetime.now()
        # Create immutable snapshots of items bought (Capturing product state at checkout time)
        self.__purchased_items: List[tuple] = [
            (item.get_product(), item.get_quantity(), item.get_product().get_unit_price()) 
            for item in items
        ]
        self.__discount_applied: float = discount_applied
        self.__grand_total: float = grand_total
        self.__status: str = "Placed"  # Internal State: Placed / Canceled

    # Getters
    def get_order_id(self) -> str: return self.__order_id
    def get_customer_id(self) -> str: return self.__customer_id
    def get_grand_total(self) -> float: return self.__grand_total
    def get_status(self) -> str: return self.__status
    def get_purchased_items(self) -> List[tuple]: return self.__purchased_items
    def get_discount_applied(self) -> float: return self.__discount_applied
    def get_timestamp_str(self) -> str: return self.__timestamp.strftime("%Y-%m-%d %H:%M:%S")

    def cancel_order(self) -> None:
        self.__status = "Canceled"


# ==========================================
# 2. DISCOUNT & COUPON ENGINE (POLYMORPHISM & ABSTRACTION)
# ==========================================

class CouponStrategy(ABC):
    """Abstract base class establishing interface for contract-based pricing mutations."""
    @abstractmethod
    def calculate_discount(self, items: List[CartItem]) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class FlatDiscountCoupon(CouponStrategy):
    """Concrete Strategy: Deducts fixed amount if global threshold condition is met."""
    def __init__(self, discount_amount: float, threshold: float, code: str):
        self.__discount_amount = discount_amount
        self.__threshold = threshold
        self.__code = code

    def calculate_discount(self, items: List[CartItem]) -> float:
        subtotal = sum(item.calculate_item_total() for item in items)
        if subtotal >= self.__threshold:
            return self.__discount_amount
        return 0.0

    def get_description(self) -> str:
        return f"₹{self.__discount_amount} off on orders above ₹{self.__threshold} ({self.__code})"


class CategoryPercentageCoupon(CouponStrategy):
    """Concrete Strategy: Targets matching categorizations for fractional deduction."""
    def __init__(self, category: str, percentage: float, code: str):
        self.__category = category.lower()
        self.__percentage = percentage
        self.__code = code

    def calculate_discount(self, items: List[CartItem]) -> float:
        discount = 0.0
        for item in items:
            if item.get_product().get_category().lower() == self.__category:
                discount += item.calculate_item_total() * (self.__percentage / 100.0)
        return discount

    def get_description(self) -> str:
        return f"{self.__percentage}% off on {self.__category.capitalize()} items ({self.__code})"


# ==========================================
# 3. CORE SERVICE / MARKETPLACE ENGINE
# ==========================================

class MarketplaceEngine:
    """Orchestrates system state modifications across data registers."""
    def __init__(self):
        self.__products: Dict[str, Product] = {}
        self.__customers: Dict[str, Customer] = {}
        self.__carts: Dict[str, ShoppingCart] = {}
        self.__orders: Dict[str, Order] = {}
        self.__coupons: Dict[str, CouponStrategy] = {}
        self.__order_counter: int = 100000

    # Registration Helper Methods
    def register_product(self, product: Product) -> None:
        self.__products[product.get_product_id()] = product

    def register_customer(self, customer: Customer) -> None:
        self.__customers[customer.get_customer_id()] = customer
        self.__carts[customer.get_customer_id()] = ShoppingCart(customer.get_customer_id())

    def register_coupon(self, code: str, strategy: CouponStrategy) -> None:
        self.__coupons[code.upper()] = strategy

    # System Getters
    def get_all_products(self) -> List[Product]: return list(self.__products.values())
    def get_customer(self, c_id: str) -> Optional[Customer]: return self.__customers.get(c_id)
    def get_product(self, p_id: str) -> Optional[Product]: return self.__products.get(p_id)
    def get_cart(self, c_id: str) -> Optional[ShoppingCart]: return self.__carts.get(c_id)
    def get_order(self, o_id: str) -> Optional[Order]: return self.__orders.get(o_id)
    
    def get_orders_by_customer(self, c_id: str) -> List[Order]:
        return [ord_obj for ord_obj in self.__orders.values() if ord_obj.get_customer_id() == c_id]

    # Core Transaction Logic Execution
    def add_product_to_user_cart(self, customer_id: str, product_id: str, quantity: int) -> str:
        customer = self.get_customer(customer_id)
        if not customer:
            return "ERROR: Identified Customer record does not exist."
        
        product = self.get_product(product_id)
        if not product:
            return "ERROR: Identified Product catalog entry does not exist."

        if quantity <= 0:
            return "ERROR: Requested tracking allocation must be above 0 units."

        # Fetch structural item context to see what's already queued inside the cart
        cart = self.__carts[customer_id]
        existing_qty = 0
        for item in cart.get_items():
            if item.get_product().get_product_id() == product_id:
                existing_qty = item.get_quantity()
                break

        if product.get_stock() < (existing_qty + quantity):
            return f"ERROR: Insufficient Inventory. Available Stock: {product.get_stock()} units."

        cart.add_or_update_item(product, quantity)
        return f"SUCCESS: Aggregated {quantity} units of '{product.get_name()}' into cart."

    def execute_checkout(self, customer_id: str, coupon_code: str) -> str:
        customer = self.get_customer(customer_id)
        if not customer:
            return "ERROR: Identified Customer record does not exist."

        cart = self.__carts[customer_id]
        cart_items = cart.get_items()
        if not cart_items:
            return "ERROR: Operation aborted. Cart contains no items."

        # Real-time stock re-verification pass prior to final calculation steps
        for item in cart_items:
            if item.get_product().get_stock() < item.get_quantity():
                return f"ERROR: Inventory changed for '{item.get_product().get_name()}'. Reduce volume."

        subtotal = cart.calculate_subtotal()
        discount = 0.0

        if coupon_code.strip():
            coupon = self.__coupons.get(coupon_code.upper())
            if coupon:
                discount = coupon.calculate_discount(cart_items)
            else:
                return "ERROR: Coupon code unrecognized."

        grand_total = max(0.0, subtotal - discount)

        # Balance check logic validation
        if not customer.deduct_balance(grand_total):
            return f"ERROR: Failed Transaction. Insufficient wallet resources. Deficit: ₹{grand_total - customer.get_wallet_balance():.2f}"

        # Deduct inventories cleanly across catalogs
        for item in cart_items:
            item.get_product().reduce_stock(item.get_quantity())

        # Generate structural order log entry
        self.__order_counter += 1
        new_order_id = f"ORD-{self.__order_counter}"
        new_order = Order(new_order_id, customer_id, cart_items, discount, grand_total)
        
        self.__orders[new_order_id] = new_order
        cart.clear_cart()

        return f"SUCCESS: Order processed successfully! ID: {new_order_id} | Total Paid: ₹{grand_total:.2f}"

    def process_order_cancellation(self, order_id: str) -> str:
        order = self.get_order(order_id)
        if not order:
            return "ERROR: Identified Order tracking reference does not exist."

        if order.get_status() == "Canceled":
            return "ERROR: Processing conflict. Order has already been canceled."

        customer = self.get_customer(order.get_customer_id())
        if not customer:
            return "ERROR: Customer profile associated with order is missing."

        # Refund system transaction total
        customer.refund_balance(order.get_grand_total())

        # Inventory restoration iteration
        for prod_ref, qty, _ in order.get_purchased_items():
            prod_ref.replenish_stock(qty)

        order.cancel_order()
        return f"SUCCESS: Order '{order_id}' has been canceled. Funds refunded and stock replenished."


# ==========================================
# 4. CONSOLE USER INTERFACE ENGINE
# ==========================================

def run_zoho_assessment_simulation():
    # Instantiate Core Application Environment Engine
    engine = MarketplaceEngine()

    # Pre-Seed Directory Data Infrastructure
    engine.register_product(Product("P001", "Wireless Mouse", "Electronics", 600.00, 5))
    engine.register_product(Product("P002", "Mechanical Keyboard", "Electronics", 2500.00, 3))
    engine.register_product(Product("P003", "Coffee Mug", "Kitchen", 350.00, 10))
    engine.register_product(Product("P004", "Stainless Bottle", "Kitchen", 800.00, 0)) # Out of Stock

    engine.register_customer(Customer("C101", "Devaraj", 5000.00))
    engine.register_customer(Customer("C102", "Amit Kumar", 1200.00))

    engine.register_coupon("FLAT100", FlatDiscountCoupon(100.00, 1000.00, "FLAT100"))
    engine.register_coupon("ELEC10", CategoryPercentageCoupon("Electronics", 10.0, "ELEC10"))

    while True:
        print("\n" + "="*50)
        print("         ZOHO IN-MEMORY E-COMMERCE CONSOLE")
        print("="*50)
        print("1. Browse Products Catalog")
        print("2. Add Merchandise Item to Cart")
        print("3. View Cart Details & Checkout")
        print("4. Execute Order Cancellation")
        print("5. View Customer Order Receipts History")
        print("6. Exit Platform Terminal")
        print("="*50)
        
        choice = input("Select operation interface sequence (1-6): ").strip()

        if choice == "1":
            print("\n" + "-"*80)
            print(f"{'Prod ID':<10} | {'Name':<22} | {'Category':<15} | {'Unit Price':<12} | {'Stock Register'}")
            print("-"*80)
            for p in engine.get_all_products():
                stock_status = f"{p.get_stock()} Available" if p.get_stock() > 0 else "[OUT OF STOCK]"
                print(f"{p.get_product_id():<10} | {p.get_name():<22} | {p.get_category():<15} | ₹{p.get_unit_price():<11.2f} | {stock_status}")
            print("-"*80)

        elif choice == "2":
            c_id = input("Enter Active Customer Identification String: ").strip()
            p_id = input("Enter Target Product Catalog Identifier: ").strip()
            try:
                qty = int(input("Enter Desired Units Count: ").strip())
                status_msg = engine.add_product_to_user_cart(c_id, p_id, qty)
                print(status_msg)
            except ValueError:
                print("ERROR: Parsing Failure. Quantity allocation parameter must be an integer.")

        elif choice == "3":
            c_id = input("Enter Customer Identifier to parse: ").strip()
            customer = engine.get_customer(c_id)
            if not customer:
                print("ERROR: Identified Customer record does not exist.")
                continue

            cart = engine.get_cart(c_id)
            items = cart.get_items()
            if not items:
                print("Notice: Active cart configuration contains no allocated records.")
                continue

            print("\n--- CURRENT SHOPPING CART VIEW ---")
            for item in items:
                print(f" • {item.get_product().get_name()} ({item.get_product().get_product_id()}) x {item.get_quantity()} | Line Cost: ₹{item.calculate_item_total():.2f}")
            subtotal = cart.calculate_subtotal()
            print(f"Current Accrued Subtotal: ₹{subtotal:.2f}")
            print(f"Your Available Wallet Balance: ₹{customer.get_wallet_balance():.2f}")
            
            coupon_input = input("Apply Discount Code (Press enter to skip empty code evaluation): ").strip()
            
            print("\n--- TRANSACTION INVOICE RUN-TIME VERIFICATION ---")
            print(f"Subtotal Charge Basis: ₹{subtotal:.2f}")
            
            discount = 0.0
            if coupon_input:
                # Dynamic localized dry-run computation for layout validation purposes before transaction lock
                test_coupon = engine._MarketplaceEngine__coupons.get(coupon_input.upper()) # safe lookup via naming standard
                if test_coupon:
                    discount = test_coupon.calculate_discount(items)
                    print(f"Active Promotion Match: {test_coupon.get_description()}")
                else:
                    print("Active Promotion Match: INVALID/UNRECOGNIZED CODE")
            
            grand_total = max(0.0, subtotal - discount)
            print(f"Computed Discount Offset: -₹{discount:.2f}")
            print(f"Net Payable Financial Liability: ₹{grand_total:.2f}")
            print(f"Post-Transaction Projected Wallet: ₹{customer.get_wallet_balance() - grand_total:.2f}")
            
            confirm = input("\nCommit financial liability and finalize order? (Y/N): ").strip().upper()
            if confirm == "Y":
                checkout_result = engine.execute_checkout(c_id, coupon_input)
                print(checkout_result)
            else:
                print("Checkout execution pipeline suspended by user request.")

        elif choice == "4":
            o_id = input("Enter Global Order Tracking Reference ID to cancel: ").strip()
            cancel_result = engine.process_order_cancellation(o_id)
            print(cancel_result)

        elif choice == "5":
            c_id = input("Enter Target Customer ID: ").strip()
            customer = engine.get_customer(c_id)
            if not customer:
                print("ERROR: Identified Customer record does not exist.")
                continue
                
            orders = engine.get_orders_by_customer(c_id)
            print(f"\n==================================================")
            print(f" HISTORICAL TRANSACTION LOGS FOR CUSTOMER: {c_id}")
            print(f" Current Profile Wallet Balance: ₹{customer.get_wallet_balance():.2f}")
            print(f"==================================================")
            
            if not orders:
                print("No past historical transaction entries verified for this profile entity.")
                continue
                
            for ord_obj in orders:
                status_flag = "[ACTIVE PLACED]" if ord_obj.get_status() == "Placed" else "[CANCELED & REFUNDED]"
                print(f"\nOrder ID    : {ord_obj.get_order_id()}  ({status_flag})")
                print(f"Timestamp   : {ord_obj.get_timestamp_str()}")
                print(f"Items:")
                for prod_ref, qty, checked_out_price in ord_obj.get_purchased_items():
                    print(f"  - {prod_ref.get_name()} x {qty} @ ₹{checked_out_price:.2f} per unit")
                print(f"Discount    : -₹{ord_obj.get_discount_applied():.2f}")
                print(f"Grand Total : ₹{ord_obj.get_grand_total():.2f}")
                print(f"--------------------------------------------------")

        elif choice == "6":
            print("\nExiting System Simulation. Evaluation session closed.")
            break
        else:
            print("ERROR: Invalid operational input. Please choose an options sequence integer between 1 and 6.")


if __name__ == "__main__":
    run_zoho_assessment_simulation()