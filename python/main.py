import os
import json
import requests
import subprocess

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


if __name__ == '__main__':
    url = "https://www.namehero.com/blog/how-to-add-cloudflare-turnstile-to-wordpress/"

    # Without Cloudflare Bypass
    print("Without Cloudflare Bypass")
    response = requests.get(url)
    print(response.status_code, response.text)

    # With Cloudflare Bypass
    print("With Cloudflare Bypass")
    cf = CloudFlareBypasser(url)
    cf.set_headless(True)
    if cf.run():
        print({
            "User-Agent": cf.get_user_agent(),
            "Cookie": cf.get_cookies_string(),
        })
        response = requests.get(url, headers={"User-Agent": cf.get_user_agent(), "Cookie": cf.get_cookies_string()})
        print(response.status_code, response.text)
