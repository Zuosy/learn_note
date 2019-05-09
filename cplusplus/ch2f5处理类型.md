[TOC]

# 处理类型

## 类型别名

### typedef

```cpp
typedef double wages;	// wages是double的同义词
typedef wages base, *p;	// base是double的同义词，p是double *的同义词
```

关键字`typedef`作为声明语句中的<u>基本数据类型的一部分</u>出现。含有`typedef`的声明语句定义的不再是变量而是类型别名。和以前的声明语句一样，这里的声明符也可以包含类型修饰，从而也能由基本数据类型构造出复合类型来。

### using

新标准规定了一种新的方法，使用**别名声明**(alias declaration)来定义类型的别名:

```cpp
using SI = Sales_item;
```

### 指针、常量和类型别名 XX

如果某个类型别名代指的是复合类型或常量，那么把它用到声明语句里就会产生意想不到的后果。

```cpp
typedef char *pstring;
const pstring cstr = 0;		// const pstring AKA 'char *const'
const pstring *ps;
```

> 人类终究是需要经验积累的生物。

`const`修饰的是`pstring`，`pstring`的本质是一个指针，所以`const`修饰的是指针。

```cpp
#include <iostream>

using namespace std;

int main(int, char **)
{
    typedef int *pInt;

    int number = 1024;
    const pInt p1 = &number;    // int *const
    const pInt *pp2 = &p1;      // int *const *

    cout << "number = " << number << '\n';
    cout << "&number = " << &number << '\n';

    cout << "p1 = " << p1 << '\n';
    cout << "*p1 = " << *p1 << '\n';
    cout << "*pp2 = " << *pp2 << '\n';
    cout << "**pp2 = " << **pp2 << '\n';
    cout << flush;

    int *const _ = &number;
    int *const *__ = &_;

    cout << "_ = " << _ << '\n';
    cout << "*_ = " << *_ << '\n';
    cout << "*__ = " << *__ << '\n';
    cout << "**__ = " << **__ << '\n';
    cout << flush;


    return 0;
}
```

运行结果：

```cpp
number = 1024
&number = 0x7fff008787dc
p1 = 0x7fff008787dc
*p1 = 1024
*pp2 = 0x7fff008787dc
**pp2 = 1024
_ = 0x7fff008787dc
*_ = 1024
*__ = 0x7fff008787dc
**__ = 1024
```

------

后面对于`auto`和`decltype`的介绍就不在这里记录了，因为C++之父说过，~~要用魔法打败魔法~~要轻松的使用这门语言。我又不是写游戏的神仙，所以我选择复习这一部分。

---



C++11新特性，可以为数据成员提供一个**类内初始值**

```cpp
#include <iostream>

using namespace std;

struct Student {
    string name = "Tom";
    int age = 14;
};

int main(int, char **)
{
    Student tom;
    cout << "Name :[" << tom.name << "]\n";
    cout << "Age :[" << tom.age << "]\n";
    cout << flush;

    return 0;
}
```

