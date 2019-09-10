### Introduction:
计算/校验文件哈希值，支持 md5, sha1, sha256


### Required:
- python3
- click


### How to Use 1：
\<python可执行文件路径> \<此文件路径>


### How to Use 2：
alias 一个命令(.bashrc, .zshrc, .bash_profile...)

格式为：alias \<command> \<python可执行文件路径> \<此文件路径>

之后就可以在终端里使用 \<command> 去使用此脚本


### Options：
--help 查看帮助信息

-f, --file \<TEXT>   需要校验的文件路径

-m, --mode \<TEXT>   校验模式 [1:md5, 2:sha1, 3:sha256]，默认为 **md5**

-v, --value \<TEXT>  原始文件的校验值。如果不使用此参数会只计算哈希值。
