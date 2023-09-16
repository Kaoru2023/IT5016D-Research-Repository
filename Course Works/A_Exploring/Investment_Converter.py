# Investment_Converter.py
#
# author: Kaoru
# date: 16.09.23

class Money:
    def __init__(self, principal, interest_rate, period, tax_rate):
        self.principal = principal
        self.interest_rate = interest_rate
        self.period = period
        self.tax_rate = tax_rate

    def get_total(self):
        interest = self.principal * self.interest_rate/100  # easy for inputting
        tax = interest * self.tax_rate/100 
        total = self.principal + (interest - tax)/12 * self.period
                
        return total


def main():
    jp_principal = float(input("Enter JPY principal: "))
    jp_interest_rate = float(input("Enter annual JP interest rate: "))
    jp_tax_rate = float(input("Enter JP tax rate: "))
    nz_interest_rate = float(input("Enter annual NZ interest rate: "))
    nz_tax_rate = float(input("Enter NZ tax rate: "))
    wise_rate = float(input("Enter FX rate JPY/1NZD: "))
    nz_principal = jp_principal/wise_rate
    period = float(input("Enter period in month: "))
    nz_invest = Money(nz_principal, nz_interest_rate, period, nz_tax_rate)  # creating instance for NZD
    jp_invest = Money(jp_principal, jp_interest_rate, period, jp_tax_rate)  # creating instance for JPY
    print(f"JPY total: {jp_invest.get_total()}",
          f"NZD principal: {nz_principal}", 
          f"NZD total: {nz_invest.get_total()}", 
          sep="\n",
          )

    
main()







