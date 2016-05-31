# Maintainer: Shane "SajeOne" Brown <contact@shane-brown.ca>
pkgname=alarm-cli
pkgver=0.1
pkgrel=1
pkgdesc="A simple alarm app for the command line"
arch=('any')
url="https://github.com/SajeOne/alarm-cli"
license=('GPL')
groups=()
depends=('python')
makedepends=('python-setuptools')
provides=('alarm-cli')
conflicts=()
replaces=()
backup=()
source=('git+https://github.com/SajeOne/alarm-cli.git')
md5sums=('SKIP')

package() {
  cd "$srcdir/$pkgname"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
