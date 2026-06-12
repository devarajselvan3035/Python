#!/usr/bin/env python3
"""
Zoho Advanced Programming Assessment - Round 3
System: In-Memory Banking Management Application
Language: Python 3.8+ (Pure OOP, Standard Library Only)
"""

from abc import ABC, abstractmethod
from collections import deque
from datetime import datetime
from typing import Deque, Dict, Optional, Union


# =====================================================================
# 1. TRANSACTION LOG DOMAIN
# =====================================================================

class Transaction:
    """
    Represents an immutable financial record of a single system event.
    """
    _id_counter: int = 1000  # Class-level counter for unique Transaction IDs

    def __init__(
        self, 
        source_acc: Optional[str], 
        dest_acc: Optional[str], 
        amount: float, 
        txn_type: str, 
        status: str
    ) -> None:
        Transaction._id_counter += 1
        self.__txn_id: str = f"TXN-{Transaction._id_counter}"
        self.__source_acc: str = source_acc if source_acc else "SYSTEM"
        self.__dest_acc: str = dest_acc if dest_acc else "SYSTEM"
        self.__amount: float = amount
        self.__txn_type: str = txn_type
        self.__status: str = status
        self.__timestamp: datetime = datetime.now()

    # Encapsulation via Read-Only Properties
    @property
    def txn_id(self) -> str:
        return self.__txn_id

    @property
    def source_acc(self) -> str:
        return self.__source_acc

    @property
    def dest_acc(self) -> str:
        return self.__dest_acc

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def txn_type(self) -> str:
        return self.__txn_type

    @property
    def status(self) -> str:
        return self.__status

    @property
    def timestamp(self) -> str:
        return self.__timestamp.strftime("%Y-%m-%d %H:%M:%S")


# =====================================================================
# 2. CUSTOMER DOMAIN
# =====================================================================

class Customer:
    """
    Encapsulates a bank client's primary identity profiles.
    """
    _id_counter: int = 1000

    def __init__(self, name: str, contact: str, secure_pin: str) -> None:
        Customer._id_counter += 1
        self.__customer_id: str = f"CUST-{Customer._id_counter}"
        self.__name: str = name
        self.__contact: str = contact
        self.__secure_pin: str = secure_pin

    @property
    def customer_id(self) -> str:
        return self.__customer_id

    @property
    def name(self) -> str:
        return self.__name


# =====================================================================
# 3. ACCOUNT DOMAIN (INHERITANCE & ABSTRACTION)
# =====================================================================

