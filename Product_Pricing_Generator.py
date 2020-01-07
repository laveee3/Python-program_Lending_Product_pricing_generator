# Solution that allows the business to dynamically generating product pricing from a set rules defined by the finance team.
# Lavanya Elango Jan 6, 2020
import csv
import re

class Person:
    numOfPersons = 0
    def __init__(self, credit_score, state):
        self.credit_score = credit_score
        self.state = state

class Product:
    numOfProducts = 0
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate
        self.disqualified = False

class RulesEngine(Person, Product):
    def __init__(self, Person, Product, rules):
        self.credit_score = Person.credit_score
        self.state = Person.state
        self.name = Product.name
        self.interest_rate = Product.interest_rate
        self.disqualified = product.disqualified
        self.rules = rules

        # In the below for loop based on the input parameters and rules, the interest rate gets changed  and so also the variable 'disqualified'
        #the rule[1] contains the credit_score;  line  32 contains the regular expression.
        # its purpose is to split the integer and the logical operator since the field credit-score is passed as a string (ex:>720)
        #credit_score value in loadRules.csv should definetly have >,<,>=,<= symbols. And
        #searchregex.group(1) contains the logical operator and searchregex.group(2) contains the integer
        #based on the given rule for credit_score and interest_rate gets changed
        for rule in rules:
             k = 1
             if (rule[1] is not '' ):
                rgexsearch = re.compile(r'\s*([><=]*)\s*([0-9]*)\s*')
                searchregex = rgexsearch.search(rule[1])
                if searchregex.group(1) == '>':
                    if self.credit_score > int(searchregex.group(2)):
                        self.interest_rate += float(rule[3])
                if searchregex.group(1) == '>=':
                    if self.credit_score >= int(searchregex.group(2)):
                        self.interest_rate += float(rule[3])
                if searchregex.group(1) == '<':
                    if self.credit_score < int(searchregex.group(2)):
                        self.interest_rate += float(rule[3])
                if searchregex.group(1) == '<=':
                    if self.credit_score <= int(searchregex.group(2)):
                        self.interest_rate += float(rule[3])

             # rule[0] contains name of the state and rule[0] contains the product name,
             # based on the input parameters and rules, the interest rate gets changed  and so also the variable 'disqualified'
             if (rule[0] is not '' and (rule[0] == self.state)) or (rule[2] is not '' and (rule[2] == self.name)):
                 if rule[4] is not '' and rule[3] is not '':
                     if self.disqualified == False: self.disqualified = rule[4]
                     self.interest_rate += float(rule[3])
                 if rule[4] is '' and rule[3] is not '':
                     self.interest_rate += float(rule[3])
                 if rule[4] is not '' and rule[3] is '':
                     if self.disqualified == False: self.disqualified = rule[4]

    # Function to output the interest_rate and disqualification status based on the rules and the input parameters
    def printoutput(self):
        print('__', str(self.name), str(self.state), self.credit_score, '__')
        print("product.interest_rate == " + str(self.interest_rate))
        print("product.disqualified == " + str(self.disqualified))
        return ('')
# =============================================================================

rules = []
# Set of Rules for product pricing. Its given as a csv file = loadRules.csv so that it can be changed easily.
# the rules are loaded in the argument 'rules' and passed as a third argument to the class RulesEngine
with open("loadRules.csv", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.rstrip().split(",")
        #print(word)
        rules.append(word)

# person_product.txt contains the input parameters in the order of 'credit_score, state, product, interest_rate, disqualified'
with open("person_product.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        person = Person(int(word[0]), word[1])
        product = Product(word[2], float(word[3]))
        rules_engine = RulesEngine(person, product, rules)
        print(rules_engine.printoutput())
