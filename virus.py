import pyuac
from os.path import normpath


normal_web = [
    "www.facebook.com",
    "www.instagram.com",
    "www.youtube.com"
]


def block():
    with open(normpath("C:/Windows/System32/drivers/etc/hosts"), 'r+') as file:
        content = file.read()
        # from adult import adult_web
        # normal_web.extend(adult_web)
        for website in normal_web:
            0 if website in content else file.write(f"127.0.0.1 {website}\n")
    # print('Blocked!')


if __name__ == "__main__":
    try:
        if not pyuac.isUserAdmin():
            pyuac.runAsAdmin()
        else:
            block()
    except:
        # pywintypes.error
        pass
