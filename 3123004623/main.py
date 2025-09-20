import sys
import difflib

# 从命令行获取参数
original_path = sys.argv[1]   # 原文路径
plagiarized_path = sys.argv[2]  # 抄袭版路径
output_path = sys.argv[3]     # 输出路径

# 读文件内容
with open(original_path, 'r', encoding='utf-8') as f:
    original_text = f.read()

with open(plagiarized_path, 'r', encoding='utf-8') as f:
    plagiarized_text = f.read()

# 计算相似度
similarity = difflib.SequenceMatcher(None, original_text, plagiarized_text).ratio()

# 写结果到文件（百分比，两位小数）
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(f"{similarity*100:.2f}%")
