hosts_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.instagram.com", "www.youtube.com"]
with open(hosts_path, 'r+') as file:
    content = file.read()
    for website in website_list:
        0 if website in content else file.write(redirect + " " + website + "\n")
    print('Blocked!')
