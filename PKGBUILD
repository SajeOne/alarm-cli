# Maintainer: Shane "SajeOne" Brown <contact@shane-brown.ca>
pkgname=alarm-cli
pkgver=0.1
pkgrel=1
pkgdesc="Simple alarm app for the CLI"
arch=('i686' 'x86_64')
url="https://github.com/SajeOne/alarm-cli"
license=('GPL')
depends=('python')
makedepends=()
provides=('alarm-cli')
source=("git+https://github.com/SajeOne/alarm-cli")
md5sums=('SKIP')

package() {
  mkdir "$srcdir/$pkgname-$pkgver"
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}

# vim:set ts=2 sw=2 et:
