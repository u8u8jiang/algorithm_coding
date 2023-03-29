# 货币换算器
# 目的：编写一个Python脚本，可以将一种货币转换为其他用户选择的货币。
# 提示：使用Python中的API，或者通过forex-python模块来获取实时的货币汇率。
# 安装：forex-python


from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input("Enter the amount you want to convert\n "))
from_currency = input("From ").upper
to_currency = input("To ").upper
print(from_currency, "to", to_currency, amount)

result = c.convert(from_currency, to_currency, amount)
print(result)

