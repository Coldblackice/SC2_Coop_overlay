# StarCraft II Coop Overlay (SCO)

This app looks for recent replays from StarCraft II Co-op, parses them and shows the information as overlay onscreen. Or it can be added as another layer in Open Broadcaster Software (OBS) or other streaming software applications.

The overlay is fully customizable through simple editing of the HTML file. Its style can be changed, new functions or elements can be added to the visible overlay (images, text, etc).

**Download links:** 
* [Mega](https://mega.nz/file/ZgUUXawC#RGx3PNTP6-slkwwffK9pAkCNsjHkhP2tc1RKt3JqQIM)
* [Google-drive](https://drive.google.com/file/d/1uRO_pXjpXF6E3f89S7LjaGpdwRjzQ0Gy/view)
* Or run the script with Python

![Screenshot](/Screenshots/wide2.jpg)

# How to use
1. Extract the archive
2. Run the executable
3. The app will show in the system tray after few seconds
4. Set in-game display mode to Windowed fullscreen (borderless)

![system tray](/Screenshots/systray.jpg)

![Screenshot](/Screenshots/Display.jpg)


* If you want it add it as overlay in OBS separatedly, add the HTML to your sources in OBS, and set its width and height to your screen resolution.


# Config file

You don't need to change anything in the config file for normal usage.

Changes take effect the next time you start the app!

* **Changing hotkeys for manual overlay display**

   KEY_SHOW = Ctrl+/

* **Changing hotkeys for moving between replays**

   KEY_NEWER = Alt+/
  
   KEY_OLDER = Alt+*

* **Changing the duration for how long the overlay is visible when shown automatically (in seconds)**
  
   DURATION = 30

* **Choose which monitor to show the overlay on (for multi-monitor setups).**
  
   MONITOR = 1
 
* **If and only if these are set, analysed replays will be automatically uploaded to https://starcraft2coop.com/**

   AOM_NAME = Maguro (account name)

   AOM_SECRETKEY = .... (secret key generated on the site)
   
* **Some color customization directly via config file (deleting values resets to default)**

   P1COLOR = #0080F8
   
   P2COLOR = #00D532
   
   AMONCOLOR = #FF0000
   
   MASTERYCOLOR = #FFDC87
   
* **If it has trouble finding replays, specify the folder directly.**

   ACCOUNTDIR = C:\Users\Maguro\Documents\StarCraft II\Accounts

* **Prevents the from showing. You can still add it to OBS, or open in an internet browser.**  

   SHOWOVERLAY = False 
   
* **Choosing players that will be preferably shown on top.**

   PLAYER_NAMES = Maguro,SeaMaguro
   
   Note: App will automatically identify common players after some time if none players are specified here.   
   
* **This lets you have a different hotkey for showing and hiding the overlay**  

   UNIFIEDHOTKEY = False   
     
   KEY_HIDE = Ctrl+*
   
* **For debugging - changes used port. The port also needs to be changed in the html layout.**

   PORT = 7305

* **For debugging - enables logging.**

   LOGGING = True



# Other notes
* The overlay targets Windows 10. It might not work correctly on older versions of windows (black background under overlay). On Windows 7 you can try enabling aero theme, it might help.
* Some anti-virus programs are very sensitive to packaged python apps. If you have issues, add an exception for the file and the directory.
* Kills are shown for top 5 units only (this can by changed in HTML).
* You can edit the layout .html file. Changing its style through CSS or other formatting with javascript.
* [sc2reader](https://github.com/ggtracker/sc2reader) and s2protocol were used to parse replays.

# Changelog
* 1.14 version

      - The number of created Infested Bunkers and Mecha Infestors is shown as icons
      - Gary won't show created and lost numbers as they are not accurate (as with Tychus' outlaws)
      - Odin's precursor no longer counted for created & lost numbers
      - Perdition and Devastation Turrets renamed to Flaming Betties and Blaster Billies
      - Easier customization via separate CSS and JS files for custom modifications
      - Internal reorganization of dictionaries, and many comments added to the code
      - Proper HH:MM:SS format for game length for games over 60 minutes
      - Minor visual tweaks
      

* 1.13 version

      - Additional icons showing structures destroyed on Dead of Night and certain mutator kills:
        Void Rifts, Propagators, Void Reanimators, Turkeys, Mines, HftS & TUS, units sacrified to Killbots
      - APM rescaled according to accurate replay length 
      - Stats no longer contain events that happened during victory cutscenes (e.g. Cradle of Death)
      - Tweaks to replay analysis (Nova airstrike,...)

* 1.12 version

      - Masteries identified in [MM] maps
      - Automatic identification of preferred players if none are specified
      - Game length more accurate and close to speedrunning times instead of the replay length
      - Better way to find documents folder
      - Tweaks to enemy composition identification
      - Small fixes for replay analysis in custom mutations

* 1.11 version

      - Identifying enemy unit composition (best guess)
      - By default there is a single key to show/hide overlay (possible to change by user)
      - Minor graphical tweaks

* 1.10 version

      - Multimonitor support
      - Showing Outlaw order for Tychus
      - Start up notification shows hotkeys and if an update is available
      - Shows games even without any kills

* 1.9 version

      - It's now possible to view analysis of older replays and switch between them freely
      - Fixed the issue where the replay folder wasn't located correctly on certain systems
      - Replay analysis tweaked for more accurate stats
      - Overlay shows map played & winrate in the current session
      - Minor graphical tweaks
      - Small tweaks to sc2reader module to prevent load fails

* 1.8 version

      - Replay analysis tweaks and improvements
      - Start up notification
      - Better logging
      - Bug fixes

* 1.7  version

      - Colors can be changed via the config file
      - Bug fixes

* 1.6 version

      - Replays can be automatically uploaded to https://starcraft2coop.com

* 1.0 – 1.5 initial versions
