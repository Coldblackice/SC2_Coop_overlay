# StarCraft II Coop Overlay (SCO)

This app looks for recent replays from StarCraft II Co-op, parses them and shows the information as overlay onscreen. Or it can be added as another layer in Open Broadcaster Software (OBS) or other streaming software applications.

![Screenshot](/Screenshots/scr1.jpg)

# 
Download links: 
* [Mega](https://mega.nz/file/QpFjDSRJ#DvHCKvK4gI72JoVwTfhI2p2VeL-CAymNnkhY0QJ-WpU)
* [Google-drive](https://drive.google.com/file/d/11Jgk8qFB0x0RAWNoYhKd08nH0U7wlQMC/view?usp=sharing)
* Or run the script with Python

# How to use
1. Extract the archive
2. Run the executable
3. The app will show in the system tray after few seconds
4. Play StarCraft II Co-op

![system tray](/Screenshots/systray1.png)

* If you want it add it as overlay in OBS separatedly, add the HTML to your sources in OBS, and set its width and height to your screen resolution.


# Config file
**Changes take effect when you start the app next time!**

You don't need to change anything in the config file for normal usage.

* Hotkeys for manually showing the overlay can be changed here. Althought overlay will automatically show after the game.

  **KEY_SHOW = Ctrl+/**
  
  **KEY_HIDE = Ctrl+***

* If you want to change how long the overlay is visible when shown automatically, set the duration to a different number of seconds.

  **DURATION = 30**
  
* If you don't want to see overlay on your screen, you can disable it. You might be using it only as OBS overlay.

  **SHOWOVERLAY = False**
  
* If you want your name to be always on the top, list your in-game player names in the config file. For example:

  **PLAYER_NAMES = Maguro,SeaMaguro**

* If the app won't find your replays correctly, you can set the folder path manually. All file and subfolders will be searched for new replays. For example:

  **ACCOUNTDIR = C:\Users\Maguro\Documents\StarCraft II\Accounts**

# Other notes
* It works with both borderless and fullscreen mode in StarCraft II.
* I haven't tested it with non-English versions of the game.
* You can edit the layout .html file. Changing its style through CSS or other formatting with javascript.
* [sc2reader](https://github.com/ggtracker/sc2reader) was used as replay parser.
