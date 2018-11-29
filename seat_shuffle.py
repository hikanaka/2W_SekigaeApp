import random

# with文でのファイルオープン
# https://bootcamp-text.readthedocs.io/textbook/5_module.html


with open("members.txt", mode="r") as f:
    members = f.read()
# 文字列を分割するsplitメソッド
    updated_list = members.split()

# ランダムに複数の要素を選択（重複なし）: random.sample()
# https://note.nkmk.me/python-random-choice-sample-choices/
first_table = random.sample(updated_list, 6)
# for文中でremoveを使うことによってsecond_table以下の重複をさける
for i in range(0, len(first_table)):
    updated_list.remove(first_table[i])

second_table = random.sample(updated_list, 5)
for i in range(0, len(second_table)):
    updated_list.remove(second_table[i])

third_table = random.sample(updated_list, 4)


print(f"Table1: {first_table}")
print(f"Table2: {second_table}")
print(f"Table3: {third_table}")




