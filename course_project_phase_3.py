import datetime

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname


def GetDatesWorked():
    fromdate  = input("Enter the start date (mm/dd/yyyy):  ")
    todate = input("Enter the end date (mm/dd/yyyy): ")
    return fromdate, todate

               
def GetHoursWorked():
     hours = float(input("Enter amount of hours worked:  "))
     return hours   
     
def GetHourlyRate():
     hourlyrate =  float(input("Enter hourly rate: $"))
     return hourlyrate
 
def GetTaxRate():
     taxrate = float(input("Enter tax rate (e.g., 0.15 for 15%):  "))
     return taxrate


def CalTaxAndNetPay(hours, hourlyrate,taxrate):
    grosspay = hours * hourlyrate
    incometax =  grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay


    
def calculate_pay(hours, rate,tax_rate):
    """Calculate gross pay, tax amoubt, and net pay"""
    gross_pay = hours * rate
    """Calculate gross pay, tax amount, and net pay."""
    gross_pay = hours * rate
    tax = gross_pay * tax_rate
    net_pay = gross_pay - tax
    return gross_pay, tax, net_pay

def printTotals(EmpTotals):
    print("\nSummary Report")
    print(f"Total  Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']:.2f}")
    print(f"Total Gross Pay: ${EmpTotals['TotGrossPay']:.2f}")
    print(f"Total Income Taxe: ${EmpTotals['TotTax']:.2f}")
    print(f"Total Net Pay: ${EmpTotals['TotNetPay']:.2f}")
    
if __name__ == "__main__":

     EmpFile = open("Employees.txt", "a")

    #initialize accumulators
     EmpTotals = {"TotEmp": 0,  "TotHrs": 0.0,  "TotGrossPay": 0.0, "TotTax": 0.0, "TotNetPay": 0.0 }
     DetailsPrinted = False
    
     while True:
        empname = GetEmpName()
        if empname.upper() == "END":
            break
        
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        EmpDetail = f"{fromdate}|{todate}|{empname}|{hours}|{hourlyrate}|{taxrate}\n"
        
        EmpFile.write(EmpDetail)
        
     EmpFile.close()
     
     EmpFile = open("Employees.txt", "r")
     
     while True:
          rundate = input("Enter start date for report (MM/DD/YYYY) or 'ALL' for all date in file: ")
          if rundate.upper() == "ALL":
              break
          
          try:
              rundate = datetime.datetime.strptime(rundate, "%m/%d?%Y")
              break
          except ValueError:
              print("Invalid date format. Please try again.\n")
              continue
          
     while True:
          EmpDetail = EmpFile.readline()
         
          if not EmpDetail:
             break
         
          EmpDetail = EmpDetail.strip()
          EmpList = EmpDetail.split("|")
         
          fromdate = EmpList[0]
          if rundate.upper()  !=  "ALL":
             checkdate = datetime.datetime.strptime(fromdate,  "%m/%d/%Y")
             if checkdate < rundate:
                  continue
              
          todate = EmpList[1]
          empname = EmpList[2]
          hours =  float(EmpList[3])
          hourlyrate = float(EmpList[4])
          taxrate = float(EmpList[5])
         
         
          grosspay, incometax, netpay = CalTaxAndNetPay(hours, hourlyrate, taxrate)
        

          print(f"{fromdate}  {todate} {empname}  Hours: {hours:.2f}  Hourly Rate: ${hourlyrate:.2f}  "
                f"Gross Pay: {grosspay:.2f}  Tax Rate: {taxrate:.2%} Income Tax: ${incometax:.2f} Net Pay: ${netpay:.2f}")
    
 
          EmpTotals["TotEmp"]  += 1
          EmpTotals["TotHrs"]  += hours
          EmpTotals["TotGrossPay"]  += grosspay
          EmpTotals["TotTax"]  += incometax
          EmpTotals["TotNetPay"]  += netpay
        
          DetailsPrinted = True
        
     EmpFile.close()

     if DetailsPrinted:
        printTotals(EmpTotals)
     else:
         print("No detail information to print.")
        
       
   

        
      

        
                 

        