class Account(ABC):
    """
    Abstract Base Class enforcing the blueprint for polymorphic Account types.
    Defines structural encapsulation and state handling for security lifecycles.
    """
    _account_num_counter: int = 10000000000  # Structural seed for 11-digit generation
    MAX_FAILED_ATTEMPTS: int = 3
    MAX_LOG_LIMIT: int = 10

    def __init__(self, customer: Customer, secret_pin: str, initial_deposit: float) -> None:
        Account._account_num_counter += 1
        self.__account_number: str = str(Account._account_num_counter)
        self.__customer: Customer = customer
        self.__secret_pin: str = secret_pin
        self._balance: float = initial_deposit
        
        # Security fields
        self.__is_locked: bool = False
        self.__failed_attempts: int = 0
        
        # Fixed-size sliding circular history using collection tracking optimizations
        self.__history_buffer: Deque[Transaction] = deque(maxlen=self.MAX_LOG_LIMIT)
        
        # Automatically log initialization event
        self.log_transaction(None, self.__account_number, initial_deposit, "DEPOSIT", "SUCCESS")

    # --- Structural Getters ---
    @property
    def account_number(self) -> str:
        return self.__account_number

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def is_locked(self) -> bool:
        return self.__is_locked

    @property
    def history(self) -> Deque[Transaction]:
        return self.__history_buffer

    @property
    @abstractmethod
    def minimum_balance_threshold(self) -> float:
        """Polymorphic property ensuring sub-types cleanly define their floor balance."""
        pass

    @property
    @abstractmethod
    def account_type_label(self) -> str:
        """Polymorphic label representation for UI components."""
        pass

    # --- Core Business Logic Executions ---
    def verify_and_authenticate(self, input_pin: str) -> bool:
        """
        Validates security entries and dynamically handles state tracking lockouts.
        """
        if self.__is_locked:
            print(f"\n[SECURITY LOCK] Account {self.__account_number} is frozen due to past violations.")
            return False

        if self.__secret_pin == input_pin:
            self.__failed_attempts = 0  # Flush consecutive failure counter
            return True
        else:
            self.__failed_attempts += 1
            remaining: int = self.MAX_FAILED_ATTEMPTS - self.__failed_attempts
            print(f"\n[SECURITY ERROR] Invalid PIN Entry. Attempts remaining: {remaining}")
            
            if self.__failed_attempts >= self.MAX_FAILED_ATTEMPTS:
                self.__is_locked = True
                print(f"[SECURITY ALERT] 3 Failed attempts registered. Account {self.__account_number} is now LOCKED.")
            return False

    def deposit(self, amount: float) -> None:
        """Executes a simple value increment to ledger balance."""
        self._balance += amount
        self.log_transaction(None, self.__account_number, amount, "DEPOSIT", "SUCCESS")

    def withdraw(self, amount: float) -> bool:
        """
        Executes deduction checking balance floors directly.
        Returns true if transaction succeeds, false otherwise.
        """
        if self.__is_locked:
            print("\n[TRANSACTION FAILED] Cannot process actions on a locked account.")
            return False

        if self._balance - amount < self.minimum_balance_threshold:
            print(f"\n[TRANSACTION ABORTED] Withdrawal of ₹{amount:,.2f} violates minimum "
                  f"balance requirement (Floor: ₹{self.minimum_balance_threshold:,.2f}).")
            self.log_transaction(self.__account_number, None, amount, "WITHDRAW", "FAILED")
            return False

        self._balance -= amount
        self.log_transaction(self.__account_number, None, amount, "WITHDRAW", "SUCCESS")
        return True

    def debit_for_transfer(self, amount: float) -> bool:
        """Low-level abstraction helping isolate operational transaction state components."""
        if self._balance - amount < self.minimum_balance_threshold:
            return False
        self._balance -= amount
        return True

    def credit_for_transfer(self, amount: float) -> None:
        """Low-level abstraction helping isolate operational transaction state components."""
        self._balance += amount

    def log_transaction(
        self, 
        source: Optional[str], 
        dest: Optional[str], 
        amount: float, 
        txn_type: str, 
        status: str
    ) -> None:
        """Appends event records onto bounded chronological circular log frame."""
        record = Transaction(source, dest, amount, txn_type, status)
        self.__history_buffer.append(record)


class SavingsAccount(Account):
    """
    Concrete Implementations of Savings Accounts Rules.
    """
    @property
    def minimum_balance_threshold(self) -> float:
        return 5000.0

    @property
    def account_type_label(self) -> str:
        return "Savings Account"


class CurrentAccount(Account):
    """
    Concrete Implementations of Current Accounts Rules.
    """
    @property
    def minimum_balance_threshold(self) -> float:
        return 10000.0

    @property
    def account_type_label(self) -> str:
        return "Current Account"


# =====================================================================
# 4. CORE ENGINE & CORE ARCHITECTURE COORDINATOR
# =====================================================================

