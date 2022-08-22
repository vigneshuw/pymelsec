"""
This file is a collection of data storage mechanisms.
"""

from typing import NamedTuple, Any, Optional
from reprlib import repr as _r


__all__ = ["Tag"]


class Tag(NamedTuple):
    device: str                     #: device address (e.g. "D200")
    value:  Optional[Any] = None    #: value read/written, may be ``None`` on error
    type:   Optional[str] = None    #: data type of device
    error:  Optional[str] = None    #: error message if unsuccessful, else ``None``


    def __bool__(self):
        """
        ``True`` if both ``value`` is not ``None`` and ``error`` is ``None``
        ``False`` otherwise
        """
        return self.value is not None and self.error is None


    def __str__(self):
        return f"{self.device}, {_r(self.value)}, {self.type}, {self.error}"


    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"device={self.device!r},"
            f"value={self.value!r},"
            f"type={self.type!r},"
            f"error={self.error!r})"
        )


class CPUInfo(NamedTuple):
    type: str  # type (e.g. 'R08ENCPU')
    info: str  # info (e.g. '4806')


    def __str__(self):
        return f"{self.type}, {self.info}"


    def __repr__(self):
        return f"{self.__class__.__name__}(type={type.type!r}, info={self.info!r})"


class CPUStatus(NamedTuple):
    status: Optional[str] = None    # status (e.g. 'Stop')
    cause:  Optional[str] = None    # cause (e.g. 'By Error')


    def __str__(self):
        return f"{self.status}, {self.cause}"


    def __repr__(self):
        return f"{self.__class__.__name__}(status={type.status!r}, cause={self.cause!r})"


class LoopbackTest(NamedTuple):
    length: Optional[int] = 0       # length of response
    data:   Optional[str] = None    # reponse data string