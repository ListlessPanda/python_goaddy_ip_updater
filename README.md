# python_godaddy_ip_update
 Python script to update domain IP for godaddy

1. Get an API key at : https://developer.godaddy.com/ and make sure it's a Production type
2. Copy config_default.json file and rename it to config.json
3. Setup the config.json

 - domain_name is the name of the site (excluding www/http) ie. google.co.za
 - secret_key is a key given by godaddy
 - public_key is a key given by godaddy
 - minutes is the amount of minutes between checks ie. 60
