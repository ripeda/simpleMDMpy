#!/usr/bin/env python

""" Custom Configuration Profiles module """
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class CustomConfigurationProfiles(SimpleMDMpy.SimpleMDM.Connection):
    """work with custom profiles"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/custom_configuration_profiles")

    def get_profiles(self):
        """returns profiles"""
        url = self.url
        return self._get_data(url)

    def create_profile(self, name, mobileconfig, user_scope=None, attribute_support=False):
        """upload a config file"""
        url = self.url
        data = {'name': name}
        files = {'mobileconfig': open(mobileconfig, 'rb')}
        if user_scope:
            data['user_scope'] = user_scope
        if attribute_support:
            data['attribute_support'] = attribute_support
        return self._post_data(url, data, files)

    def update_profile(self, profile_id, name=None, mobileconfig=None, # pylint: disable=too-many-arguments
        user_scope=None, attribute_support=None):
        """update a config file"""
        url = self.url + "/" + profile_id
        data = {}
        files = {}
        if name:
            data['name'] = name
        if mobileconfig:
            files['mobileconfig'] = open(mobileconfig, 'rb')
        if user_scope:
            data['user_scope'] = user_scope
        if attribute_support:
            data['attribute_support'] = attribute_support
        return self._patch_data(url, data, files)


    def delete_profile(self, profile_id):
        """deletes custom profile"""
        url = self.url + "/" + profile_id
        return self._delete_data(url)

