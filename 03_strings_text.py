# -*- coding: utf-8 -*-
"""
第 3 章  字符串与文本处理基础
（三章拆分之 3/3，原 hello_world.py）

阅读约定
--------
1. 每段 Python 代码都有逐行注释，说明这一行在做什么
2. 每个知识点后面跟着 "[C++] 对照 ↓" 段，给出等价的 C++ 写法；
   这些 C++ 代码写在注释里，只用于对比，不参与运行
3. 运行方式：py 03_strings_text.py
"""

import csv   # 3.7 节：按标准 CSV 规则解析
import io    # 3.7 节：把字符串包装成文件对象
import re    # 3.7 节：正则表达式


def title(text):
    """打印章节大标题，让终端输出更好看。"""
    print("\n" + "=" * 72)
    print(text)
    print("=" * 72)


def sub(text):
    """打印小节标题，让终端输出更好看。"""
    print("\n--- " + text + " ---")


# ============================================================================
title("第 3 章  字符串与文本处理基础")

sub("3.1 字符串的创建与不可变性")
s1 = 'single'                 # 单引号字符串
s2 = "double"                 # 双引号字符串，与单引号完全等价
s3 = """三引号
可以跨行
"""                           # 三引号保留换行，也常用来写 docstring
print(s1, s2, s3, sep="|")    # 用 | 分隔查看三种写法

# 不可变（immutable）：任何"修改"都会返回一个新字符串，原串永远不动
s = "abc"                     # s 指向字符串 "abc"
# s[0] = "X"                  # TypeError：'str' object does not support item assignment
upper_s = s.upper()           # upper() 返回新串 "ABC"
print("原串：", s, "| 新串：", upper_s)   # 原串仍是 abc

# [C++] 对照 ↓
# #include <string>
# int main() {
#     std::string s1 = "single", s2 = "double";
#     std::string s3 = "三引号\n可以跨行\n";      // C++ 没有三引号，只能显式写 \n
#     std::string s = "abc";
#     s[0] = 'X';                                // std::string 可变，可以直接改
#     std::cout << s << std::endl;               // 输出 Xbc
#     const std::string cs = "abc";              // const 才近似 Python 的不可变
#     // cs[0] = 'X';                            // 编译错误：const 禁止修改
#     return 0;
# }

sub("3.2 索引与切片")
text = "Python"                             # 6 个字符
print("len =", len(text), "| text[0] =", text[0], "| text[-1] =", text[-1], "| text[2] =", text[2])
print("text[1:4] =", text[1:4])              # yth：从下标 1 取到下标 4 之前（含头不含尾）
print("text[:3] =", text[:3], "| text[3:] =", text[3:], "| text[:] =", text[:])   # 省略即到头/到底
print("text[::2] =", text[::2])              # 步长 2，隔一个取一个 -> Pto
print("text[::-1] =", text[::-1])            # 步长 -1，反转字符串 -> nohtyP
print("text[100:] =", repr(text[100:]))      # 切片越界不报错，返回空串 ''
# print(text[100])      # 单个索引越界才报 IndexError

# [C++] 对照 ↓
# #include <string>
# #include <algorithm>
# int main() {
#     std::string text = "Python";
#     int len = text.size();                      // 6
#     char first = text[0];                       // 'P'
#     char last = text[text.size() - 1];          // 'n'，C++ 没有负索引
#     std::string sub = text.substr(1, 3);        // "yth"：起始下标 + 长度（不是结束下标）
#     std::reverse(text.begin(), text.end());     // 反转需要 <algorithm>
#     // text[100] 是越界访问（UB 或直接抛异常），不会像 Python 切片那样自动截断
#     return 0;
# }

sub("3.3 常用字符串方法")
raw = "  Hello, Python World  "              # 两端带空格的原始串
print("strip ->", repr(raw.strip()))         # 去掉两端空白 -> 'Hello, Python World'
print("lstrip ->", repr(raw.lstrip()), "| rstrip ->", repr(raw.rstrip()))   # 只去左 / 只去右
print("'---abc---'.strip('-') ->", "---abc---".strip("-"))   # 参数是"字符集合"，不是子串

