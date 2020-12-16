my_english_dict = {}


def delete_from_dict(my_dict={}, my_key=""):
    if type(my_dict) != dict:
        print(f"You need to send a dictionary. You sent: {type(my_dict)}")

    elif my_key == "":
        print("You need to specify a word to delete.")

    elif not(my_key in my_dict):
        print(f"{my_key} is not in this dict. Won't delete.")

    else:
        del my_dict[my_key]
        print(f"{my_key} has been deleted.")


delete_from_dict("hello", "kimchi")
delete_from_dict(my_english_dict)
delete_from_dict(my_english_dict, "galbi")
delete_from_dict(my_english_dict, "kimchi")
