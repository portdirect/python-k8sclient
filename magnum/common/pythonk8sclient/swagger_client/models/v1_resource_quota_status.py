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


class V1ResourceQuotaStatus(object):
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
            'hard': 'str',
            'used': 'str'
        }

        self.attribute_map = {
            'hard': 'hard',
            'used': 'used'
        }

        self._hard = None
        self._used = None

    @property
    def hard(self):
        """
        Gets the hard of this V1ResourceQuotaStatus.
        hard is the set of enforced hard limits for each named resource; see http://releases.k8s.io/v1.0.4/docs/design/admission_control_resource_quota.md#admissioncontrol-plugin-resourcequota

        :return: The hard of this V1ResourceQuotaStatus.
        :rtype: str
        """
        return self._hard

    @hard.setter
    def hard(self, hard):
        """
        Sets the hard of this V1ResourceQuotaStatus.
        hard is the set of enforced hard limits for each named resource; see http://releases.k8s.io/v1.0.4/docs/design/admission_control_resource_quota.md#admissioncontrol-plugin-resourcequota

        :param hard: The hard of this V1ResourceQuotaStatus.
        :type: str
        """
        self._hard = hard

    @property
    def used(self):
        """
        Gets the used of this V1ResourceQuotaStatus.
        used is the current observed total usage of the resource in the namespace

        :return: The used of this V1ResourceQuotaStatus.
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this V1ResourceQuotaStatus.
        used is the current observed total usage of the resource in the namespace

        :param used: The used of this V1ResourceQuotaStatus.
        :type: str
        """
        self._used = used

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