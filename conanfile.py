from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class LibpngConan(ConanFile):
    name = "libpng"
    version = "1.6.29"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    requires = "zlib/1.2.11@conan/stable"

    def source(self):
        tools.download("http://download.sourceforge.net/libpng/libpng-1.6.29.tar.gz", "libpng.tar.gz")
        tools.unzip("libpng.tar.gz")
        os.remove("libpng.tar.gz")

    def build(self):
        atbe = AutoToolsBuildEnvironment(self)
        atbe.configure(configure_dir="libpng-1.6.29")
        atbe.make()

    def package(self):
        self.copy("*.h", dst="include", src="libpng-1.6.29")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["png16"]
