# from apriori_func import apriori

adult_data = open("adult.data",'r')
all_string_Set = set()
curStr = ''
d = dict()
int_data = []
threshold = 1/5
got_it = []
string_d = []

def add( str1, all_elements ): 
    if str1[0] == ' ':
        return
    if str1 not in all_string_Set:
        all_elements.write(str1 + '\n')
        all_string_Set.add(str1)
    
def separate_string_data():
    all_elements = open("elements","w+")
    while True:
        line = adult_data.readline()
        curStr = ''
        if len(line) == 0:
            break
        cur = 0
        for c in line:
            if c == ',':
                cur += 1
                if cur == 13:
                    if int(curStr) < 20:
                        curStr = "low-hour"
                    elif int(curStr) <= 50:
                        curStr = "medium-hour"
                    else:
                        curStr = "high-hour"
                if cur == 1:
                    if int(curStr) < 25:
                        curStr = "young"
                    elif int(curStr) <= 50:
                        curStr = "middle-aged"
                    else:
                        curStr = "senior"
                if cur != 3 and cur != 11 and cur!=12 and cur!=5:
                    add(curStr, all_elements)
                curStr = ''
            elif c != ' ':
                curStr += c
        if len(curStr) > 0:
            add(curStr, all_elements)


def map_string_to_int():
    all_elements = open("elements","r")
    word_list = []
    while True:
        word = all_elements.readline()
        if len(word) == 0:
                break
        word_list.append(word)
    global d
    d = dict([(y,x+1) for x,y in enumerate(sorted(set(word_list)))])


def convert_sample_to_int():
    while True:
        l = []
        line = adult_data.readline()
        curStr = ''
        if len(line) < 5:
            break
        cur = 0
        for c in line:
            if c == ',':
                cur += 1
                if curStr == "?" or curStr == "?\n":
                    curStr = ""
                    continue
                if cur == 13:
                    if int(curStr) < 20:
                        curStr = "low-hour"
                    elif int(curStr) <= 50:
                        curStr = "medium-hour"
                    else:
                        curStr = "high-hour"
                if cur == 1:
                    if int(curStr) < 25:
                        curStr = "young"
                    elif int(curStr) <= 50:
                        curStr = "middle-aged"
                    else:
                        curStr = "senior"
                if cur != 3 and cur != 11 and cur!=12 and cur!=5:
                    l.append(d[curStr + "\n"])
                curStr = ''
            elif c != ' ':
                curStr += c
        if len(curStr) > 0:
            l.append(d[curStr])
        int_data.append(l)
        got_it.append([])
        for i in range(0,150):
            got_it[len(got_it)-1].append(False)
        sample = int_data[len(int_data) - 1]
        for num in sample:
             got_it[len(got_it)-1][num] = True


def check(itemset, sample_num):
    for i in itemset:
        if got_it[sample_num][i] == False:
            return False
    return True

def brute_check(itemset, sample):
    for i in itemset:
        flag = False
        for j in sample:
            if i == j:
                flag = True
        if flag == False:
            return False
    return True

def exist(itemset, nextlist):
    for l in nextlist:
        if brute_check(itemset, l) == True:
            return True
    return False

def union(l1, l2):
    ans = []
    for i in l1:
        ans.append(i)
    for j in l2:
        flag = False
        for i in l1:
            if i == j:
                flag = True
                break
        if flag == False:
            ans.append(j)
    return ans        

def get_key(val): 
    for key, value in d.items(): 
         if val == value: 
             return key 

def setup_dictionary(): 
    for i in range(1,107):
        string_d.append(get_key(i))

def reversePrint(l):
    string_ans = []
    for i in l:
        string_ans.append(get_key(i)[:-1])
    print(string_ans)

def check_ans():
    ans = [9, 30, 45, 55, 57, 94, 97, 104]
    cnt = 0
    for i in range(0, len(int_data)):
        if check(ans, i):
            cnt += 1
    print(cnt)

def prepare():
    map_string_to_int()
    convert_sample_to_int()
    setup_dictionary()


