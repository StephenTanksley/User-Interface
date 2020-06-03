def second_calc(min, sec):
    seconds_in_minutes = (min * 60)
    return seconds_in_minutes + sec


print(second_calc(21, 15))


def kilometers_to_miles(kilometers):
    return f"There are {kilometers * 0.621371192} miles in {kilometers} kilometers."


print(kilometers_to_miles(5))


def print_spam(val):
    print(val)


def do_twice(f, val):
    f(val)
    f(val)


do_twice(print_spam, "Googledy poogledy poo")
