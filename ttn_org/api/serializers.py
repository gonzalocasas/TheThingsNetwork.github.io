from django.contrib.auth.models import User, Group
from rest_framework import serializers
from influxdb import resultset
import base64
import json
import bson


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'date_joined')


class InfluxSerializer:

    def remap(self, result, sort_key=None):
        """Remap from InfluxDB format (tag, keys => [values]) to list of rows"""
        if isinstance(result, resultset.ResultSet):
            result = result.raw
        results = []
        for serie in result.get('series', {}):
            tags = serie.get('tags', {})
            columns = serie.get('columns', {})
            for row_values in serie.get('values'):
                item = tags.copy()
                for key, value in zip(columns, row_values):
                    item[key] = value
                results.append(item)
        # InfluxDB sorting is weird. Let's fix the order
        if sort_key:
            reverse = False
            if sort_key[:1] == '-':
                reverse = True
                sort_key = sort_key[1:]
            results = sorted(results, key=lambda k: k.get(sort_key), reverse=reverse)
        return results

    def annotate(self, rows):
        for i, row in enumerate(rows):
            if 'raw_data' in row:
                rows[i]['data_raw'] = rows[i].pop('raw_data')
            if 'data' in row:
                try:
                    rows[i]['data_plain'] = base64.b64decode(row['data']).decode()
                except Exception as e:
                    pass
            if 'data_plain' in row:
                try:
                    rows[i]['data_json'] = json.loads(row['data_plain'])
                    pass
                except Exception as e:
                    pass
        return rows


class MongoSerializer:

    def remap(self, result, sort_key=None):
        """Remap from MongoDB format (tag, keys => [values]) to list of rows"""
        _rename = {'nodeeui': 'node_eui', 'gatewayeui': 'gateway_eui',
                   'rawdata': 'data_raw'}
        for i, item in enumerate(result):
            keys = item.keys() # will change during loop
            for key in keys:
                if isinstance(item[key], bson.ObjectId):
                    result[i][key] = str(item[key])
                elif key in _rename:
                    result[i][_rename[key]] = result[i].pop(key)
        return result

    def annotate(self, rows):
        for i, row in enumerate(rows):
            if 'data' in row:
                try:
                    rows[i]['data_plain'] = base64.b64decode(row['data']).decode()
                except Exception as e:
                    pass
            if 'data_plain' in row:
                try:
                    rows[i]['data_json'] = json.loads(row['data_plain'])
                    pass
                except Exception as e:
                    pass
        return rows

