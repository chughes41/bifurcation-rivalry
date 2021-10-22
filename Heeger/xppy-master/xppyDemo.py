# coding: utf-8
import xppy
xppy.set_cmd('/Users/christopherhughes/Applications')
subHopf=xppy.run('tristable.ode')
subHopf.getDesc()
sHData=subHopf.getRawData()
sHData.shape
from xppy.utils import plot
plot.plotLC(subHopf.getRawData())
plot.pl.show()
