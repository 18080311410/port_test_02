"""
通过mock模拟用户余额函数返回值
"""
from mock_demo_01 import balance_user
from unittest import mock

# user=balance_user()
mock_user=mock.Mock(return_value=10000)

price=1000

# result=user-price
result=mock_user(20,500)-price
print(result)

