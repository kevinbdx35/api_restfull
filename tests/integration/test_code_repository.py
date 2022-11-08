from src.api.models.submitted_codes import Code
from src.api.repositories.code_repository import CodeRepository
import os


def test_save_code(start):
    code = Code(uid=2, eid=1, filepath='src.api.repositories.code_repository',
                digest='eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ')
    repot = CodeRepository()
    repot.save_code(2, 1, 'src.api.repositories.code_repository',
                    'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ')
    assert code.uid == 2
    assert code.eid == 1
    assert code.user_code == 'src.api.repositories.code_repository'
    assert code.digest == 'eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ'
