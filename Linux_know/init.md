# 关于启动服务

## 关闭apache服务器的自动启动

    sudo update-rc.d apache2 disable 2
    update-rc.d <basename> disable|enable [S|2|3|4|5]

And then, reboot the Ubuntu.
在`/etc/rc2.d`中查看,S开头的是启动的服务,D开都的是关闭的服务.