options=['Lo',"jo",'so',"Po","no"]
choose=input("Please choose from the given list: {} ->".format(options))
for i in options:
    if i == choose:
        print("We are delighted to serve you {}".format(i))
    while i==choose:
        print(input("Anything else sir:{} ->".format(options)))
       
else:
    print('Unavailable at the moment,Sir')
