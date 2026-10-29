# -*- coding: utf-8 -*-
"""
第 2 章  运算符与表达式
（三章拆分之 2/3，原 hello_world.py）

阅读约定
--------
1. 每段 Python 代码都有逐行注释，说明这一行在做什么
2. 每个知识点后面跟着 "[C++] 对照 ↓" 段，给出等价的 C++ 写法；
   这些 C++ 代码写在注释里，只用于对比，不参与运行
3. 运行方式：py 02_operators_expressions.py
"""

import math   # 2.2 节的 isclose、2.9 节的 isnan 需要它


def title(text):
    """打印章节大标题，让终端输出更好看。"""
    print("\n" + "=" * 72)
    print(text)
    print("=" * 72)


def sub(text):
    """打印小节标题，让终端输出更好看。"""
    print("\n--- " + text + " ---")


# ============================================================================
title("第 2 章  运算符与表达式")

sub("2.1 算术运算符")
print(7 + 2, 7 - 2, 7 * 2)               # 加 9 / 减 5 / 乘 14
print("7 / 2 =", 7 / 2, type(7 / 2))     # 真除法：结果 3.5（float）；C++ 整数相除会得 3！
print("7 // 2 =", 7 // 2)                # 地板除：向负无穷取整，这里 3
print("7 % 2 =", 7 % 2)                  # 取模（余数），这里 1
print("2 ** 10 =", 2 ** 10, "| 2 ** 0.5 =", 2 ** 0.5)   # 幂：1024 / 开平方 1.414...
# 负数时的规则：// 向下取整，% 的符号跟随"除数"（C++ 是向零取整、余数跟随被除数）
print("-7 // 2 =", -7 // 2, "| -7 % 2 =", -7 % 2)        # -4 | 1（C++ 是 -3 和 -1）
print("7 // -2 =", 7 // -2, "| 7 % -2 =", 7 % -2)        # -4 | -1（C++ 是 -3 和 1）
print("divmod(7, 2) =", divmod(7, 2))    # 一次拿到 (商, 余数) = (3, 1)

# [C++] 对照 ↓
# #include <cmath>
# #include <cstdlib>
# int main() {
#     int i = 7 / 2;                  // 3：两个 int 相除，小数部分直接丢弃
#     double d = 7 / 2.0;             // 3.5：只要有一个浮点数才是真除法
#     int q = -7 / 2;                 // -3：C++ 向零取整，与 Python 的 -4 不同
#     int r = -7 % 2;                 // -1：余数符号跟随被除数，Python 是 1
#     double p = std::pow(2, 10);     // 1024，需要 #include <cmath>
#     std::div_t dr = std::div(7, 2); // 一次拿商和余数：dr.quot=3, dr.rem=1
#     return 0;
# }

sub("2.2 比较运算符与链式比较")
print(1 == 1.0, 1 != 2, 3 > 2, 2 <= 2)      # 比较结果永远是 bool；1 == 1.0 为 True
print("1 < 2 < 3 ->", 1 < 2 < 3)            # 链式比较 = (1<2) and (2<3)，结果是 True
val = 5                                      # 准备一个中间值
print("1 < val <= 10 ->", 1 < val <= 10)    # 链式写法更直观，不用写两次 val
print("apple" < "banana")                    # 字符串按 Unicode 逐字符比较 -> True
# 不同类型不能比大小（bool 与 int 例外，因为 bool 就是 int 子类）
# print(1 < "2")        # TypeError: '<' not supported between instances of 'int' and 'str'
print("0.1+0.2 == 0.3 ->", 0.1 + 0.2 == 0.3)            # False，浮点误差导致
print("math.isclose ->", math.isclose(0.1 + 0.2, 0.3))  # True，近似比较的正确姿势

# [C++] 对照 ↓
# #include <cmath>
# #include <string>
# int main() {
#     bool a = (1 == 1.0);            // int 与 double 比较：1 提升为 1.0
#     bool chained = (1 < 2) && (2 < 3);   // 链式比较必须拆成两个表达式
#     // 注意：C++ 里 1 < 2 < 3 会先算 1<2 得 true(1)，再算 1<3，恰好也是 true，
#     // 但语义完全不同，不能照搬
#     std::string s1 = "apple", s2 = "banana";
#     bool lt = s1 < s2;              // 字典序比较，等价于 Python
#     bool eq = std::fabs((0.1 + 0.2) - 0.3) < 1e-9;   // 浮点近似相等
#     return 0;
# }

sub("2.3 逻辑运算符 and / or / not")
print(True and False, True or False, not True)   # False True False
# 重点：and / or 返回"操作数本身"，不一定是 bool（C++ 的 && / || 结果一定是 bool）
print("1 and 2 ->", 1 and 2)          # 2：左边为真就返回右边
print("0 and 2 ->", 0 and 2)          # 0：左边为假直接返回左边
print("'' or '默认值' ->", "" or "默认值")   # "默认值"：常用技巧，空值兜底
print("None or 0 ->", None or 0)      # 0：左边假就返回右边


def side_effect():
    """用来验证短路求值：被调用时会打印一行。"""
    print("右边被求值了")
    return True


print("False and side_effect() ->", False and side_effect())   # 不会打印"右边..."，短路了
print("True or side_effect() ->", True or side_effect())       # 不会打印"右边..."，短路了
# 真值测试：下面这些值在 if/while 里都等价于 False
falsy_values = [0, 0.0, "", [], {}, set(), (), None, False]
print("各值 bool 结果：", [bool(v) for v in falsy_values])      # 全是 False

# [C++] 对照 ↓
# int main() {
#     bool a = true && false;         // 结果一定是 bool，不会返回操作数
#     bool b = true || false;
#     bool c = !true;
#     // 短路求值规则相同：
#     // false && sideEffect()  —— 右边不执行
#     // true  || sideEffect()  —— 右边不执行
#     // "假值"概念：C++ 里 0、0.0、nullptr 转 bool 为 false；
#     // 容器（vector/string）不能隐式转 bool，要写 if (v.empty())
#     // Python 的 []、""、{} 可以直接当条件用，C++ 不行
# }

sub("2.4 位运算符")
print("6 & 3 =", 6 & 3, "| 6 | 3 =", 6 | 3, "| 6 ^ 3 =", 6 ^ 3)   # 按位与 2 / 或 7 / 异或 5
print("~5 =", ~5)                      # 按位取反：-6，满足 ~x == -x-1，与 C++ 一致
print("1 << 4 =", 1 << 4, "| 16 >> 2 =", 16 >> 2)   # 左移 16 / 右移 4
print("-1 & 0xFF =", -1 & 0xFF)        # 255：负数以补码参与运算（与 C++ 相同）
flags = 0b1010                         # 用二进制表示一组标志位
print("取第 2 位：", (flags & 0b0010) != 0)   # 用掩码取出某一位并判断是否为 1

# [C++] 对照 ↓
# int main() {
#     int a = 6 & 3;          // 2
#     int b = 6 | 3;          // 7
#     int c = 6 ^ 3;          // 5
#     int d = ~5;             // -6，同样满足 ~x == -x-1
#     int e = 1 << 4;         // 16
#     int f = 16 >> 2;        // 4
#     int g = -1 & 0xFF;      // 255，负数补码参与运算
#     bool bit2 = (0b1010 & 0b0010) != 0;   // 掩码取位
#     // 注意：Python 整数没有位宽上限，右移是算术右移；
#     // C++ 的 unsigned 右移是逻辑右移（高位补 0），行为不同
# }

sub("2.5 赋值运算符与海象运算符")
n = 10          # 初始值
n += 3          # 10 + 3 = 13
n -= 3          # 13 - 3 = 10
n *= 2          # 10 * 2 = 20
n //= 2         # 20 // 2 = 10
n %= 5          # 10 % 5  = 0
n **= 3         # 0 ** 3  = 0
print("复合赋值后的 n =", n)          # 输出 0

# 大坑：+= 对"不可变对象"只是重新绑定名字，而不是像 C++ 引用那样改原对象
s = "ab"                # s 指向字符串 "ab"
t = s                   # t 也指向同一个字符串对象
s += "cd"               # 生成新字符串 "abcd"，把 s 改指向它；t 仍指向 "ab"
print("s =", s, "| t =", t)           # abcd | ab

lst1 = [1]              # list 是可变对象
lst2 = lst1             # 两个名字指向同一个 list
lst1 += [2]             # list 的 += 是原地修改（__iadd__），不新建对象
print("lst1 =", lst1, "| lst2 =", lst2)   # 都是 [1, 2]，说明改的是同一个对象

# 海象运算符 := 可以在"表达式内部"赋值（3.8+）
data = [1, 2, 3, 4]
if (length := len(data)) > 2:        # 先算 len 赋给 length，再用它做比较
    print("长度是", length)
print("while 用法：")
k = 3
while (k := k - 1) > 0:              # 每次循环先减 1 再判断
    print("  k =", k)                # 输出 2、1

# [C++] 对照 ↓
# int main() {
#     int n = 10; n += 3; n -= 3; n *= 2; n /= 2; n %= 5;   // 复合赋值语义相同
#     std::string s = "ab", t = s;      // 值拷贝：t 是独立对象
#     s += "cd";                        // s 变成 abcd，t 仍是 ab（值语义）
#     std::vector<int> l1{1};
#     auto l2 = l1;                     // 拷贝构造：l2 是独立容器
#     l1.push_back(2);                  // l1 = {1,2}，l2 仍为 {1}
#     // C++17 的"表达式内声明"：if (int len = data.size(); len > 2) { ... }
#     // 与 Python 的 := 最接近
#     return 0;
# }

sub("2.6 成员运算符 in 与身份运算符 is")
print("'py' in 'python' ->", "py" in "python")   # 子串判断 -> True
print("3 in [1, 2, 3] ->", 3 in [1, 2, 3])       # 列表元素判断 -> True
print("'k' in {'k': 1} ->", "k" in {"k": 1})     # 字典判断"键"是否存在 -> True
print("3 not in [1, 2] ->", 3 not in [1, 2])     # not in 是 in 的取反 -> True

# == 比较"值是否相等"，is 比较"是不是同一个对象"（近似比较地址）
p1 = [1, 2]                    # 新建一个 list 对象
p2 = [1, 2]                    # 再新建一个内容相同的 list 对象
print("p1 == p2 ->", p1 == p2, "| p1 is p2 ->", p1 is p2)   # True False

# 实现细节：CPython 会缓存 -5~256 的小整数对象，所以小整数的 is 有时为 True
small_a = int("256")           # int() 解析出 256，命中小整数缓存，返回同一个对象
small_b = int("256")           # 再次取到同一个缓存对象
print("小整数 256：is ->", small_a is small_b)     # True（属于实现细节，不可依赖）
big_a = int("1000")            # 1000 超出缓存范围，每次新建对象
big_b = int("1000")
print("大整数 1000：is ->", big_a is big_b)         # False

# 判断 None 一律用 is / is not（None 是全局唯一对象，语义明确）
empty = None
print("empty is None ->", empty is None)            # True

# [C++] 对照 ↓
# #include <algorithm>
# #include <map>
# int main() {
#     std::vector<int> v{1, 2, 3};
#     bool has = std::find(v.begin(), v.end(), 3) != v.end();   // 等价于 3 in v
#     std::map<std::string, int> m{{"k", 1}};
#     bool keyIn = m.count("k") > 0;                            // 等价于 "k" in m
#     std::vector<int> p1{1, 2}, p2{1, 2};
#     bool eq = (p1 == p2);          // operator== 比内容，等价于 p1 == p2
#     bool same = (&p1 == &p2);      // 比较地址，才是 Python 的 is
#     int* ptr = nullptr;
#     bool isNone = (ptr == nullptr); // 等价于 is None
#     return 0;
# }

sub("2.7 条件表达式（Python 的三元运算符）")
age = 20                                          # 待判断的年龄
label = "成年" if age >= 18 else "未成年"          # 条件为真取前面，否则取后面
print(label)                                      # 输出 成年
num = 7                                           # 另一个示例值
print("偶数" if num % 2 == 0 else "奇数")          # 表达式里直接用，无需写 if 块
score1 = 85                                       # 成绩
grade = "A" if score1 >= 90 else "B" if score1 >= 80 else "C"   # 可以链式嵌套
print("等级：", grade)                             # 85 -> B

# [C++] 对照 ↓
# int main() {
#     int age = 20;
#     std::string label = (age >= 18) ? "成年" : "未成年";   // 三目运算符
#     int num = 7;
#     std::cout << ((num % 2 == 0) ? "偶数" : "奇数") << std::endl;
#     int score = 85;
#     std::string grade = (score >= 90) ? "A" : (score >= 80) ? "B" : "C";
#     std::cout << "等级：" << grade << std::endl;
#     return 0;
# }

sub("2.8 运算符优先级（高 → 低）")
print("""
**                        幂（右结合，如 2**3**2 = 2**(3**2)）
+x  -x  ~x                一元运算
*  /  //  %               乘、除、整除、取模
+  -                      加、减
<<  >>                    移位
&                         按位与
^                         按位异或
|                         按位或
< <= > >= == != in, is    比较 / 成员 / 身份（支持链式）
not                       逻辑非
and                       逻辑与
or                        逻辑或
a if cond else b          条件表达式
=  +=  -=  ...  :=        赋值（最低）
""")                                              # 三引号一次输出整张表
print("2 + 3 * 4 =", 2 + 3 * 4)                   # 14：乘法先于加法
print("(2 + 3) * 4 =", (2 + 3) * 4)               # 20：括号强制先加
print("2 ** 3 ** 2 =", 2 ** 3 ** 2)               # 512：幂是右结合 = 2**(3**2)

# [C++] 对照 ↓
# int main() {
#     int a = 2 + 3 * 4;          // 14，乘法优先，与 Python 相同
#     int b = (2 + 3) * 4;        // 20
#     double c = std::pow(2, std::pow(3, 2));   // C++ 没有 ** 运算符，要用 pow
#     // C++ 多出这些运算符：++ -- -> :: ?: , (逗号运算符)
#     // C++ 比较运算符不支持链式，1 < 2 < 3 会被当成 (1<2) < 3
#     // 其余优先级顺序与 Python 基本一致：一元 > 乘除 > 加减 > 移位 > 位与 > 异或 > 位或 > 比较 > 逻辑 > 赋值
#     return 0;
# }

sub("2.9 运算细节与常见坑")
print("10 ** 100 =", 10 ** 100)                    # 整数自动扩展精度，不会溢出
print("兜底：not 0 ->", not 0, "| not [] ->", not [])   # True True
print("无穷与 NaN：", float("inf"), float("-inf"), float("nan"))   # inf -inf nan
print("math.isnan(nan) ->", math.isnan(float("nan")))              # True
print("NaN == NaN ->", float("nan") == float("nan"))               # False：NaN 不等于自身
print("round(2.5) =", round(2.5), "| round(3.5) =", round(3.5))     # 2 | 4：银行家舍入
print("round(2.675, 2) =", round(2.675, 2))                        # 2.67，浮点表示经典坑
print("abs(-5) =", abs(-5), "| pow(2, 3) =", pow(2, 3), "| max =", max(1, 2, 3), "| min =", min([4, 5, 6]))

# [C++] 对照 ↓
# #include <cmath>
# #include <limits>
# #include <algorithm>
# int main() {
#     // int / long long 都会溢出（UB），需要 __int128 或大数库
#     double inf = std::numeric_limits<double>::infinity();
#     double nan = std::numeric_limits<double>::quiet_NaN();
#     bool isNan = std::isnan(nan);                 // true
#     bool nanEq = (nan == nan);                    // false，与 Python 一致
#     double r1 = std::round(2.5);                  // 3（四舍五入远离 0），Python 是 2
#     double r2 = std::round(2.675 * 100) / 100;    // 2.67，同样的浮点坑
#     int a = std::abs(-5);
#     double p = std::pow(2, 3);
#     int mx = std::max({1, 2, 3});                 // 初始化列表写法
#     int mn = std::min({4, 5, 6});
#     return 0;
# }

# ============================================================================
# 第 3 章  字符串与文本处理基础
