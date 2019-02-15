#coding:utf-8

st="""convertEt_wps-web
convertPptx_wps-web
convertPpt_wps-web
convertRtf_wps-web
convertWps_wps-web
convertXlsx_wps-web
convertXls_wps-web
deletepdf_wps-web
download_preview
encryptpdf_wps-web
insertpdf_wps-web
mergepdf_wps-web
numberofpagesDocx_wps
numberofpagesDoc_wps-web
numberofpagesDps_wps-web
numberofpagesWps_wps-web
numberofpagesXlsx_wps-web
numberofpagesXls_wps
splitpdf_wps-web
"""

templt="""
                <screen_item>
                    <resourcetype>0</resourcetype>
                    <width>500</width>
                    <height>100</height>
                    <x>{0}</x>
                    <y>{1}</y>
                    <colspan>1</colspan>
                    <rowspan>1</rowspan>
                    <elements>0</elements>
                    <valign>0</valign>
                    <halign>0</halign>
                    <style>0</style>
                    <url/>
                    <dynamic>0</dynamic>
                    <sort_triggers>0</sort_triggers>
                    <resource>
                        <name>{2}</name>
                        <host>translation-vm10-0-0-4</host>
                    </resource>
                    <max_columns>3</max_columns>
                    <application/>
                </screen_item>
"""
# for l in  st.splitlines():
#     hostname=l.split()[0]
#     ip=l.split()[1]
#     alis_name='vm'+'-'.join(ip.split('.'))
#     # print "{0} ansible_ssh_host={1} ansible_ssh_user=root ansible_ssh_pass=KsoCloudNotify2018".format(hostname,ip)
#     print templt.format(alis_name,hostname,ip)
#     # print hostname
x=0
y=1
for l in  st.splitlines():
    print templt.format(x, y, l)
    x=x+1
    if x > 3:
        x=0
        y=y+1

