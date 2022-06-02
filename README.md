# Lending_Product_pricing
Product pricing generator

This project has the following files:
person_product.txt
loadRules.csv
Product_pricing_generator.py

person_product.txt file 
- This has the Input parameters - Person.credit_score, Person.state, Product.name, Product.interest_rate. 
- New test cases can be added here.

loadRules.csv 
- file has rules based on which the product pricing is generated. 
- In this file each line has parameters in this order:State,Creditscore,Product,interestRate ,Disqualified. 
- Using the first three parameters, the original interest_rate value is updated and so also the field 'disqualified'. 
- Add new rules to this file.
- The field 'Creditscore' should have any of >,<,>=,<= symbols before the integer.Ex:'>=720'


Product_pricing_generator.py
- Has the logic to generate the product pricing. 
- Its designed to be dynamic taking inputs from person_product.txt and loadRules.csv.
- Run this file to see the product price
