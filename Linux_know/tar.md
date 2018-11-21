# 关于一些打包和解压的命令

## tar

### 打包

    tar -cvf XXXX.tar XXXX

### 解包

    tar -xvf XXXX.tar

## gzip

gzip只能压缩文件

### 压缩

    gzip -kv XXX.tar

### 解压

    gunzip -kv XXX.tar.gz