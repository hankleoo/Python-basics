#！/usr/bin/env python
# Author:Hank
'''
网络编程：

什么是网络编程？

网络：它是一种隐形的媒介；可以将多台计算机使用(将它们连接到一起)

网络编程：将多台计算机之间可以相互通信了(做数据交互)

一旦涉及到网络编程，划分为两个方向存在，一方我们称为客户端(cilent)，一方我们称为服务端(server)

冲浪概念(上网)，打开浏览器举例：访问百度页面

我们可以认为是浏览器的进程和百度服务器之间进行数据交互

IP：

IP地址的作用：

如果我们需要上网，每台计算机都需要有一个唯一的识别号(标识)，就需要用到ip的概念

【注意事项】：

ip地址是每台计算机在网络中的唯一识别(切记)

但是在最初人们是考虑到使用主机名(计算机名称)来查找在网络中直接对应的计算机；

可以多态计算机之间可能存在主机名重复的现象，伴随着完全隐患；

所以我们就舍弃了使用主机名作为计算机的识别，改而使用ip；

如何查看ip(有两种方式)：

1).通过控制台 --> 启动cmd，输入ipconfig指令

2).打开网络共享 --> 选择更改适配器设置，选择属性，点击ipv4(双击操作)，可以看到ip的信息

对于ip的获取有两种方式：

1).自动获取ip地址

2).手动获取ip地址

ip地址由4个网段组成：

其本质为：

4个字节的二进制数据的组合

二进制数据：10110101110101001000111110101001

十进制数据：数据1数据2数据3数据4

对于每个网段的数据设置有相应的要求：必须是0~255之间

由于每个网段数字都是由1个字节翻译得到的十进制数据，所以最大数值只能为255

以下内容作为尝试需要知道：

1).ping指令：

2).127.0.0.1：本机回环地址(解析为本机的ip)，理解：相当于localhost

3).xxx.xxx.xxx.255：广播地址

端口：

一台计算机可能装有很多的应用程序，如果我们需要去实现网络编程，

那么两台计算机之间程序的数据交互需要通过端口号来找到需要的那款程序

总结：端口号可以理解为电脑中的程序(软件)的唯一标识

范围：0~65535之间

【注意】：0~1024之间的端口我们不能直接使用，因为它们被常用的一些服务所占用了

常见的一些端口号如下：

http：80

ftp：21

smtp：25

1024~65535之间的端口：

mysql：3306

redis：6379

网络编程：

分类：

osi参考模型：(七层)

tcp/ip参考模型：(四层)

python六十七课——网络编程（基础知识了解）
只要理解传输层的作用，确定使用到底是tcp还是udp协议(规则)，进行数据传输

socket(套接字)：

python将网络编程观想的函数都封装到了socket模块中，我们只需要导入socket即可使用

代码核心：

不管是client还是server，获取/得到socket对象才是关键，然后可以调用send或者recv等函数实现操作

'''