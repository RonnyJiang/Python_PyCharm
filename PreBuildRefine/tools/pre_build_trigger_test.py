#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 @desc:
 @author: ronny
 @contact: set@aliyun.com
 @site: www.lemon.pub
 @software: PyCharm  @since:python 3.5.2(32bit) on 2016/11/24.19:01
"""
import os,logging,re
logging.basicConfig(level=logging.INFO)
def get_env(ev):
    return os.environ.get(ev)

def get_profile_list(content):
    profile_list = {}
    rex_noGroup = "repo_xml=.+\s+repo_config_path=.+\s*"
    rex_namedGroup = "repo_xml=(?P<xml>.+)\s+repo_config_path=(?P<trigger_config_path>.+)\s*"
    total_xml = re.findall(rex_noGroup, content)
    print('------------total_xml----------:',total_xml)

    for index,one_xml in enumerate(total_xml):
        logging.info("index=%s(%s)" % (index,one_xml))
        result = re.search(rex_namedGroup, one_xml)
        print('result:',result,'result.group():',result.group(),'result.group(1):',result.group(1),'result.group(2)',result.group(2))
        print('---mingminggroup----',result.group('xml'),result.group('trigger_config_path'))
        profile_list[result.group('xml')] = result.group('trigger_config_path')


    print('list:',profile_list)
    return profile_list

env = '''repo_xml=venus_aurora.xml
repo_config_path=/var/ftpd/incoming/pre_build_config/venus_aurora_trigger_config
repo_xml=minidvb_seperate_zx2000_cherry.xml
repo_config_path=/var/ftpd/incoming/pre_build_config/minidvb_trigger_config
repo_xml=zx2000.xml
repo_config_path=/var/ftpd/incoming/pre_build_config/zx2000_durian_trigger_config
repo_xml=apps_hubei.xml
repo_config_path=/var/ftpd/incoming/pre_build_config/app_hubei_trigger_config
repo_xml=apps_elite1000_banana.xml
repo_config_path=/var/ftpd/incoming/pre_build_config/app_elite1000_trigger_config
repo_xml=apps_aurora.xml
repo_config_path=/var/ftpd/incoming/pre_build_config/app_aurora_trigger_config'''

# print(env)


get_profile_list(env)