t = "hello world"
print("upper/lower/title/capitalize/swapcase:")             # 大小写变换方法
print(" ", t.upper(), "|", t.lower(), "|", t.title(), "|", t.capitalize(), "|", t.swapcase())
print("casefold ->", "PyThon".casefold())     # 比 lower 更彻底的小写（如德语 ß -> ss）

sentence = "I like C++ and C++ is fast"
print("replace ->", sentence.replace("C++", "Python"))       # 全部替换，返回新串
print("replace 只换 1 次 ->", sentence.replace("C++", "Python", 1))   # 第三个参数限定次数
print("count ->", sentence.count("C++"), "| find ->", sentence.find("C++"), "| find 不存在 ->", sentence.find("Java"))
# find 找不到返回 -1；index 找不到会抛 ValueError：
# sentence.index("Java")     # ValueError: substring not found
print("startswith ->", sentence.startswith("I"), "| endswith ->", sentence.endswith("fast"))
print("startswith 传元组 ->", sentence.startswith(("I", "You")))   # 满足任一前缀即为 True

line = "a,b,c"
print("split(',') ->", line.split(","))       # 按逗号切成列表 -> ['a', 'b', 'c']
print("'a b   c'.split() ->", "a b   c".split())    # 不带参数：按任意空白切分并丢弃空串
print("split(',', 1) ->", line.split(",", 1))       # 最多切 1 次 -> ['a', 'b,c']
multi = "第一行\n第二行\n第三行"
print("splitlines ->", multi.splitlines())    # 按行切分（比 split("\n") 更稳）
print("join ->", ",".join(["x", "y", "z"]))  # 用逗号把列表拼成一个串；元素必须是 str
# "-".join([1, 2, 3])     # TypeError: sequence item 0: expected str, int found

print("is* 判断系列：")
for v in ["abc", "123", "abc123", "   ", "ABC"]:      # 逐个测试判断类方法
    print(f"  {v!r}: isalpha={v.isalpha()}, isdigit={v.isdigit()}, "
          f"isalnum={v.isalnum()}, isspace={v.isspace()}")

print("填充与对齐：")
print(" ", "42".zfill(5), "|", "abc".center(9, "*"), "|", "abc".ljust(6, "-") + "|", "|", "abc".rjust(6, "-") + "|")

# [C++] 对照 ↓（对应关系见注释，C++ 大多数方法要自己手写或借助标准库算法）
# #include <string>
# #include <algorithm>
# #include <cctype>
# #include <sstream>
# int main() {
#     std::string raw = "  Hello, Python World  ";
#     // strip：找到第一个/最后一个非空白字符，再 substr
#     size_t b = raw.find_first_not_of(" \t\n");
#     size_t e = raw.find_last_not_of(" \t\n");
#     std::string stripped = (b == std::string::npos) ? "" : raw.substr(b, e - b + 1);
#     std::string t = "hello world";
#     std::transform(t.begin(), t.end(), t.begin(), ::toupper);   // upper()
#     // replace：C++ 的 replace 需要"位置 + 长度"
#     std::string s = "I like C++";
#     size_t pos = s.find("C++");
#     if (pos != std::string::npos) s.replace(pos, 3, "Python");
#     // find：找不到返回 std::string::npos
#     bool has = (s.find("Java") == std::string::npos);
#     // startswith：C++20 有 s.starts_with("I")；老版本用 compare(0, n, prefix) == 0
#     // split：stringstream + getline 第三参指定分隔符
#     std::string line = "a,b,c"; std::stringstream ss(line); std::string item;
#     while (std::getline(ss, item, ',')) { /* item 依次为 a b c */ }
#     // join：循环 += 拼接
#     // isalpha/isdigit：std::isalpha(c)、std::isdigit(c)，需要 <cctype>
#     // 填充对齐：std::setw + std::setfill + std::left/std::right，需要 <iomanip>
#     return 0;
# }

sub("3.4 字符串运算")
print("'ab' + 'cd' =", "ab" + "cd")          # 拼接，生成新串
print("'ab' * 3 =", "ab" * 3)                # 重复 3 次 -> ababab
print("'py' in 'python' ->", "py" in "python")   # 子串包含判断 -> True
# 性能提示：循环里用 + 拼接是 O(n²)（每次都新建字符串），应改用 join 或 list 收集
parts = ["a", "b", "c"]                     # 准备一批片段
print("''.join(parts) =", "".join(parts))   # 一次性拼成 abc，只需遍历一次

