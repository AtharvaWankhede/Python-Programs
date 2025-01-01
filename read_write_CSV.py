import csv

with open ('data/employee.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',',quotechar='"')
    print(csv_reader)
    line_cnt=0
    for row in csv_reader:
        if line_cnt==0:
            print(f'Column names are {', '.join(row)}')
            line_cnt+=1
        else :
            print(f'\t{row[0]} emp_ids name is {row[1]} and works in {row[2]} department')
            line_cnt+=1
    print(f'processed {line_cnt-1} lines ')

#
# with open('data/employee.csv') as dictionary_file:
#     dict_reader = csv.DictReader(dictionary_file,delimiter=',',quotechar='"')
#     line_count=0
#     print(f'dict_reader is : {dict_reader} !')
#     for row in dict_reader:
#         if line_count==0:
#             print(f'Column names are {', '.join(row)}')
#             line_count += 1
#         print('dict_row',row)
#         print(f'\t{row['EmployeeID']} emp_ids name is {row['Name']} and works in {row['Department']} department')
#         line_count += 1
#         print(f'processed {line_count - 1} lines ')

with open('data/created_csv.csv',mode='w',newline='') as writing:
    writer=csv.writer(writing)
    header=['name','empid','imsi']
    data =[ ['andy','0001','915814'],
            ['chopper','6969','1432']]

    writer.writerow(header)
    writer.writerow('-------------------')
    writer.writerows(data)
