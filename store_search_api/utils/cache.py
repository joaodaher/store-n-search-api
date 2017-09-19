from rest_framework_extensions.key_constructor import bits
from rest_framework_extensions.key_constructor.constructors import KeyConstructor


class QueryListParamsKeyBit(bits.AllArgsMixin, bits.KeyBitDictBase):
    def get_source_dict(self, params, view_instance, view_method, request, args, kwargs):
        data = {
            k: request.query_params.getlist(k) for k in request.GET.keys()
        }
        return data


class CacheKeyConstructor(KeyConstructor):
    unique_view_id = bits.UniqueMethodIdKeyBit()
    args = bits.ArgsKeyBit()
    kwargs = bits.KwargsKeyBit()
    all_query_params = QueryListParamsKeyBit()


cache_key_constructor = CacheKeyConstructor()
