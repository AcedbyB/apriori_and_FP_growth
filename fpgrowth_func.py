import copy
import time

from mining import got_it, int_data, threshold, exist, prepare, string_d
from mining import check_ans, brute_check, reversePrint

class Tree:
    def __init__(self):
        self.child = []
        self.data = None
        self.cnt = 0
    
    def insert(self, sample, cur, fp_order):
        if cur < len(fp_order):
            num = fp_order[cur][1]
            random = [num]
            if brute_check(random, sample[1]) == True:
                if self.data == num:
                    self.cnt += sample[0]
                    self.insert(sample, cur + 1, fp_order)
                else:
                    flag = False
                    for c in self.child:
                        if c.data == num:
                            flag = True
                            c.insert(sample, cur, fp_order)
                            break
                    if flag == False:
                        next_child = Tree()
                        next_child.data = num
                        next_child.cnt = sample[0]
                        next_child.insert(sample, cur + 1, fp_order)
                        self.child.append(next_child)
            else:
                self.insert(sample, cur + 1, fp_order)
    
    def build(self, list_sample, fp_order):
        for j in list_sample:
            self.insert(j, 0, fp_order)

    def conditional_database(self, item, curlist, database):
        if self.data == item:
            database.append([self.cnt, copy.copy(curlist)])
        else:
            if self.data != None:
                curlist.append(self.data)
            for j in self.child:
                j.conditional_database(item, curlist, database)
            if self.data != None:
                curlist.pop()


def fp_growth(database):
    if len(database) <= 1: 
        return database
    ans = []
    num_set = set([])
    fp_order = []
    for j in database:
        for i in j[1]:
            num_set.add(i)
    for i in num_set:
        cnt = 0
        for j in database:
            ran = []
            ran.append(i)
            if brute_check(ran,j[1]) == True:
                cnt += j[0]
        if cnt > threshold*len(int_data): 
            fp_order.append([cnt, i])
    fp_order.sort(reverse = True)
    root = Tree()
    root.build(database, fp_order) 
    fp_order.sort()
    for i in fp_order:
        cond_database = []
        root.conditional_database(i[1], [], cond_database)
        counted_item_sets = fp_growth(cond_database)
        for j in counted_item_sets:
            j[1].append(i[1])
            ans.append(j)
    return ans
    

def main():
    prepare()
    transform_int_data = []
    for i in int_data:
        cur = [1]
        cur.append(i)
        transform_int_data.append(cur)
    start = time.time()
    final_data = fp_growth(transform_int_data)
    for i in final_data:
        if i[0] > threshold*len(int_data) and len(i[1])>4:
            i[1].sort()
            reversePrint(i[1])
    end = time.time()
    print("time elapsed:", end = " ")
    print(end - start)

main()