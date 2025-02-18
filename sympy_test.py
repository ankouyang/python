# import sympy  # 导入 sympy 库，用于符号计算


# def derivative(expression, variable):
#     """
#     计算给定表达式关于指定变量的导数。

#     Args:
#       expression: 一个字符串，表示数学表达式。 例如: "x**2 + 3*x + 2"
#       variable: 一个字符串，表示要对其求导的变量。 例如: "x"

#     Returns:
#       一个字符串，表示表达式的导数（LaTeX 格式）。
#       如果输入无效，则返回错误消息。
#     """
#     try:
#         # 定义变量为一个符号。必须使用 sympy.symbols，而不是直接使用字符串名称。
#         x = sympy.symbols(variable)  # 重要：创建一个 sympy 符号

#         # 预处理表达式以使其与 sympy.sympify 兼容  （替换 **  和 ^)
#         expr_str = expression.replace("^", "**")  # 保证幂运算使用 ** 符号

#         # 使用 sympy 解析表达式。
#         expr = sympy.sympify(expr_str)

#         # 计算导数。
#         derivative = sympy.diff(expr, x)

#         # 返回导数作为字符串（LaTeX 格式）。适合公式显示
#         return sympy.latex(derivative)

#     except (
#         SyntaxError,
#         TypeError,
#         AttributeError,
#         ValueError,
#     ) as e:  # 捕获常见的错误类型
#         return f"错误：无效的表达式或变量。 详细信息：{e}"
#     except Exception as e:  # 捕获其他未知的错误
#         return f"发生了一个未知的错误: {e}"


# 示例用法：
# expression1 = "x**3 + 3*x**2 + 2*x + 4"
# variable1 = "x"
# derivative1 = derivative(expression1, variable1)
# print(f"关于 {variable1} 求 {expression1} 的导数为: {derivative1}")  # 输出 LaTeX 格式

# expression2 = "sin(x)"
# variable2 = "x"
# derivative2 = derivative(expression2, variable2)
# print(f"关于 {variable2} 求 {expression2} 的导数为: {derivative2}")

# expression3 = "x*y + y**2"
# variable3 = "y"
# derivative3 = derivative(expression3, variable3)
# print(f"关于 {variable3} 求 {expression3} 的导数为: ${derivative3}$")

# expression4 = "Invalid Expression"
# variable4 = "x"
# derivative4 = derivative(expression4, variable4)
# print(derivative4)  # 打印错误消息

# expression5 = "x**(1/2)"
# variable5 = "x"
# derivative5 = derivative(expression5, variable5)
# print(f"关于 {variable5} 求 {expression5} 的导数为: ${derivative5}$")

# expression6 = "Exp[x]"  # Mathematica syntax
# variable6 = "x"
# derivative6 = derivative(expression6, variable6)
# print(f"关于 {variable6} 求 {expression6} 的导数为: ${derivative6}$")

# expression7 = "Log[x]"  # Mathematica syntax for natural log
# variable7 = "x"
# derivative7 = derivative(expression7, variable7)
# print(f"关于 {variable7} 求 {expression7} 的导数为: ${derivative7}$")

# 1 / 0
# try:
#     1 / 0
# except ZeroDivisionError:
#     print("除数不能为零")

# number1 = "1"
# number2 = "2"
# try:
#     print(number1 * number2)
# except Exception as e:
#     print(e)
# finally:
#     print("finally")
