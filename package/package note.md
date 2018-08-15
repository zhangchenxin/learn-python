#模块

- 一个模块就是一个包含Python代码的文件,就是一个Python文件
- 为什么要使用模块
   - 程序太大,编写维护非常不方便,需要拆分
   - 模块可以增加代码重复利用的方式
   - 当做命名空间使用,避免命名冲突
- 如何定义模块
   - 模块就是一个普通文件,所以任何代码都可以直接使用
   - 不过根据模块的规范,最好在模块中编写以下内容
      - 函数(单一功能)
      - 类 (相似的功能的组合, 或者有类似业务的模块)
      - 测试代码
      
- 如何使用模块
   - 模块可以直接导入 
      - 加入模块可以使用数字,但必须导入一个模块importlib.否则出错
   - 语法
   
         
         import module_name
         module_name.function_name
         moudul_name.class_name
   - import 模块 as 别名
      - 导入用法和以上相同
      - 但是在使用时,要使用别名而不是模块名
   - from module_name import func_name, class_name 案例在p03
      - 将模块中部分内容导入
      - 不用使用前缀
   - from moudle_name import *           
       - 意思为将模块中的所有全部导入
       - 优点是可以在以后的使用中不用去加前缀
       - 缺点是在使用时可能会造成名称污染
- if __name__ == '__main__' 的使用
   - 可以有效的避免模块被导入的时候被动执行的问题
   - 建议所有的程序入口都以此代码为入口

## 1.模块的搜索路径个存储
- 什么是模块的搜索路径
   - 加载模块的时候,系统会在那些地方寻找此模块
- 系统默认的模块搜索路径(案例在p04)

     
         import sys
         sys.path
- 可以在sys.path中添加一个路径;
   - sys.path是一个list,就用list的方法添加就好了
 
# 包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于将模块包在一起的东西就是包
-自定义包的格式
 
 
      /---包
      /---/---__init__.py 包的标志性文件
      /---/--- 模块1
      /---/--- 模块2
      /---/--- 子包(子文件夹)
      /---/---/--- __init__.py 子包的标志性文件
      /---/---/--- 子包模块一
      /---/---/--- 子包模块二
- 包导入操作
   - import package_name
      - 直接导入一个包
      - 可以使用__init__.py中的内容
      - 此种方式访问的内容
      - 案例pkg01,p07
   - important package_name as 别名
      - 使用方法和导入模块一样
   - import package.moudle
      - 导入包中某个具体的模块   
   - 导入包时一般也使用if语句作为入口
   - from ... import导入
      - from package import module, module2 , module3
      - 导入时不会执行__init__的内容
   - from package import*
      - 导入当前包 '__init__'文件当中的所有函数和类
      - func_name()
        class_name.function_name()
        class_name.var
      - 案例在p06.注意导入的内容,其实只导入了__init__中的所有内容
   - from package.module import *
      - 导入包中指定模块的所有内容
      - 案例在p07.py
   
- 在开发环境中经常会用到其他模块,可以在当前包中直接导入其他模块中的内容
   - import 完整的包或者模块的路径
_ '__all__'的用法
   - 在使用from package import * 的时候,* 可以导入的内容 
   - 首先,__all__不是一个函数
   - '__init__'中如果文件为空, 或者没有'__all__'.那么只可以把'__init__'中的内容导入
   - '__init__'如果设置了'__all__'的值,那么按照'__all__'指定的模块载入,则不会载入'__init__'
   中的内容.        
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
 
 
 
 
 
 
 
 