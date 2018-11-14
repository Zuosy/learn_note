# cmake的Hello World

## 没有引言

### 先编写一个`main.c`文件

```c
// main.c
#include <stdio.h>
int main()
{
    printf("Hello World from t1 Main!\n");
    return 0;
}
```

### 然后创建一个`CMakeLists.txt`文件,写入如下内容

```c
PROJECT (HELLO)
SET (SRC_LIST main.c)
MESSAGE(STATUS "This is BINARY dir " ${HELLO_BINARY_DIR})
MESSAGE(STATUS "This is SOURCE dir " ${HELLO_SOURCE_DIR})
ADD_EXECUTABLE(hello ${SRC_LIST})
```

### 运行如下命令

> `cmake .`

```txt
-- The C compiler identification is GNU 4.8.5
-- The CXX compiler identification is GNU 4.8.5
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- This is BINARY dir /home/zuoshiyu/workspace/cmake/t1
-- This is SOURCE dir /home/zuoshiyu/workspace/cmake/t1
-- Configuring done
-- Generating done
-- Build files have been written to: /home/zuoshiyu/workspace/cmake/t1
```

> `make`

```txt
[ 50%] Building C object CMakeFiles/hello.dir/main.c.o
[100%] Linking C executable hello
[100%] Built target hello
```

### 最后目录下会生成这些

```txt
-rw-r--r-- 1 zuoshiyu zuoshiyu  13K 9月  28 10:36 CMakeCache.txt
drwxr-xr-x 5 zuoshiyu zuoshiyu 4.0K 9月  28 10:36 CMakeFiles
-rw-r--r-- 1 zuoshiyu zuoshiyu 1.5K 9月  28 10:36 cmake_install.cmake
-rw-r--r-- 1 zuoshiyu zuoshiyu  188 9月  28 10:23 CMakeLists.txt
-rwxr-xr-x 1 zuoshiyu zuoshiyu 8.2K 9月  28 10:36 hello
-rw-r--r-- 1 zuoshiyu zuoshiyu  103 9月  28 10:20 main.c
-rw-r--r-- 1 zuoshiyu zuoshiyu 4.7K 9月  28 10:36 Makefile
```

### 运行可执行文件`hello`

> `./hello`

就会输出:

```txt
Hello World from t1 Main!
```

___

## 简单的解释

**CMakeLists.txt**
这个文件是`cmake`的构建定义文件,文件名是大小写相关的.如果工程存在过个目录,需要确保每个要管理的目录都存在一个`CMakeLists.txt`(好惨啊,每个目录都要写).

**PROJECT**
    PROJECT(projectname [CXX] [C] [Java])

这个命令用于定义工程名称,并可指定工程支持的语言,支持的语言列表是可以忽略的,默认情况表示支持所有语言.
这个命令隐式定义了两个cmake变量

    <projectname>_BINARY_DIR && <projectname>_SOURCE_DIR

>在这里就是`HELLO_BINARY_DIR`和`HELLO_SOURCE_DIR`,当然两者可以指定不同.

同时cmake系统也帮助我们预定义了`PROJECT_BINARY_DIR`和`PROJECT_SOURCE_DIR`变量.他们的值分别与`HELLO_BINARY_DIR`与`HELLO_SOURCE_DIR`一致.
为了统一起见,可以直接使用`PROJECT_BINARY_DIR`和`PROJECT_SOURCE_DIR`.

**SET指令的语法**
    SET (VAR [VALUE] [CACHE TYPE DOSSTRING [FORCE]])

现阶段,只需要了解`SET`指令可以用于显式定义变量.
比如`SET (SRC_LIST main.c)`如果有多个源文件,可以定义成:`SET (SRC_LIST main.c t1.c t2.c)`.

**MESSAGE**
    MESSAGE ([SEND_ERROR | STATUS | FATAL_ERROR] "message to display" ...)

这个指令用于向终端输出用户定义的信息,包含了三种类型.

* SEND_ERROR: 产生错误,生成过程被跳过.
* STATUS: 输出前缀位`--`的信息.
* FATAL_ERROR:立即终止所有cmake过程.

**ADD_EXECUTABLE**
    ADD_EXECUTABLE(hello ${SRC_LIST})

定义了这个工程会生成一个文件名为hello的可执行文件,相关的源文件是SRC_LIST中定义的源文件列表,本例中也可以写成
`ADD_EXECUTABLE(hello main.c)`.

>`${}`这是cmake的,但是在**IF**控制语句中除外,
>在IF控制语句中,变量是直接使用变量名引用,不需要`${}`,
>如果使用了`${}`去引用变量,其实IF会去找名为`${var_name}`的变量(怎么可能会存在呢?)


## 基本语法规则

1. 变量使用`${}`方式取值,但是在IF控制语句中是直接使用变量名
2. 指令(参数1 参数2)   参数使用括弧括起,参数之间使用空格或分好分开.
3. 指令是大小写无关的, 参数和 变量是大小写相关的,但是推荐全部使用大写指令.

>以上面的ADD_EXECUTABLE为例,如果存在另外一个`func.c`文件,就可以写成:
>ADD_EXECUTABLE(hello main.c func.c) or ADD_EXECUTABLE(hello main.c;func.c)
>>这里需要特别解释的是PROJECT_NAME `HELLO` 和 生成的可执行文件`Hello`是没有任何关系的.

## 关于语法的疑惑

cmake的语法还是比较灵活而且考虑到各种情况, 比如:
`SET (SRC_LIST main.c)`也可以写成`SET (SRC_LIST "main.c")`这是没有区别的.
但是如果有一个源文件名字是`fu k.c`(文件名里面有空格)
这种情况下就必须使用双引号,`SET (SRC_LIST "fu k.c")`

## 清理工程

`make clean`即可对构建结果进行清理.

## 啥?啥?啥?的

有人会尝试运行`make distclean`清理构建过程中产生的中间文件.
但是cmake并不支持`make distclean`,官方解释是:
    因为CMakeLists.txt可以执行脚本并通过脚本生成一些临时文件,但是却没有办法来跟踪这些临时文件到底是哪些.
    因此,没有办法提供一个可靠的`make distclean`方案.

同时,cmake强烈推荐使用外部构建(out-of-source build).

## 内部构建与外部构建

上面的例子就是内部编译,它会生成一些无法自动删除的中间文件

接下来的操作将会把前面的`内部构建`变成`外部构建`:

1. 首先,清楚目录中除`main.c`,`CMakeLists.txt`之外的所有中间文件.(关键是CMakeCache.txt)
2. 在目录下建立一个`build`目录,当然这个可以建立在任何地方,甚至工程之外.
3. 进入`build`目录,运行`cmake ..`(其实就是`cmake <工程的路径>`,路径可以是相对的,也可以使绝对的.)
4. 运行`make`构建工程,就会在当前目录(build目录)中获取目标文件`hello`.

*out-of-source*外部编译,一个最大的好处就是,对于原有工程没有任何影响,
