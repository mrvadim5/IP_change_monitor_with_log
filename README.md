# IP_change_monitor_with_log
This program will check for external IP address changes and create a .txt in the event that it changes, logging the new address. Set to check every 300 seconds.
I currently have this program running with Task Scheduler with cmd and "/c python filepath.py".
Changing file extension to .pyw will allow it to run in the background. Otherwise a cmd window will remain open.
