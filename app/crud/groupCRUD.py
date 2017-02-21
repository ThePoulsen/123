## -*- coding: utf-8 -*-

from flask import session
from authAPI import authAPI

def getGroups(includes=None):
    if includes:
        includeString = '?'
        for r in includes:
            includeString = includeString + str(r) + str('=True&')
        return authAPI(endpoint='group'+includeString, method='get', token=session['token'])
    else:
        return authAPI(endpoint='group', method='get', token=session['token'])

def postGroup(dataDict):
    return authAPI(endpoint='group', method='post', dataDict=dataDict, token=session['token'])

def putGroup(dataDict, id):
    return authAPI(endpoint='group/'+str(id), method='put', dataDict=dataDict, token=session['token'])

def deleteGroup(id):
    return authAPI(endpoint='group/'+str(id), method='delete', token=session['token'])

def getGroup(id, includes=None):
    if includes:
        includeString = '?'
        for r in includes:
            includeString = includeString + str(r) + str('=True&')
        return authAPI(endpoint='group/'+str(id)+includeString, method='get', token=session['token'])
    else:
        return authAPI(endpoint='group/'+str(id), method='get', token=session['token'])

def checkGroup(groupName):
    groups = getGroups()['groups']
    exists = False
    for g in groups:
        if g['name'] == groupName:
            exists = True
    return exists
