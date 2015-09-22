# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

"""
Hook which chooses an environment file to use based on the current context.

"""

from tank import Hook

class PickEnvironment(Hook):

    def execute(self, context, **kwargs):
        """
        The default implementation assumes there are three environments, called shot, asset 
        and project, and switches to these based on entity type.
        """

        if context.project is None:
            # our context is completely empty! 
            # don't know how to handle this case.
            return None
        
        if context.entity is None:
            # we have a project but not an entity
            return "Project"
        
        if context.entity and context.step:
            return context.entity["type"]

        return None

