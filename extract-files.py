#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'device/xiaomi/sm6150-common',
    'hardware/qcom/display',
    'hardware/qcom/display/gralloc',
    'hardware/qcom/display/libdebug',
    'hardware/qcom/display/sde-drm',
    'hardware/qcom/media/mm-core',
    'hardware/xiaomi',
    'vendor/qcom/opensource/dataservices',
    'vendor/qcom/common/vendor/display',
    'vendor/qcom/common/vendor/display/4.14',
    'vendor/qcom/common/vendor/gps-legacy',
    'vendor/qcom/common/vendor/keymaster',
    'vendor/qcom/common/vendor/wlan-legacy',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.qualcomm.qti.dpm.api@1.0',
        'vendor.qti.hardware.fm@1.0',
        'vendor.qti.imsrtpservice@3.0',
    ): lib_fixup_vendor_suffix,
    (
        'libOmxCore',
        'libwpa_client',
    ): lib_fixup_remove,
}

module = ExtractUtilsModule(
    'sm6150-common',
    'xiaomi',
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
