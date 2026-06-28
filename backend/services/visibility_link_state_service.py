class VisibilityLinkStateService:

    def __init__(self):
        self.links = []

    def update(self, links):
        self.links = links

    def get_links(self):
        return self.links


visibility_link_state_service = (
    VisibilityLinkStateService()
)