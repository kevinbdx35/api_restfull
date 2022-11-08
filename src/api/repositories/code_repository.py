from src.api.models.submitted_codes import Code
from src.api.repositories.generic_repository import GenericRepository


class CodeRepository(GenericRepository):
    def save_code(self, uid, eid, user_code, digest):
        return self.save(Code(uid, eid, user_code, digest))
