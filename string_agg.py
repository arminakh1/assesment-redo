## find whteher list of strings are aggronom or not
def aggronom(agg_list):
    if len(agg_list) < 2 :
        return False
    agg1=[]
    for i in agg_list:
        st=sorted(i)
        if len(agg1)== 0:
            agg1=st
        else:
            if agg1 != st:
                return False
            else:
                continue
    print(agg1)
    return True
       
def main():
    print("Please enter all the words for aggronom check:")
    agg_list=[]
    while(True):
        s=input()
        if s=="done":
            break
        else:
            agg_list.append(s)
    print(aggronom(agg_list))

if __name__=="__main__":
    main()
