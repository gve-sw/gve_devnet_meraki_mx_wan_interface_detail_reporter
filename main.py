""" Copyright (c) 2021 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
           https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied. 
"""

import meraki
import config
import pprint
import csv
from datetime import datetime


tocsv = []
dashboard = meraki.DashboardAPI(config.key,single_request_timeout=999999,output_log=False)
orgs = dashboard.organizations.getOrganizations()

for org in orgs:
    try:
        devices = dashboard.appliance.getOrganizationApplianceUplinkStatuses(org["id"],total_pages=-1)
        for device in devices:

            temp = {}
            network = dashboard.networks.getNetwork(networkId=device['networkId'])
            temp['network_name'] = network['name']
            temp['MX'] = device['model']
            temp['serial'] = device['serial']
            temp['last_checkin'] = device['lastReportedAt']
            mx = dashboard.devices.getDevice(serial=device['serial'])
            if mx['wan1Ip'] != None:
                temp['device_public_ip'] = mx['wan1Ip']
            else:
                temp['device_public_ip'] = mx['wan2Ip']

            for uplink in device['uplinks']:
                if uplink['interface'] == 'wan1':
                    temp['public_wan_1'] = uplink['publicIp']
                    temp['wan_1_ip'] = uplink['ip']
                    if uplink['ipAssignedBy'] == 'static':
                        temp['w1_static_ip'] = 'TRUE'
                    if uplink['ipAssignedBy'] != 'static':
                        temp['w1_static_ip'] = 'FALSE'
                    temp['w1_gateway'] = uplink['gateway']
                if uplink['interface'] == 'wan2':
                    temp['public_wan_2_ip'] = uplink['publicIp']
                    temp['wan_2_ip'] = uplink['ip']
                    temp['w2_static_ip'] = ''
                    temp['w2_gateway'] = uplink['gateway']
                if uplink['interface'] == 'cellular':
                    temp['modem'] = uplink['model']
                    temp['cellular_ip_address'] = uplink['ip']
                    temp['carrier'] = uplink['provider']
                    if uplink['status'] != 'not connected':
                        temp['cell_connected'] = 'TRUE'
                    if uplink['status'] == 'active':
                        temp['cell_active?'] = 'TRUE'
                    if uplink['status'] != 'active':
                        temp['cell_active?'] = 'FALSE'
            temp['uplink_state_json'] = device['uplinks']
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            temp['time'] = dt_string
            tocsv.append(temp)
    except Exception as e: 
        print(e)
        continue

headerList = ['network_name', 'MX', 'serial','modem', 'cellular_ip_address','carrier','cell_connected','cell_active?','device_public_ip','public_wan_1','public_wan_2_ip','wan_1_ip','w1_static_ip','w1_gateway','wan_2_ip','w2_static_ip','w2_gateway','last_checkin','uplink_state_json','time']

with open('report.csv','w',encoding='utf8',newline='') as output_file:
    fc = csv.DictWriter(output_file,fieldnames=headerList,)
    fc.writeheader()
    fc.writerows(tocsv)