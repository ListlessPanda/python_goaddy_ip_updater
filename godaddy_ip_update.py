import time
import json
import urllib
try:
    import requests
    import schedule
except:
    import os
    os.system('cmd /c "pip3 install requests"')
    os.system('cmd /c "pip3 install schedule"')
    del os
    import requests
    import schedule
    
class Bot:
    def __init__(self):
        try:
            print("Initilizing bot")            
            self.secret_key = ""
            self.public_key = ""
            self.domain_ip = "0.0.0.0"
            self.live_ip = "0.0.0.0"
            self.domain_name = ""
            self.minutes = 0
            self.read_json()
            print("Starting bot")
            self.loop()
        except Exception as err:
            print(err)
            raise Exception("Bot stopped")
    def __str__(self):
        return 'Bot:\nsecret_key={}\npublic_key={}\ndomain_ip={}\nlive_ip={}\ndomain_name={}\nminutes={}'.format(self.secret_key,self.public_key,self.domain_ip,self.live_ip,self.domain_name,self.minutes)
    
    def get_domain_ip(self):
        try:
            headers = {"Authorization":"sso-key {}:{}".format(self.public_key,self.secret_key)}
            url = "https://api.godaddy.com/v1/domains/{}/records/A/@".format(self.domain_name)
            response = requests.get(url, headers=headers)
            self.domainIP = test[0]['data']
            del response
            del headers
            del url
        except:
            raise Exception("Error occured getting domain IP")

    def internet_access(self):
        try:
            ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            del ip
            return True
        except:
            return False
        
    def update_live_ip(self):
        if(self.internet_access()):
            try:
                self.live_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
            except:
                raise Exception("Error occured getting current live IP")
        else:
            raise Exception("No Internet Access")
    
    def compare_ip(self):
        try:
            self.update_domain_ip()
            self.update_live_ip()
            if(self.domain_ip != self.live_ip):
                try:
                    self.update_domain_ip()
                except Exception as err:
                    print(err)       
        except Exception as err:
            print(err)
    
    def update_domain_ip(self):
        print("Updating domain IP")
        print("Current domain IP: {}".format(self.live_ip))
        try:
            url = "https://api.godaddy.com/v1/domains/{}/records/A/@".format(self.domain_name)           
            payload = json.dumps([{"data": self.live_ip}])            
            headers = {
            'Authorization': 'sso-key {}:{}'.format(self.public_key,self.secret_key),
            'Content-Type': 'application/json'
            }
            response = requests.request("PUT", url, headers=headers, data=payload)
            self.domain_ip = self.live_ip
            print("New domain IP: {}".format(self.domain_ip))
        except:
            raise Exception("Error occured updating domain IP to live IP")        
    
    def loop(self):
        while True:
            self.compare_ip()
            for x in range(self.minutes):
                print("{} minutes until next check          ".format(self.minutes),end="\r")
                time.sleep(60)
                    
    
    def read_json(self):
        try:
            with open("config.json") as f:
                config = json.load(f)
                self.domain_name = config['domain_name']
                self.secret_key = config['secret_key']
                self.public_key = config['public_key']
                self.minutes = config['minutes']
        except:
            raise Exception("Config file error")
        

        
if __name__ == "__main__":
    try:
        bot = Bot()
        print(bot)
    except Exception as err:
        print(err)  
