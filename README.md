# Send-Files-Over-LAN
Quick and dirty scripts to get files from one computer to another on a LAN

##Usage

1. Create a folder with all the files you want to send (sent files will be deleted)
2. Run Server.py from that folder
3. Edit the Client.py file and set `ip` to whatever the server ip is (run `ipconfig` to figure out ip address
4. Run Client.py on the computer that will be receiving the files
5. Enjoy your copied files :D

##Some Notes
- These are Python 2.7 Scripts
- This has only been tested on Windows. I don't recommend running this on Linux/Mac without checking the script.
