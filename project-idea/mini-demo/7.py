# 邮件地址切片器    
# 目的：编写一个Python脚本，可以从邮件地址中获取用户名和域名。      
# 提示：使用@作为分隔符，将地址分为分为两个字符串。     


# Get the user's email address
email = input("what's your email address?: ").strip()


user_name = email[:email.index("@")]    # Slice out the user name
domain_name = email[email.index("@")+1:]    # Slice out the domain name
res = f"your username is '{user_name}', and your domain name is '{domain_name}' "
print(res)
