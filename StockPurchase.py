

'''
Stock Purchase The following steps calculate the amount of a stock purchase: 
A. Assign the value 25.625 to the variable cost_per_share.
B. Assign the value 400 to the variable number_of_shares.
C. Assign the product of cost_per_share and number_of_shares to the variable markdown.
D. Display the value of the variable markdown in the console application
'''

def main():    
    # Input: -------------------------
    #A. Assign the value 25.625 to the variable cost_per_share.
    # costPerShare = 25.625 # I am hardcoding the value of cost per share.
    costPerShare = float(input("Enter the value of cost per share: "))

    #B. Assign the value 400 to the variable number_of_shares.
    # numberOfShares = 400
    numberOfShares = float(input("Enter the value of number of shares: "))
    # Processing: -------------------------
    #C. Assign the product of cost_per_share and number_of_shares to the variable markdown.
    markdown = costPerShare * numberOfShares
    #Output:---------------------------
    #D. Display the value of the variable markdown in the console application
    print("The value of the variable markdown is: $", markdown)
main()