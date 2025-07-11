def banner_test(text=" ",screen_width=90):
    if len(text)==screen_width-4:
        raise ValueError("String '{0}' is larger than specified length {1}"
                         .format(text,screen_width))
    if text=="*":
        print("*"*screen_width)
    else:
        output_string="**{0}**".format(text.center(screen_width-4))
        print(output_string)

banner_test("*",60)
banner_test("Ya devi Sarva Bhuteshu",60)
banner_test(screen_width=60)
banner_test("I am Piyush Kumar Singh",60)
banner_test("I am a Data Analyst and Scientist",60)
banner_test("*",60)
