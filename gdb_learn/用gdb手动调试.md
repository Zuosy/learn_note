[TOC]

# 用gdb手动调试

## 准备

* eng版本的Ｒｅｌｅａｓｅ

* arm-linux-gdb
* 会使用ｇｄｂ

### arm-linux-gdb编译

> 注意版本

[参考](https://blog.csdn.net/kangear/article/details/8635029)

## 调试

### 编译

`make voicerecog-navi-test -j8`

带有ｇｄｂ调试信息的版本在`out/target/product/taurusavn/obj/cmake/bin`下面

把`voicerecog-navi-test`push到机器中。

`adb push voicerecog-navi-test /vdata`

### 启动ｇｄｂｓｅｒｖｅｒ

在车机上面启动ｇｄｂｓｅｒｖｅｒ

`gdbserver :4399 /vdata/voicerecog-navi-test`

### adb forward

`adb forward tcp:4399 tcp:4399`

## gdb

在ＰＣ上运行`arm-linux-gdb`

`target remote :4399`

`symbol-file /home/zuoshiyu/workspace/srcCode/530B/out/target/product/taurusavn/obj/cmake/bin/voicerecog-navi-test`

`continue`



好了。