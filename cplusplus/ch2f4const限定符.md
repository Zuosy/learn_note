[TOC]

# const限定符

### 插曲

> const限定符修饰的类型真的不能被修改吗？(你就想当一条咸鱼吗？)

首先我萌要明确const对象声明定义之后必须要初始化。一种是运行时初始化，另一种是编译时初始化。

```cpp
const int i = get_size();	// 运行时初始化
const int j = 42;			// 编译时初始化
const int k;		// error: must initialize a const variable...
```

#### 运行时初始化

```cpp
int getsize()
{
    int temp;
    cout << "Input:";
    cin >> temp;
    return temp;
}

int main()
{
	const int i = getsize();

    int n = 1;
    int m = 2;
    m = n + i;

    cout << "const int i = " << i << endl;

    void *pointer = (void *) &i;
    cout << "*(int *) pointer = " << *(int *) pointer << endl;

    int *pi = (int *) pointer;
    *pi = 2345;
    cout << "*pi = " << *pi << endl;
    cout << "*&i = " << *&i << endl;

    cout << "address  i :" << &i << endl;
    cout << "address pi :" << pi << endl;

    cout << "const int i = " << i << endl;
    
    return 0;
}

```

运行结果：

```cpp
Input:1234
const int i = 1234
*(int *) pointer = 1234
*pi = 2345
*&i = 2345
address  i :0x7ffdf3d28214
address pi :0x7ffdf3d28214
const int i = 2345
```

> `const int i`在经过指针操作之后数据被修改了。说明常量经过指针强制转换是可以修改的

#### 编译时初始化

```cpp
int main(int, char **)
{
    const int i = 1234;
    cout << "const int i = " << i << endl;
    int *pi = (int *) &i;
    *pi = 2048;
    cout << "const int i = " << i << endl;
    cout << "*&i = " << *&i << endl;
    cout << "*pi = " << *pi << endl;

    cout << "*(int *) &i = " << *(int *) &i << endl;

    return 0;
}
```

运行结果：

```cpp
const int i = 1234
const int i = 1234
*&i = 1234
*pi = 2048
*(int *) &i = 2048
```

> 编译阶段初始化的const常量，在编译阶段凡是用到该常量(`i`)的地方都会被替代成**常量值**。即使像`*&i`这样的表达式也会被优化，但是！劳动人民的智慧是无穷的！`*(int *) &i`我看你怎么优化？
>
> 编译阶段被优化可通过看反汇编的代码得知。

------

#### 还有一种初始化

``` cpp
int i = 42;
const int ci = i;		// 编译时初始化
int j = ci;				// 编译时初始化
```

> 如果利用一个对象去初始化另外一个对象，则它们是不是const都无关紧要。

## 默认状态下，const对象仅在<u>文件内</u>有效

默认情况下，const对象被设定为仅在文件内有效。

如果你也和我一样有强迫症(非要在其他文件里用!)

解决的办法就是：

​		对于const变量不管是声明还是定义都添加extern关键字。

```cpp
// file_1.cc
extern const int bufSize = fun();
// file_1.h
extern const int bufSize;
```

> Note:如果想在多个文件之间共享const对象，必须在变量的定义之前添加extern关键字。

## const的引用

> 可以吧引用绑定到const对象上，就像绑定到其他对象上一样，我们称之为**对常量的引用**(reference to const)。

```cpp
const int ci = 1024;
const int &r1 = ci;
r1 = 42;		// error r1 is const
int &r2 = ci;	// error ci is const
```

### 初始化和对const的引用

在初始化常量引用时允许用任意表达式作为初始值，只要该表达式的结果能转换成引用的类型即可。尤其，允许为一个常量引用绑定<u>**非常量的对象**</u>、<u>**字面值**</u>，甚至是个<u>**一般表达式**</u>。

```cpp
int i = 42;
const int &r1 = i;
const int &r2 = 42;
const int &r3 = r1 * 2;
int &r4 = r1 * 2;		// error r4是一个普通的非常量引用
```

#### 临时变量的常量性

```cpp
double dval = 3.14;
const int &ri = dval;
```

实际上编译器把代码变成了如下格式:

```cpp
double dval = 3.14;
const int temp = dval;
const int &ri = temp;
```

#### 对const的引用可能引用一个并非const的对象

必须认识到，常量引用仅对引用可参与的操作做出了限定，对于引用的对象本身是不是一个常量未作限定。因为对象也可能是个非常量，所以允许通过其他途径改变它的值：

```cpp
int i = 42;
int &r1 = i;
const int &r2 - i;
r1 = 0;
r2 = 0;		// error r2是一个常量引用
```

## 指针和const

**指向常量的指针**(pointer to const)不能用于改变所指对象的值。要想存放常量对象的地址，只能使用指向常量的指针：

```cpp
const double pi = 3.14;
double *ptr = &pi;		// error pi是一个常量
const double *cptr = &pi;
*cptr = 42;				// cptr指向的对象是一个常量
```

