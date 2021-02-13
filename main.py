import ftplib

path = ' '
filename = ' '

ftp = ftplib.FTP( "192.168.0.12" )
ftp.login("admin", "admin")
ftp.cwd(path)
ftp.quit()