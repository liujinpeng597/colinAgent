# -*- coding: utf-8 -*-
"""
第 1 章  变量、数据类型与输入输出
（三章拆分之 1/3，原 hello_world.py）

阅读约定
--------
1. 每段 Python 代码都有逐行注释，说明这一行在做什么
2. 每个知识点后面跟着 "[C++] 对照 ↓" 段，给出等价的 C++ 写法；
   这些 C++ 代码写在注释里，只用于对比，不参与运行
3. 运行方式：py 01_variables_types_io.py
"""

import keyword   # 1.2 节：打印所有关键字


# 改成 True 后运行会停下来，等待键盘输入（1.8 节使用）
DEMO_INPUT = False


def title(text):
    """打印章节大标题，让终端输出更好看。"""
    print("\n" + "=" * 72)
    print(text)
    print("=" * 72)


def sub(text):
    """打印小节标题，让终端输出更好看。"""
    print("\n--- " + text + " ---")


# ============================================================================
title("第 1 章  变量、数据类型与输入输出")

sub("1.1 变量：动态类型，赋值即声明")
a = 10                           # 名字 a 绑定到 int 对象 10；没有 "int a" 这种声明
print(a, type(a))                # type(a) 返回 a 当前所指对象的类型 -> <class 'int'>
a = "现在变成了字符串"            # 同一个名字改指向 str 对象，合法（动态类型）
print(a, type(a))                # 再看一次类型 -> <class 'str'>
b = a                            # b 与 a 指向同一个对象，没有发生任何拷贝
print("a is b ->", a is b)       # is 判断"是否同一个对象"，这里是 True

# [C++] 对照 ↓  C++ 是静态类型：变量的类型在编译期就固定，之后不能改
# #include <iostream>
# #include <string>
# int main() {
#     int a = 10;                       // 类型写在声明里，编译期确定
#     std::cout << a << std::endl;      // 输出 10
#     // a = std::string("字符串");     // 编译错误：int 不能赋 std::string
#     std::string s = "字符串";          // 需要另一个类型的变量
#     std::cout << s << std::endl;
#     int b = a;                        // 值拷贝：b 是独立变量，改 b 不影响 a
#     // C++ 没有 "is"（同一性）运算符，同一对象要用指针/引用比较地址
#     int* p1 = &a; int* p2 = &a;
#     std::cout << (p1 == p2) << std::endl;   // true，两个指针指向同一地址
#     return 0;
# }

sub("1.2 命名规则与约定")
# 规则：只能由 字母/数字/下划线 组成；不能以数字开头；区分大小写；不能是关键字
# 约定（PEP 8）：变量与函数用 snake_case，类用 PascalCase，常量用全大写
user_name = "Tom"                # 普通变量：小写 + 下划线（snake_case）
MAX_SIZE = 100                   # 常量：全大写；Python 没有 const，只是"约定"
_private = 1                     # 下划线开头表示"内部使用"（约定，并非强制私有）
print(user_name, MAX_SIZE, _private)   # 依次输出 Tom 100 1
print("关键字列表：", keyword.kwlist)   # 打印所有不能用作变量名的关键字

# [C++] 对照 ↓
# const int MAX_SIZE = 100;        // C++ 的 const 是编译器强制，改就报错
# static constexpr int SIZE = 100; // 编译期常量
# class Foo {
# private:                         // C++ 有真正的访问控制，Python 只有 _ 约定
#     int m_private = 1;           // m_ 前缀是常见命名约定
# public:
#     void bar() { }
# };
# int userName = 0;                // C++ 社区更常用 camelCase，编译器不限制风格

sub("1.3 基本数据类型")
big = 2 ** 100                   # ** 是幂运算；int 是任意精度，多大都不会溢出
print("2**100 =", big, type(big))# 输出一个 31 位十进制大整数，类型仍是 int
pi = 3.14                        # 3.14 默认是 float（IEEE 754 双精度，同 C++ double）
print(pi, type(pi))              # <class 'float'>
print("0.1 + 0.2 =", 0.1 + 0.2)  # 0.30000000000000004：二进制浮点误差，和 C++ 完全一样
print(True, False, type(True))   # bool 只有 True/False，首字母必须大写
print("True + True =", True + True, "| True == 1 ->", True == 1)  # 2 | True：bool 是 int 子类
s = "你好, Python"                # str 是 Unicode 字符序列（不是字节数组）
print(s, type(s))                # <class 'str'>
n = None                         # None 表示"没有值"，全局唯一的一个 None 对象
print(n, type(n))                # <class 'NoneType'>
print(type(1) is int)            # type() 精确判断类型 -> True
print("isinstance(True, int) ->", isinstance(True, int))   # True，bool 继承自 int

