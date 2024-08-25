import pandas as pd

assortment_df = pd.read_csv('database/assortment.csv', sep=';', header=0)
branch_df = pd.read_csv('database/branch.csv', sep=';', header=0)
customers_df = pd.read_csv('database/customers.csv', sep=';', header=0)
departments_df = pd.read_csv('database/departments.csv', sep=';', header=0)
main_df = pd.read_csv('database/main.csv', sep=';', header=0)
packaging_df = pd.read_csv('database/packaging.csv', sep=';', header=0)
products_df = pd.read_csv('database/products.csv', sep=';', header=0)
provider_contacts_df = pd.read_csv('database/provider_contacts.csv', sep=',', header=0)
providers_df = pd.read_csv('database/providers.csv', sep=';', header=0)
staff_df = pd.read_csv('database/staff.csv', sep=';', header=0)

print(customers_df)
# print(len(max(customers_df.city, key=len)))
