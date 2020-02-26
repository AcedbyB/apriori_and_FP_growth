import time
import copy

from mining import int_data, brute_check, threshold, exist, union, reversePrint, prepare, check_ans, check, reversePrint
candidates = []
cur_sample = []
number_of_partitions = 30 #config the number of partitions

def apriori(cur_list):
    prelist = []
    for itemset in cur_list:
        cnt = 0
        for i in cur_sample:
            if check(itemset,i) == True:
                cnt+=1
        if cnt > threshold*len(cur_sample):
            if exist(itemset, candidates) == False:
                candidates.append(itemset)
            prelist.append(itemset)
    nextlist = []
    for i in range(1,len(prelist)):
        for j in range(0, i):
            next_list = union(prelist[i],prelist[j])
            if len(next_list) == len(prelist[i]) + 1:
                if exist(next_list, nextlist) == False:
                    next_list.sort()
                    nextlist.append(next_list)
    if len(nextlist) > 0:
        apriori(nextlist)

def second_scan():
    for i in candidates:
        cnt = 0
        for j in range(0, len(int_data)):
            if check(i, j) == True:
                cnt += 1
        if cnt > threshold*len(int_data) and len(i) > 4:
            reversePrint(i)

def improved_apriori(num_of_parts):
    global cur_sample
    cur_list = []
    for i in range(1,108):
        cur_list.append([i])
    length = int(len(int_data)/num_of_parts)
    for i in range(0, len(int_data)):
        if int(i/length) > int((i-1)/length): 
            print("current working on batch", end = " ")
            print(int(i/length))
            apriori(copy.copy(cur_list))
            cur_sample = []
            cur_sample.append(i)
        else:
            cur_sample.append(i)
    apriori(copy.copy(cur_list))
    second_scan()
    

def main():
    prepare()
    start = time.time()
    improved_apriori(number_of_partitions)
    end = time.time()
    print("time elapsed:", end = " ")
    print(end - start)

main()