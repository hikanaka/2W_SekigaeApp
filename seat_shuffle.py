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

second_table = random.sample(updated_list, 5)

third_table = random.sample(updated_list, 4)


print(f"Table1: {first_table}")
print(f"Table2: {second_table}")
print(f"Table3: {third_table}")




# def main():
#
# if __name__ == '__main__':



# members = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# for member in members:
#     print(member)



