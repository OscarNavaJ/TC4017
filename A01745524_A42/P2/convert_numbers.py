
"""
A01745524 - Oscar Nava Jiménez
MNA - TC4017 A4.2
"""
import argparse
import time

def integer_to_bin(i : int):
    """
    :param i:int Array of integers to be sorted
    :return:str
    """
    return bin(i & 0xff).split("0b")[1]

def integer_to_hex(i : int):
    """
    :param i:int Array of integers to be sorted
    :return:str
    """
    return hex(i & ((1 << 32) - 1)).split("0x")[1].upper()

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
                val = int(val)
                numbers.append(val)
            except ValueError:
                print(f"Invalid data found: {val}")
                corrected_val = ''.join(c for c in val if c.isdigit())
                print(f"Correcting with: {corrected_val}")
                try :
                    val = int(corrected_val)
                    numbers.append(val)
                except ValueError:
                    print(f"Cannot correct: {val}")
    with open("../ConvertionResults.txt", "w", encoding="UTF-8") as f:
        f.write("DECIMAL, BIN, HEX\n" )
        print("DECIMAL, BIN, HEX\n")
        for i in numbers:
            hex_val = integer_to_hex(i)
            bin_val = integer_to_bin(i)
            f.write(f"{i}, {bin_val}, {hex_val}\n" )
            print(f"{i}, {bin_val}, {hex_val}\n")

        end_time = time.perf_counter()
        exec_time = end_time-start_time
        f.write(f"EXECUTION TIME:{exec_time}\n" )

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
