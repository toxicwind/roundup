from __future__ import annotations

import roundup.utils.lazy_loader as lazy

__getattr__, __dir__, __all__ = lazy.attach_extras(
    __name__,
    attrs={
        "PILImage": lazy.ExtraAttr("PIL", alias="Image"),
        "Image": lazy.ExtraAttr("PIL.Image", alias="Image"),
        "iio": lazy.ExtraAttr("imageio", alias="v3"),
    },
    error_message="Please install roundup[vision] to use image/video features",
)
