from sdv.model import DataPointBoolean, DataPointBooleanArray, DataPointDouble, DataPointDoubleArray, DataPointFloat, DataPointFloatArray, DataPointInt16, DataPointInt16Array, DataPointInt32, DataPointInt32Array,DataPointInt64,DataPointInt64Array,DataPointInt8,DataPointInt8Array,DataPointString, DataPointUint16, DataPointStringArray,DataPointUint16Array, DataPointUint32,DataPointUint32Array,DataPointUint64,DataPointUint64Array,DataPointUint8,DataPointUint8Array
from sdv.vdb.reply import DataPointReply


async def digital_auto_get(self):
    return await self.get_velocitas()


async def digital_auto_subscribe(self, callback):
    async def callback_transform(reply: DataPointReply):
        value = reply.get(self).value
        await callback(value)

    return await self.subscribe_velocitas(callback_transform)


def patch_datapoints(class_list):
    for clazz in class_list:
        clazz.get_velocitas = clazz.get
        clazz.subscribe_velocitas = clazz.subscribe
        clazz.get = digital_auto_get
        clazz.subscribe = digital_auto_subscribe


patch_datapoints([DataPointBoolean, DataPointBooleanArray, DataPointDouble, DataPointDoubleArray, DataPointFloat, DataPointFloatArray, DataPointInt16, DataPointInt16Array, DataPointInt32, DataPointInt32Array,DataPointInt64,DataPointInt64Array,DataPointInt8,DataPointInt8Array,DataPointString, DataPointUint16, DataPointStringArray,DataPointUint16Array, DataPointUint32,DataPointUint32Array,DataPointUint64,DataPointUint64Array,DataPointUint8,DataPointUint8Array])
