def quick_sort(arr, low, high):
    """
    快速排序函数
    参数：
        arr: 需要排序的列表
        low: 起始索引
        high: 结束索引
    """
    def partition(low, high):
        """
        分区函数：选择最右边的元素作为基准值，
        将小于基准值的元素放在左边，大于基准值的元素放在右边
        """
        pivot = arr[high]  # 选择最右边的元素作为基准值
        i = low - 1  # 小于基准值的区域边界
        
        for j in range(low, high):
            # 如果当前元素小于或等于基准值
            if arr[j] <= pivot:
                i += 1  # 扩展小于基准值的区域
                arr[i], arr[j] = arr[j], arr[i]  # 交换元素
                print(f"交换后: {arr}")
        
        # 将基准值放到正确的位置
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        print(f"分区完成: {arr}")
        return i + 1

    if low < high:
        # 获取分区点
        pi = partition(low, high)
        print(f"\n以 {arr[pi]} 为基准值的分区结果: {arr}")
        print(f"对左半部分 {arr[low:pi]} 进行递归排序")
        # 递归排序左半部分
        quick_sort(arr, low, pi - 1)
        print(f"对右半部分 {arr[pi+1:high+1]} 进行递归排序")
        # 递归排序右半部分
        quick_sort(arr, pi + 1, high)

def main():
    # 测试数组
    test_array = [10, 20, 33, 21, 3, 5, 11, 55]
    print(f"原始数组: {test_array}")
    print("\n开始排序...")
    
    # 进行排序
    quick_sort(test_array, 0, len(test_array) - 1)
    
    print("\n排序完成!")
    print(f"排序后的数组: {test_array}")

if __name__ == "__main__":
    main() 


# Python基础语法大纲

"""
1. Python简介
   - Python的历史和特点
   - Python的应用领域
   - Python的安装和环境配置

2. 基础语法
   - 变量和数据类型
   - 运算符
   - 注释
   - 缩进和代码块

3. 流程控制
   - if条件语句
   - for循环
   - while循环
   - break和continue
   - pass语句

4. 数据结构
   - 列表(List)
   - 元组(Tuple) 
   - 字典(Dictionary)
   - 集合(Set)
   - 字符串操作

5. 函数
   - 函数定义和调用
   - 参数传递
   - 返回值
   - 匿名函数(Lambda)
   - 内置函数

6. 面向对象编程
   - 类和对象
   - 继承
   - 多态
   - 封装
   - 类方法和静态方法

7. 模块和包
   - 模块导入
   - 包的概念
   - 常用标准库
   - pip包管理

8. 文件操作
   - 文件的读写
   - 文件和目录操作
   - 异常处理

9. 高级特性
   - 生成器
   - 装饰器
   - 迭代器
   - 上下文管理器

10. 实践项目
    - 基础项目示例
    - 代码规范
    - 调试技巧
    - 性能优化
"""

"""
1. 变量基础
   - 变量是存储数据的容器
   - Python中的变量不需要声明类型
   - 变量名必须以字母或下划线开头
   - 变量名区分大小写

示例:
name = "Python"  # 字符串类型
age = 25         # 整数类型
price = 3.14     # 浮点数类型
is_valid = True  # 布尔类型

2. 变量命名规则
   - 只能包含字母、数字和下划线
   - 不能以数字开头
   - 不能使用Python关键字
   - 建议使用有意义的名称
   - 多个单词用下划线连接(snake_case)

3. 变量的特点
   - 动态类型：可以随时改变变量的类型
   - 引用机制：变量实际上是对象的引用
   - 垃圾回收：自动管理内存

4. 多重赋值
x, y = 1, 2      # 同时给多个变量赋值
a = b = c = 0    # 给多个变量赋相同的值
"""
