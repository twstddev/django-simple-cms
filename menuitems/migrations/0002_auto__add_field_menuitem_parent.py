# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MenuItem.parent'
        db.add_column(u'menuitems_menuitem', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['menuitems.MenuItem'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MenuItem.parent'
        db.delete_column(u'menuitems_menuitem', 'parent_id')


    models = {
        u'menuitems.menuitem': {
            'Meta': {'object_name': 'MenuItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['menuitems.MenuItem']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['menuitems']