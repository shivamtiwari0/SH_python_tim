import webbrowser

# webbrowser.open("https://www.python.org/", new=1 ) # new =1 new window, new =2 new window with new tab but if possible
# webbrowser.open_new("https://www.python.org/")

safari = webbrowser.get(using='safari')
safari.open("https://www.python.org/")
