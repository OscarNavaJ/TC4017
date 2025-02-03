
"""
A01745524 - Oscar Nava Jiménez
MNA - TC4017 A4.2
"""
import argparse
import time
def sort(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    n = len(m)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    return m
def mean(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    acumm = 0
    for i in m:
        acumm += i
    mean_val = acumm/len(m)

    return mean_val

def median(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    sorted_list = sort(m)
    n = len(m)
    if n % 2 == 0:
        return mean([sorted_list[int(n/2)-1],sorted_list[int(n/2)]])
    return sorted_list[int(n/2)]

def mode(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    occurrences = {}
    max_ocurrence = 0
    for i in m:
        if i not in occurrences:
            occurrences[i] = 1
        else:
            occurrences[i] += 1
        if max_ocurrence == 0 or occurrences[i] >= occurrences[max_ocurrence]:
            max_ocurrence = i
    return max_ocurrence

def standard_deviation(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    mean_val = mean(m)
    squared_dev = 0
    for i in m:
        squared_dev += (i-mean_val)**2
    standard_dev = (squared_dev/len(m))**0.5
    return standard_dev

def variance(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    mean_val = mean(m)
    squared_dev = 0
    for i in m:
        squared_dev += (i-mean_val)**2
    variance_val = (squared_dev/(len(m)-1))
    return variance_val
def main(file_path : str):
    """
    :param file:str File path of numbers to be received
    :return:
    """
    start_time = time.perf_counter()
    numbers = []
    with open(file_path, "r+", encoding="UTF-8") as f:
        data = f.readlines()
        for n in data:
            val = n.split("\n")[0]
            try:
                val = float(val)
                numbers.append(val)
            except ValueError:
                print(f"Invalid data found: {val}")
                corrected_val = ''.join(c for c in val if c.isdigit())
                print(f"Correcting with: {corrected_val}")
                try :
                    val = float(corrected_val)
                    numbers.append(val)
                except ValueError:
                    print(f"Cannot correct: {val}")


    sort(numbers)
    mean_val = mean(numbers)
    median_val = median(numbers)
    mode_val = mode(numbers)
    standar_dev_val = standard_deviation(numbers)
    variance_val = variance(numbers)
    end_time = time.perf_counter()
    exec_time = end_time-start_time
    with open("../StatisticsResults.txt", "w", encoding="UTF-8") as f:
        f.write(f"MEAN:{mean_val}\n" )
        f.write(f"MEDIAN:{median_val}\n" )
        f.write(f"MODE:{mode_val}\n" )
        f.write(f"STANDARD DEVIATION:{standar_dev_val}\n" )
        f.write(f"VARIANCE:{variance_val}\n" )
        f.write(f"EXECUTION TIME:{exec_time}\n" )
    print("MEAN:", mean_val)
    print("MEDIAN:", median_val)
    print("MODE:", mode_val)
    print("STANDARD DEVIATION:", standar_dev_val)
    print("VARIANCE:", variance_val)
    print(f"EXECUTION TIME: {exec_time} s" )

if __name__ == "__main__":
    # l = [1,20,50,3,10,15,20]
    # print(sort(l))
    # print(mean(l))
    # print(median(l))
    # print(mode(l))
    # print(standard_deviation(l))
    # print(variance(l))
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type= str)
    args = parser.parse_args()
    file = args.file
    main(file)
