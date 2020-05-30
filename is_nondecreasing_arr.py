class Sol:
    def is_nondecreasing_arr(self,arr):
        count=0
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                count+=1
        if count>1:
            return False
        return True


if __name__ == '__main__':
    p=Sol()
    print(p.is_nondecreasing_arr([4,2,1]))