# [C++] 对照 ↓
# #include <iostream>
# #include <limits>
# #include <typeinfo>
# int main() {
#     // int b = 2 << 99;  会溢出 UB，需要 long long / __int128 或大数库
#     long long big = 1;  for (int i = 0; i < 10; ++i) big *= 1024;   // 远达不到 2**100
#     double pi = 3.14;                          // 字面量默认 double
#     double x = 0.1 + 0.2;                      // 同样得到 0.30000000000000004
#     bool t = true, f = false;                  // 关键字是小写 true/false
#     std::string s = "你好, Python";             // 字节序列，不是 Unicode 码点序列
#     // C++ 的空值：nullptr（指针），没有统一的 None 对象
#     std::cout << typeid(pi).name() << std::endl;  // 运行时类型信息
# }
# // C++ 的 bool 就是 1 字节布尔，不会自动当 int 用（true + true 需要先强转）

sub("1.4 数字字面量与书写方式")
print(123, -45, 0)               # 十进制整数字面量
print(0b1010, 0o17, 0xFF)        # 二进制 10 / 八进制 15 / 十六进制 255
print(1_000_000)                 # 下划线只是分隔符，值仍是 1000000
print(1.5e3, 1.5e-3)             # 科学计数：1500.0 / 0.0015
print(1 + 2j)                    # 复数用 j 作虚部后缀，内建支持
print("复数实部：", (1 + 2j).real)  # 复数对象有 .real / .imag 属性

# [C++] 对照 ↓
# int a = 0b1010;            // 二进制 10（C++14 起）
# int b = 017;               // 八进制 15 —— C++ 是 0 前缀，Python 是 0o 前缀
# int c = 0xFF;              // 十六进制 255
# int d = 1'000'000;         // 数字分隔符（C++14 用单引号，Python 用下划线）
# double e = 1.5e3;          // 科学计数
# std::complex<double> z(1, 2);   // 复数需要 #include <complex>
# std::cout << z.real() << std::endl;   // 实部用方法调用，不是属性

sub("1.5 类型转换")
print(int("42"), int(3.9), int(-3.9))     # 字符串→int；float→int 向零截断：3 / -3
print(int("1010", 2), int("ff", 16))      # 第二个参数指定进制：10 / 255
print(float("3.14"), float(7))            # 字符串/整数 → float：3.14 / 7.0
print(str(123), str(3.14), str(True))     # 任意对象 → str："123" "3.14" "True"
print(bool(0), bool(0.0), bool(""), bool([]), bool(None))   # 全部 False（假值）
print(bool(1), bool(-1), bool("0"), bool([0]))              # 全部 True（非零/非空）
print(1 + 2.0, type(1 + 2.0))             # 1 自动提升为 float，结果是 3.0
# C++ 同样不会把字符串隐式转成数字；Python 更严格：数字与字符串不能相加
# print(1 + "2")      # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# [C++] 对照 ↓
# #include <iostream>
# #include <string>
# #include <cstdlib>
# int main() {
#     int a = std::stoi("42");                    // 字符串 → int
#     int b = static_cast<int>(3.9);              // 3   ，向零截断，同 Python
#     int c = static_cast<int>(-3.9);             // -3
#     double d = std::stod("3.14");               // 字符串 → double
#     std::string s = std::to_string(123);        // 数字 → 字符串
#     bool e = 0;                                 // int → bool：0 为 false
#     bool f = 1;                                 // 非 0 为 true
#     double g = 1 + 2.0;                         // int 自动提升为 double
#     // int + std::string 也是编译错误，C++ 不会隐式转
#     return 0;
# }

sub("1.6 输出 print()")
print("a", "b", "c")              # 多个参数会被自动用空格分隔：a b c
print("a", "b", sep="-")          # sep 指定分隔符：a-b
print("第一行", end=" ")          # end 指定结尾（默认 "\n"），所以下一句会接在同一行
print("第二行")                   # 输出完自动换行
print()                           # 不带参数 = 输出一个空行
print("立即输出", flush=True)     # flush=True 立即刷新缓冲区（进度日志常用）

# [C++] 对照 ↓
# #include <iostream>
# int main() {
#     std::cout << "a" << " " << "b" << " " << "c" << std::endl;  // 分隔符要自己写
#     std::cout << "a" << "-" << "b" << "\n";                     // sep 相当于手打分隔符
#     std::cout << "第一行" << " ";                               // end 相当于自己控制结尾
#     std::cout << "第二行\n";
#     std::cout << std::endl;                                     // 空行
#     std::cout << "立即输出" << std::flush;                       // flush 对应 std::flush
#     return 0;
# }

