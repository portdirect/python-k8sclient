# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1CephFSVolumeSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'monitors': 'list[str]',
            'path': 'str',
            'user': 'str',
            'secret_file': 'str',
            'secret_ref': 'V1LocalObjectReference',
            'read_only': 'bool'
        }

        self.attribute_map = {
            'monitors': 'monitors',
            'path': 'path',
            'user': 'user',
            'secret_file': 'secretFile',
            'secret_ref': 'secretRef',
            'read_only': 'readOnly'
        }

        self._monitors = None
        self._path = None
        self._user = None
        self._secret_file = None
        self._secret_ref = None
        self._read_only = None

    @property
    def monitors(self):
        """
        Gets the monitors of this V1CephFSVolumeSource.
        Required: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :return: The monitors of this V1CephFSVolumeSource.
        :rtype: list[str]
        """
        return self._monitors

    @monitors.setter
    def monitors(self, monitors):
        """
        Sets the monitors of this V1CephFSVolumeSource.
        Required: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :param monitors: The monitors of this V1CephFSVolumeSource.
        :type: list[str]
        """
        self._monitors = monitors

    @property
    def path(self):
        """
        Gets the path of this V1CephFSVolumeSource.
        Optional: Used as the mounted root, rather than the full Ceph tree, default is /

        :return: The path of this V1CephFSVolumeSource.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this V1CephFSVolumeSource.
        Optional: Used as the mounted root, rather than the full Ceph tree, default is /

        :param path: The path of this V1CephFSVolumeSource.
        :type: str
        """
        self._path = path

    @property
    def user(self):
        """
        Gets the user of this V1CephFSVolumeSource.
        Optional: User is the rados user name, default is admin More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :return: The user of this V1CephFSVolumeSource.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this V1CephFSVolumeSource.
        Optional: User is the rados user name, default is admin More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :param user: The user of this V1CephFSVolumeSource.
        :type: str
        """
        self._user = user

    @property
    def secret_file(self):
        """
        Gets the secret_file of this V1CephFSVolumeSource.
        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :return: The secret_file of this V1CephFSVolumeSource.
        :rtype: str
        """
        return self._secret_file

    @secret_file.setter
    def secret_file(self, secret_file):
        """
        Sets the secret_file of this V1CephFSVolumeSource.
        Optional: SecretFile is the path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :param secret_file: The secret_file of this V1CephFSVolumeSource.
        :type: str
        """
        self._secret_file = secret_file

    @property
    def secret_ref(self):
        """
        Gets the secret_ref of this V1CephFSVolumeSource.
        Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :return: The secret_ref of this V1CephFSVolumeSource.
        :rtype: V1LocalObjectReference
        """
        return self._secret_ref

    @secret_ref.setter
    def secret_ref(self, secret_ref):
        """
        Sets the secret_ref of this V1CephFSVolumeSource.
        Optional: SecretRef is reference to the authentication secret for User, default is empty. More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :param secret_ref: The secret_ref of this V1CephFSVolumeSource.
        :type: V1LocalObjectReference
        """
        self._secret_ref = secret_ref

    @property
    def read_only(self):
        """
        Gets the read_only of this V1CephFSVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :return: The read_only of this V1CephFSVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1CephFSVolumeSource.
        Optional: Defaults to false (read/write). ReadOnly here will force the ReadOnly setting in VolumeMounts. More info: http://releases.k8s.io/release-1.2/examples/cephfs/README.md#how-to-use-it

        :param read_only: The read_only of this V1CephFSVolumeSource.
        :type: bool
        """
        self._read_only = read_only

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()