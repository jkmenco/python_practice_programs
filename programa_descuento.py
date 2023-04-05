
def data_request_to_user():
    print()
    print("\tBienvenido, vamos a calcular apartir de un precio o total un porcentaje de descuento a selección \n\tUsted debe ingresar un precio y luego ingresar en cuanto quiere su descuento")
    print()
    
    price_product = float(input("Digite el precio del producto -> $ "))
    price_discount = int(input("Digite el descuento -> % "))
    
    print()
    return price_product, price_discount

def discount_process(a,b):
    
    discount = (a * b) / 100

    final_discount = (a - discount)
    
    return final_discount

def process_of_informing_the_user():
    print()
    print(f"De ${price_product}")
    print()
    print(f"Usted debe pagar ${final_discount}\nCon un {price_discount}% de descuento")
    print()


price_product, price_discount = data_request_to_user()

final_discount = discount_process(price_product,price_discount)

process_of_informing_the_user()
