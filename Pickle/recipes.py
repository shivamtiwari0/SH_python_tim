import shelve

# blt = ["bacon", "lattuce", "bread", "tomato"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
# soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open("recipies1") as recipes:
with shelve.open("recipies1", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta
    # recipes["blt"].append("butter")  # This will not work. List is appended but shelve is not triggered.
    # print(recipes["blt"])

    # temp_list = recipes["blt"]  #without using writeback
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    # del recipes["blt"][4]
    # recipes["pasta"].append("croutons")  #with writeback = True
    
    for snack in recipes:
        print(snack, recipes[snack])

