"""Stop simping u noob shit"""
def main():
    """hum"""
    degree_in = input()
    line_in = int(input())
    list_str = []
    res_list = []
    loop_counter = 0
    checker = ""
    for i in range(line_in):
        v_in = input()
        greedy = len(v_in)
        if loop_counter != 0 and greedy != temp_len:
            checker = "Invalid size"
        if degree_in == "90":
            for i in v_in:               
                list_str.append(i)
        elif degree_in == "180" or degree_in == "flip":
            v_in = v_in[::-1]
            list_str.append(v_in)
        temp_len = len(v_in)
        loop_counter += 1
    
    if checker != "":
        print(checker)
    else:
        if degree_in == "90":
            temp_text = ""
            real_i = 0
            counter = 0
            for i in range(len(list_str)):
                temp_text += list_str[real_i]
                real_i += greedy
                if real_i > len(list_str) - 1:
                    counter += 1
                    real_i = counter
                    res_list.append(temp_text[::-1])
                    temp_text = ""
            for i in res_list:
                print(i)
        else:
            if degree_in == "180":
                for i in list_str[::-1]:
                    print(i)
            else:
                for i in list_str:
                    print(i)
main()
