import math,csv,sys

from loan_calculator import LoanCalculator
from lender_csv_reader import LenderCSVLoader


def calculate_figures(loan_amt,filename):
    '''     
    Used for calculating the loan repayment amounts and displaying the results expected

    Parameters
    ----------
    loan_amt : float
        Stores the loan amount required by the borrower.
    filename : String
        Stores the name of the file containing the lender's information.

    Returns
    -------
    list
        Returns a list with Boolean and loan repayment amount.

    '''
	# Load Lender CSV
    lender_loader = 0
    loan_calculator = 0
    try:
        lender_loader = LenderCSVLoader(filename)
    except IOError as err: 
        print(err)
        return [False, 0]
	
    loan_calculator = LoanCalculator(lender_loader.get_lender_list())
    loan_calculator.calculate_repayment(loan_amt)
	
    #Printing Results 
	
    print ("-- Results --")
    print ("Requested amount: £%.2f" % (loan_calculator.get_loan_amt()))
    print ("Rate: %.2f%%" % (loan_calculator.get_interest()*100))
    print ("Monthly repayment: £%.2f" % loan_calculator.get_repayment())
    print ("Total repayment: £%.2f" % loan_calculator.get_total_repayment())
    return [True,loan_calculator]
	

if __name__ == "__main__":
	# Grab command-line arguments
    loan_amt =1000 #Default Amount if not entered by the user
    filename = "resources/market_data.csv"#Default file name in case the file name is not entered
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    if len(sys.argv) >= 3:
        loan_amt = float(sys.argv[2])

    calculate_figures(loan_amt,filename)







