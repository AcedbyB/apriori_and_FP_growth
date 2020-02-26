import time

from mining import int_data, check, threshold, exist, union, reversePrint, prepare

def apriori(cur_list):
    cur_list.sort()
    prelist = []
    for itemset in cur_list:
        cnt = 0
        for i in range(0,len(int_data)):
            if check(itemset,i) == True:
                cnt+=1
        if cnt > threshold*len(int_data):
            reversePrint(itemset)
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

def main():
    prepare()
    cur_list = []
    for i in range(1,107):
        cur_list.append([i])
    start = time.time()
    apriori(cur_list)
    end = time.time()
    print("time elapsed:", end = " ")
    print(end - start)
    
main()

# [45, 55, 57, 94, 104, 105]
# [45, 55, 57, 97, 104, 105]
# [55, 76, 94, 97, 104, 105]