sub("1.7 字符串格式化（三种写法，f-string 最常用）")
name, score = "小明", 92.567        # 一行赋值两个名字，右边是元组解包
# ① % 旧式（写法最接近 C 的 printf，% 后接元组）
print("%s 的成绩是 %.1f" % (name, score))     # %s 字符串、%.1f 保留 1 位小数
# ② str.format()：{} 是占位符，按顺序填充
print("{} 的成绩是 {:.1f}".format(name, score))   # 输出 "小明 的成绩是 92.6"
print("{0} {1} {0}".format("A", "B"))             # 位置参数可重复使用 -> A B A
print("{n} {s}".format(n=name, s=score))           # 关键字参数，可读性更好
# ③ f-string（3.6+）：字符串前加 f，{} 内直接写变量或表达式，最推荐
print(f"{name} 的成绩是 {score:.1f}")               # 输出 "小明 的成绩是 92.6"

# 格式说明符完整语法：[[填充]对齐][符号][#][0][宽度][,][.精度][类型]
x = 3.14159
print(f"{x:.2f}")           # 精度：保留 2 位小数 -> 3.14
print(f"{x:+.2f}")          # 符号：正数也显示 + -> +3.14
print(f"{x:10.2f}|")        # 宽度 10，数字默认右对齐，右侧补空格
print(f"{x:<10.2f}|")       # < 左对齐
print(f"{x:^10.2f}|")       # ^ 居中
print(f"{x:*^10.2f}|")      # * 是填充字符，配合 ^ 居中填充 -> ***3.14***
print(f"{1234567:,}")       # 千分位分隔 -> 1,234,567
print(f"{0.256:.1%}")       # 百分比：乘 100 再加 % 号，保留 1 位小数 -> 25.6%
print(f"{255:b} {255:o} {255:x} {255:#x}")   # 二进制/八进制/十六进制；#x 带 0x 前缀
print(f"{42:08.3f}")        # 0 表示左侧补零，宽度 8 -> 0042.000
print(f"{'abc':>8}|")       # 字符串也能对齐，> 表示右对齐
print(f"{name=}")           # 3.8+ 调试专用：自动带出 "name='小明'"

# 转义字符（与 C++ 基本一致）
print("换行\n制表\t反斜杠\\ 引号\" 单引号\'")   # \n 换行、\t 制表、\\ 表示一个反斜杠
print("\x41", "\u4e2d")      # \xhh 十六进制字符 A；\uXXXX Unicode 码点 -> 中
print(r"C:\new\test")        # r"" 原始字符串：反斜杠不转义（写 Windows 路径很方便）
# 注意：原始字符串不能以单个反斜杠结尾，r"\" 是非法写法

# [C++] 对照 ↓
# #include <iostream>
# #include <iomanip>
# #include <string>
# #include <cstdio>
# #include <format>        // C++20
# int main() {
#     std::string name = "小明"; double score = 92.567;
#     printf("%s 的成绩是 %.1f\n", name.c_str(), score);      // ① 与 Python %% 风格一致
#     std::cout << std::format("{} 的成绩是 {:.1f}\n", name, score);  // ② 即 std::format
#     std::cout << std::fixed << std::setprecision(2) << 3.14159;      // .2f
#     std::cout << std::setw(10) << 3.14159 << "|";                    // 宽度 10 右对齐
#     std::cout << std::left << std::setw(10) << 3.14159 << "|";       // <
#     std::cout << std::setfill('*') << std::setw(10) << std::right << 3.14159;  // * 填充
#     std::cout << std::format("{:,}", 1234567);                       // 千分位
#     std::cout << std::format("{:.1%}", 0.256);                       // 百分比
#     std::cout << std::hex << 255 << std::dec;                        // 十六进制
#     std::cout << std::format("{:08.3f}", 42.0);                      // 0042.000
#     std::cout << "\n\t\\\"\'\n";                                     // 转义字符同 Python
#     std::cout << R"(C:\new\test)" << std::endl;                      // C++11 原始字符串
#     // f-string 的 "name=" 调试写法 C++ 没有直接等价物，只能手写 cout << "name=" << name;
# }

sub("1.8 输入 input()")
# 关键：input() 永远返回 str；要数字必须自己转换，否则后面运算会 TypeError
if DEMO_INPUT:                             # 只有把文件顶部 DEMO_INPUT 改成 True 才执行
    user = input("请输入姓名：")            # 从键盘读一行，返回 str
    age = int(input("请输入年龄："))        # 再把 str 转成 int；输错格式会抛 ValueError
    print(f"你好 {user}，明年你 {age + 1} 岁")   # age 现在是 int，可以做加法

