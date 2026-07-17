# Project 1: Sales Chatbot Simulation
# Author 

# Greeting
print("--------")
print("Hello, Welcome to your Destiny and Beyond")
print("My name is Destiny, your friendly virtual assistant.")
print("--------")
# Product Prompt
# Ask the user if they want to learn about the product
learn_more = input("Would you like to learn about our product? (yes/no): ")
# Convert to lowercase to handle variations in user typing
learn_more.lower()
if learn_more == "y":
    print("AWESOME CHOICE! Meet your destiny. and go beyond your imagination")
    print("Use on any device at anytime!")
    print("Go beyond your imaginations and go off the grid!")
    print("Budget Friendly, create a payment plan!")
else:
    print("No problem, Your Destiny will wait! ")
    exit()
buy_choice = input("Are your ready to out your destiny in our hands? (y/n): ")

if buy_choice == "y":
    print("FANTASTIC! Let's get your order processed right away. ")
else:
    print("Thank you for chatting with me!")
    exit()

#Gather customer details
print("n\------")
print("Please enter your order details below:")
print("--------")
first_name = input("First Name: ")
last_name = input("Last Name: ")
email = input("Email Address: ")
phone = input("Phone Number: ")
# Polite exit message
print("Thank you for your order. Have a great Destination!")
  
