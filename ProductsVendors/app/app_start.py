from app.impl import productservicesimp,Product
from app.vendor_info import vendor


def take_product_input():
    '''Take input from user --> and create product object...'''

    pid = int(input('Enter Product Id : '))
    pnam = input('Enter Product Name : ')
    pqty = int(input('Enter Product Qty : '))
    prc = float(input('Enter Product Price : '))
    ven = take_vendor_input()
    cat = input('Enter Product Category : ')
    return Product(pid=pid,pnm=pnam,pric=prc,pqty=pqty,pven=ven,pcat=cat)

def take_vendor_input():
    '''Take input from User and create Vendor Object'''
    vid = int(input('Enter Vendor Id : '))
    vname = input('Enter Vendor Name : ')
    vadr = input('Enter Vendor Address : ')
    return vendor(vid,vname,vadr)


if __name__=='__main__':
    productservices = productservicesimp()
    while True:
        print('''
                    1 Add_product
                    2 Avg_product_price
                    3 Delete_product
                    4 Get_all_product
                    5 Max_product_price
                    6 Min_product_price
                    7 Search_by_category
                    8 Search_by_id
                    9 Search_by_vendor
                    10 Total_product_price
                    11 Update_product

            ''')
        choice = int(input('Enter Your Choice : '))
        if choice == 1:
            product = take_product_input()
            productservices.add_product(product)
        elif choice == 2:
            avg = productservices.avg_product_price()
            print('Total Product Price : ', avg)
        elif choice==3:
            try:
                pid=int(input("enter product id to delete product?: "))
                print(productservices.delete_product(pid))
            except ValueError as v:
                print("please enter valid id")

        elif choice == 4:
            prodList = productservices.get_all_products()
            print('Products', prodList)
        elif choice == 5:
            max_price = productservices.max_product_price()
            print('maximum Product Price : ', max_price)



        elif choice == 6:
            min_price = productservices.min_product_price()
            print('maximum Product Price : ', min_price)


        elif choice == 7:
            search_cat=input("enter product catagory you want to search: ")
            prod=productservices.search_by_catagories(search_cat)
            print(prod)

        elif choice == 8:
            search_pid=int(input("enter product id you want to search: "))
            prod=productservices.search_by_id(search_pid)
            print(prod)


        elif choice == 9:
            search_ven = input("enter product vendor name  you want to search: ")
            prod = productservices.search_by_vendor(search_ven)

        elif choice == 10:
            total = productservices.total_product_price()
            print('Total Product Price : ', total)

        else:
            print('Invalid Choice..')

        ch = input('Do you want to continue : Y/N')
        if ch.lower() in ['n', 'no']:
            break




