""" Configuration class for Insights"""

import logging
import sys
import os
import configparser
import six
import shutil
from logging import config
from insights.configs import casts

LOGGER = logging.getLogger(__name__)
SETTINGS_FILE_NAME = 'pool.conf'


def get_project_root():
    """Return the path to the Insights project root directory.
    :return: A directory path.
    :rtype: str
    """
    return os.path.realpath(os.path.join(
         os.path.dirname(__file__),
         os.pardir,
         os.pardir,
    ))


class PropertyReader(object):
    # Helper casters
    cast_boolean = casts.Boolean()
    cast_dict = casts.Dict()
    cast_list = casts.List()
    cast_logging_level = casts.LoggingLevel()
    cast_tuple = casts.Tuple()

    def __init__(self, Path):
        self.config_parser = configparser.ConfigParser()
        with open(Path) as handler:
            self.config_parser.readfp(handler)
            if sys.version_info[0] < 3:
                # ConfigParser.readfp is deprecated on Python3, read_file
                # replaces it
                self.config_parser.readfp(handler)
            else:
                self.config_parser.read_file(handler)

    def get(self, section, option, default=None, cast=None):
        try:
            value = self.config_parser.get(section, option)
            if cast is not None:
                if cast is bool:
                    value = self.cast_boolean(value)
                elif cast is dict:
                    value = self.cast_dict(value)
                elif cast is list:
                    value = self.cast_list(value)
                elif cast is tuple:
                    value = self.cast_tuple(value)
                else:
                    value = cast(value)
        except(six.moves.NoSectionError, six.moves.NoOptionError):
            value = default
        return value

    def has_section(self, section):
        """Check if section is present"""
        return self.config_parser.has_section(section)


class ImproperlyConfigured(Exception):
    """Insights is improperly configured
    If settings file is not present, it will
    raise this exception
    """


