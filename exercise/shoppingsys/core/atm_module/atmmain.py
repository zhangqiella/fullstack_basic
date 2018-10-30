# -*- coding: utf-8 -*-
'''
@Author: Administrator
@Time: 2018/10/29
@File: atmmain.py
'''

from core.atm_module.atmauth import atmlogin
from log import logger
from core.atm_module import db_handler
from core.atm_module import accounts
from core.atm_module import transaction

atm_user_data={
    'user_name':None,
    'is_authenticated':False,
    'acc_data':None
}

atm_logger = logger.logger('atm_logger')

@atmlogin
def main():
    # pass
    #paycheck(10)
    atm_show_info = u'''
    ------------Bank----------
    1.  账户信息
    2.  还款(功能已实现)
    3.  取款(功能已实现)
    4.  转账
    5.  账单
    6.  退出'''
    print(atm_show_info)

    menu_dic={
        '1':account_info,
        '2':repay,
        '3':withdraw,
        '4':transfer,
        '5':bills,
        '6':quit
    }

    exit_flag = False
    acc_data = atm_user_data['acc_data']

    while not exit_flag:
        operation = input('input the operation index you would like:>>>').strip()
        if operation in menu_dic.keys():
            menu_dic[operation](acc_data)
        else:
            atm_logger.warning('your input illegal')
@atmlogin
def account_info(acc_data):
    print(atm_user_data['acc_data'])

@atmlogin
def repay(acc_data):
    current_acc_data = accounts.loaddata(acc_data['id'])
    # cur_balance = current_acc_data['balance']
    # cur_credit = current_acc_data['credit']
    # print('current credit value is %f, balance is %f' %(cur_credit,cur_balance))
    back_flag = False


    while not back_flag:
        repay_amount = input('input the money amounts:').strip()
        if repay_amount == 'b':
            back_flag = True
            break
        if len(repay_amount) > 0 and repay_amount.isdigit():
            repay_amount =  float(repay_amount)
            if repay_amount > 0:
                new_acc_data = transaction.make_transaction(repay_amount,'repay',current_acc_data,atm_logger)
                if new_acc_data:
                    atm_user_data['acc_data'] = new_acc_data
                    atm_logger.debug("the new balance is %f"%new_acc_data['balance'])
            else:
                atm_logger.warning('invalid input')
        else:
            atm_logger.warning('invalid input')


@atmlogin
def withdraw(acc_data):
    pass

#购物时调的付款接口
@atmlogin
def consume(sum):
    current_acc_data = accounts.loaddata(atm_user_data['user_name'])
    new_acc_data = transaction.make_transaction(sum, 'consume', current_acc_data, atm_logger)

    if new_acc_data:
        atm_logger.warning('consume success')
        return True
    else:
        atm_logger.warning('no enough money, consume failed')
        return False

@atmlogin
def transfer(acc_data):
    pass

@atmlogin
def bills(acc_data):
    pass

@atmlogin
def quit(acc_data):
    exit()

def test():
    main()

if __name__ == '__main__':
    test()