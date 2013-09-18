def main():
    empId = int(input("Enter an employee id (00000):"))
    if (empId == 82500):
        empName = "Helene Mukoko"
    elif (empId == 92746):
        empName = "Raymond Kuomo"
    elif (empId == 54080):
        empName = "Henry Larson"
    else:
        empName = "Unknown"

    print("Id # ", empId," The employees name is, ", empName)

    weeklyTime = float(input("Enter the weekly time:"))
    hourlySalary = float(input("Enter the hourly salary:"))

    if (weeklyTime > 40):
        regularTime = 40
        overTime = weeklyTime - regularTime
        regularPay = regularTime * hourlySalary
        overtimePay = overTime * hourlySalary * 1.5
        netpay = overtimePay + regularPay
    else:
        regularTime = weeklyTime
        overTime = 0
        regularPay = regularTime + hourlySalary
        overtimePay = 0
        netpay = overtimePay + regularPay

    print("--------------------------Employee Payroll-------------------------------")
    print("Employee number:", empId)
    print("Employee name:", empName)
    print("Hourly salary:", hourlySalary)
    print("Weekly Time:", weeklyTime)
    print("Regular Pay:", regularPay)
    print("Overtime Pay:", overtimePay)
    print("Net Pay:", netpay)

main()