# [C++] 对照 ↓
# #include <string>
# #include <vector>
# int main() {
#     std::string a = "ab" + std::string("cd");     // + 拼接
#     std::string rep;
#     for (int i = 0; i < 3; ++i) rep += "ab";      // C++ 没有 * 重复语法
#     bool has = ("python".find("py") != std::string::npos);   // 等价于 in
#     std::vector<std::string> parts{"a", "b", "c"};
#     std::string joined;
#     for (const auto& p : parts) joined += p;      // join 要手写
#     // 注意：C++ 的 += 是原地扩容（amortized O(1)），不会有 Python 那种 O(n²) 重建
#     return 0;
# }

sub("3.5 f-string 进阶用法")
name, score = "小明", 92.5                # 准备两个变量
print(f"{name} 得分 {score}")             # {} 里可以直接写变量名
print(f"{score:.2f}")                     # 保留两位小数 -> 92.50
width = 8                                 # 宽度放在变量里
print(f"{score:{width}.1f}|")             # 嵌套字段：{} 里的 width 会被求值后再当宽度
w = 10                                    # 另一个宽度
print(f"{'标题':^{w}}")                    # 用 ^ 居中，宽度取自变量 w
print(f"{name=}, {score=}")               # 3.8+ 调试写法：输出 name='小明', score=92.5

# [C++] 对照 ↓
# #include <format>
# #include <iostream>
# int main() {
#     std::string name = "小明"; double score = 92.5;
#     std::cout << std::format("{} 得分 {}", name, score) << std::endl;
#     std::cout << std::format("{:.2f}", score) << std::endl;       // 精度
#     int width = 8;
#     std::cout << std::format("{:{}.1f}|", score, width) << std::endl;   // 动态宽度
#     std::cout << std::format("{:^{}}", "标题", 10) << std::endl;        // 居中
#     // C++ 没有 "name=" 调试语法，只能手写 std::cout << "name=" << name;
#     return 0;
# }

sub("3.6 字符、Unicode 与编码")
print("ord('A') =", ord("A"), "| ord('中') =", ord("中"))     # 字符 → 码点：65 / 20013
print("chr(65) =", chr(65), "| chr(20013) =", chr(20013))     # 码点 → 字符：A / 中
encoded = "中文".encode("utf-8")          # str → bytes，按 UTF-8 规则转成字节序列
print("encode ->", encoded, "| 字节数 =", len(encoded))       # 每个汉字 3 字节，共 6 字节
print("decode ->", encoded.decode("utf-8"))                   # bytes → str，还原成 "中文"
print("字符数 len('中文') =", len("中文"))                     # 2：str 的 len 数的是"字符"
print("bytes 字面量：", b"abc", type(b"abc"))                 # b"" 前缀表示 bytes 对象
# "中文" + b"abc"       # TypeError：str 与 bytes 不能直接拼接，必须先统一类型

# [C++] 对照 ↓
# #include <string>
# int main() {
#     char c = 'A';
#     int code = c;                    // 65，等价于 ord
#     char back = static_cast<char>(65);   // 'A'，等价于 chr
#     // C++ 的 "中文" 直接就是 UTF-8 字节串，没有"字符对象"这一层
#     std::string raw = "中文";
#     std::cout << raw.size() << std::endl;      // 6：数的是字节，不是字符
#     // C++20 可用 std::u8string 明确表示 UTF-8 字符串
#     // 编码转换（如 GBK → UTF-8）需要 ICU / iconv 等第三方库
#     return 0;
# }

sub("3.7 文本处理实战小例")
# 1) 清理一行 CSV 文本：去换行 → 按逗号切分 → 每项去两端空格
raw_line = "  张三 , 18 , 男 \n"          # 模拟从文件里读到的一行
fields = [item.strip() for item in raw_line.strip().split(",")]   # 列表推导式逐步处理
print("手工解析 ->", fields)              # ['张三', '18', '男']

