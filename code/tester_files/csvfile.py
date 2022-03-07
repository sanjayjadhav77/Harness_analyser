import csv
import os 
circuits=[[1,2,3],[4,5],[8,10]]
file_path='/home/pi/Desktop/testfile'+'.csv'
def test_file_write():
    with open(file_path, 'w') as csvFile:
        print(file_path)
        writer = csv.writer(csvFile)
        for x in range(len(circuits)):
            writer.writerow(circuits[x])  
    csvFile.close()
    
def test_file_Read():
    try:
        with open(file_path, 'r') as readFile:
            print(file_path)
            reader = csv.reader(readFile)
            print("reader",reader)
            lines = list(reader)
            print('lines',lines)
    except:
         print("file not found")
    
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            print(lines[x][y])
            circuits[x].append(int(lines[x][y]))
            
    print(circuits)
    
if __name__ == '__main__':
    #test_file_write()
    circuits=[[],[],[]]
    test_file_Read()
