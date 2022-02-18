from app.services import *
#from product_info import product

class productservicesimp(productservices):
    productlist=[]
    venprodlist=[]
    def add_product(self, prod:Product):
       if type(prod)==Product:
           if prod.prodid>0:
               if prod.prodprice>=100:
                   result=self.search_by_id(prod.prodid)
                   if result:
                        print('duplicate product')
                   else:
                        productservicesimp.productlist.append(prod)
                        print('product added successfully.......')
               else:
                   print("invalid product price")
           else:
               print('invalid product ID')
       else:
           print('invalid product type...product cannot be added')


    def delete_product(self, pid: int):
        if productservicesimp.productlist:
            delete_prodlist=[]
            for prod in productservicesimp.productlist:
                if prod.prodid == pid:
                    delete_prodlist.append(prod)
                    productservicesimp.productlist.remove(prod)
                    print('product Removed successfully.......')
                return delete_prodlist
        else:
            print("product list empty")


    def get_all_products(self):
        return productservicesimp.productlist


    def search_by_id(self, pid: int):
        if type(pid)==int:
            for prod in productservicesimp.productlist:
                if prod.prodid==pid:
                   return prod
        else:
            print("invalid prodt id.....")


    def search_by_vendor(self, pven: str):
        if type(pven) == str:
            for prod in productservicesimp.productlist:
                if prod.vendor == pven:
                    productservicesimp.venprodlist.append(prod)
            return productservicesimp.venprodlist
        else:
            print("invalid vendor name.....")

    def search_by_catagories(self, pcat: str):
        if type(pcat)==str:
            for prod in productservicesimp.productlist:
                if prod.prodcat== pcat:
                    return (prod)
        else:
            print("invalid product category")


    def min_product_price(self):
        minimum=productservicesimp.productlist[0].prodprice
        for i in range(len(productservicesimp.productlist)-1):
            if productservicesimp.productlist[i+1].prodprice<minimum:
                minimum=productservicesimp.productlist[i+1].prodprice
        return minimum

    def max_product_price(self):
        maximum = productservicesimp.productlist[0].prodprice
        for i in range(len(productservicesimp.productlist) - 1):
            if productservicesimp.productlist[i + 1].prodprice > maximum:
                maximum = productservicesimp.productlist[i + 1].prodprice
        return maximum


    def total_product_price(self):
        total_prod_price=0.0
        for prod in productservicesimp.productlist:
            total_prod_price = total_prod_price +(prod.prodprice*prod.prodqty)
        return total_prod_price

    def avg_product_price(self):
        try:
            total_product_price = self.total_product_price()
            avgPrice = total_product_price / len(productservicesimp.productlist)
            return avgPrice
        except ZeroDivisionError:
            print("No any Product Exist..")






