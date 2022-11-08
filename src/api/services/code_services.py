from src.api.repositories.code_repository import CodeRepository
from src.api.utils.constants import LOCALPATH

import os
import hashlib


class CodeServices:
    def __init__(self):
        self.repository = CodeRepository()

    @staticmethod
    def save_file_locally(uid, eid, code_from_user):
        os.makedirs(r"/".join([LOCALPATH["codes"], str(uid), str(eid)]), exist_ok=True)

        inc = 0
        filepath = r"/".join([LOCALPATH["codes"], str(uid), str(eid), str(inc) + ".py"])
        while os.path.isfile(filepath):
            inc += 1
            filepath = r"/".join([LOCALPATH["codes"], str(uid), str(eid), str(inc) + ".py"])

        code_from_user.save(filepath)

        return filepath, CodeServices.__hashfile(filepath)

    @staticmethod
    def __hashfile(filepath):
        # A arbitrary (but fixed) buffer
        BUF_SIZE = 65536

        # Initializing the sha256() method
        sha256 = hashlib.sha256()

        with open(filepath, 'rb') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break

                sha256.update(data)
                condensat = sha256.hexdigest()

        return condensat
