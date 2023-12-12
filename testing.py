import subprocess

spotify_path = r'AppData\\Roaming\\Spotify\\Spotify.exe' 
discord_path = r'C:\Users\D E L L\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk'
chrome_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe' 

input = input("Enter the application name: ").lower()

if input == "discord":
    subprocess.run(discord_path, shell=True)
elif input == "chrome":
    subprocess.run(chrome_path, shell=True)
elif input == "spotify":
    subprocess.run(spotify_path, shell=True)
else:
    print("Application not found")
    

