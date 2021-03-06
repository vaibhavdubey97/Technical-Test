import unittest
from loan_calculator import LoanCalculator
import main
from lender_csv_reader import LenderCSVLoader

class TestLoanCalculator(unittest.TestCase):

    lender_list = []
    def setUp(self):
        ''' 
        Setting up a test lender's list.
        
        Returns
        -------
        None.
        '''
        
        self.lender_list = []
        self.lender_list.append(("Bob", 0.075, 640))
        self.lender_list.append(("Jane", 0.069, 480))
        self.lender_list.append(("Mary", 0.104, 170))

    def test_Loan_in_range(self):
        '''
        Testing Loan Amount within the [1000,15000] range.
        
        Returns
        -------
        None.
        '''
        loan_amt= 1000
        loan_calculator = LoanCalculator(self.lender_list)
        result = loan_calculator.calculate_repayment(loan_amt)
        assert result == True

    def test_Loan_below_range(self):
        '''
        Testing Loam Amount lower than the the [1000,15000] range.
        
        Returns
        -------
        None.
        '''
        try:
            loan_amt = 50
            loan_calculator = LoanCalculator(self.lender_list)
            loan_calculator.calculate_repayment(loan_amt)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
    
    def test_Loan_above_range_limit(self):
        '''
        Testing Loam Amount higher than the the [1000,15000] range.
        
        Returns
        -------
        None.

        '''
        try:
            loan_amt = 30000
            loan_calculator = LoanCalculator(self.lender_list)
            loan_calculator.calculate_repayment(loan_amt)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
    

    def test_Insufficient_Funds(self):
        '''
        Testing Loan Amount that is within the [1000,150000] range but the lender's amounts 
        in the mar_data.csv file are insufficient to cover the loan amount.

        Returns
        -------
        None.

        '''
        try:
            loan_amt = 5000
            loan_calculator = LoanCalculator(self.lender_list)
            loan_calculator.calculate_repayment(loan_amt)
            self.assertTrue(False)
        except ValueError:
            self.assertTrue(True)
    
    def test_Calculate_Repayments(self):
        '''
        Testing the calculation of the repayment amount using the market_data.csv file 
        given in the problem statement.

        Returns
        -------
        None.

        '''
        pair = main.calculate_figures( 1000, "resources/market_data.csv")
        loan_calculator = pair[1]
        assert loan_calculator.get_repayment() > 0.0
        assert loan_calculator.get_interest()*100 > 0


    def test_No_CSV_File(self):
        '''
        Testing the calculation of the repayment amount when a wrong file is given
        by the user of the application.

        Returns
        -------
        None.

        '''
        pair = main.calculate_figures( 1000, "No_file.csv")
        assert pair[0] == False

    def test_CSV_File_with_incorrect_data(self):
        '''
        Testing the calculation of the repayment amount when the CSV file containing the 
        lender's details has incorrect data formats.'

        Returns
        -------
        None.

        '''
        pair = main.calculate_figures( 1000, "resources/wrong_market_data.csv")
        assert pair[0] == False


if __name__ == '__main__':
    unittest.main()