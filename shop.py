def show_title():
    print("-"*40)
    print("1.상품목록 / 2.담기 / 3.빼기 / 4.장바구니 / 5.쿠폰 / 6.결제 / q.종료")
    print("-"*40)

# 사용자 메뉴 선택 출력
def menu_choice():
    while True:
        choice = input("선택: ").strip()
        if choice in ("1", "2", "3", "4", "5", "6", "q"):
            return choice
        print("메뉴를 선택해주세요.: ")


class Product: # 상품 1개를 담는 클래스
    count = 0  # 클래스 변수: 상품이 만들어질 때마다 1씩 늘어남 (자동 번호용)

    def __init__(self, name, price, stock):
        Product.count += 1
        self.id = Product.count   # 자동으로 1, 2, 3... 번호가 붙음
        self.name = name
        self.price = price
        self.__stock = stock      # 밑줄 2개: 밖에서 직접 못 바꾸게 숨김

    # 재고 보기
    def get_stock(self):
        return self.__stock


class Shop: # 상품 객체들을 모아서 갖고 있는 선반
    def __init__(self):
        self.product_list = []

    # 상품 등록 기능
    def add_product_data(self, name, price, stock):
        product = Product(name, price, stock)
        self.product_list.append(product)

    # 상품 목록 출력
    def show_product(self):
        for p in self.product_list:
            if p.get_stock() == 0:
                print(f"{p.id}. {p.name}    {p.price:,}원  (품절)")
            else:
                print(f"{p.id}. {p.name}    {p.price:,}원  (재고 {p.get_stock()}개)")


class ShoppingCart: # 장바구니 (조회, 추가, 삭제)
    def __init__(self):
        self.Shopping_cart_list = []

    # 장바구니 (장바구니 조회)
    def show_Shopping_items(self):
        return self.Shopping_cart_list
        
    # 상품 담기(장바구니에 추가)
    def add_product(self, item):
        self.Shopping_cart_list.append(item)

    # 상품 빼기(장바구니에서 삭제)
    def del_product(self, item):
        self.Shopping_cart_list.remove(item)

# 쿠폰 사용
def coupon():
    pass

# 결제 단계
def payment():
    pass


shop = Product() # 상품 선반 객체 만들기
shop.add_product_data("무선 이어폰", 89000, 3) # 테스트용 상품
shop.add_product_data("텀블러", 15000, 10)
shop.add_product_data("보조배터리", 32000, 5)
shop.add_product_data("마우스패드", 9000, 0)
shop.add_product_data("USB 허브", 18000, 4)

cart = ShoppingCart()

while True:
    show_title()
    choice = menu_choice()

    if choice == "1":
        shop.show_product()
    elif choice == "2":
        shop.add_product_data()
    elif choice == "3":
        cart.del_product()
    elif choice == "4":
        cart.show_Shopping_items()
    elif choice == "5":
        pass #"?".coupon()
    elif choice == "6":
        pass #"?".payment()
    elif choice == "q":
        print("프로그램을 종료합니다.")
        break