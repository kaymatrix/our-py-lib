PyOne - Help
Kumaresan - Nov 18 2017


First time runner setup

- delete 'config.ini' file if present
- make sure no 'argument' attach to exe
- start the app and close the app
- will create 'userScripts' and config.ini
- setup 4 digit secret code and attach to argument of this exe
- start the app again
- open new file and run below command
print(dev.encrypt('4132'))
- get the value displayed in output 
- paste that value in 'config.ini' file for below mentioned setting
 decryptValue=9687
- make sure to add double quote for your value
eg: 
decryptValue=";67|8"
- save the config