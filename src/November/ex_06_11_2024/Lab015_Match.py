browser_name = input("Enter your browser name\n")
browser_name = browser_name.lower()
match browser_name:
    case "chrome":
        print("Exicute Chrome Browser")
    case "firefox":
        print("Exicute FireFox Browser")
    case "safari":
        print("Exicute FireFox Browser")
    case _ :
        print("No Browser Match")