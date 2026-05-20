class Mergesorts:
    def mergeSort(self,list1,list2):
        list3=[]
        j=0
        i=0
        k=0
        while i<len(list1) and j<len(list2):
            if list1[i]<list2[j]:
               list3.append(list1[i])
               i+=1
               k+=1
            else:
                list3.append(list2[j])
                j+=1
                k+=1

        while len(list1)>i:
            list3.append(list1[i])
            i+=1
            k+=1

        while len(list2)>j:
            list3.append(list2[j])
            i+=1
            k+=1
        
        
        return list3
    
if __name__ == '__main__':
    obj=Mergesorts()
    list1=[1,3,5,7,9]
    list2=[2,4,6]
    ans=obj.mergeSort(list1,list2)
    print(ans)