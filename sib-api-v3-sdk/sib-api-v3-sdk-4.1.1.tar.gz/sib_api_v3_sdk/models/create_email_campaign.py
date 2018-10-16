# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from sib_api_v3_sdk.models.create_email_campaign_recipients import CreateEmailCampaignRecipients  # noqa: F401,E501
from sib_api_v3_sdk.models.create_email_campaign_sender import CreateEmailCampaignSender  # noqa: F401,E501


class CreateEmailCampaign(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'tag': 'str',
        'sender': 'CreateEmailCampaignSender',
        'name': 'str',
        'html_content': 'str',
        'html_url': 'str',
        'template_id': 'int',
        'scheduled_at': 'datetime',
        'subject': 'str',
        'reply_to': 'str',
        'to_field': 'str',
        'recipients': 'CreateEmailCampaignRecipients',
        'attachment_url': 'str',
        'inline_image_activation': 'bool',
        'mirror_active': 'bool',
        'recurring': 'bool',
        'type': 'str',
        'footer': 'str',
        'header': 'str',
        'utm_campaign': 'str',
        'params': 'object'
    }

    attribute_map = {
        'tag': 'tag',
        'sender': 'sender',
        'name': 'name',
        'html_content': 'htmlContent',
        'html_url': 'htmlUrl',
        'template_id': 'templateId',
        'scheduled_at': 'scheduledAt',
        'subject': 'subject',
        'reply_to': 'replyTo',
        'to_field': 'toField',
        'recipients': 'recipients',
        'attachment_url': 'attachmentUrl',
        'inline_image_activation': 'inlineImageActivation',
        'mirror_active': 'mirrorActive',
        'recurring': 'recurring',
        'type': 'type',
        'footer': 'footer',
        'header': 'header',
        'utm_campaign': 'utmCampaign',
        'params': 'params'
    }

    def __init__(self, tag=None, sender=None, name=None, html_content=None, html_url=None, template_id=None, scheduled_at=None, subject=None, reply_to=None, to_field=None, recipients=None, attachment_url=None, inline_image_activation=False, mirror_active=None, recurring=False, type=None, footer=None, header=None, utm_campaign=None, params=None):  # noqa: E501
        """CreateEmailCampaign - a model defined in Swagger"""  # noqa: E501

        self._tag = None
        self._sender = None
        self._name = None
        self._html_content = None
        self._html_url = None
        self._template_id = None
        self._scheduled_at = None
        self._subject = None
        self._reply_to = None
        self._to_field = None
        self._recipients = None
        self._attachment_url = None
        self._inline_image_activation = None
        self._mirror_active = None
        self._recurring = None
        self._type = None
        self._footer = None
        self._header = None
        self._utm_campaign = None
        self._params = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        self.sender = sender
        self.name = name
        if html_content is not None:
            self.html_content = html_content
        if html_url is not None:
            self.html_url = html_url
        if template_id is not None:
            self.template_id = template_id
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        self.subject = subject
        if reply_to is not None:
            self.reply_to = reply_to
        if to_field is not None:
            self.to_field = to_field
        if recipients is not None:
            self.recipients = recipients
        if attachment_url is not None:
            self.attachment_url = attachment_url
        if inline_image_activation is not None:
            self.inline_image_activation = inline_image_activation
        if mirror_active is not None:
            self.mirror_active = mirror_active
        if recurring is not None:
            self.recurring = recurring
        self.type = type
        if footer is not None:
            self.footer = footer
        if header is not None:
            self.header = header
        if utm_campaign is not None:
            self.utm_campaign = utm_campaign
        if params is not None:
            self.params = params

    @property
    def tag(self):
        """Gets the tag of this CreateEmailCampaign.  # noqa: E501

        Tag of the campaign  # noqa: E501

        :return: The tag of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this CreateEmailCampaign.

        Tag of the campaign  # noqa: E501

        :param tag: The tag of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def sender(self):
        """Gets the sender of this CreateEmailCampaign.  # noqa: E501


        :return: The sender of this CreateEmailCampaign.  # noqa: E501
        :rtype: CreateEmailCampaignSender
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this CreateEmailCampaign.


        :param sender: The sender of this CreateEmailCampaign.  # noqa: E501
        :type: CreateEmailCampaignSender
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

    @property
    def name(self):
        """Gets the name of this CreateEmailCampaign.  # noqa: E501

        Name of the campaign  # noqa: E501

        :return: The name of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateEmailCampaign.

        Name of the campaign  # noqa: E501

        :param name: The name of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def html_content(self):
        """Gets the html_content of this CreateEmailCampaign.  # noqa: E501

        Mandatory if htmlUrl and templateId are empty. Body of the message (HTML)  # noqa: E501

        :return: The html_content of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._html_content

    @html_content.setter
    def html_content(self, html_content):
        """Sets the html_content of this CreateEmailCampaign.

        Mandatory if htmlUrl and templateId are empty. Body of the message (HTML)  # noqa: E501

        :param html_content: The html_content of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._html_content = html_content

    @property
    def html_url(self):
        """Gets the html_url of this CreateEmailCampaign.  # noqa: E501

        Mandatory if htmlContent and templateId are empty. Url to the message (HTML)  # noqa: E501

        :return: The html_url of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._html_url

    @html_url.setter
    def html_url(self, html_url):
        """Sets the html_url of this CreateEmailCampaign.

        Mandatory if htmlContent and templateId are empty. Url to the message (HTML)  # noqa: E501

        :param html_url: The html_url of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._html_url = html_url

    @property
    def template_id(self):
        """Gets the template_id of this CreateEmailCampaign.  # noqa: E501

        Mandatory if htmlContent and htmlUrl are empty. Id of the SMTP template with status 'active'. Used to copy only its content fetched from htmlContent/htmlUrl to an email campaign for RSS feature.  # noqa: E501

        :return: The template_id of this CreateEmailCampaign.  # noqa: E501
        :rtype: int
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this CreateEmailCampaign.

        Mandatory if htmlContent and htmlUrl are empty. Id of the SMTP template with status 'active'. Used to copy only its content fetched from htmlContent/htmlUrl to an email campaign for RSS feature.  # noqa: E501

        :param template_id: The template_id of this CreateEmailCampaign.  # noqa: E501
        :type: int
        """

        self._template_id = template_id

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this CreateEmailCampaign.  # noqa: E501

        Sending UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.  # noqa: E501

        :return: The scheduled_at of this CreateEmailCampaign.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this CreateEmailCampaign.

        Sending UTC date-time (YYYY-MM-DDTHH:mm:ss.SSSZ). Prefer to pass your timezone in date-time format for accurate result.  # noqa: E501

        :param scheduled_at: The scheduled_at of this CreateEmailCampaign.  # noqa: E501
        :type: datetime
        """

        self._scheduled_at = scheduled_at

    @property
    def subject(self):
        """Gets the subject of this CreateEmailCampaign.  # noqa: E501

        Subject of the campaign  # noqa: E501

        :return: The subject of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CreateEmailCampaign.

        Subject of the campaign  # noqa: E501

        :param subject: The subject of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def reply_to(self):
        """Gets the reply_to of this CreateEmailCampaign.  # noqa: E501

        Email on which the campaign recipients will be able to reply to  # noqa: E501

        :return: The reply_to of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this CreateEmailCampaign.

        Email on which the campaign recipients will be able to reply to  # noqa: E501

        :param reply_to: The reply_to of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def to_field(self):
        """Gets the to_field of this CreateEmailCampaign.  # noqa: E501

        To personalize the «To» Field. If you want to include the first name and last name of your recipient, add {FNAME} {LNAME}. These contact attributes must already exist in your SendinBlue account. If input parameter 'params' used please use {{contact.FNAME}} {{contact.LNAME}} for personalization  # noqa: E501

        :return: The to_field of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._to_field

    @to_field.setter
    def to_field(self, to_field):
        """Sets the to_field of this CreateEmailCampaign.

        To personalize the «To» Field. If you want to include the first name and last name of your recipient, add {FNAME} {LNAME}. These contact attributes must already exist in your SendinBlue account. If input parameter 'params' used please use {{contact.FNAME}} {{contact.LNAME}} for personalization  # noqa: E501

        :param to_field: The to_field of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._to_field = to_field

    @property
    def recipients(self):
        """Gets the recipients of this CreateEmailCampaign.  # noqa: E501


        :return: The recipients of this CreateEmailCampaign.  # noqa: E501
        :rtype: CreateEmailCampaignRecipients
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this CreateEmailCampaign.


        :param recipients: The recipients of this CreateEmailCampaign.  # noqa: E501
        :type: CreateEmailCampaignRecipients
        """

        self._recipients = recipients

    @property
    def attachment_url(self):
        """Gets the attachment_url of this CreateEmailCampaign.  # noqa: E501

        Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps  # noqa: E501

        :return: The attachment_url of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._attachment_url

    @attachment_url.setter
    def attachment_url(self, attachment_url):
        """Sets the attachment_url of this CreateEmailCampaign.

        Absolute url of the attachment (no local file). Extension allowed: xlsx, xls, ods, docx, docm, doc, csv, pdf, txt, gif, jpg, jpeg, png, tif, tiff, rtf, bmp, cgm, css, shtml, html, htm, zip, xml, ppt, pptx, tar, ez, ics, mobi, msg, pub and eps  # noqa: E501

        :param attachment_url: The attachment_url of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._attachment_url = attachment_url

    @property
    def inline_image_activation(self):
        """Gets the inline_image_activation of this CreateEmailCampaign.  # noqa: E501

        Use true to embedded the images in your email. Final size of the email should be less than 4MB. Campaigns with embedded images can not be sent to more than 5000 contacts  # noqa: E501

        :return: The inline_image_activation of this CreateEmailCampaign.  # noqa: E501
        :rtype: bool
        """
        return self._inline_image_activation

    @inline_image_activation.setter
    def inline_image_activation(self, inline_image_activation):
        """Sets the inline_image_activation of this CreateEmailCampaign.

        Use true to embedded the images in your email. Final size of the email should be less than 4MB. Campaigns with embedded images can not be sent to more than 5000 contacts  # noqa: E501

        :param inline_image_activation: The inline_image_activation of this CreateEmailCampaign.  # noqa: E501
        :type: bool
        """

        self._inline_image_activation = inline_image_activation

    @property
    def mirror_active(self):
        """Gets the mirror_active of this CreateEmailCampaign.  # noqa: E501

        Use true to enable the mirror link  # noqa: E501

        :return: The mirror_active of this CreateEmailCampaign.  # noqa: E501
        :rtype: bool
        """
        return self._mirror_active

    @mirror_active.setter
    def mirror_active(self, mirror_active):
        """Sets the mirror_active of this CreateEmailCampaign.

        Use true to enable the mirror link  # noqa: E501

        :param mirror_active: The mirror_active of this CreateEmailCampaign.  # noqa: E501
        :type: bool
        """

        self._mirror_active = mirror_active

    @property
    def recurring(self):
        """Gets the recurring of this CreateEmailCampaign.  # noqa: E501

        For trigger campagins use false to make sure a contact receives the same campaign only once  # noqa: E501

        :return: The recurring of this CreateEmailCampaign.  # noqa: E501
        :rtype: bool
        """
        return self._recurring

    @recurring.setter
    def recurring(self, recurring):
        """Sets the recurring of this CreateEmailCampaign.

        For trigger campagins use false to make sure a contact receives the same campaign only once  # noqa: E501

        :param recurring: The recurring of this CreateEmailCampaign.  # noqa: E501
        :type: bool
        """

        self._recurring = recurring

    @property
    def type(self):
        """Gets the type of this CreateEmailCampaign.  # noqa: E501

        Type of the campaign  # noqa: E501

        :return: The type of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateEmailCampaign.

        Type of the campaign  # noqa: E501

        :param type: The type of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["classic", "trigger"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def footer(self):
        """Gets the footer of this CreateEmailCampaign.  # noqa: E501

        Footer of the email campaign  # noqa: E501

        :return: The footer of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._footer

    @footer.setter
    def footer(self, footer):
        """Sets the footer of this CreateEmailCampaign.

        Footer of the email campaign  # noqa: E501

        :param footer: The footer of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._footer = footer

    @property
    def header(self):
        """Gets the header of this CreateEmailCampaign.  # noqa: E501

        Header of the email campaign  # noqa: E501

        :return: The header of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this CreateEmailCampaign.

        Header of the email campaign  # noqa: E501

        :param header: The header of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def utm_campaign(self):
        """Gets the utm_campaign of this CreateEmailCampaign.  # noqa: E501

        Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed  # noqa: E501

        :return: The utm_campaign of this CreateEmailCampaign.  # noqa: E501
        :rtype: str
        """
        return self._utm_campaign

    @utm_campaign.setter
    def utm_campaign(self, utm_campaign):
        """Sets the utm_campaign of this CreateEmailCampaign.

        Customize the utm_campaign value. If this field is empty, the campaign name will be used. Only alphanumeric characters and spaces are allowed  # noqa: E501

        :param utm_campaign: The utm_campaign of this CreateEmailCampaign.  # noqa: E501
        :type: str
        """

        self._utm_campaign = utm_campaign

    @property
    def params(self):
        """Gets the params of this CreateEmailCampaign.  # noqa: E501

        Pass the set of attributes to customize the type classic campaign. For example, {'FNAME':'Joe', 'LNAME':'Doe'}. Only available if 'type' is 'classic'  # noqa: E501

        :return: The params of this CreateEmailCampaign.  # noqa: E501
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this CreateEmailCampaign.

        Pass the set of attributes to customize the type classic campaign. For example, {'FNAME':'Joe', 'LNAME':'Doe'}. Only available if 'type' is 'classic'  # noqa: E501

        :param params: The params of this CreateEmailCampaign.  # noqa: E501
        :type: object
        """

        self._params = params

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, CreateEmailCampaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