class BankEngine:
    """
    Façade Coordinator handling routing processing structures, 
    in-memory entity indexes, and transaction atomicity logic.
    """
    def __init__(self) -> None:
        self.__accounts_registry: Dict[str, Account] = {}

    def get_account(self, account_number: str) -> Optional[Account]:
        """Fetches dynamic object instance safely from register references."""
        return self.__accounts_registry.get(account_number)

    def register_account(
        self, name: str, contact: str, account_choice: int, pin: str, initial_deposit: float
    ) -> Optional[Account]:
        """
        Builds, registers and checks system requirements parameters during account creation.
        """
        # Formulate temporary instance properties object reference
        temp_customer = Customer(name, contact, pin)
        
        if account_choice == 1:
            new_account: Account = SavingsAccount(temp_customer, pin, initial_deposit)
        elif account_choice == 2:
            new_account = CurrentAccount(temp_customer, pin, initial_deposit)
        else:
            print("\n[ERROR] Invalid Account Type selection.")
            return None

        # Check if constraints were validated during structural building phase 
        if new_account.balance < new_account.minimum_balance_threshold:
            print(f"\n[REGISTRATION REJECTED] Initial deposit of ₹{initial_deposit:,.2f} is lower than "
                  f"required minimum threshold (₹{new_account.minimum_balance_threshold:,.2f}) for a {new_account.account_type_label}.")
            return None

        # Commit to ledger maps index tracking references
        self.__accounts_registry[new_account.account_number] = new_account
        return new_account

    def execute_atomic_transfer(
        self, source_num: str, dest_num: str, amount: float, pin_entry: str
    ) -> bool:
        """
        Executes safe inter-account money transfer operations. Implements 
        clean manual application rollbacks if thresholds are violated.
        """
        source_acc = self.get_account(source_num)
        dest_acc = self.get_account(dest_num)

        if not source_acc:
            print(f"\n[ERROR] Source Account: '{source_num}' not found inside our records.")
            return False
        if not dest_acc:
            print(f"\n[ERROR] Destination Account: '{dest_num}' not found inside our records.")
            return False
        if source_num == dest_num:
            print("\n[ERROR] Operations Rejected: Source and Destination cannot be identical.")
            return False
        if amount <= 0:
            print("\n[ERROR] Amount must be greater than zero.")
            return False

        # Authenticate operations via Security modules
        if not source_acc.verify_and_authenticate(pin_entry):
            return False

        # --- CRITICAL TRANSACTION ATOMICITY SEGMENT ---
        # Attempt deduction operation phase (isolation verification check)
        if not source_acc.debit_for_transfer(amount):
            print(f"\n[TRANSACTION ABORTED - ROLLBACK] Transfer of ₹{amount:,.2f} from {source_num} failed. "
                  f"Balance cannot drop below threshold floor (₹{source_acc.minimum_balance_threshold:,.2f}).")
            source_acc.log_transaction(source_num, dest_num, amount, "TRANSFER", "FAILED")
            return False

        # Since validation checked out cleanly, proceed with credit allocation phase safely
        dest_acc.credit_for_transfer(amount)

        # Log completion updates to historical ledgers on both tracking interfaces
        source_acc.log_transaction(source_num, dest_num, amount, "TRANSFER", "SUCCESS")
        dest_acc.log_transaction(source_num, dest_num, amount, "TRANSFER", "SUCCESS")

        print(f"\n[TRANSACTION SUCCESS] Safely routed funds across entities.")
        print(f"Transferred: ₹{amount:,.2f} | From: {source_num} -> To: {dest_num}")
        return True


# =====================================================================
# 5. CLI INTERACTIVE CONSOLE DRIVER RUNNER LOOP
# =====================================================================

