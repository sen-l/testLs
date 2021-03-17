
class Tools(object):

    def __init__(self):
        # 增、删、改、查
        self.add_str = '增'
        self.delete_str = '删'
        self.update_str = '改'
        self.select_str = '查'

    def add(self):
        print('增方法')

    def delete(self):
        print('删方法')

    def update(self):
        print('改方法')

    def select(self):
        print('查方法')

    def __str__(self):
        return '%s--%s--%s--%s' % (self.add_str, self.delete_str, self.update_str, self.select_str)

# 多次增加，多次删除
class HMTools(Tools):

    def my_func1(self):
        print(super().select())
    #
    # def my_func2(self):
    #     pass
    #
    # def __str__(self):
    #     return '%s--%s--%s--%s222' % (self.add_str, self.delete_str, self.update_str, self.select_str)
#
t = HMTools()
# t = Tools()
# t.select()
print(t)