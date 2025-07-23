print ("*****Welcome to FLAT-RATE-EMI Calculator*****")

Loan_AMT = float(input("Enter your Loan Amount : "))
Months = float(input("How many months you have taken the Loan : "))
Int_Rate = float(input("Enter your interest rate per month in % : "))
Process_Fee = float(input("Enter your processing fee in % : "))

years = Months / 12
interest = Int_Rate / 100
fee = (Process_Fee * Loan_AMT) / 100

EMI = (Loan_AMT + (Loan_AMT * years * interest)) / (years * 12)
Final_EMI = EMI + fee
print ("Your final EMI wil be : " + str(Final_EMI))