def main() -> None:
    engine = BankEngine()
    
    while True:
        print("\n" + "=" * 45)
        print("     ZOHO RETAIL BANK MANAGEMENT SYSTEM     ")
        print("=" * 45)
        print("1. Create Bank Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Funds to Another Account")
        print("5. View Account Statement")
        print("6. Exit")
        print("=" * 45)
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            print("\n--- Account Onboarding Module ---")
            name = input("Enter Customer Name: ").strip()
            contact = input("Enter Contact Number: ").strip()
            
            try:
                acc_choice = int(input("Select Account Type (1 for Savings, 2 for Current): "))
                pin = input("Set 4-Digit Secret Security PIN: ").strip()
                deposit = float(input("Enter Initial Deposit Amount (INR): "))
                
                if not name or not contact or not pin:
                    print("\n[ERROR] Registration properties cannot be blank values.")
                    continue
                
                account = engine.register_account(name, contact, acc_choice, pin, deposit)
                if account:
                    print(f"\n[SUCCESS] Bank entity initialization completed!")
                    print(f"Customer Name  : {account.customer.name}")
                    print(f"Customer ID    : {account.customer.customer_id}")
                    print(f"Account Number : {account.account_number} ({account.account_type_label})")
                    print(f"Initial Balance: ₹{account.balance:,.2f}")
            except ValueError:
                print("\n[SYSTEM ERROR] Numeric processing error. Input discarded.")

        elif choice == "2":
            print("\n--- Deposit Transaction Module ---")
            acc_num = input("Enter 11-Digit Account Number: ").strip()
            account = engine.get_account(acc_num)
            
            if account:
                try:
                    amount = float(input("Enter Amount to Deposit (INR): "))
                    if amount <= 0:
                        print("\n[ERROR] Amount must be positive.")
                        continue
                    account.deposit(amount)
                    print(f"\n[SUCCESS] Credited funds. New Balance: ₹{account.balance:,.2f}")
                except ValueError:
                    print("\n[SYSTEM ERROR] Invalid data volume precision.")
            else:
                print("\n[ERROR] Account data reference profile missing.")

        elif choice == "3":
            print("\n--- Withdrawal Transaction Module ---")
            acc_num = input("Enter 11-Digit Account Number: ").strip()
            account = engine.get_account(acc_num)
            
            if account:
                if account.is_locked:
                    print("\n[SECURITY ALERT] This account is currently locked due to invalid PIN entries.")
                    continue
                try:
                    amount = float(input("Enter Amount to Withdraw (INR): "))
                    pin = input("Enter Secret PIN: ").strip()
                    
                    if account.verify_and_authenticate(pin):
                        if account.withdraw(amount):
                            print(f"[SUCCESS] Dispensed Funds. New Balance: ₹{account.balance:,.2f}")
                except ValueError:
                    print("\n[SYSTEM ERROR] Mathematical parsing parameter faults.")
            else:
                print("\n[ERROR] Account data reference profile missing.")

        elif choice == "4":
            print("\n--- Atomic Inter-Account Fund Routing Module ---")
            src_num = input("Enter Source Account Number: ").strip()
            dest_num = input("Enter Destination Account Number: ").strip()
            try:
                amount = float(input("Enter Transfer Amount (INR): "))
                pin = input("Enter Secret PIN for Source Account: ").strip()
                engine.execute_atomic_transfer(src_num, dest_num, amount, pin)
            except ValueError:
                print("\n[SYSTEM ERROR] Verification input stream parsing error.")

        elif choice == "5":
            print("\n--- Chronological Account Statement Engine ---")
            acc_num = input("Enter Account Number to Query: ").strip()
            account = engine.get_account(acc_num)
            
            if account:
                print("\n" + "=" * 84)
                print(f" STATEMENTS RECORD OVERVIEW FOR ACCOUNT: {account.account_number} ({account.account_type_label})")
                print("=" * 84)
                print(f"{'TXN ID':<12} {'TIMESTAMP':<21} {'TYPE':<12} {'SOURCE':<13} {'DEST':<13} {'AMOUNT':<11} {'STATUS'}")
                print("-" * 84)
                
                # Fetch rolling snapshot records
                for txn in account.history:
                    print(f"{txn.txn_id:<12} {txn.timestamp:<21} {txn.txn_type:<12} "
                          f"{txn.source_acc:<13} {txn.dest_acc:<13} ₹{txn.amount:<10,.2f} {txn.status}")
                
                print("=" * 84)
                print(f"ACTIVE COLLECTIBLE AVAILABLE BALANCE: ₹{account.balance:,.2f}")
                print("=" * 84)
            else:
                print("\n[ERROR] Matching statement registry reference is missing.")

        elif choice == "6":
            print("\nTerminating Systems Safely. In-memory matrix flushed. Goodbye.")
            break
        else:
            print("\n[ERROR] Invalid Entry. Select numbers between 1 and 6.")


if __name__ == "__main__":
    main()