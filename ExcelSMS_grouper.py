import csv
#user enters folder path, the CSV file in the path, and the name of the output file they want the data to be saved 2
folderPath = input("Enter Folder Path of Csv(with out the file name of the csv): ")
CsvFile = input("Enter The CSV File Name ")
outputName = input("Enter the Output Filename with the extension ie .txt (If the file doesnt exist it will create one in the folderPath): ")
#assigns folder paths for ouput and csv file 
di = folderPath+CsvFile
ou = folderPath + outputName

#does all the magic
with open(di, newline='') as csvfile:
        sms = csv.reader(csvfile,delimiter=",")
        print("SMS TYPE: " + str(type(sms)))

        DailyAmt = int()
        i = int(0)
        
        while i <= 23:
            for sms_ in sms:
                print(sms_)
                if "," in sms_[2]:
                  x = sms_[2].split(",",1)
                  m = str(x[0]) + str(x[1])
                  DailyAmt = DailyAmt + int(m)
                    
                  i = i + 1
                else:
                  DailyAmt = DailyAmt + int(sms_[2])
                  i = i + 1
                if i > 23:
                    with open(ou, 'a') as f:
                        f.write(sms_[0] + ", "  + str(DailyAmt) + "\n")
                    f.close()
                    DailyAmt = 0
                    i = 0   
