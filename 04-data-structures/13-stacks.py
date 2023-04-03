browser_history = []
browser_history.append("google.com")
browser_history.append("linkedin.com")
browser_history.append("discord.com")
print(browser_history)
last_visit = browser_history.pop()
print("last visit: ", last_visit)
print(browser_history)

if not browser_history:
    browser_history[-1]