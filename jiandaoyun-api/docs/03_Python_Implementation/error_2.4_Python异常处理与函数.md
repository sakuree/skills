# 2.4 Python异常处理与函数

URL: https://hc.jiandaoyun.com/open/12051

![](https://help-assets.jiandaoyun.com/upload/h2DN2XcfoG0l)

**本节主题：** 2.4 Python 异常处理与函数

**课程讲师：** Yunlin

**观看地址：**[点我进入](https://edu.fanruan.com/video/181)

## 1 本节要点

* 了解 Python 中异常处理的概念
* 重点掌握 Python 中函数的概念、用法

## 2 课前准备

### 2.1 检查pip命令

在 cmd 输入 pip 或终端中输入 pip 或 pip3 ，会输出 pip 的使用方法

![](https://help-assets.jiandaoyun.com/upload/1qSnS8EM6RAi)

## 3 课程ne

### 3.1 异常处理

#### 3.1.1 程序常见的错误

什么是异常？

* 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
* 一般情况下，在 Python 无法正常处理程序时就会发生一个异常。
* 异常是 Python 对象，表示一个错误。
* 当 Python 脚本发生异常时我们需要捕获处理它，否则程序会终止执行。

|  |  |
| --- | --- |
| **异常名称** | **描述** |
| BaseException | 所有异常的基类 |
| SystemExit | 解释器请求退出 |
| KeyboardInterrupt | 用户中断执行(通常是输入^C) |
| Exception | 常规错误的基类 |
| StopIteration | 迭代器没有更多的值 |
| GeneratorExit | 生成器(generator)发生异常来通知退出 |
| StandardError | 所有的内建标准异常的基类 |
| ArithmeticError | 所有数值计算错误的基类 |
| FloatingPointError | 浮点计算错误 |
| OverflowError | 数值运算超出最大限制 |
| ZeroDivisionError | 除(或取模)零 (所有数据类型) |
| AssertionError | 断言语句失败 |
| AttributeError | 对象没有这个属性 |
| EOFError | 没有内建输入,到达 EOF 标记 |
| EnvironmentError | 操作系统错误的基类 |
| IOError | 输入/输出操作失败 |
| OSError | 操作系统错误 |
| WindowsError | 系统调用失败 |
| ImportError | 导入模块/对象失败 |
| LookupError | 无效数据查询的基类 |
| IndexError | 序列中没有此索引(index) |
| KeyError | 映射中没有这个键 |
| MemoryError | 内存溢出错误(对于Python 解释器不是致命的) |
| NameError | 未声明/初始化对象 (没有属性) |
| UnboundLocalError | 访问未初始化的本地变量 |
| ReferenceError | 弱引用(Weak reference)试图访问已经垃圾回收了的对象 |
| RuntimeError | 一般的运行时错误 |
| NotImplementedError | 尚未实现的方法 |
| SyntaxError | Python 语法错误 |
| IndentationError | 缩进错误 |
| TabError | Tab 和空格混用 |
| SystemError | 一般的解释器系统错误 |
| TypeError | 对类型无效的操作 |
| ValueError | 传入无效的参数 |
| UnicodeError | Unicode 相关的错误 |
| UnicodeDecodeError | Unicode 解码时的错误 |
| UnicodeEncodeError | Unicode 编码时错误 |
| UnicodeTranslateError | Unicode 转换时错误 |
| Warning | 警告的基类 |
| DeprecationWarning | 关于被弃用的特征的警告 |
| FutureWarning | 关于构造将来语义会有改变的警告 |
| OverflowWarning | 旧的关于自动提升为长整型(long)的警告 |
| PendingDeprecationWarning | 关于特性将会被废弃的警告 |
| RuntimeWarning | 可疑的运行时行为(runtime behavior)的警告 |
| SyntaxWarning | 可疑的语法的警告 |
| UserWarning | 用户代码生成的警告 |

#### 3.1.2 如何判断和捕捉异常

捕捉异常可以使用 try/except 语句。

try/except 语句用来检测 try 语句块中的错误，从而让 except 语句捕获异常信息并处理。 如果你不想在异常发生时结束你的程序，只需在 try 里捕获它。

**以下为简单的 try…except…else 的语法：**

```
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生
```

* try 的工作原理是，当开始一个 try 语句后，python 就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try 子句先执行，接下来会发生什么依赖于执行时是否出现异常。
* 如果当 try 后的语句执行时发生异常，python 就跳回到 try 并执行第一个匹配该异常的 except 子句，异常处理完毕，控制流就通过整个 try 语句（除非在处理异常时又引发新的异常）。
* 如果在 try 后的语句里发生了异常，却没有匹配的 except 子句，异常将被递交到上层的 try，或者到程序的最上层（这样将结束程序，并打印默认的出错信息）。
* 如果在 try 子句执行时没有发生异常，python 将执行 else 语句后的语句（如果有 else 的话），然后控制流通过整个 try 语句。

下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，且并未发生异常：

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()
```

下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，但文件没有写入权限，发生了异常：

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print ("内容写入文件成功")
    fh.close()
```

### 3.2 函数

#### 3.2.1 函数的概念

* 你可以定义一个由自己想要功能的函数，以下是简单的规则：
* 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**；
* 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数；
* 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明；
* 函数内容以冒号起始，并且缩进；
* **return [表达式]**结束函数，选择性地返回一个值给调用方。不带表达式的 return 相当于返回 None。

### 3.3 构建一个函数

在 Python 中，定义一个函数要使用 def 语句：

```
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
```

函数可以返回多个值吗？

```
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
```

### 3.4 形参与实参

username 就是一个形参，小明是我在调用函数时传入的一个实参，它的值被存储在形参 username 中：

![](https://help-assets.jiandaoyun.com/upload/OJavHNhfIkcO)

### 3.5 局部变量与全局变量

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2 # total在这里是局部变量.
   print ("函数内是局部变量 : ", total)
   return total
#调用sum函数
sum( 10, 20 )
print("函数外是全局变量 : ", total)
```

在函数中声明变量为全局变量：

```
#在函数里定义全局变量
a=0
def plus_a():
  global a
  a +=1
```

### 3.6 关键词参数、默认参数、收集参数

#### 3.6.1 位置参数

我们先写一个计算 x^2 的函数：

```
def power(x):
    return x * x
```

对于 power(x) 函数，参数x就是一个位置参数。 当我们调用 power 函数时，必须传入有且仅有的一个参数x：

```
>>> power(5)
25
>>> power(15)
225
```

现在，如果我们要计算 x3 怎么办？可以再定义一个 power3 函数，但是如果要计算 x4、x5…… 怎么办？我们不可能定义无限多个函数。 你也许想到了，可以把 power(x) 修改为 power(x, n)，用来计算 xn：

```
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

对于这个修改后的 power(x, n) 函数，可以计算任意 n 次方：

```
>>> power(5, 2)
25
>>> power(5, 3)
125
```

修改后的 power(x, n) 函数有两个参数：x 和 n，这两个参数都是位置参数，调用函数时，传入的两个值按照位置顺序依次赋给参数 x 和 n。

#### 3.6.2 默认参数

新的 power(x, n) 函数定义没有问题，但是，旧的调用代码失败了，原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：

```
>>> power(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: power() missing 1 required positional argument: 'n'
```

Python 的错误信息很明确：调用函数 power() 缺少了一个位置参数 n。 这个时候，默认参数就排上用场了。由于我们经常计算 x2，所以，完全可以把第二个参数 n 的默认值设定为 2：

```
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

这样，当我们调用 power(5) 时，相当于调用 power(5, 2)：

```
>>> power(5)
25
>>> power(5, 2)
25
```

而对于 n > 2 的其他情况，就必须明确地传入 n，比如 power(5, 3)。

从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

* 一是必选参数在前，默认参数在后，否则 Python 的解释器会报
* 二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度。

#### 3.6.3 可变参数

在 Python 函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是 1 个、2 个到任意个，还可以是 0 个。

我们以数学题为例子，给定一组数字 a，b，c……，请计算 a2 + b2 + c2 + ……。

要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把 a，b，c…… 作为一个 list 或 tuple 传进来，这样，函数可以定义如下：

```
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

但是调用的时候，需要先组装出一个 list 或 tuple：

```
>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
```

所以，我们把函数的参数改为可变参数：

```
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

定义可变参数和定义一个 list 或 tuple 参数相比，仅仅在参数前面加了一个 \* 号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括 0 个参数：

```
>>> calc(1, 2)
5
>>> calc()
0
```

如果已经有一个 list 或者 tuple，要调用一个可变参数怎么办？可以这样做：

```
>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])
14
```

这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个\*号，把list或tuple的元素变成可变参数传进去：

```
>>> nums = [1, 2, 3]
>>> calc(*nums)
14
```

注：nums 表示把 nums 这个 list 的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。

#### 3.6.4 关键字参数

可变参数允许你传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple。而关键字参数允许你传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：

```
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

函数 person 除了必选参数 name 和 age 外，还接受关键字参数 kw。在调用该函数时，可以只传入必选参数：

```
>>> person('Michael', 30)
name: Michael age: 30 other: {}
也可以传入任意个数的关键字参数：
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

关键字参数有什么用？它可以扩展函数的功能。比如，在 person 函数里，我们保证能接收到 name 和 age 这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

和可变参数类似，也可以先组装出一个 dict，然后，把该 dict 转换为关键字参数传进去：

```
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

当然，上面复杂的调用可以用简化的写法：

```
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra)
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

extra 表示把该变量的所有 key-value 用关键字参数传入到函数的 kw 参数，kw 将获得一个 dict，注意 kw 获得的 dict 是extra 的一份拷贝，对 kw 的改动不会影响到函数外的 extra。