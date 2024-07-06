hosts_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.instagram.com", "www.youtube.com"]
with open(hosts_path, 'r+') as file:
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
    file.truncate()
    print('Unblocked!')
