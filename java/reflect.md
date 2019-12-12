# Java反射笔记

[TOC]

## 反射能得到什么

首先你要学会`get class`

对于对象

```java
Student stu = new Student();
Class clazz = stu.getClass();
```

对于类

```java
Class clazz = Student.class;
```

对于基本类型

```java
Class clazz = int.class;
```

### 类名

* getName

```java
Class clazz = String.class;
String className = clazz.getName();
System.out.println(className);
```

输出结果：`java.lang.String`

* getSimpleName

```
Class clazz = String.class;
String className = clazz.getSimpleName();
System.out.println(className);
```

输出结果：`String`

### 访问修饰符

```java
Class clazz = String.class;
int mod = clazz.getModifiers();
System.out.println(Modifier.isPublic(mod));
System.out.println(Modifier.isFinal(mod));
System.out.println(Modifier.toString(mod));
```

输出结果：

`true
true
public final`

### 包信息

```java
Class clazz = String.class;
Package $package = clazz.getPackage();
System.out.println($package.getName());
System.out.println($package.toString());
```

输出结果：

`java.lang
package java.lang, Java Platform API Specification, version 1.8`

### 父类

获取直接的父类，不能获取爷爷类。

```java
Class clazz = ArrayList.class;
Class superClass = clazz.getSuperclass();
System.out.println(superClass.getName());
System.out.println(superClass.getSimpleName());
```

输出结果：

`java.util.AbstractList
AbstractList`

### 接口

获取类实现的接口们，因为接口可以多实现

```java
Class clazz = String.class;
Class[] interfaces = clazz.getInterfaces();
System.out.println("length :" + interfaces.length);
for (Class face : interfaces) {
	System.out.println(face.getName());
}
```

输出结果：

`length :3
java.io.Serializable
java.lang.Comparable
java.lang.CharSequence`

### 构造器（构造函数）

* getConstructors 获取能够看到的构造器

```java
Class clazz = String.class;
Constructor[] constructors = clazz.getConstructors();
System.out.println("length :" + constructors.length);
for (Constructor cons : constructors) {
	System.out.println(cons.toString());
}
```

输出结果：

`length :15
public java.lang.String(byte[],int,int)
public java.lang.String(byte[],java.nio.charset.Charset)
public java.lang.String(byte[],java.lang.String) throws java.io.UnsupportedEncodingException
public java.lang.String(byte[],int,int,java.nio.charset.Charset)
public java.lang.String(byte[],int,int,java.lang.String) throws java.io.UnsupportedEncodingException
public java.lang.String(java.lang.StringBuilder)
public java.lang.String(java.lang.StringBuffer)
public java.lang.String(byte[])
public java.lang.String(int[],int,int)
public java.lang.String()
public java.lang.String(char[])
public java.lang.String(java.lang.String)
public java.lang.String(char[],int,int)
public java.lang.String(byte[],int)
public java.lang.String(byte[],int,int,int)`

* getDeclaredConstructors 获取类声明的构造函数
```java
Class clazz = String.class;Constructor[] constructors = clazz.getDeclaredConstructors();System.out.println("length :" + constructors.length);for (Constructor cons : constructors) {    System.out.println(cons.toString());}
```

输出结果：

`length :16
public java.lang.String(byte[],int,int)
public java.lang.String(byte[],java.nio.charset.Charset)
public java.lang.String(byte[],java.lang.String) throws java.io.UnsupportedEncodingException
public java.lang.String(byte[],int,int,java.nio.charset.Charset)
public java.lang.String(byte[],int,int,java.lang.String) throws java.io.UnsupportedEncodingException
java.lang.String(char[],boolean)
public java.lang.String(java.lang.StringBuilder)
public java.lang.String(java.lang.StringBuffer)
public java.lang.String(byte[])
public java.lang.String(int[],int,int)
public java.lang.String()
public java.lang.String(char[])
public java.lang.String(java.lang.String)
public java.lang.String(char[],int,int)
public java.lang.String(byte[],int)
public java.lang.String(byte[],int,int,int)`

### 方法

```java
Class clazz = String.class;
Method[] methods = clazz.getMethods();
System.out.println("length :" + methods.length);
```

输出结果：

`length :76`

太多了，就打印一下大小。。。

### 域（成员变量）

```java
Class clazz = String.class;
Field[] fields = clazz.getFields();
System.out.println(fields.length);
for (Field field : fields) {
	System.out.println(field.toString());
}
```

输出结果：

`1
public static final java.util.Comparator java.lang.String.CASE_INSENSITIVE_ORDER`

### 注解

```java
Class clazz = Override.class;
Annotation[] annotations = clazz.getAnnotations();
System.out.println(annotations.length);
```

输出结果：

`2`

确实在类声明注解的没有几个，所以只好那注解了。

## 总结

我们可以获得类的九大信息：

类名、包名、访问修饰符、父类、接口、构造函数、 方法、属性、注解。