# 2) 字段里可能含逗号/引号时，用标准库 csv 更稳妥
buf = io.StringIO('姓名,年龄\n"李四,小王",20\n王五,18\n')   # 把字符串包成"文件对象"
rows = list(csv.reader(buf))              # csv.reader 自动处理引号转义
print("csv 解析 ->", rows)                # [['姓名','年龄'], ['李四,小王','20'], ['王五','18']]

# 3) 用替换表一次替换多个字符（比多次 replace 更清晰）
table = str.maketrans({"你": "N", "好": "H"})   # 构建"字符 → 字符"映射表
print("translate ->", "你好，世界".translate(table))   # 按表替换 -> NH，世界

# 4) 正则表达式 re 模块基础
log = "2026-10-29 ERROR user=1001 msg=timeout"       # 模拟日志行
date_match = re.search(r"\d{4}-\d{2}-\d{2}", log)    # \d 数字，{4} 重复 4 次；返回第一个匹配
print("search ->", date_match.group() if date_match else None)   # 取出整段匹配
print("findall ->", re.findall(r"\d+", log))         # 找出所有连续数字 -> ['2026','10','29','1001']
print("sub ->", re.sub(r"\d+", "#", log))            # 把所有数字替换成 #
print("match 只从开头匹配 ->", re.match(r"\d{4}", log) is not None)   # True

# [C++] 对照 ↓
# #include <string>
# #include <sstream>
# #include <regex>
# int main() {
#     // 手工解析 CSV：
#     std::string line = "  张三 , 18 , 男 ";
#     std::stringstream ss(line); std::string item;
#     while (std::getline(ss, item, ',')) { /* 再对 item 做 trim */ }
#     // 带引号转义的 CSV 需要手写状态机或引入第三方库
#     // 一次替换多个字符：循环 std::replace，或用 std::map 查表后重组
#     std::string log = "2026-10-29 ERROR user=1001 msg=timeout";
#     std::regex dateRe(R"(\d{4}-\d{2}-\d{2})");     // 原始字符串写正则
#     std::smatch m;
#     if (std::regex_search(log, m, dateRe)) std::cout << m.str() << std::endl;
#     std::regex numRe(R"(\d+)");
#     std::string replaced = std::regex_replace(log, numRe, "#");   // 等价 re.sub
#     bool startsWithNum = std::regex_search(log, std::regex(R"(^\d{4})"));  // 近似 match
#     return 0;
# }

sub("3.8 常见坑速查")
# 1) is 比较身份、== 比较值；字符串可能被"驻留(interning)"，所以 is 的结果不可依赖
print("[1, 2] == [1, 2] ->", [1, 2] == [1, 2], "| [1, 2] is [1, 2] ->", [1, 2] is [1, 2])
# 2) 循环里 + 拼接字符串是 O(n²)，用 list 收集 + join
# 3) strip/replace/upper 都返回新串，原串不会变
orig = " abc "                            # 带空格的原始串
print("strip 后原串不变：", repr(orig), "->", repr(orig.strip()))   # 原串仍是 ' abc '
# 4) split("") 会报错，按空白切分直接写 split()
# "abc".split("")        # ValueError: empty separator
# 5) 索引越界抛 IndexError，切片越界只是截断
# 6) 文件读写编码不一致会乱码：统一显式指定 encoding="utf-8"
# 7) f-string 的 :.2f 只能用于数字，对字符串使用会抛 ValueError

# [C++] 对照 ↓
# #include <vector>
# #include <string>
# int main() {
#     std::vector<int> a{1, 2}, b{1, 2};
#     bool eq = (a == b);           // true：operator== 比内容
#     bool same = (&a == &b);       // false：C++ 用指针/引用比较身份，没有 is/== 之分
#     std::string orig = " abc ";
#     std::string t = orig;         // 拷贝一份再原地 trim，近似 Python 的"返回新串"
#     size_t first = t.find_first_not_of(" \t\n");
#     size_t last = t.find_last_not_of(" \t\n");
#     if (first != std::string::npos) t = t.substr(first, last - first + 1); else t = "";
#     std::cout << orig << " -> " << t << std::endl;   // 原串 orig 不会被改
#     // 越界：s.at(i) 会抛 std::out_of_range，s[i] 则是未定义行为
#     // 编码：std::string 不带编码信息，项目内约定统一用 UTF-8
#     return 0;
# }

print("\n全部示例执行完毕。")
