from app.adapters.pantip_adapter import PantipAdapter

class PantipRepository:
    def __init__(self, pantip_adapter) -> None:
        self.pantip_adapter: PantipAdapter = pantip_adapter

    def get_pantip_topic_info(self, topic_id):
        return self.pantip_adapter.get_pantip_topic_info(topic_id=topic_id)
    
    def get_pantip_topic_by_room(self, tid, room):
        return self.pantip_adapter.get_pantip_topic_by_room(tid=tid, room=room)
    
    def get_pantip_topic_by_tag(self, tid, tag):
        return self.pantip_adapter.get_pantip_topic_by_tag(tid=tid, tag=tag)