class Node:
    """链表节点类"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    """链式栈类"""
    def __init__(self):
        self.top = None  # 初始化时栈顶指针为空

    def is_empty(self):
        """判断栈是否为空"""
        return self.top is None

    def push(self, data):
        """入栈操作"""
        new_node = Node(data)  # 创建一个新节点
        new_node.next = self.top  # 新节点的next指向当前栈顶
        self.top = new_node  # 更新栈顶为新节点

    def pop(self):
        """出栈操作"""
        if self.is_empty():
            print("栈为空，无法出栈")
            return None
        else:
            popped_node = self.top  # 取出栈顶节点
            self.top = self.top.next  # 更新栈顶为下一个节点
            popped_node.next = None  # 断开与下一个节点的连接
            return popped_node.data

    def peek(self):
        """查看栈顶元素，不移除"""
        if not self.is_empty():
            return self.top.data
        else:
            print("栈为空")
            return None

    def size(self):
        """返回栈的大小"""
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

# 测试函数
def test_linked_stack():
    stack = LinkedStack()
    print("栈是否为空:", stack.is_empty())  # 应该返回True

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

    # 测试栈的大小
    print("栈的大小:", stack.size())  # 应该返回2

test_linked_stack()


def is_balanced(expression):
    """
    检查括号表达式是否平衡。

    :param expression: 包含括号的字符串
    :return: 如果括号平衡返回True，否则返回False
    """
    stack = LinkedStack()  # 创建链式栈实例
    mapping = {')': '(', '}': '{', ']': '['}  # 括号映射关系

    for char in expression:
        if char in mapping:  # 如果是闭括号
            # 栈为空或者栈顶不是对应的开括号
            if stack.is_empty() or stack.peek() != mapping[char]:
                return False
            stack.pop()  # 否则，弹出栈顶元素
        else:
            stack.push(char)  # 如果是开括号，压入栈中

    # 如果栈为空，则括号匹配
    return stack.is_empty()


# 测试括号匹配函数
def test_bracket_matching():
    expressions = [
        "()",  # 应该返回True
        "([]){}",  # 应该返回True
        "{[)]}",  # 应该返回False
        "((()))",  # 应该返回True
        "{[}]",  # 应该返回True
        "{[(])}",  # 应该返回False
        "",  # 应该返回True，空字符串视为平衡
        "{[(])}(]",  # 应该返回False
    ]

    for expr in expressions:
        print(f"The expression '{expr}' is balanced: {is_balanced(expr)}")


test_bracket_matching()