import re
from collections import Counter


def analyze_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_:
        content = file_.read()

    # 统计行数
    line__count = content.count('\n') + 1

    # 分词并统计词频
    words = re.findall(r'\b\w+\b', content.lower())
    word__count = Counter(words)

    return line__count, word__count


if __name__ == '__main__':
    file_path = 'tasks.txt'  # 替换为你的文件路径
    line_count, word_count = analyze_file(file_path)

    print(f"总行数: {line_count}")
    print("词频统计:")
    for word, count in word_count.items():
        print(f"{word}: {count}")
