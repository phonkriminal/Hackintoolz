from pathlib import Path
import tarfile

def extract_tar(tar_path, extract_path='.'):
    """This function extracts the tar file.

        Most of the knowledge graph dataset are donwloaded in a compressed
        tar format. This function is used to extract them

        Args:
            tar_path (str): Location of the tar folder.
            extract_path (str): Path where the files will be decompressed.

        Todo:
            * Move this module to utils!
    """
    tar = tarfile.open(tar_path, 'r')
    for item in tar:
        tar.extract(item, extract_path)
        if item.name.find(".tgz") != -1 or item.name.find(".tar") != -1:
            extract_tar(item.name, "./" + item.name[:item.name.rfind('/')]) 