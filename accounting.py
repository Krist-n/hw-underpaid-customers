melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}")


melon_cost = 1.00
#Create a function that takes in Customer orders from txt file.
def customer_orders_paid_vs_expected(txt_file):
    """cleans up txt file and provides customer paid vs expected"""
    
   

    over_paid_customers = []
    under_paid_customers = []
    
    #clean up info, customer orders = open(customer-orders.txt) use rstrip, and split(|)
    customer_orders = open('customer-orders.txt')
    for line in customer_orders:
        line = line.rstrip()
        words = line.split('|')
    
    #customer number, name, melon amount and how much paid
    order_num = int(words[0])
    customer_name = words[1]
    melon_amt = int(words[2])
    customer_paid = float(words[3])

    #Amount expexted to get paid for melons and what was actually paid
    customer_expected = melon_amt * melon_cost

    #if customer under paid we had them to a list for future payment
    if  customer_expected < customer_paid:
        
        #adding customers name and num to under-paid list
        over_paid_customers.append(customer_name)
        over_paid_customers.append(order_num)
        
        #calculating refund amount
        refund_amount = customer_paid - customer_expected 
        
        print(f"Order num:{order_num}, customer name: {customer_name}, paid ${customer_paid:.2f},",
          f"expected ${customer_expected:.2f}, ${refund_amount:.2f} to be refunded.")
        

    #if customer over paid we add customer to list for repayment
    if customer_expected > customer_paid:
        
        #adding customers name and num to over-paid list
        under_paid_customers.append(customer_name)
        under_paid_customers.append(order_num)
        
        #calculating amount owed
        owed_amount = customer_expected - customer_paid
        
        print(f"Order num: {order_num}, customer name: {customer_name}, paid ${customer_paid:.2f},",
          f"expected ${customer_expected:.2f}, ${owed_amount:.2f} to be billed.")
    
    #closing text file    
    customer_orders.close()
          
customer_orders_paid_vs_expected("customer-orders.txt")