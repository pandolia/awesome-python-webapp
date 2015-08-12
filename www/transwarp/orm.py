#!/user/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
Database operation module.
This mudule is independent with web module.
'''

import time, logging
import db

class Field(object):
    _count = 0

    def __init__(self, **kw):
        self.name = kw.get('name', None)
        self._default = kw.get('default', None)
        self.primary_key = kw.get('primary_key', False)
        self.nullable = kw.get('nullable', False)
        self.updatable = kw.get('updatable', True)
        self.insertable = kw.get('insertable', True)
        self.ddl = kw.get('ddl', '')
        self._order = Field._count
        Field._count = Field._count + 1

    @property
    def default(self):
        d = self._default
        return d() if callable(d) else d    

    def __str__(self):
        s = [ '<%s:%s,%s,default(%s),' % \
                ( self.__class__.__name__, self.name, \
                  self.ddl, self._default ) ]
        self.nullable and s.append('N')
        self.updatable and s.append('U')
        self.insertable and s.append('I')
        s.append('>')
        return ''.join(s)

class StringField(Field):
    def __init__(self, **kw):
        if 'default' not in kw:
            kw['default'] = ''

        if 'ddl' not in kw:
            kw['ddl'] = 'varchar(255)'

        super(StringField, self).__init__(**kw)

class IntegerField(Field):
    def __init__(self, **kw):
        if 'default' not in kw:
            kw['default'] = 0

        if 'ddl' not in kw:
            kw['ddl'] = 'bigint'

        super(IntegerField, self).__init__(**kw)

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        mappings = dict()
        name_lower = name.lower()

        create_sql = 'create table %s (\n' % name_lower
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                mappings[k] = v
                create_sql += '    %s %s,\n' % (v.name, v.column_type)
        create_sql = create_sql.strip(',\n')
        create_sql += '\n)'
        print create_sql

        for k in mappings.iterkeys():
            attrs.pop(k)

        attrs['__table__'] = name_lower
        attrs['__mapping__'] = mappings

        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mapping__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % \
                    (self.__table__, ','.join(fields), ','.join(params))

        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
u.save()

