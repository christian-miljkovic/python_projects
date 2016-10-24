# Christian Miljkovic
# CSCI-UA.0002 section 03
# Assignment #8

# Part A,B,C


# create the product list with costs

product_names= ["hamburgers","hot dogs","fries"]
product_costs= [4.00, 2.00,1.00]
product_quantity= [10,20,30]


# ask user for input with data validation

while True:

    answer=input("(s)earch,(l)ist,(a)dd,(r)emove,(u)pdate, r(e)port or (q)uit: ")

# if the user asks to search for products

    if answer=="s":

# create a while loop in order to validate the items searched

        while True:
            
            product=input("Enter a product name: ")

# if-elif statements that give response for searched item

            if product==product_names[0]:
                print("We sell",product_names[0], "at", product_costs[0],"per unit")
                print("We currently have",product_quantity[0],"in stock")
                break

            elif product==product_names[1]:
                print("We sell",product_names[1], "at", product_costs[1],"per unit")
                print("We currently have",product_quantity[1],"in stock")
                break

            elif product==product_names[2]:
                print("We sell",product_names[2], "at", product_costs[2],"per unit")
                print("We currently have",product_quantity[2],"in stock")
                break

            else:
                print("Sorry, we don't sell",product)
                break

        print()
        
# if the user asks for the list

    elif answer=="l":
        print("Product","\t","Price","Quantity")
        for i in range(len(product_quantity)):
            format_names=format(product_names[i],"<16s")
            format_costs=str(product_costs[i])
            format_costs1=format(format_costs,"<5s")

            print(format_names,format_costs1,product_quantity[i])
           
        print()

# if the user asks to add an item to the list

    elif answer=="a":

# adding product name

        while True:
            add_name=input("Enter a new product name: ")

            if add_name in product_names:
                print("Sorry, we already sell that product. Try again.")
                
            else:
                break

# adding product cost

        while True:
            add_cost=float(input("Enter a new product cost: "))

            if add_cost<=0:
                print("Invalid cost. Try again.")
            else:
                break

# adding product quantity

        while True:
            add_quantity=int(input("Enter a new product quantity: "))

            if add_quantity<=0:
                print("Invalid quantity. Try again.")
            else:
                break

        print("Product succesfully added!")
        print()
            
        product_names.append(add_name)
        product_costs.append(add_cost)
        product_quantity.append(add_quantity)
        

# add the remove feature to the program

    elif answer=="r":

        while True:

            remove_product=input("What product would you like to remove from the list: ")

            if remove_product in product_names:
                break

            else:
                print("That product is not in the list")
                
# create a tracker so you can delete the correct item in its position
        tracker=0

# run through the list in order to find out what is the position of the item to delete
        
        for i in range(len(product_names)):
            if remove_product==product_names[i]:
                tracker+=i

        del product_names[tracker]
        del product_costs[tracker]
        del product_quantity[tracker]
                
       
        print("Product removed!")
        print()
                
# add the update feature to the program

    elif answer=="u":

# data validation

        while True:
            update_product=input("What product would you like to update: ")

            if update_product in product_names:
                location=product_names.index(update_product)
                break

            else:
                print("Product doesn't exist. Can't update.")
                
        while True:
            print("What would you like to update?")
            update_choice=input("(n)ame,(c)ost, or (q)uantity: ")

            if update_choice=="n" or update_choice=="c" or update_choice=="q":
                break
            else:
                print("Invalid input")

# use if-elif statement to modify list for the name 

        if update_choice=="n":
            
            while True:
                new_name=input("Enter a new name: ")
                if new_name in product_names:
                    print("That is a duplicate")

                else:
                    break

# find place and replace it with the requested input

            product_names[location]=new_name
            print("Product name has been updated")
            print()


# use if-elif statement to modify list for the cost 

        if update_choice=="c":
            
            while True:
                new_cost=float(input("Enter a new cost: "))
                if new_cost in product_costs:
                    print("That is a duplicate")

                elif new_cost<=0:
                    print("That is an invalid input")

                else:
                    break

# find place and replace it with the requested input

            product_costs[location]=new_cost
            print("Product cost has been updated")
            print()
            

# use if-elif statement to modify list for the quantity 

        if update_choice=="q":
            
            while True:
                new_quant=int(input("Enter a new quantity: "))
                if new_quant in product_quantity:
                    print("That is a duplicate")

                elif new_quant<=0:
                    print("That is an invalid input")

                else:
                    break

# find place and replace it with the requested input

            product_quantity[location]=new_quant
            print("Product cost has been updated")
            print()            





# add the report feature

    elif answer=="e":

# find min and max of the list

        biggest=max(product_costs)
        smallest=min(product_costs)

# find location of the item <

        
        location2=product_costs.index(biggest)
        location3=product_costs.index(smallest)

# find total value of products
        total_value=0
        for i in range(len(product_costs)):
            total_value+=product_costs[i]*product_quantity[i]

# format answers

        form_expensive=format("Most expensive product:","<29s")
        form_least=format("Least expensive product:","<29s")
        form_val=format("Total value of all products:","<29s")
        format_biggest=format(biggest,".2f")
        name_biggest="("+product_names[location2]+")"
        format_smallest=format(smallest,".2f")
        name_smallest="("+product_names[location3]+")"
        format_value=format(total_value,".2f")

        print(form_expensive,format_biggest,name_biggest)
        print(form_least,format_smallest,name_smallest)
        print(form_val,format_value)


#  if the user asks to quit the program

    elif answer=="q":
        break
        print()

# if the user inputs an invalid input

    else:
        print("Invalid input")
        print()

print("See you soon!")







    





            
