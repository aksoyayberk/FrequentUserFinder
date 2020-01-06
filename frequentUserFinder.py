import csv
import numpy as np

def findFrequentUsers():
    userCSV = input("Enter the name of the USERS CSV file without the extension: ")
    userCSV += '.csv'
    
    recordCSV = input("Enter the name of the RECORDS CSV file without the extension: ")
    recordCSV += '.csv'
    
    threshold = input("Enter the minimum number of rides: ")
    threshold = int(threshold)
    
    line_count = 0
    
    with open(userCSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row[0]} {row[3]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
        
    with open(recordCSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        current_row = 0
        arr_size = 0

        for row in csv_reader:
            current_row += 1
            if line_count == current_row:
                arr_size = int(row[0]) + 1

    arr = [0] * (arr_size)

    with open('2019-12-23.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                current_user_id = int(row[2])
                if current_user_id < len(arr):
                    arr[current_user_id] += 1
                    line_count += 1

    frequentUserList = []
    oneTimeUserList = []
    for i in range(0, len(arr) - 1):
        if (arr[i] >= threshold):
            frequentUserList.append([i, arr[i]])
        elif (arr[i] == 1):
            oneTimeUserList.append([i, arr[i]])

    resultFrequent = f'\nFrequent users with minimum {threshold} sessions found: {len(frequentUserList)}'
    print(resultFrequent)
    header = ["user_id:", "number_of_sessions:"]
    print("\t{0: <20} {1: <20}".format(*header))
    for i in frequentUserList:
        print("\t{0: <20} {1: <20}".format(*i))

    resultOneTime = f'\nOne time users found: {len(oneTimeUserList)}'
    print(resultOneTime)
    print("\t{0: <20} {1: <20}".format(*header))
    for i in oneTimeUserList:
        print("\t{0: <20} {1: <20}".format(*i))

findFrequentUsers()