# 常用输入模板（把 DEMO_INPUT 改成 True 后取消注释即可试）
# a, b = map(int, input().split())       # 一行两个整数：split 按空白切开，map 逐个转 int
# xs = list(map(float, input().split())) # 一行多个浮点数，收集成 list
# 输入可能为空或格式错误时，需要 try...except（异常章节会讲）
print("输入示例（当前未启用交互）：")
print("  一行两个整数 -> a, b = map(int, input().split())")

# [C++] 对照 ↓
# #include <iostream>
# #include <string>
# int main() {
#     std::string name; int age;
#     std::cout << "请输入姓名："; std::cin >> name;    // 遇到空格就停止读取
#     std::cout << "请输入年龄："; std::cin >> age;     // 类型安全，直接读成 int
#     std::cout << "你好 " << name << "，明年你 " << age + 1 << " 岁\n";
#     // 读"一行两个整数"：
#     // int a, b; std::cin >> a >> b;                  // 空格自动分隔
#     // 或先 getline 再 stringstream 解析：
#     // std::string line; std::getline(std::cin, line);
#     // std::stringstream ss(line); ss >> a >> b;
#     return 0;
# }

sub("1.9 多重赋值、交换、解包、del")
p = q = 0                        # 连续赋值：p、q 都指向同一个 int 对象 0
x, y = 1, 2                      # 解包：右边其实是元组 (1, 2)，按位置分给左边
x, y = y, x                      # 交换：等号右边先整体求值，再统一赋值
print(x, y)                      # 输出 2 1
first, *rest = [1, 2, 3, 4]      # *rest 把剩余元素收成 list -> first=1, rest=[2,3,4]
print(first, rest)
z = None                         # 先给 z 一个值
del z                            # del 删除"名字"；对象本身由垃圾回收管理
# 注意：del 之后再使用 z 会抛 NameError（名字不存在了）

# 类型注解（3.5+）：只是给人和静态检查工具看的提示，运行时不强制检查
count: int = 5                   # 声明风格：名字: 类型 = 值
ratio: float = 0.5
print(count, ratio)

# [C++] 对照 ↓
# int p = 0, q = 0;              // C++ 的连续赋值写法含义不同：p 和 q 是两份独立存储
# int x = 1, y = 2;
# std::swap(x, y);               // 或用 std::tie(x, y) = std::make_tuple(y, x);
# int arr[] = {1, 2, 3, 4};
# int first = arr[0];            // C++17 结构化绑定：auto [first, second, third, fourth] = ...
#                                // 但没有"剩余元素"语法，需要自己写容器
# std::optional<int> z;          // 用 optional 表示"可能没有值"
# z.reset();                     // 清空 optional，近似 del
# // 类型注解：C++ 的类型声明本身就是强制注解，无需额外语法

sub("1.10 作用域一览（LEGB）")
# 查找顺序：Local 局部 → Enclosing 外层函数 → Global 模块全局 → Builtin 内置
g = "模块全局变量"                # 模块级（文件顶部）的变量就是"全局变量"


def read_global():
    """函数内部读全局变量：直接读即可。"""
    local_var = "局部变量"        # 函数里第一次赋值 = 定义局部变量
    print(g, local_var)          # 读全局 g 合法，输出 "模块全局变量 局部变量"


def write_global():
    """函数内部给全局变量重新赋值：必须用 global 声明。"""
    global g                     # 声明"我接下来要改的是模块级 g"
    g = "被函数改写的全局变量"    # 这才是改全局；不写 global 会被当成新的局部变量


read_global()                    # 调用第一个函数
write_global()                   # 调用第二个函数（改写全局 g）
print(g)                         # 输出 "被函数改写的全局变量"
# C++ 对照：Python 没有"块级作用域"，if/for/while 里首次赋值的变量函数内依然可见

# [C++] 对照 ↓
# std::string g = "模块全局变量";                 // 全局变量
# void readGlobal() {
#     std::string localVar = "局部变量";          // 函数局部变量
#     std::cout << g << " " << localVar << std::endl;
# }
# void writeGlobal() {
#     g = "被函数改写的全局变量";                 // 直接赋值即可，C++ 不需要 global 声明
# }
# int main() {
#     readGlobal(); writeGlobal();
#     std::cout << g << std::endl;
#     // 块级作用域：{ int tmp = 1; } 出块后 tmp 立刻不可见（Python 不是这样）
# }

# ============================================================================
# 第 2 章  运算符与表达式
