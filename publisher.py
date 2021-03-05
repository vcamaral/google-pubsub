from google.cloud import pubsub_v1
import json

project_id = "ardent-rush-297422"
topic_id = "test"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

data = {"affiliationCode": "123456789"}
json = json.dumps(data)
data = json.encode("utf-8")
future = publisher.publish(topic_path, data, event="update")

print(future.result())
