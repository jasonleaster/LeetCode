class number() :
    key = 0
    bit_list = []
    cnt = 0
    
def num_init(array) :
    if array is None :
        return;

    num_array = []
    for i in range(0, len(array)) :
        cls_num = number()
        tmp = array[i]

        cnt = 1
        while tmp > 10 :
            bit_list  = bit_list + [tmp % 10]
            tmp /= 10
            cnt += 1

        cls_num.key = array[i]
        cls_num.cnt = cnt
        
        num_array += [cls_num]

    return num_array


def lgst_num(num_array) :
    if num_array is None :
        return

    output = [num_array[0]]

    for i in range(1, len(num_array)) :
        for j in range(1, len(num_array)) :
            

            if  output[j].key is num_array[j].key :

                output += [num_array[j]]

            else :
                k = 0
                a = num_array[max_loc].bit_list[k]
                b = num_array[j].bit_list[k]
                while a == b and k < min(a.cnt, b.cnt) :
                    k += 1
                    a = num_array[max_loc].bit_list[k]
                    b = num_array[j].bit_list[k]
                
                if k is a.cnt :

                elif k is b.cnt :
                    
                else :

                max_loc = j

        num_array.bit_list[0]


        

lgst_num([5,2,6,3,1,4])

