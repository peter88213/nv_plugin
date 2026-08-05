"""Plugin template for novelibre.

Requires Python 3.7+
Copyright (c) Peter Triesberger
For further information see https://github.com/peter88213/nv_plugin
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from nvplugin.nvplugin_locale import _
# this should be the first import
from nvlib.controller.plugin.plugin_base import PluginBase


class Plugin(PluginBase):
    """plugin class."""
    VERSION = '@release'
    API_VERSION = '5.63'
    DESCRIPTION = 'Plugin'
    URL = 'https://github.com/peter88213/nv_plugin'
    HELP_SITE = 'https://peter88213.github.io/nv_plugin'
    HELP_PAGE = _('help')

    def install(self, model, view, controller):
        """Install the plugin at runtime.
        
        Positional arguments:
            model -- reference to the novelibre main model instance.
            view -- reference to the novelibre main view instance.
            controller -- reference to the novelibre main controller instance.

        Extends the superclass method.
        """
        super().install(model, view, controller)

        #--- Configure the user interface.

        self._add_help_menu_entry(_('nv_plugin plugin help'))

