from django.db import models
from influxdb import InfluxDBClient, resultset
import re

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
        for where_key in ['eui', 'node_eui', 'gateway_eui']:
            if kwargs.get(where_key):
                where.append("{} = '{}'".format(where_key, kwargs[where_key]))
        if kwargs.get('time_span') and re.match('[0-9]+[a-zA-Z]+', kwargs['time_span']):
            where.append("time > now() - {}".format(kwargs['time_span']))
        if where:
            query += " WHERE " + " AND ".join(where)
        if 'group_by' in kwargs:
            query += " GROUP BY {}".format(kwargs['group_by'])
        if 'order_by' in kwargs:
            direction = 'DESC' if kwargs['order_by'].startswith('-') else 'ASC'
            key = kwargs['order_by'][1:] if kwargs['order_by'].startswith('-') else kwargs['order_by']
            query += " ORDER BY {} {}".format(key, direction)
        if 'limit' in kwargs:
            limit = kwargs['limit']
            if isinstance(limit, int) or limit.isdigit():
                limit = min(100, int(limit))
                query += " LIMIT {}".format(limit)
        if 'offset' in kwargs:
            offset = kwargs['offset']
            if isinstance(offset, int) or offset.isdigit():
                offset = min(100, int(offset))
                query += " OFFSET {}".format(offset)
        return query


class IFGateways(Influx):

    def get(self, eui=None, time_span=None, limit=20, offset=0, **kwargs):
        query = self.make_query(table='gateway_status',
                                eui=eui, time_span=time_span,
                                limit=limit, offset=offset, **kwargs)
        print("Q", query)
        result = self.client.query(query)
        return result


class IFNodes(Influx):

    def get(self, node_eui=None, time_span=None, limit=20, offset=0, **kwargs):
        query = self.make_query(table='rx_packets',
                                node_eui=node_eui, time_span=time_span,
                                limit=limit, offset=offset, **kwargs)
        print("Q", query)
        result = self.client.query(query)
        return result

