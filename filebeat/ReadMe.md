To test from local pc:
download file beat from https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html

root@csk-ai-revolution:/home/csk/filebeat-7.7.0-linux-x86_64# ./filebeat -e -c filebeat.yml


Logs appear http://localhost:5601/app/kibana#/discover?_g=(refreshInterval:(pause:!t,value:0),time:(from:now-2h,to:now))&_a=(columns:!(_source),index:'29a78eb0-966d-11ea-a447-a3532861663f',interval:auto,query:(language:kuery,query:''),sort:!('@timestamp',desc))


chmod go-w /home/csk/elk/filebeat_/filebeat-log-kafka.yaml