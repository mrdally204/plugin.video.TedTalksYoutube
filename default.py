# -*- coding: utf-8 -*-
#------------------------------------------------------------
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.TedTalksYoutube'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')
icon = local.getAddonInfo('icon')
fanart = local.getAddonInfo('fanart')

# Entry point
def run():
    plugintools.log("TedTalks.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("TedTalks.main_list "+repr(params))
    
    plugintools.add_item( 
        title="Latest Talks",
        url="plugin://plugin.video.youtube/user/TEDtalksDirector/",
        thumbnail=icon,
        folder=True )

    plugintools.add_item( 	
       title="TEDx Talks",
       url="plugin://plugin.video.youtube/channel/UCsT0YIqwnpJCM-mx7-gSA4Q/",
       thumbnail=icon,
       folder=True )		
	   
    plugintools.add_item( 	
       title="TED-Ed",
       url="plugin://plugin.video.youtube/channel/UCsooa4yRKGN_zEE8iknghZA/",
       thumbnail=icon,
       folder=True )		
	   
    plugintools.add_item( 	
       title="TEDxYouth",
       url="plugin://plugin.video.youtube/channel/UC-yTB2bUcin9mmah36sXiYA/",
       thumbnail=icon,
       folder=True )		

    plugintools.add_item( 	
       title="TEDFellowsTalks",
       url="plugin://plugin.video.youtube/channel/UCBjBZmguQzn6WCYR7DQykLw/",
       thumbnail=icon,
       folder=True )	
	   
    plugintools.add_item( 	
       title="TEDPartners",
       url="plugin://plugin.video.youtube/channel/UCDAdYdnCDt9zx3p3e_78lEQ/",
       thumbnail=icon,
       folder=True )	
    
run()