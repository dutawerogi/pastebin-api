import urllib.parse
import urllib.request
 
url = "http://pastebin.com/api/api_post.php"
values = {'api_option' : 'paste',
          'api_dev_key' : 'Dev Key Here',
          'api_paste_code' : 'dank python create paste test kappa',
          'api_paste_private' : '0',
          'api_paste_name' : 'NameHere.php',
          'api_paste_expire_date' : 'N',
          'api_paste_format' : 'python',
          'api_user_key' : 'User Key Here',
          'api_paste_name' : 'NameHere.php',
          'api_paste_code' : 'dank python create paste test kappa'}
 
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be bytes
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
   the_page = response.read()
print(the_page)
