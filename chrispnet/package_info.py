MAJOR = 0
MINOR = 1
PATCH = 0
PRE_RELEASE = "rc0"

# Use the following formatting: (major, minor, patch, pre-release)
VERSION = (MAJOR, MINOR, PATCH, PRE_RELEASE)

__shortversion__ = ".".join(map(str, VERSION[:3]))
__version__ = ".".join(map(str, VERSION[:3])) + "".join(VERSION[3:])

__package_name__ = "chrispnet"
__contact_names__ = "Eesung Kim"
__contact_emails__ = "eesungk@gmail.com"
__homepage__ = ""
__repository_url__ = "https://github.com/eesungkim/e2e_asr"
__download_url__ = "https://github.com/eesungkim/"
__description__ = "Personal Library for Conversational AI"
__license__ = "Apache2"
__keywords__ = ""

