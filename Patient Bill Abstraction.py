
# # # Lab 53
# # # Task 1: Define the Abstract Base Class 

# # from abc import ABC, abstractmethod

# # class BillingRecord(ABC):
# #     @abstractmethod
# #     def get_bill(self):
# #         pass
# #     @abstractmethod
# #     def update_bill(self, amount):
# #         pass

# # # Task 2: Define the Concrete Class 

# # class PatientBill(BillingRecord):
# #     def __init__(self, patient_id, patient_name, billing_amount=0):
# #         self.patient_id = patient_id
# #         self.patient_name = patient_name
# #         self.billing_amount = billing_amount

# #     def get_bill(self):
# #         return {
# #             'Patient ID' : self.patient_id,
# #             'Patient Name' : self.patient_name,
# #             'Billing Amount' : f"₹{self.billing_amount:.2f}"
# #         }

# #     def update_bill(self, amount):
# #         if amount > 0:
# #             self.billing_amount += amount
# #             print(f"Billing amount updated by ₹{amount:.2f}. New amount is ₹{self.billing_amount:.2f}.")
# #         else:
# #             print("Amount to update must be positive.")

# # # Task 3: Use the Concrete Class 

# # if __name__ == "__main__":

# #     patient_bill = PatientBill(
# #         patient_id="P001",
# #         patient_name="Smriti Gupta",
# #         billing_amount=150.00
# #     )
# #     print("Initial Bill Details:")
# #     print(patient_bill.get_bill())

# #     patient_bill.update_bill(50.00)

# #     print("\nUpdated Bill Details:")
# #     print(patient_bill.get_bill())
























































