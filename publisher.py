from google.cloud import pubsub_v1
import json

project_id = ""
topic_id = ""

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

data = {"foo": "bar"}
json = json.dumps(data)
data = json.encode("utf-8")
future = publisher.publish(topic_path, data, event="test")

print(future.result())
