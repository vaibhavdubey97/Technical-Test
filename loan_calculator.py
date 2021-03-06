import math

class LoanCalculator:
    '''
    Class used to calculate the loan repayment amounts for the user's requirement.
    '''
    
    # total number of payments        
    n_payment = 36
    lender_list = []
    selected_lender_list = []
    
    # Input
    loan_amt = 0.0
    
    # Ouput
    payment_combined = 0.0
    average_interest = 0.0

    def __init__(self, lender_list):
        self.lender_list = lender_list    
        # Sort lender_list by interest to facilitate selection of lenders
        self.lender_list.sort(key=lambda x: x[1])
        
    def calculate_monthly_repayment_per_lender(self, loan_amt, interest):
        '''
        Used to calculate the monthly repayment amount for each lender.

        Parameters
        ----------
        loan_amt : float
            Stores the loan amount required by the borrower.
        interest : float
            Contains the interest rate for each lender.

        Returns
        -------
        payment : float
            Conatins the monthly repayment amount for each lender.

        '''
        
        interest_rate = interest/12
        # Monthly Payment calculations
        payment = loan_amt * (interest_rate/(1-math.pow((1+interest_rate), (-self.n_payment))))
        return payment


    def generate_selected_lenders(self, loan_amt):
        '''
        
        Used to generate a list of lenders who can be used for the user's requirement

        Parameters
        ----------
        loan_amt : float
            Stores the loan amount required by the borrower.

        Raises
        ------
        ValueError
            Error message to be displayed when funds in the CSV are insufficient for the borrower's loan.

        Returns
        -------
        List of Tuples
            List containing details of the selected lender's from the CSV file.

        '''
        self.selected_lender_list = []
        for lender in self.lender_list:
            if loan_amt <= lender[2]:
                lender = (lender[0], lender[1], loan_amt)
                self.selected_lender_list.append (lender)
                loan_amt = 0
                break;
            # Substract for next iteration
            loan_amt = loan_amt - lender[2]
            self.selected_lender_list.append(lender)

        # Check whether sufficient funds
        if loan_amt > 0:
            self.selected_lender_list = []
            raise ValueError("Insufficient funds")
        return self.selected_lender_list
        

    def calculate_repayment(self, loan_amt):
        '''
        Used to calculate the final repayment amount for all the lenders.

        Parameters
        ----------
        loan_amt : float
            Stores the loan amount required by the borrower.

        Raises
        ------
        ValueError
            Error message to be displayed when the borrower's loan is outside the [1000,15000] range.

        Returns
        -------
        bool
            Returns True if repayments are calculated without errors.

        '''
        
        if not(loan_amt >= 1000 and loan_amt <= 15000): 
            raise ValueError("loan_amt exceeds range [1000,15000]")
        
        self.loan_amt = loan_amt
        self.selected_lender_list = self.generate_selected_lenders(loan_amt)
        
        # Calculate Repayments for lenders
        self.payment_combined = 0.0
        self.average_interest = 0.0
        for lender in self.selected_lender_list:
            payment = self.calculate_monthly_repayment_per_lender(lender[2],lender[1])
            self.payment_combined += payment
            self.average_interest += lender[1]
        self.average_interest = self.average_interest / len(self.selected_lender_list)
        return True

    def get_average_interest(self):
        return self.average_interest

    def get_repayment(self):
        return self.payment_combined

    def get_total_repayment(self):
        return self.payment_combined * self.n_payment

    def get_interest(self):
        return self.average_interest

    def get_loan_amt(self):
        return self.loan_amt
