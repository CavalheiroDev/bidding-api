from abc import ABC

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from typing import Dict

from utils.exceptions import ObjectNotFound


class Repositories(ABC):
    not_found_exception: Exception = None

    @property
    def model(self):
        raise NotImplementedError()

    def create(self, **fields) -> model:
        return self.model.objects.create(**fields)

    def update(self, object_, /, **fields):
        for key, value in fields.items():
            setattr(object_, key, value)

        object_.save()
        return object_

    def safe_get(self, **kwargs) -> model:
        try:
            return self.model.objects.get(**kwargs)
        except ObjectDoesNotExist:
            return None

    def get_or_raise(self, _custom_exception: Exception = None, **kwargs) -> model:
        obj = self.safe_get(**kwargs)
        if not obj:
            raise _custom_exception or self.not_found_exception or self._generic_not_found_exception()
        return obj

    def _generic_not_found_exception(self):
        obj_name = str(self.model._meta).split('.')[-1]
        message = f"{obj_name.capitalize()} not found."
        code = f"{obj_name.upper()}_NOT_FOUND"
        exception = ObjectNotFound(message, code=code)
        return exception

    def has_queryset_values(self, queryset: QuerySet, /, **kwargs) -> Dict[str, bool]:
        result_dict = {}

        for key, value in kwargs.items():
            has_item = queryset.filter(**{key: value}).exists()
            result_dict[key] = has_item

        return result_dict
