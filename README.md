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
This software is to provide an exe file that can happily pass the challenge without making it public. so you can contact me at [Telegram](https://t.me/sandroputraa "Telegram") to get a software.  only for donation user will get a software or you can buy a full source code
