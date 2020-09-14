from distutils.core import setup, Extension

ext = Extension("ext", sources=["./ext/ext.c", "./ext/PQ.c", "./ext/Stack.c"],
                include_dirs=["./ext"])

setup(
    name="Dijkstras-Priority-Queue",
    author="Mahan Mahtabfar",
    description="Python extension module with PriorityQueue suited for Dijkstras Algorithm",
    version="1.0",
    ext_modules=[ext],
)
