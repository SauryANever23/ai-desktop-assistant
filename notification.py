import gi 
gi.require_version("Notify", "0.7")
from gi.repository import Notify

class GetNotification():

    def notify(title:str, input: str):
        Notify.init("Notification")
        nt = Notify.Notification.new(f"{title}", f"{input}")

        return nt

get = GetNotification(notify("Hello", "message"))
get.show()
