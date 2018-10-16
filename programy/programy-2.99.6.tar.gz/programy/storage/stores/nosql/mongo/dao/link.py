"""
Copyright (c) 2016-2018 Keith Sterling http://www.keithsterling.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from programy.storage.stores.utils import DAOUtils

class Link(object):

    def __init__(self, primary_user, generated_key, provided_key, expired=None, expires=None):
        self.id = None
        self.primary_user = primary_user
        self.generated_key = generated_key
        self.provided_key = provided_key
        self.expired = expired
        self.expires = expires

    def __repr__(self):
        return "<Linked(id='%d', primary='%s', generated='%s', provided='%s', expired='%s', expires='%s')>" % (
            DAOUtils.valid_id(self.id),
            self.primary_user,
            self.generated_key,
            self.provided_key,
            DAOUtils.valid_id(self.expired),
            DAOUtils.valid_id(self.expires))

    def to_document(self):
        document = {"primary_user": self.primary_user,
                    "generated_key": self.generated_key,
                    "provided_key": self.provided_key,
                    "expired": self.expired,
                    "expires": self.expires}
        if self.id is not None:
            document['_id'] = self.id
        return document

    @staticmethod
    def from_document(data):
        link = Link(None, None, None)
        if '_id' in data:
            link.id = data['_id']
        if 'primary_user' in data:
            link.primary_user = data['primary_user']
        if 'generated_key' in data:
            link.generated_key = data['generated_key']
        if 'provided_key' in data:
            link.provided_key = data['provided_key']
        if 'expired' in data:
            link.expired = data['expired']
        if 'expires' in data:
            link.expires = data['expires']
        return link