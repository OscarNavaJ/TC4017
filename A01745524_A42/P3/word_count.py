
"""
A01745524 - Oscar Nava Jiménez
MNA - TC4017 A4.2
"""
import argparse
import time


def count_words(m : list):
    """
    :param m:str Array of integers to be sorted
    :return:list Array sorted
    """
    occurrences = {}

    for i in m:
        if i not in occurrences:
            occurrences[i] = 1
        else:
            occurrences[i] += 1

    return occurrences

def main(file_path : str):
    """
    :param file:str File path of numbers to be received
    :return:
    """
    start_time = time.perf_counter()
    words = []
    with open(file_path, "r+", encoding="UTF-8") as f:
        data = f.readlines()
        for n in data:
            val = n.split("\n")[0]
            words.append(val)
    word_count = count_words(words)

    end_time = time.perf_counter()
    exec_time = end_time-start_time
    with open("../WordCountResults.txt", "w", encoding="UTF-8") as f:
        for word, occurences in word_count.items():
            f.write(f"{word} {occurences}\n" )
            print(f"{word} {occurences}\n" )

        f.write(f"EXECUTION TIME:{exec_time}\n" )
    print(f"EXECUTION TIME: {exec_time} s" )

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type= str)
    args = parser.parse_args()
    file = args.file
    main(file)