> 指向常量的指针，没说指针是常量。

允许令一个指向常量的指针指向一个非常量对象：

```cpp
double dval = 3.14;
cptr = &dval;			// 而且cptr指针本身不是常量
```

和常量引用一样，指向常量的指针也没有规定其所指的对象必须是一个常量。所谓指向常量的指针仅仅要求不能通过该指针改变对象的值，而没有规定那个对象的值能不能通过其他途径改变。

>所谓指向常量的指针或引用，不过是指针或引用“自以为是”罢了，他们觉得自己指向了常量，所以自觉的不去改变所指对象的值。

### const指针

指针是对象而引用不是，因此就像其他对象类型一样，允许把指针本身定义为常量。**常量指针**(const pointer)必须初始化，而且一旦初始化完成，则它的值就不能再改变了。

把`*`放在`const`关键字之前用以说明指针是一个常量；指针本身是不变的，而非指向的对象。

```cpp
int errNumb = 0;
int *const curErr = &errNumb;		// curErr 是一个常量
const double pi = 3.14159;
const double *const pip = &pi;		// 常量的常量指针
```

## 顶层const
指针本身是不是常量以及指针所指的是不是一个常量是两个相互独立的问题。**顶层const**(top-level const)标志指针本身是一个常量；**底层const**(low-level const)表示指针所指的对象是一个常量。

```cpp
int i = 0;
int *const p1 = &i;		// top-level const
const int ci = 42;		// top-level const
const int *p2 = &ci;	// low-level const
const int *const p3 = p2;	// low-level const left; top-level const right
const int &r = ci;		// low-level const because of reference
```

当执行对象的拷贝操作时，常量是顶层const还是底层const区别明显。其中，顶层const不受什么影响。底层const的限制却不能忽视。

当执行对象的拷贝操作时，拷入和拷出的对象必须具有相同的底层const资格；或者两个对象的数据类型必须能够转换。一般来说，非常量可以转换成常量，反之则不行：

```cpp
int *p = p3;		// const int *const p3 = p2;
p2 = p3;
p2 = &i;
int &r = ci;		// const int ci = 42;
const int &r2 = i;
```

## constexpr和常量表达式

**常量表达式**(const expression)是指值不会改变并且在编译过程就能得到计算结果的表达式。

字面值属于常量表达式。C++语言中有集中情况下是要用到常量表达式的。

```cpp
const int max_files = 20;	// 是
const int limit = max_files + 1;	// 是
int staff_size = 27;		// 不是
const int sz = get_size();	// 不是
```

> 指针和constexpr的内容过于复杂在《C++ Primer》第59～60页。
>
> `constexpr`其实没啥太大用处。

------



```cpp
#include <iostream>

using namespace std;

int aConst()
{
    return 1024;
}

constexpr int aConstexpr()
{
    return 2048;
}

int main(int, char **)
{
    const int aNum = aConst();
    cout << aNum << endl;

    constexpr int anNumm = aConstexpr();
    cout << anNumm << endl;

    return 0;
}
```

> 对于上面的代码，`aConst`函数并不会编译时优化，而`aConstexpr`函数会在编译时尽可能的优化。换句话说17行是运行时初始化，20行是编译时初始化。20行更省时间和空间，`constexpr`还是有点用处的。

### 指针和constexpr

> Note(有点重要):在`constexpr`声明中如果定义了一个指针，限定符`constexpr`仅对指针有效，与指针所指的对象无关。



```cpp
const int *p = nullptr;		// 指向整数常量的指针
constexpr int *q = nullptr;	// 指向整数的常量指针
```

constexpr把它所定义的对象置为顶层const

尽管指针和引用都能定义成`constexpr`，但它们的初始值却收到严格限制。一个`constexpr`指针的初始值必须是`nullptr`或者`0`，或者是存储于某个固定地址中的对象。

存储于某个固定地址的对象：比如一个不在函数中声明定义的对象。

j 和i拥有代码段中的相对地址。

```cpp
#include <iostream>

using namespace std;

int j = 0;
constexpr int i = 42;

int main(int, char **)
{
    constexpr int *np = nullptr;
    constexpr const int *p = &i;
    constexpr int *p1 = &j;

    if (not np) {
        cout << "p = " << p << endl;
        cout << "*p = " << *p << endl;
        cout << "p1 = " << p1 << endl;
        cout << "*p1 = " << *p1 << endl;
    }

    return 0;
}
```

这么说静态变量也可以了。

```cpp
#include <iostream>

using namespace std;

void fun()
{
    static int counter = 0;
    ++counter;
    constexpr int *pointer = &counter;
    cout << "No. " << *pointer << " call fun()." << endl;
}

int main(int, char **)
{
    for (int i = 0; i < 5; ++i) {
        fun();
    }

    return 0;
}
```

```c
No. 1 call fun().
No. 2 call fun().
No. 3 call fun().
No. 4 call fun().
No. 5 call fun().
```

