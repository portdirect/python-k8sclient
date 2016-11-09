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


class V1ReplicationControllerSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, replicas=None, selector=None, template=None):
        """
        V1ReplicationControllerSpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'replicas': 'int',
            'selector': 'object',
            'template': 'V1PodTemplateSpec'
        }

        self.attribute_map = {
            'replicas': 'replicas',
            'selector': 'selector',
            'template': 'template'
        }

        self._replicas = replicas
        self._selector = selector
        self._template = template

    @property
    def replicas(self):
        """
        Gets the replicas of this V1ReplicationControllerSpec.
        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: http://releases.k8s.io/release-1.4/docs/user-guide/replication-controller.md#what-is-a-replication-controller

        :return: The replicas of this V1ReplicationControllerSpec.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1ReplicationControllerSpec.
        Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: http://releases.k8s.io/release-1.4/docs/user-guide/replication-controller.md#what-is-a-replication-controller

        :param replicas: The replicas of this V1ReplicationControllerSpec.
        :type: int
        """

        self._replicas = replicas

    @property
    def selector(self):
        """
        Gets the selector of this V1ReplicationControllerSpec.
        Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: http://releases.k8s.io/release-1.4/docs/user-guide/labels.md#label-selectors

        :return: The selector of this V1ReplicationControllerSpec.
        :rtype: object
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1ReplicationControllerSpec.
        Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: http://releases.k8s.io/release-1.4/docs/user-guide/labels.md#label-selectors

        :param selector: The selector of this V1ReplicationControllerSpec.
        :type: object
        """

        self._selector = selector

    @property
    def template(self):
        """
        Gets the template of this V1ReplicationControllerSpec.
        Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. More info: http://releases.k8s.io/release-1.4/docs/user-guide/replication-controller.md#pod-template

        :return: The template of this V1ReplicationControllerSpec.
        :rtype: V1PodTemplateSpec
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this V1ReplicationControllerSpec.
        Template is the object that describes the pod that will be created if insufficient replicas are detected. This takes precedence over a TemplateRef. More info: http://releases.k8s.io/release-1.4/docs/user-guide/replication-controller.md#pod-template

        :param template: The template of this V1ReplicationControllerSpec.
        :type: V1PodTemplateSpec
        """

        self._template = template

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
