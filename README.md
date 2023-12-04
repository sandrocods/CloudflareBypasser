# CloudflareBypasser

Cloudflarebypasser its a software based on exe to bypass Cloudflare Challenge + Turnstile and collect session cookies in a cloudflare IUAM protected site. Base on exe file you can use at multiple programming languages just run it using a [subprocess - Python3](https://docs.python.org/3/library/subprocess.html "subprocess - Python3") , [shell_exec - Php](https://www.php.net/manual/en/function.shell-exec.php "shell_exec - Php") , [child_process - Nodejs](https://nodejs.org/api/child_process.html "child_process - Nodejs")


### 🔰 Feature
| Feature  | State  |
| ------------ | ------------ |
| Bypass Cloudflare Challenge + Turnstile   | ✅  |
| Auto Random User Agent  | ✅  |
| Auto Get Cookies  | ✅  |
| Proxy Support  | ✅  |
| Headless  Mode  | ✅  |
| Support multiple programming languages | ✅  |
| API Server  |  🔁 In Progress    |
| Linux Support |  🔁 In Progress    |

### ⚙ How it works
[![](https://github.com/sandrocods/CloudflareBypasser/assets/59155826/badb50e3-da91-4555-93c4-3217763a3a78)](https://github.com/sandrocods/CloudflareBypasser/assets/59155826/badb50e3-da91-4555-93c4-3217763a3a78)

Based on Flowchart, Will start a web browser to Bypass Cloudflare When a program is able to pass through the IUAM or Captcha verification, it immediately return a User-Agent, Cookies contains
```json
{
        "name": "cf_clearance",
        "value": "0xxxxxxxxYlX_TE-1694029199-0-1-de4fxxxx37.894e7c66-250.0.0",
        "domain": ".yoursite.com"
}
```
and cookies in site to access the site using requests library.

### 📷 Demo

https://github.com/sandrocods/CloudflareBypasser/assets/59155826/e3dceda5-9e34-40a2-9663-12947195bc6c

### 📚 Command Line Interface Args
```man
usage: CloudflareBypasser.exe [-h] -u URL [-p PROXY] [-mw MAX_WAIT] [-mr MAX_RETRY] [-gp GET_PAGE] [-hd HEADLESS]

Cloudflare Bypasser | Code by: Sandroputraa

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Target URL
  -p PROXY, --proxy PROXY
                        Proxy URL
  -mw MAX_WAIT, --max-wait MAX_WAIT
                        Max Wait
  -mr MAX_RETRY, --max-retry MAX_RETRY
                        Max Retry
  -gp GET_PAGE, --get-page GET_PAGE
                        Get Page after bypass done
  -hd HEADLESS, --headless HEADLESS
                        Headless Mode
```


| Parameter |  Description                |
| :-------- | :------------------------- |
| `url` |  **Required**. Your target site |
| `proxy` | **Http/Https**. Proxy |
| `max-wait` | Timeout Bypass **Default is 30 sec** |
| `max-retry` | Timeout Retry Bypass **Default is 5x** |
|`get-page`| Will Return a requests verbose use a bypassed cookies **Default is False**|
|`headless`| Will Run in mode Headless **Default is False**|

## 📩 Response

##### Target site detected use a cloudflare
```json
{
  "status": true,
  "message": "CloudFlare Detected, Trying to Bypass",
  "time": "2023-09-07 03:53:28"
}
```

##### Success Bypass
```json
{
  "status": true,
  "message": "CloudFlare Bypassed",
  "solution": {
    "url": "https://nowsecure.nl",
    "cookies_string": "cf_clearance=D3pCE1KPUC1xLInKA1_ZY7t8y4xOBNFtbM0BMoYVswc-1694033611-0-1-a7b619d3.473fa7c.2544f376-250.2.1694033611",
    "cookies": [
      {
        "name": "cf_clearance",
        "value": "D3pCE1KPUC1xLInKA1_ZY7t8y4xOBNFtbM0BMoYVswc-1694033611-0-1-a7b619d3.473fa7c.2544f376-250.2.1694033611",
        "domain": ".nowsecure.nl"
      }
    ],
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "response": "<!DOCTYPE html>...</html>"
  },
  "start_time": "2023-09-07 03:53:27",
  "end_time": "2023-09-07 03:53:41",
  "elapsed_time": "14.19853138923645 seconds"
}
```

##### Max Retry Reached
```json
{
  "status": false,
  "message": "CloudFlare Bypass Failed, Max Retry Reached",
  "start_time": "",
  "end_time": "",
  "elapsed_time": ""
}
```
##### Get Page Verbose
```
< GET / HTTP/1.1
< Host: nowsecure.nl
< User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
< Accept-Encoding: gzip, deflate
< Accept: */*
< Connection: keep-alive
< Cookie: cf_clearance=D3pCE1KPUC1xLInKA1_ZY7t8y4xOBNFtbM0BMoYVswc-1694033611-0-1-a7b619d3.473fa7c.2544f376-250.2.1694033611
<

> HTTP/1.1 200 OK
> Date: Wed, 06 Sep 2023 20:53:41 GMT
> Content-Type: text/html
> Transfer-Encoding: chunked
> Connection: keep-alive
> Last-Modified: Fri, 27 May 2022 01:42:42 GMT
> Vary: Accept-Encoding
> Content-Security-Policy: upgrade-insecure-requests
> CF-Cache-Status: DYNAMIC
> Report-To: {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=3ybU6pFycy9dSWA%2Bu1RVmHYBTFS9nA%2Bh9nRoRdeVxBaw4a2ePZuCbconY5z3gIiJ1XswnZeJ25tJRJXnJCSI39haa4XX3RLmJGR0KRqFRDWbVA7jm25M2Q6gHI%2FOIHI%3D"}],"group":"cf-nel","max_age":604800}
> NEL: {"success_fraction":0,"report_to":"cf-nel","max_age":604800}
> Server: cloudflare
> CF-RAY: 80299a545f9740cb-SIN
> Content-Encoding: gzip
> alt-svc: h3=":443"; ma=86400
>
<!doctype html class="h-100">
.	..
</html>
```


## 🍳 Usage/Examples

##### Direct Usage
```bash
CloudflareBypasser.exe --url https://yoursite.com
```

##### Python3

```python
url = "https://yoursite.com"
cf = CloudFlareBypasser(url)
cf.set_headless(True)
if cf.run():
    print({
        "User-Agent": cf.get_user_agent(),
        "Cookie": cf.get_cookies_string(),
    })
        
```
Full Example Python3 : [Example Python3](https://github.com/sandrocods/CloudflareBypasser/blob/main/python/main.py "Example Python3")


### ⚠ Attention 
This software is to provide an exe file that can happily pass the challenge without making it public. so you can contact me at [Telegram](https://t.me/sandroputra "Telegram") to get a software.  only for donation user will get a software or you can buy a full source code
