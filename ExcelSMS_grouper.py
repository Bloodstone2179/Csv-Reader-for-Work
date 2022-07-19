import csv
line = int()
FileName = input("Enter The Name Of The File To Read From: ")
file = input("Enter The File Path: ")
with open(file + 'SmsCount.csv', newline='') as csvfile:
    sms = csv.reader(csvfile,delimiter=",")
    print(type(sms))

    DailyAmt = int()
    i = int(0)
    while i <= 23:
        for sms_ in sms:
            print(sms_)
            DailyAmt = DailyAmt + int(sms_[2])
            i = i + 1
            if i == 23:
                with open(file + 'Output.txt', 'a') as f:
                    f.write("DATE: " + sms_[0] + ", Dai Amount: " + str(DailyAmt) + "\n")
                    i = 0
                    DailyAmt = 0
       
            