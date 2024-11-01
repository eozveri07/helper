from bs4 import BeautifulSoup # type: ignore
from concurrent.futures import ThreadPoolExecutor
import requests
import json


with open("config.json", "r") as f:

    read = json.load(f)


def Check(proxy):

    try:

        proxies = {
            "https": f"http://{proxy}",
            "http": f"http://{proxy}"
            }

        get = requests.get("https://ipinfo.io/json", proxies=proxies, timeout=read["timeout"])

        if get.json()["ip"] == proxy.split(":")[0]:

            get = requests.get(read["host"], proxies=proxies, timeout=read["timeout"])


            if get.status_code == 200:

                print(f"{proxy} - Başarılı")

                with open(read["export"], "+a") as f:

                    f.write(f"{proxy}\n")
                    f.close()

            else:

                print(f"{proxy} - Başarısız")

        else:

            print(f"{proxy} - Başarısız")

    
    except:

        print(f"{proxy} - Başarısız")
        pass

with open(read["import"], "r") as f:

    with ThreadPoolExecutor(max_workers=read["thread"]) as executor:

        for i in f.readlines():

            executor.submit(Check, i.replace("\n", ""))