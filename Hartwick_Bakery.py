# Elizabeth Fuller
# 10/14/19
# Hartwick Bakery

cookies = []
candies = []


def cookie_data():
    # adds cookie data to cookies list
    for i in range(0, 6):
        j = i + 1
        data = input(f"Enter cookie data for Month {j}\n> ")
        data = int(data)
        cookies.append(data)


def candy_data():
    # adds candy data to candies list
    for i in range(0, 6):
        j = i + 1
        data = input(f"Enter candy data for Month {j}\n> ")
        data = int(data)
        candies.append(data)


def average_cookies():
    # averages cookie data
    total = 0
    months = 0
    for cookie in cookies:
        months = months + 1
        total = total + cookie
    cookie_average = total / months
    print(f"The average cookie sales for the last {months} Months is {round(cookie_average,2)} cookies.")
    return cookie_average


def average_candies():
    # averages candies data
    total = 0
    months = 0
    for candy in candies:
        months = months + 1
        total = total + candy
    candy_average = total / months
    print(f"The average candy sales for the last {months} Months is {round(candy_average, 2)} cookies.")
    return candy_average


def maximum_cookies():
    # finds maximum cookie sale
    max_cookie = 0
    for cookie in cookies:
        if cookie > max_cookie:
            max_cookie = cookie
    print(f"The maximum cookie sample size was {max_cookie}.")
    return max_cookie


def maximum_candies():
    # finds max candy sale
    max_candies = 0
    for candy in candies:
        if candy > max_candies:
            max_candies = candy
    print(f"The maximum candy sample size was {max_candies}.")
    return max_candies


def minimum_cookies(max_cookies):
    # find min cookie sale
    min_cookie = max_cookies
    for cookie in cookies:
        if cookie < min_cookie:
            min_cookie = cookie
    print(f"The minimum cookie sample size was {min_cookie}.")
    return min_cookie


def minimum_candies(max_candies):
    # find min candy sale
    min_candies = max_candies
    for candy in candies:
        if candy < min_candies:
            min_candies = candy
    print(f"The minimum candy sample size was {min_candies}.")
    return min_candies


def popular(aver_cookies, aver_candies):
    # determines the most popular, cookies or candy?
    if average_cookies() > average_candies():
        print("Cookies are more popular.")
    else:
        print("Candy is more popular.")


cookie_data()
print("")  # blank line for spacing
candy_data()
# the following commented out print statement
# enables viewing of inputted list values, useful in debugging
# print(cookies)
# print(candies)
aver_cookies = average_cookies()
aver_candies = average_candies()
print("")  # blank line for spacing
max_cookies = maximum_cookies()
max_candies = maximum_candies()
print("")  # blank line for spacing
minimum_cookies(max_cookies)
minimum_candies(max_candies)
print("")  # blank line for spacing
popular(aver_cookies, aver_candies)

