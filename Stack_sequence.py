""""
栈的顺序存储方式就是在顺序表的基础上对插入和删除操作限制它们在顺序表的同一端进行，
所以同顺序表一样也可用一维数组表示。
一般地，可以设定一个足够大的一维数组存储栈，数组中下标为0或的元素就是栈底，
对于栈顶，可以设一个指针top指示它。
为了方便，设定top所指的位置是栈顶，这样，当top=-1时就表示是一个空的栈。
一个栈的几种状态以及在这些状态下栈顶指针top和栈中结点的关系如下图所示。
"""
class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size  # 初始化栈空间
        self.top = -1  # 栈顶指针，初始时指向空栈

    def is_empty(self):
        """判断栈是否为空"""
        return self.top == -1

    def is_full(self):
        """判断栈是否已满"""
        return self.top == self.max_size - 1

    def push(self, item):
        """入栈操作"""
        if self.is_full():
            print("栈已满，无法入栈")
        else:
            self.top += 1
            self.stack[self.top] = item

    def pop(self):
        """出栈操作"""
        if self.is_empty():
            print("栈为空，无法出栈")
            return None
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item

    def peek(self):
        """查看栈顶元素，不移除"""
        if not self.is_empty():
            return self.stack[self.top]
        else:
            print("栈为空")
            return None

    def size(self):
        """返回栈的大小"""
        return self.top + 1

# 测试函数
def test_stack():
    stack = Stack(5)  # 创建一个最大容量为5的栈
    print("栈是否为空:", stack.is_empty())  # 应该返回True
    print("栈的大小:", stack.size())  # 应该返回0

    # 入栈操作
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("当前栈顶元素:", stack.peek())  # 应该返回3

    # 出栈操作
    print("出栈元素:", stack.pop())  # 应该返回3
    print("当前栈顶元素:", stack.peek())  # 应该返回2

    # 继续入栈操作
    stack.push(4)
    stack.push(5)
    stack.push(6)

    # 测试栈满
    print("尝试入栈7:")  # 应该提示栈已满
    stack.push(7)

    # 测试栈空
    while not stack.is_empty():
        print("出栈元素:", stack.pop())
    print("尝试出栈:", stack.pop())  # 应该提示栈为空

test_stack()