# telegram_sender
Very easy telegram sender for windows (also work in Linux), can send photo, message and file, using official BotApi and system variables

Windows: 
  set TELEGRAM_API_KEY=API-KEY
  
  set CHAT_ID=Chat-ID

Linux: 

  export TELEGRAM_API_KEY=API-KEY
  
  export CHAT_ID=Chat-ID"

Usage:

  telegram_sender.exe --message Its, Works!!!
  
  telegram_sender.exe --photo C:\temp\picture.jpg
  
  telegram_sender.exe --file C:\temp\myfile.txt



*.exe file dont need any dependens in windows.
