from control.controller.Controller import Controller
from control.linker.FeedbackLinker import FeedbackLinker

class FeedbackController(Controller):
    @property
    def linker(self):
        return FeedbackLinker()