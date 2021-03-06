# coding: utf-8

"""
    ICFP Contest 2020 API

    See <a href='https://github.com/icfpcontest2020/aliens-proxy-protocol' target='_blank'>https://github.com/icfpcontest2020/aliens-proxy-protocol<a/>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class ProblemDescriptionDto(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'problem_id': 'str',
        'description': 'str'
    }

    attribute_map = {
        'problem_id': 'problemId',
        'description': 'description'
    }

    def __init__(self, problem_id=None, description=None, local_vars_configuration=None):  # noqa: E501
        """ProblemDescriptionDto - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._problem_id = None
        self._description = None
        self.discriminator = None

        self.problem_id = problem_id
        self.description = description

    @property
    def problem_id(self):
        """Gets the problem_id of this ProblemDescriptionDto.  # noqa: E501


        :return: The problem_id of this ProblemDescriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id):
        """Sets the problem_id of this ProblemDescriptionDto.


        :param problem_id: The problem_id of this ProblemDescriptionDto.  # noqa: E501
        :type: str
        """

        self._problem_id = problem_id

    @property
    def description(self):
        """Gets the description of this ProblemDescriptionDto.  # noqa: E501


        :return: The description of this ProblemDescriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProblemDescriptionDto.


        :param description: The description of this ProblemDescriptionDto.  # noqa: E501
        :type: str
        """

        self._description = description

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProblemDescriptionDto):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProblemDescriptionDto):
            return True

        return self.to_dict() != other.to_dict()
