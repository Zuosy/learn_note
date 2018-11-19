# How To Install Oh-my-zsh

## install zsh

    sudo apt-get install zsh

## change shell to zsh

    chsh -s /bin/zsh

Then relog.

## install oh-my-zsh

可以在他们的github上看到README里面,正确的安装方式

    sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

## install zsh-autosuggestions

    get clone git://github.com/zsh-users/zsh-autosuggestions

## install zsh-syntax-highlighting

    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git

## install autojump

    sudo apt-get install autojump
    oh-my-zsh里面添加autojump插件
    根据`/usr/share/doc/autojump/README.Debian`抄到`.zshrc`中
    再加上一句`unsetopt BG_NICE` (in WSL)

## 剩下的自己配置吧
