#!/usr/bin/env python

"""assignment groups module for SimpleMDMpy"""
#pylint: disable=invalid-name

import SimpleMDMpy.SimpleMDM

class AssignmentGroups(SimpleMDMpy.SimpleMDM.Connection):
    """assignment groups module for SimpleMDMpy"""
    def __init__(self, api_key):
        SimpleMDMpy.SimpleMDM.Connection.__init__(self, api_key)
        self.url = self._url("/assignment_groups")

    def get_assignment_groups(self, assignment_group_id="all"):
        """returns assignment group(s), defaults to all if none specified"""
        url = self.url
        if assignment_group_id != 'all':
            url = url + "/" + assignment_group_id
        return self._get_data(url)

    def create_assignment_group(self, name, auto_deploy):
        """creates an assignment group"""
        url = self.url
        data = {'name': name, 'auto_deploy': auto_deploy}
        return self._post_data(url, data)

    def delete_assignment_group(self, assignment_group_id):
        """delete an app to an assignment group"""
        url = self.url + "/" + assignment_group_id
        return self._delete_data(url)

    def assign_app(self, assignment_group_id, app_id, deployment_type, install_type):
        """assign app to an assignment group"""
        # deployment_type: 'standard' or 'munki'
        # install_type: 'managed', 'self_serve', 'default_installs' or 'managed_updates'
        # Defaults to managed.
        url = self.url + "/" + assignment_group_id + "/apps/" + app_id
        data = {'deployment_type': deployment_type, 'install_type': install_type}
        return self._post_data(url, data)

    def unassign_app(self, assignment_group_id, app_id):
        """unassign app to an assignment group"""
        url = self.url + "/" + assignment_group_id + "/apps/" + app_id
        return self._delete_data(url)

    def unassign_device_group(self, assignment_group_id, device_group_id):
        """delete a device group assignment"""
        url = self.url + "/" + assignment_group_id + "/device_groups/" + device_group_id
        return self._delete_data(url)

    def assign_device(self, assignment_group_id, device_id):
        """assign device to an assignment group"""
        url = self.url + "/" + assignment_group_id + "/devices/" + str(device_id)
        data = {}
        return self._post_data(url, data)

    def unassign_device(self, assignment_group_id, device_id):
        """unassign device to an assignment group"""
        url = self.url + "/" + assignment_group_id + "/devices/" + str(device_id)
        return self._delete_data(url)

    def push_apps(self, assignment_group_id):
        """push apps in an assignment group"""
        url = self.url + "/" + assignment_group_id + "/push_apps"
        data = {}
        return self._post_data(url, data)

    def update_apps(self, assignment_group_id):
        """update apps in an assignment group"""
        url = self.url + "/" + assignment_group_id + "/update_apps"
        data = {}
        return self._post_data(url, data)

    def assign_profile(self, assignment_group_id, profile_id):
        """assign profile to an assignment group"""
        url = self.url + "/" + assignment_group_id + "/profiles/" + str(profile_id)
        data = {}
        return self._post_data(url, data)
    
    def unassign_profile(self, assignment_group_id, profile_id):
        """unassign profile to an assignment group"""
        url = self.url + "/" + assignment_group_id + "/profiles/" + str(profile_id)
        return self._delete_data(url)
    
    def sync_profiles(self, assignment_group_id):
        """sync profiles in an assignment group"""
        url = self.url + "/" + assignment_group_id + "/sync_profiles"
        data = {}
        return self._post_data(url, data)
    
    def clone_assignment_group(self, assignment_group_id, name):
        """clone an assignment group"""
        url = self.url + "/" + assignment_group_id + "/clone"
        data = {'name': name}
        return self._post_data(url, data)