# -*- coding: utf-8 -*-

from pymongo import MongoClient


def configure(app):
    client = MongoClient(app.config.get('DB_URI'))
    app.db = client[app.config.get('DB_NAME')]
