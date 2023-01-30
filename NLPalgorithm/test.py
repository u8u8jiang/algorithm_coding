
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter

filter1 = make_filter("8")  #這一行調用了make_filter函數, 接受了 the_filter函數作為返回值, 
# 也就是說這裡的 filter1 等於函數 the_filter

filter_result = filter1("data.csv")
# print(filter_result)

