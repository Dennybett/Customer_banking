# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE

from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function

def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = float(input('Input your savings account balance: '))
    savings_interest = float(input('Input the interest rate of the savings account: '))
    savings_maturity = int(input('Input the months for the account: '))
    
    
    # Call the create_savings_account function and pass the variables from the user.
    
    updated_savings_balance, interest_savings_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)


    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"The updated savings account balance is: {updated_savings_balance:,.2f} and interest earned is {interest_savings_earned:,.2f}")


    # # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # # ADD YOUR CODE HERE
    cd_balance = float(input('Input your CD account balance: '))
    cd_interest = float(input('Input your CD interest rate: '))
    cd_maturity = int(input('Input the months for the account: '))

    # # Call the create_cd_account function and pass the variables from the user.


    # def create_cd_account():

    updated_cd_balance, interest_cd_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    print(f"The updated CD account balance is: {updated_cd_balance:,.2f} and interest earned is {interest_cd_earned:,.2f}")

if __name__ == "__main__":
    # Call the main function.
    main()
