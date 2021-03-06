import csv

class LenderCSVLoader:
  ''' 
  Used for loading the Lenders' data from the CSV file specified by the user'
  '''
  
  filename = ""
  lender_list = []
  
  def __init__(self, filename):
    self.filename = filename
    self.lender_list = []
    
    # Read CSV
    self.lender_list = []
    with open(self.filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        data_list = iter(readCSV)
        next(data_list)#Using the first row from the CSV File
        for row in data_list:
            if len(row) != 3:
                raise IOError("Incorrect Data")
            self.lender_list.append((row[0],float(row[1]),int(row[2]))) #Inside Tuple: (name,rate,amount)
            
  def get_lender_list(self):
    return self.lender_list

   
