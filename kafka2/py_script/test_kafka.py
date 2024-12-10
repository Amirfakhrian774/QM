try:
    from kafka import KafkaProducer, KafkaConsumer
    from kafka.admin import KafkaAdminClient, NewTopic
    print("Kafka package is working")
except ImportError as e:
    print(f"Error importing Kafka package: {e}")

