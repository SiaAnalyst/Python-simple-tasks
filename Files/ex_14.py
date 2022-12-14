import shutil


def unpack(archive_path, path_to_unpack):
    shutil.unpack_archive(str(archive_path), str(path_to_unpack))