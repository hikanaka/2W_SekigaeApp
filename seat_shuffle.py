import random

# with文でのファイルオープン
# https://bootcamp-text.readthedocs.io/textbook/5_module.html


with open("members.txt", mode="r") as f:
    members = f.read()


print(members)




# def main():
#
# if __name__ == '__main__':



# members = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# for member in members:
#     print(member)



