# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: main.py
'''

from log import logger
#注意这个import,指明前面具体的core.shopping_module.auth
from core.shopping_module.auth import login
from core.atm_module import atmmain

shop_user_data={
    'user_name': None,
    'is_authenticated': False,
    'user_data': None
}

shop_logger = logger.logger('shop_logger')

@login
def run(logger_obj):
    product_list = [
        ('Mac', 9000),
        ('kindle', 800),
        ('tesla', 900000),
        ('python book', 105),
        ('bike', 2000),

    ]

    shop_cart = []
    while True:
        for i,v in enumerate(product_list,1):
            print(i,'>>>>>',v)
        choice = input('please input the product you want to buy[q to quit]:')
        choice = choice.strip()
        if choice.isdigit():
            print(choice)
            shop_cart.append(int(choice))
            paynow = input('do you want to pay now?\'Y\' or \'N\'')
            if paynow == 'Y' or paynow =='y':
                sum = 0
                ##注意遍历list的方法，都忘了
                for i in range(0,len(shop_cart)):
                    index = shop_cart[i] -1
                    # print('index is %d'%index)
                    sum += product_list[index][1]
                    # sum +=product_list[i-1][1]
                print('the sum money is:%d'%sum)
                shop_logger.warning('you should pay %d'%sum)
                pay_success = atmmain.consume(sum)
                if pay_success:
                    shop_logger.info('you have bought the things successfully!')
                    break
                else:
                    shop_logger.warning('your payment is failed.')
                    break

        elif choice == 'q':
            shop_logger.warning('you will quit the shopping')
            break
        else:
            shop_logger.warning('invalid imput')



def main():
    run(shop_logger)

def test():
    pass


if __name__ == '__main__':
    test()
