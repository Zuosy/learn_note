[TOC]

# 变量



## 含有无符号类型的表达式

> C++的一个大坑,非常非常坑

当一个算数表达式中基友无符号数又有int值时,那个int值就会转换成无符号数.

```cpp
	unsigned u = 10; // unsigned 等于 unsigned int
	int i = -42;
	cout << i + i << endl; // -84
	cout << u + i << endl; // 溢出 0XFF FF FF E0
```

**一定要注意**:切勿混用带符号类型和无符号类型



------

默认的浮点型字面值是一个double,默认的整数字面值是一个int、long、long long中尽可能小的。

当一行字符串太长了，写不下时。可以分开写。

```cpp
	std::cout << "a really, really long string literal "
				 "that spans two lines" << std::endl;
```

## 变量

变量定义的基本形式：首先是**类型说明符**(type specifier)，随后紧跟由一个或多个变量名组成的列表。其中变量名以逗号分隔，最后以分号结束。

------

**WARNING**：初始化不是赋值，初始化的含义是创建变量时赋予其一个初始值，而赋值的含义是把对象当前值擦除，而以一个新值来替代。

## 列表初始化

当用于内置类型的变量时，这种初始化形式有一个重要的特点：如果我们使用列表初始化切初始值存在信息丢失的风险，则编译器将**报错**。

> 在clang编译器中会报错，在g++编译器中会警告。



------

## 变量声明和定义的关系

**声明**使得名字为程序所知，一个文件如果想使用别处定义的名字则必须包含对那个名字的声明。而**定义**负责创建与名字关联的*实体*。

```cpp
extern int i; // 声明
int j; // 定义
```

> Note：变量能且只能被定义一次，但是可以被多次声明。



## 标识符

> 由字母、数字和下划线组成，其中必须以字母或下划线开头。长度没有限制，大小写敏感。



## 名字的作用域

```cpp
#include <iostream>

using namespace std;

int main(int, char **)
{
    int sum = 0;
    // sum 用于存放从1到10所有数的和
    for (int val = 1; val <= 10; ++val)
        sum += val;
    cout << "Sum of 1 to 10 inclusive is "
         << sum << endl;
    return 0;
}
```

函数(例如`main`)拥有**全局作用域**(global scope)，sum叫做**块作用域**(block scope)

### 嵌套的作用域

```cpp
#include <iostream>

using namespace std;

int reused = 42;
int main()
{
    int unique = 0;
    cout << reused << " " << unique << endl;
    int reused = 0;
    cout << reused << " " << unique << endl;
    cout << ::reused << " " << unique << endl;
    return 0;
}
```

运行结果：

```cpp
42 0
0 0
42 0
```