class APIResourcesReader:
    """
    Reader for Insights API resources
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('resources/api_resources.conf')

    def get(self, section, option):
        return self.config.get(section, option)


class FeatureSettings(object):
    """
    Create a instance of this class and assign attributes to map to the feature
    options.
    """
    def read(self, reader):
        """
        Subclasses must implement this method in order to populate itself
        with expected settings values.
        :param reader:
        :return:
        """

        raise NotImplementedError('Subclasses must implement read method.')

    def validate(self):
        """Subclasses must implement this method in order to validade the
        settings and raise ``ImproperlyConfigured`` if any issue is found.
        """

        raise NotImplementedError('Subclasses must implement read method.')


class RHNLoginSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(RHNLoginSettings, self).__init__(*args, **kwargs)
        self.base_url = None
        self.rhn_username = None
        self.rhn_password = None
        self.chrome_driver_path = None

    def read(self, reader):
        self.base_url = reader.get(
            'rhn_login','base_url'
        )
        self.rhn_username = reader.get(
            'rhn_login', 'rhn_username'
        )
        self.rhn_password = reader.get(
            'rhn_login', 'rhn_password'
        )
        self.chrome_driver_path = reader.get(
            'rhn_login', 'chrome_driver_path'
        )

    def validate(self):
        validation_errors = []
        if not any((self.base_url, self.rhn_password,
                    self.rhn_username, self.chrome_driver_path)):
            validation_errors.append(
                'RHNLogin details are not specified'
            )
        return validation_errors


class OpenstackVMSettings(FeatureSettings):
    def __init__(self, *args, **kwargs):
        super(OpenstackVMSettings, self).__init__(*args, **kwargs)
        self.username = None
        self.api_key = None
        self.auth_url = None
        self.project_id = None

    def read(self, reader):
        self.username = reader.get(
            'openstack_vms', 'username'
        )
        self.api_key = reader.get(
            'openstack_vms', 'api_key'
        )
        self.auth_url = reader.get(
            'openstack_vms', 'auth_url'
        )
        self.project_id = reader.get(
            'openstack_vms', 'project_id'
        )

    def validate(self):
        validation_errors = []
        if not any((self.username, self.api_key,
                    self.auth_url, self.project_id)):
            validation_errors.append(
                'Openstack VM settings are not specified.'
            )
        return validation_errors


class SSHConfSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(SSHConfSettings, self).__init__(*args, **kwargs)
        self.ssh_key_path = None

    def read(self, reader):
        self.ssh_key_path = reader.get(
            'ssh', 'ssh_key_path'
        )

    def validate(self):
        validation_errors = []
        if not any((self.ssh_key_path)):
            validation_errors.append(
                'SSH key path is not provided.'
            )
        return validation_errors


class RHNRegisterSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(RHNRegisterSettings, self).__init__(*args, **kwargs)
        self.rh_username = None
        self.rh_password = None

    def read(self, reader):
        self.rh_username = reader.get(
            'rhn_register', 'rh_username'
        )
        self.rh_password = reader.get(
            'rhn_register', 'rh_password'
        )

    def validate(self):
        validation_errors = []
        if not any((self.rh_password, self.rh_username)):
            validation_errors.append(
                'RHN credentials not provided.'
            )
        return validation_errors


class Sat62Settings(FeatureSettings):
    def __init__(self, *args, **kwargs):
        super(Sat62Settings, self).__init__(*args, **kwargs)
        self.sat6_cert = None
        self.sat6_key = None
        self.sat6_cacert = None
        self.remote_branch = None
        self.remote_leaf = None
        self.registered_machine_id = None
        self.hostname = None

    def read(self, reader):
        self.sat6_cert = reader.get(
            'sat62', 'sat6_cert')
        self.sat6_key = reader.get(
            'sat62', 'sat6_key')
        self.sat6_cacert = reader.get(
            'sat62', 'sat6_cacert')
        self.remote_branch = reader.get(
            'sat62', 'remote_branch')
        self.remote_leaf = reader.get(
            'sat62', 'remote_leaf')
        self.registered_machine_id = reader.get(
            'sat62', 'registered_machine_id')
        self.hostname = reader.get(
            'sat62', 'hostname')

    def validate(self):
        validation_errors = []
        if not any((self.sat6_cert, self.sat6_key, self.sat6_cacert)):
            validation_errors.append(
                'Satellite certificates are not provided'
            )
        if not any((self.remote_leaf, self.remote_branch,
                    self.registered_machine_id, self.hostname)):
            validation_errors.append(
                'Hostname or Remote details for sat62 are not configured'
            )
        return validation_errors


class APISettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(APISettings, self).__init__(*args, **kwargs)
        self.url = None

    def read(self, reader):
        self.url = reader.get(
            'api', 'url'
        )

    def validate(self):
        validation_errors = []
        if not any((self.url)):
            validation_errors.append(
                'API endpoint is not provided.'
            )
        return validation_errors


class CertsSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(CertsSettings, self).__init__(*args, **kwargs)
        self.cert_path = None
        self.key_path = None

    def read(self, reader):
        self.cert_path = reader.get(
            'certs', 'cert_path'
        )
        self.key_path = reader.get(
            'certs', 'key_path'
        )

    def validate(self):
        validation_errors = []
        if not any((self.cert_path, self.key_path)):
            validation_errors.append(
                'Certificates path not provided.'
            )
        return validation_errors


class ArchiveSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(ArchiveSettings, self).__init__(*args, **kwargs)
        self.new_bash_version = None
        self.un_archive_file_location = None
        self.machine_id_path = None
        self.search_file_path = None
        self.archive_file_path = None

    def read(self, reader):
        self.new_bash_version = reader.get(
            'upload_archive', 'new_bash_version'
        )
        self.un_archive_file_location = reader.get(
            'upload_archive', 'un_archive_file_location'
        )
        self.machine_id_path = reader.get(
            'upload_archive', 'machine_id_path'
        )
        self.search_file_path = reader.get(
            'upload_archive', 'search_file_path'
        )
        self.archive_file_path = reader.get(
            'upload_archive', 'archive_file_path'
        )

    def validate(self):
        validation_errors = []
        if not any((self.new_bash_version,
                    self.un_archive_file_location, self.machine_id_path,
                    self.search_file_path, self.archive_file_path)):
            validation_errors.append(
            'Upload archieve details are not provided.'
            )
        return validation_errors


class ENVSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(ENVSettings, self).__init__(*args, **kwargs)
        self.env_base_url = None
        self.env_password = None
        self.env_username = None

    def read(self, reader):
        self.env_base_url = reader.get(
            'env', 'env_base_url'
        )
        self.env_username = reader.get(
            'env', 'env_username'
        )
        self.env_password = reader.get(
            'env', 'env_password'
        )

    def validate(self):
        validation_errors = []
        if not any((self.env_base_url, self.env_username,
                    self.env_password)):
            validation_errors.append(
                'Environment details are not provided.'
            )
        return validation_errors


class RepoSettings(FeatureSettings):
    def __init__(self,*args, **kwargs):
        super(RepoSettings, self).__init__(*args, **kwargs)
        self.rhel6_repo = None
        self.rhel7_repo = None
        self.insights_repo_el6 = None
        self.insights_repo_el7 = None

    def read(self, reader):
        self.rhel6_repo = reader.get(
            'repo', 'rhel6_repo'
        )
        self.rhel7_repo = reader.get(
            'repo', 'rhel7_repo'
        )
        self.insights_repo_el6 = reader.get(
            'repo', 'insights_repo_el6'
        )
        self.insights_repo_el7 = reader.get(
            'repo', 'insights_repo_el7'
        )

    def validate(self):
        validation_errors = []
        if not any((self.rhel6_repo, self.rhel7_repo,
                    self.insights_repo_el6, self.insights_repo_el7)):
            validation_errors.append(
                'Insights and RHEL repo details are not provided.'
            )
        return validation_errors


class Settings(object):
    """
    Insights Settings representation.
    """

    def __init__(self):
        """
        Init for Settings
        """
        self._all_features = None
        self._configured = False
        self.reader = None
        self._validation_error = []
        self.screenshots_path = None
        self.webdriver = None
        self.webdriver_binary = None
        self.webdriver_desired_capabilities = None

        self._configure_logging()
        self.api_resources = APIResourcesReader()
        self.sat62 = Sat62Settings()
        self.rhn_login = RHNLoginSettings()
        self.openstack_vm = OpenstackVMSettings()
        self.ssh = SSHConfSettings()
        self.rhn_register = RHNRegisterSettings()
        self.api = APISettings()
        self.certs = CertsSettings()
        self.upload_archive = ArchiveSettings()
        self.env = ENVSettings()
        self.repo = RepoSettings()

    def configure(self):
        if self.configured:
            return

        settings_path = os.path.join(get_project_root(), SETTINGS_FILE_NAME)
        if not os.path.isfile(settings_path):
            raise ImproperlyConfigured(
                'Not able to find settings file at {}'.format(settings_path))

        self.reader = PropertyReader(settings_path)
        self._read_insights_settings()
        self._cleanup_downloads()

        if self.reader.has_section('rhn_login'):
            self.rhn_login.read(self.reader)
            self._validation_error.extend(self.rhn_login.validate())
        if self.reader.has_section('openstack_vms'):
            self.openstack_vm.read(self.reader)
            self._validation_error.extend(self.openstack_vm.validate())
        if self.reader.has_section('ssh'):
            self.ssh.read(self.reader)
            self._validation_error.extend(self.ssh.validate())
        if self.reader.has_section('rhn_register'):
            self.rhn_register.read(self.reader)
            self._validation_error.extend(self.rhn_register.validate())
        if self.reader.has_section('sat62'):
            self.sat62.read(self.reader)
            self._validation_error.extend(self.sat62.validate())
        if self.reader.has_section('api'):
            self.api.read(self.reader)
            self._validation_error.extend(self.api.validate())
        if self.reader.has_section('certs'):
            self.certs.read(self.reader)
            self._validation_error.extend(self.certs.validate())
        if self.reader.has_section('upload_archive'):
            self.upload_archive.read(self.reader)
            self._validation_error.extend(self.upload_archive.validate())
        if self.reader.has_section('env'):
            self.env.read(self.reader)
            self._validation_error.extend(self.env.validate())
        if self.reader.has_section('repo'):
            self.repo.read(self.reader)
            self._validation_error.extend(self.repo.validate())

        if self._validation_error:
            raise ImproperlyConfigured(
                'Failed to validate the configuration, check the message(s):\n'
                '{}'.format('\n'.join(self._validation_error))
            )
        self._configured = True

    def _cleanup_downloads(self):
        """
        Remove all files from ./downloads
        :return:
        """
        LOGGER.info("Cleaning up downloads")
        try:
            shutil.rmtree(os.path.join(get_project_root(), 'downloads'))
        except:
            LOGGER.info("downloads directory not present")

    def _read_insights_settings(self):
        self.browser = self.reader.get(
            'insights', 'browser', 'selenium'
        )
        self.webdriver = self.reader.get(
            'insights', 'webdriver', 'chrome'
        )
        self.webdriver_binary = self.reader.get(
            'insights', 'webdriver_binary', None
        )
        self.screenshots_path = self.reader.get(
            'insights', 'screenshots_path', '/tmp/insights/screenshots'
        )

    def _configure_logging(self):
        """Configure logging for Insights.

        It will load configuration from logging.conf if present
        in root directory, otherwise custom logging format is used by
        default

        """

        if self.configured:
            LOGGER.info("Already configured")
            return

        # All output should be made by the logging module, including warnings
        logging.captureWarnings(True)

        # Allow overriding logging config based on the presence of logging.conf
        # file on Insights's project root
        logging_conf_path = os.path.join(get_project_root(), 'logging.conf')
        if os.path.isfile(logging_conf_path):
            config.fileConfig(logging_conf_path)
        else:
            logging.basicConfig(
                format='%(levelname)s %(module)s:%(lineno)d: %(message)s'
            )

    @property
    def configured(self):
        """Returns True if the settings have already been configured."""
        return self._configured

    @property
    def all_features(self):
        """List all expected feature settings sections."""
        if self._all_features is None:
            self._all_features = [
                name for name, value in vars(self).items()
                if isinstance(value, FeatureSettings)
            ]
        return self._all_features

