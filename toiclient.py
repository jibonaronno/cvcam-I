from ftplib import FTP

ftp_ip = "ftp.toiconnect.net"
ftp_usr = "jibon@toiconnect.net"
ftp_pwd = "jibon@2021"

ftp_client = FTP(ftp_ip)
ftp_client.login(user=ftp_usr, passwd = ftp_pwd)

#ftp_client = FTP(ftp_ip)
#ftp_client.login(user=ftp_usr, passwd = ftp_pwd)

#ftp_client.cwd("image")
print("before upload\n", ftp_client.retrlines("LIST"))
file_path = "masud.jpg"
file_name = "masud.jpg"
file_stream = open(file_path,"rb")         # read file to send to byte

# send the file       
ftp_client.storbinary("{CMD} {FileName}".format(CMD="STOR",FileName="masud.jpg"),file_stream)     
file_stream.close()                     
print("after upload\n", ftp_client.retrlines("LIST"))
ftp_client.close
