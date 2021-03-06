# coding: utf-8

"""
    

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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
import re


class V1ResourceFieldSelector(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, container_name=None, resource=None, divisor=None):
        """
        V1ResourceFieldSelector - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'container_name': 'str',
            'resource': 'str',
            'divisor': 'str'
        }

        self.attribute_map = {
            'container_name': 'containerName',
            'resource': 'resource',
            'divisor': 'divisor'
        }

        self._container_name = container_name
        self._resource = resource
        self._divisor = divisor

    @property
    def container_name(self):
        """
        Gets the container_name of this V1ResourceFieldSelector.
        Container name: required for volumes, optional for env vars

        :return: The container_name of this V1ResourceFieldSelector.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """
        Sets the container_name of this V1ResourceFieldSelector.
        Container name: required for volumes, optional for env vars

        :param container_name: The container_name of this V1ResourceFieldSelector.
        :type: str
        """

        self._container_name = container_name

    @property
    def resource(self):
        """
        Gets the resource of this V1ResourceFieldSelector.
        Required: resource to select

        :return: The resource of this V1ResourceFieldSelector.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this V1ResourceFieldSelector.
        Required: resource to select

        :param resource: The resource of this V1ResourceFieldSelector.
        :type: str
        """

        self._resource = resource

    @property
    def divisor(self):
        """
        Gets the divisor of this V1ResourceFieldSelector.
        Specifies the output format of the exposed resources, defaults to \"1\"

        :return: The divisor of this V1ResourceFieldSelector.
        :rtype: str
        """
        return self._divisor

    @divisor.setter
    def divisor(self, divisor):
        """
        Sets the divisor of this V1ResourceFieldSelector.
        Specifies the output format of the exposed resources, defaults to \"1\"

        :param divisor: The divisor of this V1ResourceFieldSelector.
        :type: str
        """

        self._divisor = divisor

    def to_dict(self):
        """
        Returns the model properties as a dict
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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
