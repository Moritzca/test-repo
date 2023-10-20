# checking for prime



def main():
    for x in range (100):
        if is_prime(x+1)==0:
            print (x+1," Prime")
        else:
            print (x+1," - [",is_prime(x+1),"]")



def is_prime (num):
    a = 2
    if num <= 2:
        return True
    else:
        while a<num:
            if num%a == 0:
                return a
            else:
                a += 1
            
        return 0
        


if __name__ == "__main__":
    main()
