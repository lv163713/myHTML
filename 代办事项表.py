import os

# 文件路径
TASKS_FILE = "tasks.txt"

# 初始化任务列表
work_list = []

# 加载任务（如果存在）
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    task, priority, done = line.strip().split(" | ")
                    work_list.append({
                        "task": task,
                        "priority": priority,
                        "done": done == "True"
                    })
                except ValueError:
                    continue  # 忽略格式错误行


def save_tasks_to_file():
    """将当前任务列表保存到文件"""
    with open(TASKS_FILE, "w", encoding="utf-8") as f_:
        for item in work_list:
            f_.write(f"{item['task']} | {item['priority']} | {item['done']}\n")


def show_tasks():
    """展示当前任务列表"""
    if not work_list:
        print("没有待办事项")
        return
    print("\n当前任务列表：")
    for i, item in enumerate(work_list):
        status = "✓" if item["done"] else "✗"
        print(f"{i}. [{status}] [{item['priority']}] {item['task']}")


while True:
    print("\n--- 待办事项管理 ---")
    choice = input("1. 添加任务  2. 删除任务  3. 查看任务  4. 标记完成  5. 退出\n")

    if choice == '1':
        task = input("请输入待办事项：")
        priority = input("请输入优先级（高/中/低）：").strip()
        if priority not in ["高", "中", "低"]:
            print("优先级无效，默认设为‘中’")
            priority = "中"
        work_list.append({"task": task, "priority": priority, "done": False})
        print("添加成功")

    elif choice == '2':
        show_tasks()
        try:
            index = int(input("请输入要删除的任务编号："))
            if 0 <= index < len(work_list):
                removed = work_list.pop(index)
                print(f"已删除任务: {removed['task']}")
            else:
                print("编号无效")
        except ValueError:
            print("请输入有效数字")

    elif choice == '3':
        show_tasks()

    elif choice == '4':
        show_tasks()
        try:
            index = int(input("请输入已完成的任务编号："))
            if 0 <= index < len(work_list):
                work_list[index]["done"] = True
                print(f"任务“{work_list[index]['task']}”标记为已完成")
            else:
                print("编号无效")
        except ValueError:
            print("请输入有效数字")

    elif choice == '5':
        save_tasks_to_file()
        print("任务已保存，程序退出。")
        break

    else:
        print("输入错误")
