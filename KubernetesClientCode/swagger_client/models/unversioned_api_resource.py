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


class UnversionedAPIResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, namespaced=None, kind=None):
        """
        UnversionedAPIResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'namespaced': 'bool',
            'kind': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'namespaced': 'namespaced',
            'kind': 'kind'
        }

        self._name = name
        self._namespaced = namespaced
        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this UnversionedAPIResource.
        name is the name of the resource.

        :return: The name of this UnversionedAPIResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UnversionedAPIResource.
        name is the name of the resource.

        :param name: The name of this UnversionedAPIResource.
        :type: str
        """

        self._name = name

    @property
    def namespaced(self):
        """
        Gets the namespaced of this UnversionedAPIResource.
        namespaced indicates if a resource is namespaced or not.

        :return: The namespaced of this UnversionedAPIResource.
        :rtype: bool
        """
        return self._namespaced

    @namespaced.setter
    def namespaced(self, namespaced):
        """
        Sets the namespaced of this UnversionedAPIResource.
        namespaced indicates if a resource is namespaced or not.

        :param namespaced: The namespaced of this UnversionedAPIResource.
        :type: bool
        """

        self._namespaced = namespaced

    @property
    def kind(self):
        """
        Gets the kind of this UnversionedAPIResource.
        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

        :return: The kind of this UnversionedAPIResource.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this UnversionedAPIResource.
        kind is the kind for the resource (e.g. 'Foo' is the kind for a resource 'foo')

        :param kind: The kind of this UnversionedAPIResource.
        :type: str
        """

        self._kind = kind

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
