from django.db import models
from influxdb import InfluxDBClient, resultset

from ttn_org import settings


class Influx:
    def __init__(self):
        self.client = InfluxDBClient(
            settings.API_INFLUX_HOST, settings.API_INFLUX_PORT,
            '', '', settings.API_INFLUX_DB)

    def make_query(self, table, **kwargs):
        fields = ", ".join(kwargs['fields']) if 'fields' in kwargs else "*"
        query = "SELECT {fields} FROM {table}".format(
            fields=fields, table=table)
        where = []
        if kwargs.get('eui'):
            where.append("eui = '{}'".format(kwargs['eui']))
        if kwargs.get('time_span'):
            where.append("time > now() - {}".format(kwargs['time_span']))
        if where:
            query += " WHERE " + " AND ".join(where)
        if 'limit' in kwargs:
            query += " LIMIT {}".format(kwargs['limit'])
        if 'offset' in kwargs:
            query += " OFFSET {}".format(kwargs['offset'])
        return query

    def remap(self, result):
        """Remap from InfluxDB format (tag, keys => [values]) to list of rows"""
        if isinstance(result, resultset.ResultSet):
            result = result.raw
        results = []
        for serie in result.get('series'):
            tags = serie.get('tags', {})
            columns = serie.get('columns')
            for row_values in serie.get('values'):
                item = tags.copy()
                for key, value in zip(columns, row_values):
                    item[key] = value
                results.append(item)
        return results


class IFGateways(Influx):

    def get(self, eui=None, time_span=None, limit=20, offset=0):
        query = self.make_query(table='gateway_status',
                                eui=eui, time_span=time_span,
                                limit=limit, offset=offset)
        print("Q", query)
        result = self.client.query(query)
        return self.remap(result)

