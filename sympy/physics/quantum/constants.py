"""Constants (like hbar) related to quantum mechanics."""

from sympy.core.numbers import NumberSymbol
from sympy.core.singleton import Singleton
from sympy.printing.pretty.stringpict import prettyForm
import mpmath.libmp as mlib

#-----------------------------------------------------------------------------
# Constants
#-----------------------------------------------------------------------------

__all__ = [
    'hbar',
    'HBar',
    'bohr_radius',
    'BohrRadius',
    'e',
    'ElementaryCharge'
]


class HBar(NumberSymbol, metaclass=Singleton):
    """Reduced Plank's constant in numerical and symbolic form [1]_.

    Examples
    ========

        >>> from sympy.physics.quantum.constants import hbar
        >>> hbar.evalf()
        1.05457162000000e-34

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Planck_constant
    """

    is_real = True
    is_positive = True
    is_negative = False
    is_irrational = True

    __slots__ = ()

    def _as_mpf_val(self, prec):
        return mlib.from_float(1.05457162e-34, prec)

    def _sympyrepr(self, printer, *args):
        return 'HBar()'

    def _sympystr(self, printer, *args):
        return 'hbar'

    def _pretty(self, printer, *args):
        if printer._use_unicode:
            return prettyForm('\N{PLANCK CONSTANT OVER TWO PI}')
        return prettyForm('hbar')

    def _latex(self, printer, *args):
        return r'\hbar'

# Create an instance for everyone to use.
hbar = HBar()

class BohrRadius(NumberSymbol, metaclass=Singleton):
    is_real = True
    is_positive = True
    is_negative = False
    is_irrational = True

    __slots__ = ()

    def _as_mpf_val(self, prec):
        return mlib.from_float(5.29177210903e-11, prec)

    def _sympyrepr(self, printer, *args):
        return 'BohrRadius()'

    def _sympystr(self, printer, *args):
        return 'a_0'

    def _pretty(self, printer, *args):
        return prettyForm('a_0')

    def _latex(self, printer, *args):
        return r'a_0'

bohr_radius = BohrRadius()

class ElementaryCharge(NumberSymbol, metaclass=Singleton):
    is_real = True
    is_positive = True
    is_negative = False
    is_irrational = True

    __slots__ = ()

    def _as_mpf_val(self, prec):
        return mlib.from_float(1.602176634e-19, prec)

    def _sympyrepr(self, printer, *args):
        return 'ElementaryCharge()'

    def _sympystr(self, printer, *args):
        return 'e'

    def _pretty(self, printer, *args):
        return prettyForm('e')

    def _latex(self, printer, *args):
        return r'e'

e = ElementaryCharge()
