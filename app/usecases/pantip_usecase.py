from app.repositories.pantip_repository import PantipRepository

class PantipUsecase:
    def __init__(self, pantip_repo) -> None:
        self.pantip_repo: PantipRepository = pantip_repo
    
    def excute(self):
        print("""
        1. Get Pantip Topic Info
        2. Get Pantip Topic By room
        3. Get Pantip Topic By tag
        """)
        pantip_request = input("Please select number of pantip request: ")
        if (pantip_request == '1'):
            print("---[ Get Pantip Topic Info ]---")
            topic_id = input("Enter topic id: ")
            return self.pantip_repo.get_pantip_topic_info(topic_id=topic_id)

        if (pantip_request == '2'):
            print("---[ Get Pantip Topic By room ]---")
            room = input("Enter room: ")
            tid = input("Enter tid: ")
            return self.pantip_repo.get_pantip_topic_by_room(tid=tid, room=room)

        if (pantip_request == '3'):
            print("---[ Get Pantip Topic By tag ]---")
            tag = input("Enter tag: ")
            tid = input("Enter tid: ")
            return self.pantip_repo.get_pantip_topic_by_tag(tid=tid, tag=tag)
        
        else:
            print("[ERROR] Please enter number 1-3")