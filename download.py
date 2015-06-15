# download.py

import urllib.request


print("Downloading")
url = 'https://www.python.org/ftp/python/3.4.1/python-3.4.1.msi'
print('File Downloading')
urllib.request.urlretrieve(url, 'python-3.4.1.msi')
 
