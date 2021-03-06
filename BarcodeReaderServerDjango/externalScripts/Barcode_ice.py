# **********************************************************************
#
# Copyright (c) 2003-2009 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

# Ice version 3.3.1
# Generated from file `Barcode.ice'

import Ice, IcePy, __builtin__

if not Ice.__dict__.has_key("_struct_marker"):
    Ice._struct_marker = object()

# Start of module Demo
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

if not _M_Demo.__dict__.has_key('_t_ByteSeq'):
    _M_Demo._t_ByteSeq = IcePy.defineSequence('::Demo::ByteSeq', (), IcePy._t_byte)

if not _M_Demo.__dict__.has_key('Barcode'):
    _M_Demo.Barcode = Ice.createTempClass()
    class Barcode(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_Demo.Barcode:
                raise RuntimeError('Demo.Barcode is an abstract class')

        def ice_ids(self, current=None):
            return ('::Demo::Barcode', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Barcode'

        def ice_staticId():
            return '::Demo::Barcode'
        ice_staticId = staticmethod(ice_staticId)

        #
        # Operation signatures.
        #
        # def priceForBarcode(self, code, current=None):
        # def saveProduct(self, bc, desc, price, image, current=None):

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_Barcode)

        __repr__ = __str__

    _M_Demo.BarcodePrx = Ice.createTempClass()
    class BarcodePrx(Ice.ObjectPrx):

        def priceForBarcode(self, code, _ctx=None):
            return _M_Demo.Barcode._op_priceForBarcode.invoke(self, ((code, ), _ctx))

        def saveProduct(self, bc, desc, price, image, _ctx=None):
            return _M_Demo.Barcode._op_saveProduct.invoke(self, ((bc, desc, price, image), _ctx))

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_Demo.BarcodePrx.ice_checkedCast(proxy, '::Demo::Barcode', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_Demo.BarcodePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_Demo._t_BarcodePrx = IcePy.defineProxy('::Demo::Barcode', BarcodePrx)

    _M_Demo._t_Barcode = IcePy.defineClass('::Demo::Barcode', Barcode, (), True, None, (), ())
    Barcode.ice_type = _M_Demo._t_Barcode

    Barcode._op_priceForBarcode = IcePy.Operation('priceForBarcode', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string),), (), IcePy._t_int, ())
    Barcode._op_saveProduct = IcePy.Operation('saveProduct', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, (), (((), IcePy._t_string), ((), IcePy._t_string), ((), IcePy._t_int), ((), _M_Demo._t_ByteSeq)), (), IcePy._t_int, ())

    _M_Demo.Barcode = Barcode
    del Barcode

    _M_Demo.BarcodePrx = BarcodePrx
    del BarcodePrx

# End of module Demo
