from sim import Version, AppInfo, Autor


def test_autor():
    assert Autor.name == "Harrinson Gavidia"
    assert Autor.alias == "harrinsoft"
    assert Autor.email == "harrinsoft@gmail.com"
    assert str(Autor()) == "harrinsoft -[harrinsoft@gmail.com]-"


def test_version(): 
    assert isinstance(Version().get_version(), str)
    assert isinstance(Version.major, int)
    assert isinstance(Version.minor, int)
    assert isinstance(Version.micro, int)
    assert "sim" in str(Version())


def test_info():
    assert AppInfo.name == "sim"
    assert AppInfo.license == "GPLv3"
    assert AppInfo.url == "https://github.com/harrinsoft/sim.git"
    assert AppInfo.description == "Un software para el control del mantenimiento empresarial. escrito en python."
