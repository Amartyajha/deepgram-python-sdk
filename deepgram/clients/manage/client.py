# Copyright 2023 Deepgram SDK contributors. All Rights Reserved.
# Use of this source code is governed by a MIT license that can be found in the LICENSE file.
# SPDX-License-Identifier: MIT

from .v1.async_client import AsyncManageClient as AsyncManageClientLatest
from .v1.client import ManageClient as ManageClientLatest

# input
from .v1.options import InviteOptions as InviteOptionsLatest
from .v1.options import KeyOptions as KeyOptionsLatest
from .v1.options import ProjectOptions as ProjectOptionsLatest
from .v1.options import ScopeOptions as ScopeOptionsLatest
from .v1.options import UsageFieldsOptions as UsageFieldsOptionsLatest
from .v1.options import UsageRequestOptions as UsageRequestOptionsLatest
from .v1.options import UsageSummaryOptions as UsageSummaryOptionsLatest

# responses
from .v1.response import Balance as BalanceLatest
from .v1.response import BalancesResponse as BalancesResponseLatest
from .v1.response import InvitesResponse as InvitesResponseLatest
from .v1.response import Key as KeyLatest
from .v1.response import KeyResponse as KeyResponseLatest
from .v1.response import KeysResponse as KeysResponseLatest
from .v1.response import MembersResponse as MembersResponseLatest
from .v1.response import Message as MessageLatest
from .v1.response import Project as ProjectLatest
from .v1.response import ProjectsResponse as ProjectsResponseLatest
from .v1.response import ScopesResponse as ScopesResponseLatest
from .v1.response import UsageFieldsResponse as UsageFieldsResponseLatest
from .v1.response import UsageRequest as UsageRequestLatest
from .v1.response import UsageRequestsResponse as UsageRequestsResponseLatest
from .v1.response import UsageSummaryResponse as UsageSummaryResponseLatest

"""
The client.py points to the current supported version in the SDK.
Older versions are supported in the SDK for backwards compatibility.
"""


# input
class ProjectOptions(ProjectOptionsLatest):
    """
    pass through for ProjectOptions based on API version
    """

    pass


class KeyOptions(KeyOptionsLatest):
    """
    pass through for KeyOptions based on API version
    """

    pass


class ScopeOptions(ScopeOptionsLatest):
    """
    pass through for ScopeOptions based on API version
    """

    pass


class InviteOptions(InviteOptionsLatest):
    """
    pass through for InviteOptions based on API version
    """

    pass


class UsageRequestOptions(UsageRequestOptionsLatest):
    """
    pass through for UsageRequestOptions based on API version
    """

    pass


class UsageSummaryOptions(UsageSummaryOptionsLatest):
    """
    pass through for UsageSummaryOptions based on API version
    """

    pass


class UsageFieldsOptions(UsageFieldsOptionsLatest):
    """
    pass through for UsageFieldsOptions based on API version
    """

    pass


# responses
class Message(MessageLatest):
    """
    pass through for Message based on API version
    """

    pass


class Project(ProjectLatest):
    """
    pass through for Project based on API version
    """

    pass


class ProjectsResponse(ProjectsResponseLatest):
    """
    pass through for ProjectsResponse based on API version
    """

    pass


class MembersResponse(MembersResponseLatest):
    """
    pass through for MembersResponse based on API version
    """

    pass


class Key(KeyLatest):
    """
    pass through for Key based on API version
    """

    pass


class KeyResponse(KeyResponseLatest):
    """
    pass through for KeyResponse based on API version
    """

    pass


class KeysResponse(KeysResponseLatest):
    """
    pass through for KeysResponse based on API version
    """

    pass


class ScopesResponse(ScopesResponseLatest):
    """
    pass through for ScopesResponse based on API version
    """

    pass


class InvitesResponse(InvitesResponseLatest):
    """
    pass through for InvitesResponse based on API version
    """

    pass


class UsageRequest(UsageRequestLatest):
    """
    pass through for UsageRequest based on API version
    """

    pass


class UsageRequestsResponse(UsageRequestsResponseLatest):
    """
    pass through for UsageRequestsResponse based on API version
    """

    pass


class UsageSummaryResponse(UsageSummaryResponseLatest):
    """
    pass through for UsageSummaryResponse based on API version
    """

    pass


class UsageFieldsResponse(UsageFieldsResponseLatest):
    """
    pass through for UsageFieldsResponse based on API version
    """

    pass


class Balance(BalanceLatest):
    """
    pass through for Balance based on API version
    """

    pass


class BalancesResponse(BalancesResponseLatest):
    """
    pass through for BalancesResponse based on API version
    """

    pass


# clients
class ManageClient(ManageClientLatest):
    """
    Please see ManageClientLatest for details
    """

    def __init__(self, config):
        super().__init__(config)


class AsyncManageClient(AsyncManageClientLatest):
    """
    Please see AsyncManageClientLatest for details
    """

    def __init__(self, config):
        super().__init__(config)
