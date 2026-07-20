import os
import io
import shutil
import time
import requests

print (os.getcwd())
os.chdir("./Rules")

RULE_URL = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/"
PROXY_RULES = {
    "YouTube": RULE_URL + "YouTube/YouTube.yaml",
    "Twitch": RULE_URL + "Twitch/Twitch.yaml",
    "TikTok": RULE_URL + "TikTok/TikTok.yaml",
    "Spotify": RULE_URL + "Spotify/Spotify.yaml",
    "Proxy": RULE_URL + "Proxy/Proxy.yaml",
    "PrimeVideo": RULE_URL + "PrimeVideo/PrimeVideo.yaml",
    "PayPal": RULE_URL + "PayPal/PayPal.yaml",
    "OneDrive": RULE_URL + "OneDrive/OneDrive.yaml",
    "Niconico": RULE_URL + "Niconico/Niconico.yaml",
    "Netflix": RULE_URL + "Netflix/Netflix.yaml",
    "myTVSUPER": RULE_URL + "myTVSUPER/myTVSUPER.yaml",
    "Microsoft": RULE_URL + "Microsoft/Microsoft.yaml",
    "Hulu": RULE_URL + "Hulu/Hulu.yaml",
    "HBO": RULE_URL + "HBO/HBO.yaml",
    "GoogleFCM": RULE_URL + "GoogleFCM/GoogleFCM.yaml",
    "Google": RULE_URL + "Google/Google.yaml",
    "Gits": RULE_URL + "Gits/Gits.yaml",
    "Games": RULE_URL + "Games/Games.yaml",
    "Dmm": RULE_URL + "Dmm/Dmm.yaml",
    "Disney": RULE_URL + "Disney/Disney.yaml",
    "DAZN": RULE_URL + "DAZN/DAZN.yaml",
    "Crypto": RULE_URL + "Crypto/Crypto.yaml",
    "Bahamut": RULE_URL + "Bahamut/Bahamut.yaml",
    "Abema": RULE_URL + "Abema/Abema.yaml",
    "Global": RULE_URL + "Global/Global.yaml",
    "GlobalMedia": RULE_URL + "GlobalMedia/GlobalMedia.yaml"
}
DIRECT_RULES = {
    "China": RULE_URL + "China/China.list",
    "China_Domain": RULE_URL + "China/China_Domain.list"
}

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

def load_file(rules_dict, file_dir):
    """
    下载规则文件
    """
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
        
    for key in rules_dict:
        response = requests.get(rules_dict[key], headers=HEADER)
        if response.status_code == 200:
            with open(f"./{file_dir}/{key}.list", "wb") as f:
                with response, io.BytesIO(response.content) as stream:
                    shutil.copyfileobj(stream, f)
            time.sleep(1)

def remove():
    """
    移除所有规则文件
    """
    shutil.rmtree("Proxy-Rule")
    shutil.rmtree("Direct-Rule")
    print("移除所有文件夹")

if __name__ == '__main__':
    remove()
    load_file(PROXY_RULES, "Proxy-Rule")
    load_file(DIRECT_RULES, "Direct-Rule")