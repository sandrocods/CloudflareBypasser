import os
import json
import time
import subprocess
import multiprocessing


class CloudFlareBypasser:

    def __init__(self, target_url):
        self.target_url = target_url
        self.full_response = None
        self.proxy = None
        self.headless = False
        self.cookies_string = None
        self.cookies = None
        self.user_agent = None
        self.response = None

    def set_url(self, target_url):
        self.target_url = target_url

    def set_proxy(self, proxy):
        self.proxy = proxy

    def set_headless(self, headless):
        self.headless = headless

    def get_cookies_string(self):
        return self.cookies_string

    def get_cookies(self):
        return self.cookies

    def get_user_agent(self):
        return self.user_agent

    def get_response(self):
        return self.response

    def get_full_response(self):
        return self.full_response

    def run(self):
        if os.path.exists(os.getcwd() + "//CloudflareBypasser.exe"):
            exe_file = "CloudflareBypasser.exe"
            if self.headless:
                exe_file += " --headless True"

            if self.proxy:
                exe_file += " --proxy {}".format(self.proxy)

            if self.target_url is None or self.target_url == "":
                raise Exception("Target URL is not set")

            exe_file += " --url {}".format(self.target_url)

            process = subprocess.Popen(
                exe_file,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding='utf-8',
                universal_newlines=True,
            )
            for line in process.stdout:
                json_data = json.loads(line.strip())
                if json_data["status"] and json_data['message'] == "CloudFlare Bypassed":
                    self.cookies_string = json_data["solution"]["cookies_string"]
                    self.cookies = json_data["solution"]["cookies"]
                    self.user_agent = json_data["solution"]["user_agent"]
                    self.response = json_data["solution"]["response"]
                    self.full_response = json_data
                    return True

            process.wait()
            return None
        else:
            raise Exception("CloudflareBypasser.exe not found")


def _bypass(target_site, queue):
    cf = CloudFlareBypasser(target_site)
    cf.set_headless(False)
    if cf.run():
        queue.put({
            "User-Agent": cf.get_user_agent(),
            "Cookie": cf.get_cookies_string(),
        })
    else:
        queue.put(None)


if __name__ == '__main__':
    DELAY_PER_SITE = 1
    target_site = [
        "https://your-target-site-1.com/",
        "https://your-target-site-2.com/",
    ]

    result_queue = multiprocessing.Queue()
    processes = []

    for url in target_site:
        p = multiprocessing.Process(target=_bypass, args=(url, result_queue))
        time.sleep(DELAY_PER_SITE)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = []
    while not result_queue.empty():
        result = result_queue.get()
        results.append(result)

    for result in results:
        print(result)
