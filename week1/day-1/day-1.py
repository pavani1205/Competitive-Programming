def get_products_of_all_ints_except_at_index(int_list):
    if(len(int_list)<3):
        print(int_list[0]+" "+int_list[1])
        
    prod=[0 for x in range(len(int_list))]
    product=1

    # Make a list with the products
    for i in range(0,len(int_list)):
        prod[i]=product
        product=product*int_list[i]
    product=1
    for i in range(len(int_list)-1,-1,-1):
        prod[i]=prod[i]*product
        product=product*int_list[i]

    return prod
