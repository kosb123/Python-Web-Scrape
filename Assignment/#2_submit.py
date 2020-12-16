def is_on_list(days, week):
    on_list = week in days
    return on_list


def get_x(days, order):
    return days[order]


def add_x(days, week):
    days.append(week)


def remove_x(days, week):
    days.remove(week)


days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)
