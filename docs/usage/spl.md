The Pillbox Engine processes all DailyMed SPL XML files and populates several tables.

These tables are

- SPL Products
- SPL OSDF Pills
- OSDF Ingredients

## SPL Products

The SPL products table includes the header information of all xml files.

The header includes information such as a unique setid, the author, the effective date, etc.

For the full list of fields included in this table refer to `spl.models.Product` class.

To populate or update the products table, click on `Sync Data` under SPL products action box. To check the progress click on the box again.

![Sync SPL Products](img/spl_products.png)

You can view browse and search in the SPL products by going to the SPL Products list page.

![SPL Products list page](img/spl_products_list.png)

## OSDF Pills and Ingredients

Each SPL XML file includes multiple product information. The Pillbox Engine identifies those products that are categorized as OSDF (Oral Solid Dosage Form) and sync their information with OSDF Pills and OSDF Ingredients tables.

For a full list of fields that are populated from xml files look at `spl.models.Pill` class.

To populate or update the pills table, click on `Sync Data` under OSDF Pills action box. To check the progress click on the box again.

![Sync OSDF Pills](img/osdf_pills.png)

You can view browse and search in the OSDF Pills and Ingredients by going to the OSDF Pills and Ingredients list page.

![OSDF Pills Ingredients](img/pills_ingredients.png)

