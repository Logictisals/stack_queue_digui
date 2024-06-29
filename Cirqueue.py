class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity + 1  # 加1是为了处理队列为空的情况
        self.queue = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def is_empty(self):
        """判断队列是否为空"""
        return self.head == self.tail

    def is_full(self):
        """判断队列是否已满"""
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item):
        """入队操作"""
        if self.is_full():
            print("队列已满，无法入队")
            return
        self.queue[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        print(f"元素 {item} 已入队")

    def dequeue(self):
        """出队操作"""
        if self.is_empty():
            print("队列为空，无法出队")
            return None
        item = self.queue[self.head]
        self.head = (self.head + 1) % self.capacity
        print(f"出队元素为：{item}")
        return item

    def peek(self):
        """查看队首元素，不移除"""
        if not self.is_empty():
            return self.queue[self.head]
        else:
            print("队列为空")
            return None

    def size(self):
        """返回队列的大小"""
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.capacity - (self.head - self.tail)

# 测试循环队列
def test_circular_queue():
    cq = CircularQueue(5)  # 创建一个容量为5的循环队列

    # 入队操作
    for i in range(1, 6):
        cq.enqueue(i)

    # 测试队列满的情况
    print("尝试入队：")
    cq.enqueue(6)

    # 出队操作
    while not cq.is_empty():
        print("当前队列大小:", cq.size())
        print("出队元素:", cq.dequeue())

    # 测试队列为空的情况
    print("尝试出队：", cq.dequeue())

test_circular_queue()