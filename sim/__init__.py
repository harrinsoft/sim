# -----------------------------------------------------------------------------
#   META DATA
# -----------------------------------------------------------------------------


class Version:
    major = 0
    minor = 1
    micro = 0

    def get_version(self):
        return '{0}.{1}.{2}'.format(self.major, self.minor, self.micro)

    def __str__(self):
        return "sim V-{0}.{1}.{2}".format(self.major, self.minor, self.micro)


class Autor:
    alias = 'harrinsoft'
    name = 'Harrinson Gavidia'
    email = 'harrinsoft@gmail.com'

    def __str__(self):
        return "{0} -[{1}]-".format(self.alias, self.email)


class AppInfo:
    name = 'sim'
    description = 'Un software para el control del mantenimiento empresarial. escrito en python.'
    url = 'https://github.com/harrinsoft/sim.git'
    license = 'GPLv3'
