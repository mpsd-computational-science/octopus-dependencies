

import importlib

mock_classes_and_functions = """

deps = {}
versions = {}

class AutotoolsPackage:
    pass

class CudaPackage:
    pass

def maintainers(*args):
    pass

def version(ver, **kwd):
    versions[ver] = kwd
"""





def extract_octopus_class(filename: str) -> str:
    """ extra relevant part from spack.py file and return"""
    data = open(filename, "tr").read()

    # chop off everything before token
    token = "class Octopus"
    data = token + data.split(token)[1]

    # keep everything up to (but not including) token
    token = "def configure_args(self):"
    data = data.split(token)[0]

    return mock_classes_and_functions + "\n\n" + data


def create_octopus_class(oct_class_source):
    import octopus
    #octopus = importlib.import_module("octopus.py")
    return octopus





def main():
    oct_class_source = extract_octopus_class("spack-package.py")
    with open("octopus.py", "tw") as f:
        f.write(oct_class_source)
    
    octopus = create_octopus_class(oct_class_source)
    return octopus




if __name__ == "__main__":
    octopus = main()
    print(octopus)
