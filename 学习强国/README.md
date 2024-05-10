# <img src="C:\Users\Dai\AppData\Roaming\Typora\typora-user-images\image-20240510230839336.png" alt="image-20240510230839336" style="zoom: 67%;" />学习强国刷积分脚本

学习强国的**阅读**与**视听**每天需要达到**12分**，其中6分算浏览时长，6分算有效浏览，这里使用`DrissionPage`来自动化打开学习强国**web**端来实现自动化过程



由于web端无法进行其它获取积分操作，所以这里就对阅读和视听进行了自动化

![image-20240510224718873](C:\Users\Dai\AppData\Roaming\Typora\typora-user-images\image-20240510224718873.png)

每日答题部分由于bug很多，耗时也不长，所以从脚本中进行了删除此功能。



## <img src="C:\Users\Dai\AppData\Roaming\Typora\typora-user-images\image-20240510230815769.png" alt="image-20240510230815769" style="zoom:50%;" />阅读

**阅读部分我选择浏览八篇文章，每篇文章停留65秒。**

由于学习强国web端没有频道界面，所以这里只从主页选择文章。主页的文章可能会由于更新快慢等原因，可能偶尔会遇到浏览过的文章(不会计算在有效浏览内)，如果追求12分全拿的,最后还是需要自信检查一下。



## <img src="C:\Users\Dai\AppData\Roaming\Typora\typora-user-images\image-20240510230748326.png" alt="image-20240510230748326" style="zoom:50%;" />**视听**

**视听选择看20篇，每篇看20秒。**

至于为什么选择这么多篇，其实我也不想。视听里面许多只有十几秒的内容，如果每篇停留时间过长则会造成很大的时间损失，积分也无法确保，所以采取量变带动质变的方法

![image-20240510225027238](C:\Users\Dai\AppData\Roaming\Typora\typora-user-images\image-20240510225027238.png)



## <img src="C:\Users\Dai\AppData\Roaming\Typora\typora-user-images\image-20240510230655192.png" alt="image-20240510230655192" style="zoom:50%;" />可能遇到的问题

#### 没有可选择的浏览器驱动

因为我选择的是谷歌浏览器，可能有部分人没有安装，这里我就不详细阐述了，直接给[官方解决方法](https://www.drissionpage.cn/get_start/before_start)

大家在我给的脚本指令里面进行修改即可



# 📆计划

后续将会不断维护改进，本人水平有限，尽力而为，有更好的建议大家也可以指出来，共同进步😘。

开源项目的推进有赖你的支持。欢迎投喂加速。

<img src="C:\Users\Dai\Documents\WeChat Files\wxid_ii3r5auxmexh22\FileStorage\Temp\faf375bdf48026cfbfdb1f809571bb3.jpg" alt="faf375bdf48026cfbfdb1f809571bb3" style="zoom:60%;" /><img src="C:\Users\Dai\Documents\WeChat Files\wxid_ii3r5auxmexh22\FileStorage\Temp\fe19f4534f33308a3bf65f18a743356.jpg" alt="fe19f4534f33308a3bf65f18a743356" style="zoom:52%;" />