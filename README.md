# StarCraft II Coop Overlay (SCO)

This app looks for recent replays from StarCraft II Co-op, parses them and shows the information as overlay onscreen. Or it can be added as another layer in Open Broadcaster Software (OBS) or other streaming software applications.

The overlay is fully customizable through simple editing of the HTML file. Its style can be changed, new functions or elements can be added to the visible overlay (images, text, etc).

![Screenshot](/Screenshots/scr1.jpg)

# 
Download links: 
* [Mega](https://mega.nz/file/I4c3lAgA#YsF9dn9ORNXkBEQhabWN6jlSrrlkUy3ceLKDS6paQeM)
* [Google-drive](https://drive.google.com/file/d/1KPUrlmjnr1azPUGIXCMWM0337RLdJneI/view)
* Or run the script with Python

# How to use
1. Extract the archive
2. Run the executable
3. The app will show in the system tray after few seconds
4. Set in-game display mode to Windowed fullscreen (borderless)

![system tray](/Screenshots/systray.jpg)

![Screenshot](/Screenshots/Display.jpg)


* If you want it add it as overlay in OBS separatedly, add the HTML to your sources in OBS, and set its width and height to your screen resolution.


# Config file
**Changes take effect the next time you start the app!**

You don't need to change anything in the config file for normal usage.

* **Changing hotkeys for manual overlay display**

   KEY_SHOW = Ctrl+/
  
   KEY_HIDE = Ctrl+

* **Choosing players that will be preferably shown on top**

   PLAYER_NAMES = Maguro,SeaMaguro
  
* **Changing the duration for how long the overlay is visible when shown automatically (in seconds)**
  
   DURATION = 30
  
* **Hiding overlay. This can be useful if you want the overlay to be shown only in OBS or browser**  

   SHOWOVERLAY = False
  
* **If you want to change the folder where it looks for replays. But it should fine them alone.**

   ACCOUNTDIR = C:\Users\Maguro\Documents\StarCraft II\Accounts
   
* **If and only if these are set, analysed replays will be automatically uploaded to https://starcraft2coop.com/**

   AOM_NAME = Maguro (account name)

   AOM_SECRETKEY = .... (secret key generated on the site)
   
* **Some color customization directly via config file (deleting values resets to default)**

   P1COLOR = #0080F8
   
   P2COLOR = #00D532
   
   AMONCOLOR = #FF0000
   
   MASTERYCOLOR = #FFDC87
   
   ---

* **For debugging - how old replays it looks for in seconds.**

   REPLAYTIME = 60
   
* **For debugging - changes used port. The port also needs to be changed in the html layout.**

   PORT = 7305

* **For debugging - enables logging.**

   LOGGING = True



# Other notes
* You can edit the layout .html file. Changing its style through CSS or other formatting with javascript.
* [sc2reader](https://github.com/ggtracker/sc2reader) was used as replay parser.

# Change log
* 1.8 Replay analysis tweaks and improvements, start up notification, better logging, and bug fixes.

* 1.7 Colors can be changed via the config file. Bug fixes.

* 1.6 Added support for https://starcraft2coop.com

* 1.0 – 1.5 Initial versions
