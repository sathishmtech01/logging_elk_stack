

bin/kafka-console-consumer.sh --bootstrap-server xxx.servicebus.windows.net:9093 --consumer.config consumer.properties --topic tesy --from-beginning

bin/kafka-console-producer.sh --bootstrap-server xxx.servicebus.windows.net:9093 --producer.config consumer.properties --topic tesy