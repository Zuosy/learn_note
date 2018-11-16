# 学习笔记

## 函数的组成

> 函数由**返回值**、**函数名**、**参数列表**和**函数体**四部分组成。

```cpp
// main.cpp
int main(int argc, char *argv[])
{
    return 0;
}
```

## 指针和引用的主要区别

指针“指向”内存中某个对象，而引用“绑定到”内存中的某个对象，他们都实现了对其他对象的间接访问，二者的区别主要有两方面：

第一，指针本身就是一个**对象**，允许对指针**赋值**和**拷贝**，而且在指针的生命周期内她可以指向几个不同的对象；引用**不是**一个对象，无法令引用重新绑定到另外一个对象。

第二，指针**无须**在定义时赋初值，和其他内置类型一样，在块作用域定义内的指针如果没有被初始化，也将拥有一个不确定的值；引用则**必须**在定义时赋初值。

## C++列表初始化

当用于内置类型的变量时，这种初始化形式有一个重要的特点：如果我们使用列表初始化且初始值存在**丢失信息**风险，则编译器将报错。

> 我的编译器(g++ (Ubuntu 4.8.5-4ubuntu8) 4.8.5)并没有报错，只是发出了警告；可以，使信息丢失是一个不好的习惯。

## 名字的作用域

```cpp
#include <iostream>
#include <string>

using namespace std;

int dog;

int main(int, char **)
{
    dog = 1234;
    string dog = "dog";
    {
        double dog = 1.234;
        cout << dog << endl;
        cout << ::dog << endl;
    }
    return 0;
}
```

运行结果

```txt
1.234
1234
```

## 指针的赋值

除了`const int *p = &i;`和`父类指针指向子类对象`之外,其他所有指针的类型都要和它所指向的对象**严格匹配**.

还有一种指针可以匹配任何类型--`void *`

## 指针的值

* 指向一个对象.
* 指向紧邻对对象所占空间的下一位置(++p)
* 空指针,意味着指针没有指向任何对象.
* 无效指针(野指针).

> 试图拷贝或以其他方式访问无效指针的值都将引发错误.编译器并不负责检查此类错误.这一点和试图始终未经初始化的变量是一样的.访问无效指针的后果无法预计,因此程序员必须清楚任意给定的指针是否有效.

## 理解复合类型的声明

变量的定义包括一个基本数据类型(base type)和一组声明符.

对于复合类型到底是什么,最简单的办法是**从右向左**阅读,离变量名*最近*的符号对变量的类型有最直接的影响.

### 指向指针的引用

```cpp
    // 引用绑定在指针上
    int i = 42;
    int *p = &i;
    int *&r = p;

    r = &i;
    *r = 0;
```

## 默认状态下,const对象仅在文件内有效

如果需要const常量在文件间共享:对于const变量不管是声明还是定义都添加extern关键字.

```cpp
// test.h
#ifndef TEST_H
#define TEST_H

extern const int bufsize;

void fun();

int fun2();

#endif // TEST_H
```

```cpp
// test.cpp
#include "test.h"
#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

extern const int bufsize = fun2();

void fun()
{
    cout << "&bufsize = " << &bufsize << endl;
}

int fun2()
{
    srand(time(nullptr));
    return random() % 100;
}
```

```cpp
// main.cpp
#include "test.h"
#include <iostream>

using namespace std;

int main(int, char **)
{
    fun();
    cout << bufsize << endl;
    cout << &bufsize << endl;
    return 0;
}
```

## 指针和const

> **指向常量的指针**(pointer to const) 不能用于改变其所指对象的值.要想存放常量对象的地址,只能使用指向常量的指针.

```cpp
    const double pi = 3.14;
    const double *ptr = &pi;
    *ptr = 42; // error
    double dval = 3.13;
    ptr = &dval;
```

> 指针是对象而引用不是,因此就像其他对象类型一样,允许把指针本身定义为常量.**常量指针**(const pointer)**必须**初始化.

```cpp
    int errNumb = 0;
    int *const curErr = &errNumb; // curErr将一直指向errNumb
    const double pi = 3.14159;
    const double *const pip = &pi; // pip是一个指向常量对象的常量指针
```

> 关于*const pointer* 和 *pointer to const*的写法和读法,记住从右向左的顺序阅读.

## 顶层const

> 指针本身是一个对象,他又可以指向另外一个对象.因此,指针本身是不是常量以及指针所指的是不是一个常量就是两个相互独立的问题.

* **顶层const**(top-level const) 表示指针本身是个常量.
* **底层const**(low-level const) 表示指针所指的对象是一个常量.
* **注:引用不是对象所以与常量绑定的引用都是底层const**.

```cpp
    int i = 0;
    int *const p1 = &i; // top
    const int ci = 42; // top
    const int *p2 = &ci; // low
    const int *const p3 = p2; // low top
    const int &r = ci; // low 第三种情况
```

当执行对象的拷贝操作时,常量是顶层const还是底层const区别明显.其中,顶层const不收什么影响.

```cpp
    i = ci; // 没毛病 不受影响,看到了没?
    p2 = p3; // p3 是顶层const
```