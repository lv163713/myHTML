# 先导入 rich 的 print
from rich import print

# 然后……
print("[bold red]这是 Rich 的打印风格[/bold red]")  # 会显示颜色

# 想换回普通 print？
import builtins  # 导入内置模块

print = builtins.print  # 把 print 变回原始版本

print("现在是普通的打印啦～")  # 不再有颜色和样式