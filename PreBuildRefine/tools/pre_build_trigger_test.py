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
from xml.etree import ElementTree
logging.basicConfig(level=logging.INFO)
def get_env(ev):
    return os.environ.get(ev)

def parse_xml(xml_file, project_list, branch='master'):
    os.chdir(get_env("WORKSPACE"))
    xml_path = os.path.join(get_env("WORKSPACE"), xml_file)
    root = ElementTree.parse(xml_path)

    default_branch = branch
    default_node = root.find('default')
    if default_node is not None:
        default_branch = default_node.get('revision')

    project_node = root.findall('project')
    for project_node_item in project_node:
        project_name = project_node_item.get('name')
        project_branch = default_branch
        if project_node_item.get('revision') is not None:
            project_branch = project_node_item.get('revision')
        project_list[project_name] = project_branch

    include_node = root.findall('include')
    for include_node_item in include_node:
        parse_xml(include_node_item.get("name"), project_list, default_branch)

    return project_list

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
print(os.environ.get('PYDIR'))