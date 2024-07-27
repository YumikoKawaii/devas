import application.pkg.repository.repo as repo
import application.pkg.repository.models as models
import application.dto.message as message_dto


class Service:
    repository: repo.IRepository

    def get_messages(self, conditions: models.GetMessagesFilter) -> message_dto.GetMessagesResponse:

        messages = self.repository.get_messages(conditions=conditions)

        # mapping

        pass



