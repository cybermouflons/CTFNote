import sgqlc.types
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class AssignedTagsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'TAG_ID_ASC', 'TAG_ID_DESC', 'TASK_ID_ASC', 'TASK_ID_DESC')


Boolean = sgqlc.types.Boolean

class CtfSecretsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class CtfsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('END_TIME_ASC', 'END_TIME_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SECRETS_ID_ASC', 'SECRETS_ID_DESC', 'START_TIME_ASC', 'START_TIME_DESC', 'TITLE_ASC', 'TITLE_DESC')


class Cursor(sgqlc.types.Scalar):
    __schema__ = schema


class Datetime(sgqlc.types.Scalar):
    __schema__ = schema


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class InvitationsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CTF_ID_ASC', 'CTF_ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROFILE_ID_ASC', 'PROFILE_ID_DESC')


class JSON(sgqlc.types.Scalar):
    __schema__ = schema


class Jwt(sgqlc.types.Scalar):
    __schema__ = schema


class ProfilesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DISCORD_ID_ASC', 'DISCORD_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'USERNAME_ASC', 'USERNAME_DESC')


class PublicProfilesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NATURAL',)


class Role(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('USER_ADMIN', 'USER_FRIEND', 'USER_GUEST', 'USER_MANAGER', 'USER_MEMBER')


class SettingsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


String = sgqlc.types.String

class TagsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'TAG_ASC', 'TAG_DESC')


class TasksOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CTF_ID_ASC', 'CTF_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'TITLE_ASC', 'TITLE_DESC')


class Upload(sgqlc.types.Scalar):
    __schema__ = schema


class UsersOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NATURAL',)


class WorkOnTasksOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'PROFILE_ID_ASC', 'PROFILE_ID_DESC', 'TASK_ID_ASC', 'TASK_ID_DESC')



########################################################################
# Input Objects
########################################################################
class AddTagsForTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tags', 'taskid')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    taskid = sgqlc.types.Field(Int, graphql_name='taskid')


class AssignedTagCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('tag_id', 'task_id')
    tag_id = sgqlc.types.Field(Int, graphql_name='tagId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class AssignedTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('tag_id', 'task_id')
    tag_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tagId')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')


class CancelWorkAssignInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile_id = sgqlc.types.Field(Int, graphql_name='profileId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class CancelWorkingOnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class ChangePasswordInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'newpassword', 'oldpassword')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    newpassword = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='newpassword')
    oldpassword = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='oldpassword')


class CreateAssignedTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('assigned_tag', 'client_mutation_id')
    assigned_tag = sgqlc.types.Field(sgqlc.types.non_null(AssignedTagInput), graphql_name='assignedTag')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class CreateCtfInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field(sgqlc.types.non_null('CtfInput'), graphql_name='ctf')


class CreateInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation = sgqlc.types.Field(sgqlc.types.non_null('InvitationInput'), graphql_name='invitation')


class CreateInvitationLinkInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discord_id', 'role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discord_id = sgqlc.types.Field(String, graphql_name='discordId')
    role = sgqlc.types.Field(Role, graphql_name='role')


class CreateResetPasswordLinkInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(Int, graphql_name='userId')


class CreateTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tag')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tag = sgqlc.types.Field(sgqlc.types.non_null('TagInput'), graphql_name='tag')


class CreateTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_id', 'description', 'files', 'flag', 'tags', 'title')
    ctf_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ctfId')
    description = sgqlc.types.Field(String, graphql_name='description')
    files = sgqlc.types.Field(String, graphql_name='files')
    flag = sgqlc.types.Field(String, graphql_name='flag')
    tags = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='tags')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class CreateWorkOnTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'work_on_task')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    work_on_task = sgqlc.types.Field(sgqlc.types.non_null('WorkOnTaskInput'), graphql_name='workOnTask')


class CtfCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('end_time', 'id', 'secrets_id', 'start_time', 'title')
    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')
    id = sgqlc.types.Field(Int, graphql_name='id')
    secrets_id = sgqlc.types.Field(Int, graphql_name='secretsId')
    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')
    title = sgqlc.types.Field(String, graphql_name='title')


class CtfFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'not_', 'or_', 'title')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CtfFilter')), graphql_name='and')
    not_ = sgqlc.types.Field('CtfFilter', graphql_name='not')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('CtfFilter')), graphql_name='or')
    title = sgqlc.types.Field('StringFilter', graphql_name='title')


class CtfInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_platform', 'ctf_url', 'ctftime_url', 'description', 'end_time', 'logo_url', 'start_time', 'title', 'weight')
    ctf_platform = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ctfPlatform')
    ctf_url = sgqlc.types.Field(String, graphql_name='ctfUrl')
    ctftime_url = sgqlc.types.Field(String, graphql_name='ctftimeUrl')
    description = sgqlc.types.Field(String, graphql_name='description')
    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    weight = sgqlc.types.Field(Float, graphql_name='weight')


class CtfPatch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_platform', 'ctf_url', 'ctftime_url', 'description', 'discord_event_link', 'end_time', 'logo_url', 'start_time', 'title', 'weight')
    ctf_platform = sgqlc.types.Field(String, graphql_name='ctfPlatform')
    ctf_url = sgqlc.types.Field(String, graphql_name='ctfUrl')
    ctftime_url = sgqlc.types.Field(String, graphql_name='ctftimeUrl')
    description = sgqlc.types.Field(String, graphql_name='description')
    discord_event_link = sgqlc.types.Field(String, graphql_name='discordEventLink')
    end_time = sgqlc.types.Field(Datetime, graphql_name='endTime')
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    start_time = sgqlc.types.Field(Datetime, graphql_name='startTime')
    title = sgqlc.types.Field(String, graphql_name='title')
    weight = sgqlc.types.Field(Float, graphql_name='weight')


class CtfSecretCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(Int, graphql_name='id')


class CtfSecretPatch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('extra_info', 'password', 'scoreboard_name', 'username')
    extra_info = sgqlc.types.Field(String, graphql_name='extraInfo')
    password = sgqlc.types.Field(String, graphql_name='password')
    scoreboard_name = sgqlc.types.Field(String, graphql_name='scoreboardName')
    username = sgqlc.types.Field(String, graphql_name='username')


class DeleteAssignedTagByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteAssignedTagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'tag_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    tag_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tagId')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')


class DeleteCtfByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteCtfInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class DeleteInvitationByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteInvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf_id', 'profile_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ctfId')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')


class DeleteTaskByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')


class DeleteUserInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(Int, graphql_name='userId')


class DeleteWorkOnTaskByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class DeleteWorkOnTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')


class ImportCtfInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_platform', 'ctftime_id')
    ctf_platform = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ctfPlatform')
    ctftime_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ctftimeId')


class InvitationCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_id', 'profile_id')
    ctf_id = sgqlc.types.Field(Int, graphql_name='ctfId')
    profile_id = sgqlc.types.Field(Int, graphql_name='profileId')


class InvitationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_id', 'profile_id')
    ctf_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ctfId')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')


class LoginInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'login', 'password')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class ProfileCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('discord_id', 'id', 'username')
    discord_id = sgqlc.types.Field(String, graphql_name='discordId')
    id = sgqlc.types.Field(Int, graphql_name='id')
    username = sgqlc.types.Field(String, graphql_name='username')


class ProfileFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'discord_id', 'not_', 'or_', 'username')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProfileFilter')), graphql_name='and')
    discord_id = sgqlc.types.Field('StringFilter', graphql_name='discordId')
    not_ = sgqlc.types.Field('ProfileFilter', graphql_name='not')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('ProfileFilter')), graphql_name='or')
    username = sgqlc.types.Field('StringFilter', graphql_name='username')


class ProfilePatch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('color', 'description', 'username')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    username = sgqlc.types.Field(String, graphql_name='username')


class RegisterInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'login', 'password')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class RegisterWithPasswordInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctfnote_password', 'login', 'password')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctfnote_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ctfnotePassword')
    login = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='login')
    password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='password')


class RegisterWithTokenInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'login', 'password', 'token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    login = sgqlc.types.Field(String, graphql_name='login')
    password = sgqlc.types.Field(String, graphql_name='password')
    token = sgqlc.types.Field(String, graphql_name='token')


class ResetDiscordIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class ResetPasswordInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'password', 'token')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    password = sgqlc.types.Field(String, graphql_name='password')
    token = sgqlc.types.Field(String, graphql_name='token')


class ResetProfileTokenInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class SetDiscordEventLinkInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf_id', 'link')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf_id = sgqlc.types.Field(Int, graphql_name='ctfId')
    link = sgqlc.types.Field(String, graphql_name='link')


class SettingPatch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('discord_integration_enabled', 'ical_password', 'registration_allowed', 'registration_default_role', 'registration_password', 'registration_password_allowed', 'style')
    discord_integration_enabled = sgqlc.types.Field(Boolean, graphql_name='discordIntegrationEnabled')
    ical_password = sgqlc.types.Field(String, graphql_name='icalPassword')
    registration_allowed = sgqlc.types.Field(Boolean, graphql_name='registrationAllowed')
    registration_default_role = sgqlc.types.Field(Role, graphql_name='registrationDefaultRole')
    registration_password = sgqlc.types.Field(String, graphql_name='registrationPassword')
    registration_password_allowed = sgqlc.types.Field(Boolean, graphql_name='registrationPasswordAllowed')
    style = sgqlc.types.Field(JSON, graphql_name='style')


class StartWorkingOnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class StopWorkingOnInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class StringFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('includes_insensitive',)
    includes_insensitive = sgqlc.types.Field(String, graphql_name='includesInsensitive')


class TagCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'tag')
    id = sgqlc.types.Field(Int, graphql_name='id')
    tag = sgqlc.types.Field(String, graphql_name='tag')


class TagFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'not_', 'or_', 'tag')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TagFilter')), graphql_name='and')
    not_ = sgqlc.types.Field('TagFilter', graphql_name='not')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TagFilter')), graphql_name='or')
    tag = sgqlc.types.Field(StringFilter, graphql_name='tag')


class TagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'tag')
    id = sgqlc.types.Field(Int, graphql_name='id')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')


class TaskCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('ctf_id', 'id', 'title')
    ctf_id = sgqlc.types.Field(Int, graphql_name='ctfId')
    id = sgqlc.types.Field(Int, graphql_name='id')
    title = sgqlc.types.Field(String, graphql_name='title')


class TaskFilter(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('and_', 'not_', 'or_', 'title')
    and_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TaskFilter')), graphql_name='and')
    not_ = sgqlc.types.Field('TaskFilter', graphql_name='not')
    or_ = sgqlc.types.Field(sgqlc.types.list_of(sgqlc.types.non_null('TaskFilter')), graphql_name='or')
    title = sgqlc.types.Field(StringFilter, graphql_name='title')


class TaskPatch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('description', 'files', 'flag', 'title')
    description = sgqlc.types.Field(String, graphql_name='description')
    files = sgqlc.types.Field(String, graphql_name='files')
    flag = sgqlc.types.Field(String, graphql_name='flag')
    title = sgqlc.types.Field(String, graphql_name='title')


class UpdateCtfByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(CtfPatch), graphql_name='patch')


class UpdateCtfInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    patch = sgqlc.types.Field(sgqlc.types.non_null(CtfPatch), graphql_name='patch')


class UpdateCtfSecretByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(CtfSecretPatch), graphql_name='patch')


class UpdateCtfSecretInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    patch = sgqlc.types.Field(sgqlc.types.non_null(CtfSecretPatch), graphql_name='patch')


class UpdateLastActiveInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id',)
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')


class UpdateProfileByDiscordIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'discord_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    discord_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='discordId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProfilePatch), graphql_name='patch')


class UpdateProfileByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProfilePatch), graphql_name='patch')


class UpdateProfileByUsernameInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'patch', 'username')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProfilePatch), graphql_name='patch')
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')


class UpdateProfileInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    patch = sgqlc.types.Field(sgqlc.types.non_null(ProfilePatch), graphql_name='patch')


class UpdateSettingByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(SettingPatch), graphql_name='patch')


class UpdateTaskByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null(TaskPatch), graphql_name='patch')


class UpdateTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    patch = sgqlc.types.Field(sgqlc.types.non_null(TaskPatch), graphql_name='patch')


class UpdateUserRoleInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'role', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    role = sgqlc.types.Field(Role, graphql_name='role')
    user_id = sgqlc.types.Field(Int, graphql_name='userId')


class UpdateWorkOnTaskByNodeIdInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'node_id', 'patch')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')
    patch = sgqlc.types.Field(sgqlc.types.non_null('WorkOnTaskPatch'), graphql_name='patch')


class UpdateWorkOnTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'patch', 'profile_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    patch = sgqlc.types.Field(sgqlc.types.non_null('WorkOnTaskPatch'), graphql_name='patch')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')


class WorkAssignInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile_id = sgqlc.types.Field(Int, graphql_name='profileId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class WorkOnTaskCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('profile_id', 'task_id')
    profile_id = sgqlc.types.Field(Int, graphql_name='profileId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class WorkOnTaskInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('active', 'profile_id', 'task_id')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')


class WorkOnTaskPatch(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('active', 'profile_id', 'task_id')
    active = sgqlc.types.Field(Boolean, graphql_name='active')
    profile_id = sgqlc.types.Field(Int, graphql_name='profileId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')


class WorkUnassignInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile_id', 'task_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile_id = sgqlc.types.Field(Int, graphql_name='profileId')
    task_id = sgqlc.types.Field(Int, graphql_name='taskId')



########################################################################
# Output Objects and Interfaces
########################################################################
class Node(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class AddTagsForTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')


class AssignedTagsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssignedTagsEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('AssignedTag'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class AssignedTagsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('AssignedTag'), graphql_name='node')


class CancelWorkAssignPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CancelWorkingOnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class ChangePasswordPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('change_password_response', 'client_mutation_id', 'query')
    change_password_response = sgqlc.types.Field('ChangePasswordResponse', graphql_name='changePasswordResponse')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')


class ChangePasswordResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('ok',)
    ok = sgqlc.types.Field(Boolean, graphql_name='ok')


class CreateAssignedTagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assigned_tag', 'assigned_tag_edge', 'client_mutation_id', 'query', 'tag', 'task')
    assigned_tag = sgqlc.types.Field('AssignedTag', graphql_name='assignedTag')
    assigned_tag_edge = sgqlc.types.Field(AssignedTagsEdge, graphql_name='assignedTagEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(AssignedTagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')
    task = sgqlc.types.Field('Task', graphql_name='task')


class CreateCtfPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'ctf_edge', 'query', 'secrets')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    ctf_edge = sgqlc.types.Field('CtfsEdge', graphql_name='ctfEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    query = sgqlc.types.Field('Query', graphql_name='query')
    secrets = sgqlc.types.Field('CtfSecret', graphql_name='secrets')


class CreateInvitationLinkPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'invitation_link_response', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    invitation_link_response = sgqlc.types.Field('InvitationLinkResponse', graphql_name='invitationLinkResponse')
    query = sgqlc.types.Field('Query', graphql_name='query')


class CreateInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'invitation', 'invitation_edge', 'profile', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    invitation = sgqlc.types.Field('Invitation', graphql_name='invitation')
    invitation_edge = sgqlc.types.Field('InvitationsEdge', graphql_name='invitationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(InvitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')


class CreateResetPasswordLinkPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'reset_password_link_response')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    reset_password_link_response = sgqlc.types.Field('ResetPasswordLinkResponse', graphql_name='resetPasswordLinkResponse')


class CreateTagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'tag', 'tag_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')
    tag_edge = sgqlc.types.Field('TagsEdge', graphql_name='tagEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CreateTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query', 'task')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')


class CreateWorkOnTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CtfProfilesByInvitationCtfIdAndProfileIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CtfProfilesByInvitationCtfIdAndProfileIdManyToManyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Profile'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CtfProfilesByInvitationCtfIdAndProfileIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Profile'), graphql_name='node')


class CtfSecretsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CtfSecretsEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CtfSecret'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CtfSecretsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('CtfSecret'), graphql_name='node')


class CtfsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CtfsEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Ctf'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CtfsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Ctf'), graphql_name='node')


class DeleteAssignedTagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('assigned_tag', 'assigned_tag_edge', 'client_mutation_id', 'deleted_assigned_tag_node_id', 'query', 'tag', 'task')
    assigned_tag = sgqlc.types.Field('AssignedTag', graphql_name='assignedTag')
    assigned_tag_edge = sgqlc.types.Field(AssignedTagsEdge, graphql_name='assignedTagEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(AssignedTagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_assigned_tag_node_id = sgqlc.types.Field(ID, graphql_name='deletedAssignedTagNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')
    task = sgqlc.types.Field('Task', graphql_name='task')


class DeleteCtfPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'ctf_edge', 'deleted_ctf_node_id', 'query', 'secrets')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    ctf_edge = sgqlc.types.Field(CtfsEdge, graphql_name='ctfEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    deleted_ctf_node_id = sgqlc.types.Field(ID, graphql_name='deletedCtfNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    secrets = sgqlc.types.Field('CtfSecret', graphql_name='secrets')


class DeleteInvitationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'deleted_invitation_node_id', 'invitation', 'invitation_edge', 'profile', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    deleted_invitation_node_id = sgqlc.types.Field(ID, graphql_name='deletedInvitationNodeId')
    invitation = sgqlc.types.Field('Invitation', graphql_name='invitation')
    invitation_edge = sgqlc.types.Field('InvitationsEdge', graphql_name='invitationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(InvitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')


class DeleteTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'deleted_task_node_id', 'query', 'task', 'task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    deleted_task_node_id = sgqlc.types.Field(ID, graphql_name='deletedTaskNodeId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    task_edge = sgqlc.types.Field('TasksEdge', graphql_name='taskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class DeleteUserPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'user_response')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    user_response = sgqlc.types.Field('UserResponse', graphql_name='userResponse')


class DeleteWorkOnTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'deleted_work_on_task_node_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    deleted_work_on_task_node_id = sgqlc.types.Field(ID, graphql_name='deletedWorkOnTaskNodeId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class ImportCtfPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('ctf', 'query')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    query = sgqlc.types.Field('Query', graphql_name='query')


class InvitationLinkResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(String, graphql_name='token')


class InvitationsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('InvitationsEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Invitation'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class InvitationsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Invitation'), graphql_name='node')


class ListenPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('query', 'related_node', 'related_node_id')
    query = sgqlc.types.Field('Query', graphql_name='query')
    related_node = sgqlc.types.Field(Node, graphql_name='relatedNode')
    related_node_id = sgqlc.types.Field(ID, graphql_name='relatedNodeId')


class LoginPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt = sgqlc.types.Field(Jwt, graphql_name='jwt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('add_tags_for_task', 'cancel_work_assign', 'cancel_working_on', 'change_password', 'create_assigned_tag', 'create_ctf', 'create_invitation', 'create_invitation_link', 'create_reset_password_link', 'create_tag', 'create_task', 'create_work_on_task', 'delete_assigned_tag', 'delete_assigned_tag_by_node_id', 'delete_ctf', 'delete_ctf_by_node_id', 'delete_invitation', 'delete_invitation_by_node_id', 'delete_task', 'delete_task_by_node_id', 'delete_user', 'delete_work_on_task', 'delete_work_on_task_by_node_id', 'import_ctf', 'login', 'register', 'register_with_password', 'register_with_token', 'reset_discord_id', 'reset_password', 'reset_profile_token', 'set_discord_event_link', 'start_working_on', 'stop_working_on', 'update_ctf', 'update_ctf_by_node_id', 'update_ctf_secret', 'update_ctf_secret_by_node_id', 'update_last_active', 'update_profile', 'update_profile_by_discord_id', 'update_profile_by_node_id', 'update_profile_by_username', 'update_setting_by_node_id', 'update_task', 'update_task_by_node_id', 'update_user_role', 'update_work_on_task', 'update_work_on_task_by_node_id', 'upload_ctf_logo', 'work_assign', 'work_unassign')
    add_tags_for_task = sgqlc.types.Field(AddTagsForTaskPayload, graphql_name='addTagsForTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AddTagsForTaskInput), graphql_name='input', default=None)),
))
    )
    cancel_work_assign = sgqlc.types.Field(CancelWorkAssignPayload, graphql_name='cancelWorkAssign', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CancelWorkAssignInput), graphql_name='input', default=None)),
))
    )
    cancel_working_on = sgqlc.types.Field(CancelWorkingOnPayload, graphql_name='cancelWorkingOn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CancelWorkingOnInput), graphql_name='input', default=None)),
))
    )
    change_password = sgqlc.types.Field(ChangePasswordPayload, graphql_name='changePassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ChangePasswordInput), graphql_name='input', default=None)),
))
    )
    create_assigned_tag = sgqlc.types.Field(CreateAssignedTagPayload, graphql_name='createAssignedTag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateAssignedTagInput), graphql_name='input', default=None)),
))
    )
    create_ctf = sgqlc.types.Field(CreateCtfPayload, graphql_name='createCtf', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateCtfInput), graphql_name='input', default=None)),
))
    )
    create_invitation = sgqlc.types.Field(CreateInvitationPayload, graphql_name='createInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateInvitationInput), graphql_name='input', default=None)),
))
    )
    create_invitation_link = sgqlc.types.Field(CreateInvitationLinkPayload, graphql_name='createInvitationLink', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateInvitationLinkInput), graphql_name='input', default=None)),
))
    )
    create_reset_password_link = sgqlc.types.Field(CreateResetPasswordLinkPayload, graphql_name='createResetPasswordLink', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateResetPasswordLinkInput), graphql_name='input', default=None)),
))
    )
    create_tag = sgqlc.types.Field(CreateTagPayload, graphql_name='createTag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateTagInput), graphql_name='input', default=None)),
))
    )
    create_task = sgqlc.types.Field(CreateTaskPayload, graphql_name='createTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(CreateTaskInput, graphql_name='input', default=None)),
))
    )
    create_work_on_task = sgqlc.types.Field(CreateWorkOnTaskPayload, graphql_name='createWorkOnTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateWorkOnTaskInput), graphql_name='input', default=None)),
))
    )
    delete_assigned_tag = sgqlc.types.Field(DeleteAssignedTagPayload, graphql_name='deleteAssignedTag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteAssignedTagInput), graphql_name='input', default=None)),
))
    )
    delete_assigned_tag_by_node_id = sgqlc.types.Field(DeleteAssignedTagPayload, graphql_name='deleteAssignedTagByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteAssignedTagByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_ctf = sgqlc.types.Field(DeleteCtfPayload, graphql_name='deleteCtf', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCtfInput), graphql_name='input', default=None)),
))
    )
    delete_ctf_by_node_id = sgqlc.types.Field(DeleteCtfPayload, graphql_name='deleteCtfByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteCtfByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_invitation = sgqlc.types.Field(DeleteInvitationPayload, graphql_name='deleteInvitation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInvitationInput), graphql_name='input', default=None)),
))
    )
    delete_invitation_by_node_id = sgqlc.types.Field(DeleteInvitationPayload, graphql_name='deleteInvitationByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteInvitationByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_task = sgqlc.types.Field(DeleteTaskPayload, graphql_name='deleteTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTaskInput), graphql_name='input', default=None)),
))
    )
    delete_task_by_node_id = sgqlc.types.Field(DeleteTaskPayload, graphql_name='deleteTaskByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteTaskByNodeIdInput), graphql_name='input', default=None)),
))
    )
    delete_user = sgqlc.types.Field(DeleteUserPayload, graphql_name='deleteUser', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteUserInput), graphql_name='input', default=None)),
))
    )
    delete_work_on_task = sgqlc.types.Field(DeleteWorkOnTaskPayload, graphql_name='deleteWorkOnTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteWorkOnTaskInput), graphql_name='input', default=None)),
))
    )
    delete_work_on_task_by_node_id = sgqlc.types.Field(DeleteWorkOnTaskPayload, graphql_name='deleteWorkOnTaskByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(DeleteWorkOnTaskByNodeIdInput), graphql_name='input', default=None)),
))
    )
    import_ctf = sgqlc.types.Field(ImportCtfPayload, graphql_name='importCtf', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(ImportCtfInput, graphql_name='input', default=None)),
))
    )
    login = sgqlc.types.Field(LoginPayload, graphql_name='login', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(LoginInput), graphql_name='input', default=None)),
))
    )
    register = sgqlc.types.Field('RegisterPayload', graphql_name='register', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegisterInput), graphql_name='input', default=None)),
))
    )
    register_with_password = sgqlc.types.Field('RegisterWithPasswordPayload', graphql_name='registerWithPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegisterWithPasswordInput), graphql_name='input', default=None)),
))
    )
    register_with_token = sgqlc.types.Field('RegisterWithTokenPayload', graphql_name='registerWithToken', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(RegisterWithTokenInput), graphql_name='input', default=None)),
))
    )
    reset_discord_id = sgqlc.types.Field('ResetDiscordIdPayload', graphql_name='resetDiscordId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ResetDiscordIdInput), graphql_name='input', default=None)),
))
    )
    reset_password = sgqlc.types.Field('ResetPasswordPayload', graphql_name='resetPassword', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ResetPasswordInput), graphql_name='input', default=None)),
))
    )
    reset_profile_token = sgqlc.types.Field('ResetProfileTokenPayload', graphql_name='resetProfileToken', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(ResetProfileTokenInput), graphql_name='input', default=None)),
))
    )
    set_discord_event_link = sgqlc.types.Field('SetDiscordEventLinkPayload', graphql_name='setDiscordEventLink', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(SetDiscordEventLinkInput), graphql_name='input', default=None)),
))
    )
    start_working_on = sgqlc.types.Field('StartWorkingOnPayload', graphql_name='startWorkingOn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StartWorkingOnInput), graphql_name='input', default=None)),
))
    )
    stop_working_on = sgqlc.types.Field('StopWorkingOnPayload', graphql_name='stopWorkingOn', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(StopWorkingOnInput), graphql_name='input', default=None)),
))
    )
    update_ctf = sgqlc.types.Field('UpdateCtfPayload', graphql_name='updateCtf', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCtfInput), graphql_name='input', default=None)),
))
    )
    update_ctf_by_node_id = sgqlc.types.Field('UpdateCtfPayload', graphql_name='updateCtfByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCtfByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_ctf_secret = sgqlc.types.Field('UpdateCtfSecretPayload', graphql_name='updateCtfSecret', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCtfSecretInput), graphql_name='input', default=None)),
))
    )
    update_ctf_secret_by_node_id = sgqlc.types.Field('UpdateCtfSecretPayload', graphql_name='updateCtfSecretByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateCtfSecretByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_last_active = sgqlc.types.Field('UpdateLastActivePayload', graphql_name='updateLastActive', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateLastActiveInput), graphql_name='input', default=None)),
))
    )
    update_profile = sgqlc.types.Field('UpdateProfilePayload', graphql_name='updateProfile', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProfileInput), graphql_name='input', default=None)),
))
    )
    update_profile_by_discord_id = sgqlc.types.Field('UpdateProfilePayload', graphql_name='updateProfileByDiscordId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProfileByDiscordIdInput), graphql_name='input', default=None)),
))
    )
    update_profile_by_node_id = sgqlc.types.Field('UpdateProfilePayload', graphql_name='updateProfileByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProfileByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_profile_by_username = sgqlc.types.Field('UpdateProfilePayload', graphql_name='updateProfileByUsername', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateProfileByUsernameInput), graphql_name='input', default=None)),
))
    )
    update_setting_by_node_id = sgqlc.types.Field('UpdateSettingPayload', graphql_name='updateSettingByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateSettingByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_task = sgqlc.types.Field('UpdateTaskPayload', graphql_name='updateTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTaskInput), graphql_name='input', default=None)),
))
    )
    update_task_by_node_id = sgqlc.types.Field('UpdateTaskPayload', graphql_name='updateTaskByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateTaskByNodeIdInput), graphql_name='input', default=None)),
))
    )
    update_user_role = sgqlc.types.Field('UpdateUserRolePayload', graphql_name='updateUserRole', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateUserRoleInput), graphql_name='input', default=None)),
))
    )
    update_work_on_task = sgqlc.types.Field('UpdateWorkOnTaskPayload', graphql_name='updateWorkOnTask', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkOnTaskInput), graphql_name='input', default=None)),
))
    )
    update_work_on_task_by_node_id = sgqlc.types.Field('UpdateWorkOnTaskPayload', graphql_name='updateWorkOnTaskByNodeId', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(UpdateWorkOnTaskByNodeIdInput), graphql_name='input', default=None)),
))
    )
    upload_ctf_logo = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='uploadCtfLogo', args=sgqlc.types.ArgDict((
        ('logo', sgqlc.types.Arg(sgqlc.types.non_null(Upload), graphql_name='logo', default=None)),
))
    )
    work_assign = sgqlc.types.Field('WorkAssignPayload', graphql_name='workAssign', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WorkAssignInput), graphql_name='input', default=None)),
))
    )
    work_unassign = sgqlc.types.Field('WorkUnassignPayload', graphql_name='workUnassign', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(WorkUnassignInput), graphql_name='input', default=None)),
))
    )


class PageInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('end_cursor', 'has_next_page', 'has_previous_page', 'start_cursor')
    end_cursor = sgqlc.types.Field(Cursor, graphql_name='endCursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(Cursor, graphql_name='startCursor')


class ProfileCtfsByInvitationProfileIdAndCtfIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProfileCtfsByInvitationProfileIdAndCtfIdManyToManyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Ctf'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProfileCtfsByInvitationProfileIdAndCtfIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Ctf'), graphql_name='node')


class ProfileTasksByWorkOnTaskProfileIdAndTaskIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProfileTasksByWorkOnTaskProfileIdAndTaskIdManyToManyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Task'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProfileTasksByWorkOnTaskProfileIdAndTaskIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('active', 'cursor', 'node')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Task'), graphql_name='node')


class ProfilesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ProfilesEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Profile'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ProfilesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Profile'), graphql_name='node')


class PublicProfile(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('color', 'description', 'id', 'node_id', 'role', 'username')
    color = sgqlc.types.Field(String, graphql_name='color')
    description = sgqlc.types.Field(String, graphql_name='description')
    id = sgqlc.types.Field(Int, graphql_name='id')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    role = sgqlc.types.Field(Role, graphql_name='role')
    username = sgqlc.types.Field(String, graphql_name='username')


class PublicProfileSubscriptionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'public_profile')
    event = sgqlc.types.Field(String, graphql_name='event')
    public_profile = sgqlc.types.Field(PublicProfile, graphql_name='publicProfile')


class PublicProfilesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PublicProfilesEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(PublicProfile))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PublicProfilesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(PublicProfile), graphql_name='node')


class RegisterPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt = sgqlc.types.Field(Jwt, graphql_name='jwt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class RegisterWithPasswordPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt = sgqlc.types.Field(Jwt, graphql_name='jwt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class RegisterWithTokenPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt = sgqlc.types.Field(Jwt, graphql_name='jwt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class ResetDiscordIdPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'string')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    string = sgqlc.types.Field(String, graphql_name='string')


class ResetPasswordLinkResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('token',)
    token = sgqlc.types.Field(String, graphql_name='token')


class ResetPasswordPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt = sgqlc.types.Field(Jwt, graphql_name='jwt')
    query = sgqlc.types.Field('Query', graphql_name='query')


class ResetProfileTokenPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'string')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    string = sgqlc.types.Field(String, graphql_name='string')


class SetDiscordEventLinkPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')


class SettingsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('SettingsEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Setting'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class SettingsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Setting'), graphql_name='node')


class StartWorkingOnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class StopWorkingOnPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class Subscription(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('current_profile_created', 'current_profile_deleted', 'current_profile_updated', 'listen')
    current_profile_created = sgqlc.types.Field(PublicProfileSubscriptionPayload, graphql_name='currentProfileCreated')
    current_profile_deleted = sgqlc.types.Field(PublicProfileSubscriptionPayload, graphql_name='currentProfileDeleted')
    current_profile_updated = sgqlc.types.Field(PublicProfileSubscriptionPayload, graphql_name='currentProfileUpdated')
    listen = sgqlc.types.Field(sgqlc.types.non_null(ListenPayload), graphql_name='listen', args=sgqlc.types.ArgDict((
        ('topic', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='topic', default=None)),
))
    )


class TagTasksByAssignedTagTagIdAndTaskIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagTasksByAssignedTagTagIdAndTaskIdManyToManyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Task'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TagTasksByAssignedTagTagIdAndTaskIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Task'), graphql_name='node')


class TagsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TagsEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tag'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TagsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Tag'), graphql_name='node')


class TaskProfilesByWorkOnTaskTaskIdAndProfileIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaskProfilesByWorkOnTaskTaskIdAndProfileIdManyToManyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Profile'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TaskProfilesByWorkOnTaskTaskIdAndProfileIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('active', 'cursor', 'node')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Profile'), graphql_name='node')


class TaskTagsByAssignedTagTaskIdAndTagIdManyToManyConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TaskTagsByAssignedTagTaskIdAndTagIdManyToManyEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Tag'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TaskTagsByAssignedTagTaskIdAndTagIdManyToManyEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Tag'), graphql_name='node')


class TasksConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TasksEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Task'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TasksEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Task'), graphql_name='node')


class UpdateCtfPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'ctf_edge', 'query', 'secrets')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    ctf_edge = sgqlc.types.Field(CtfsEdge, graphql_name='ctfEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    query = sgqlc.types.Field('Query', graphql_name='query')
    secrets = sgqlc.types.Field('CtfSecret', graphql_name='secrets')


class UpdateCtfSecretPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf_secret', 'ctf_secret_edge', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf_secret = sgqlc.types.Field('CtfSecret', graphql_name='ctfSecret')
    ctf_secret_edge = sgqlc.types.Field(CtfSecretsEdge, graphql_name='ctfSecretEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfSecretsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    query = sgqlc.types.Field('Query', graphql_name='query')


class UpdateLastActivePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')


class UpdateProfilePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'profile_edge', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    profile_edge = sgqlc.types.Field(ProfilesEdge, graphql_name='profileEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProfilesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    query = sgqlc.types.Field('Query', graphql_name='query')


class UpdateSettingPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'setting', 'setting_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    setting = sgqlc.types.Field('Setting', graphql_name='setting')
    setting_edge = sgqlc.types.Field(SettingsEdge, graphql_name='settingEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SettingsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class UpdateTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'ctf', 'query', 'task', 'task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    ctf = sgqlc.types.Field('Ctf', graphql_name='ctf')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    task_edge = sgqlc.types.Field(TasksEdge, graphql_name='taskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class UpdateUserRolePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'query', 'role')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    query = sgqlc.types.Field('Query', graphql_name='query')
    role = sgqlc.types.Field(Role, graphql_name='role')


class UpdateWorkOnTaskPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class User(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'login', 'node_id', 'profile', 'role')
    id = sgqlc.types.Field(Int, graphql_name='id')
    login = sgqlc.types.Field(String, graphql_name='login')
    node_id = sgqlc.types.Field(String, graphql_name='nodeId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    role = sgqlc.types.Field(Role, graphql_name='role')


class UserResponse(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('id', 'login', 'role')
    id = sgqlc.types.Field(Int, graphql_name='id')
    login = sgqlc.types.Field(String, graphql_name='login')
    role = sgqlc.types.Field(Role, graphql_name='role')


class UsersConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UsersEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(User))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UsersEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(User), graphql_name='node')


class WorkAssignPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field('WorkOnTasksEdge', graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class WorkOnTasksConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('edges', 'nodes', 'page_info', 'total_count')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkOnTasksEdge'))), graphql_name='edges')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('WorkOnTask'))), graphql_name='nodes')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class WorkOnTasksEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('WorkOnTask'), graphql_name='node')


class WorkUnassignPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'profile', 'query', 'task', 'work_on_task', 'work_on_task_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    query = sgqlc.types.Field('Query', graphql_name='query')
    task = sgqlc.types.Field('Task', graphql_name='task')
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask')
    work_on_task_edge = sgqlc.types.Field(WorkOnTasksEdge, graphql_name='workOnTaskEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class AssignedTag(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('tag', 'tag_id', 'task', 'task_id')
    tag = sgqlc.types.Field('Tag', graphql_name='tag')
    tag_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='tagId')
    task = sgqlc.types.Field('Task', graphql_name='task')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')


class Ctf(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('ctf_platform', 'ctf_url', 'ctftime_url', 'description', 'discord_event_link', 'end_time', 'granted', 'id', 'invitations', 'logo_url', 'profiles_by_invitation_ctf_id_and_profile_id', 'secrets', 'secrets_id', 'start_time', 'tasks', 'title', 'weight')
    ctf_platform = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='ctfPlatform')
    ctf_url = sgqlc.types.Field(String, graphql_name='ctfUrl')
    ctftime_url = sgqlc.types.Field(String, graphql_name='ctftimeUrl')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    discord_event_link = sgqlc.types.Field(String, graphql_name='discordEventLink')
    end_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='endTime')
    granted = sgqlc.types.Field(Boolean, graphql_name='granted')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    invitations = sgqlc.types.Field(sgqlc.types.non_null(InvitationsConnection), graphql_name='invitations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(InvitationCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(InvitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    logo_url = sgqlc.types.Field(String, graphql_name='logoUrl')
    profiles_by_invitation_ctf_id_and_profile_id = sgqlc.types.Field(sgqlc.types.non_null(CtfProfilesByInvitationCtfIdAndProfileIdManyToManyConnection), graphql_name='profilesByInvitationCtfIdAndProfileId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(ProfileCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProfileFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProfilesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    secrets = sgqlc.types.Field('CtfSecret', graphql_name='secrets')
    secrets_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='secretsId')
    start_time = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='startTime')
    tasks = sgqlc.types.Field(sgqlc.types.non_null(TasksConnection), graphql_name='tasks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(TaskCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(TaskFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    weight = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='weight')


class CtfSecret(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('ctfs_by_secrets_id', 'extra_info', 'id', 'password', 'scoreboard_name', 'username')
    ctfs_by_secrets_id = sgqlc.types.Field(sgqlc.types.non_null(CtfsConnection), graphql_name='ctfsBySecretsId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(CtfCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CtfFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    extra_info = sgqlc.types.Field(String, graphql_name='extraInfo')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    password = sgqlc.types.Field(String, graphql_name='password')
    scoreboard_name = sgqlc.types.Field(String, graphql_name='scoreboardName')
    username = sgqlc.types.Field(String, graphql_name='username')


class Invitation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('ctf', 'ctf_id', 'profile', 'profile_id')
    ctf = sgqlc.types.Field(Ctf, graphql_name='ctf')
    ctf_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ctfId')
    profile = sgqlc.types.Field('Profile', graphql_name='profile')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')


class Profile(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('color', 'ctfs_by_invitation_profile_id_and_ctf_id', 'description', 'discord_id', 'id', 'invitations', 'lastactive', 'role', 'tasks_by_work_on_task_profile_id_and_task_id', 'username', 'work_on_tasks')
    color = sgqlc.types.Field(String, graphql_name='color')
    ctfs_by_invitation_profile_id_and_ctf_id = sgqlc.types.Field(sgqlc.types.non_null(ProfileCtfsByInvitationProfileIdAndCtfIdManyToManyConnection), graphql_name='ctfsByInvitationProfileIdAndCtfId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(CtfCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CtfFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    discord_id = sgqlc.types.Field(String, graphql_name='discordId')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    invitations = sgqlc.types.Field(sgqlc.types.non_null(InvitationsConnection), graphql_name='invitations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(InvitationCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(InvitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    lastactive = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='lastactive')
    role = sgqlc.types.Field(Role, graphql_name='role')
    tasks_by_work_on_task_profile_id_and_task_id = sgqlc.types.Field(sgqlc.types.non_null(ProfileTasksByWorkOnTaskProfileIdAndTaskIdManyToManyConnection), graphql_name='tasksByWorkOnTaskProfileIdAndTaskId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(TaskCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(TaskFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    username = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='username')
    work_on_tasks = sgqlc.types.Field(sgqlc.types.non_null(WorkOnTasksConnection), graphql_name='workOnTasks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(WorkOnTaskCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class Query(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('assigned_tag', 'assigned_tag_by_node_id', 'assigned_tags', 'ctf', 'ctf_by_node_id', 'ctf_secret', 'ctf_secret_by_node_id', 'ctf_secrets', 'ctfs', 'guests', 'incoming_ctf', 'invitation', 'invitation_by_node_id', 'invitations', 'me', 'new_token', 'node', 'past_ctf', 'profile', 'profile_by_discord_id', 'profile_by_node_id', 'profile_by_username', 'profile_token', 'profiles', 'public_profiles', 'query', 'setting_by_node_id', 'settings', 'tag', 'tag_by_node_id', 'tag_by_tag', 'tags', 'task', 'task_by_node_id', 'tasks', 'users', 'work_on_task', 'work_on_task_by_node_id', 'work_on_tasks')
    assigned_tag = sgqlc.types.Field(AssignedTag, graphql_name='assignedTag', args=sgqlc.types.ArgDict((
        ('tag_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='tagId', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='taskId', default=None)),
))
    )
    assigned_tag_by_node_id = sgqlc.types.Field(AssignedTag, graphql_name='assignedTagByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    assigned_tags = sgqlc.types.Field(AssignedTagsConnection, graphql_name='assignedTags', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(AssignedTagCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(AssignedTagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    ctf = sgqlc.types.Field(Ctf, graphql_name='ctf', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    ctf_by_node_id = sgqlc.types.Field(Ctf, graphql_name='ctfByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    ctf_secret = sgqlc.types.Field(CtfSecret, graphql_name='ctfSecret', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    ctf_secret_by_node_id = sgqlc.types.Field(CtfSecret, graphql_name='ctfSecretByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    ctf_secrets = sgqlc.types.Field(CtfSecretsConnection, graphql_name='ctfSecrets', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(CtfSecretCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfSecretsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    ctfs = sgqlc.types.Field(CtfsConnection, graphql_name='ctfs', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(CtfCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(CtfFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CtfsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    guests = sgqlc.types.Field(ProfilesConnection, graphql_name='guests', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    incoming_ctf = sgqlc.types.Field(CtfsConnection, graphql_name='incomingCtf', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    invitation = sgqlc.types.Field(Invitation, graphql_name='invitation', args=sgqlc.types.ArgDict((
        ('ctf_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='ctfId', default=None)),
        ('profile_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='profileId', default=None)),
))
    )
    invitation_by_node_id = sgqlc.types.Field(Invitation, graphql_name='invitationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    invitations = sgqlc.types.Field(InvitationsConnection, graphql_name='invitations', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(InvitationCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(InvitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    me = sgqlc.types.Field(Profile, graphql_name='me')
    new_token = sgqlc.types.Field(Jwt, graphql_name='newToken')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    past_ctf = sgqlc.types.Field(CtfsConnection, graphql_name='pastCtf', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
))
    )
    profile = sgqlc.types.Field(Profile, graphql_name='profile', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    profile_by_discord_id = sgqlc.types.Field(Profile, graphql_name='profileByDiscordId', args=sgqlc.types.ArgDict((
        ('discord_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='discordId', default=None)),
))
    )
    profile_by_node_id = sgqlc.types.Field(Profile, graphql_name='profileByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    profile_by_username = sgqlc.types.Field(Profile, graphql_name='profileByUsername', args=sgqlc.types.ArgDict((
        ('username', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='username', default=None)),
))
    )
    profile_token = sgqlc.types.Field(String, graphql_name='profileToken')
    profiles = sgqlc.types.Field(ProfilesConnection, graphql_name='profiles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(ProfileCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProfileFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProfilesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    public_profiles = sgqlc.types.Field(PublicProfilesConnection, graphql_name='publicProfiles', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PublicProfilesOrderBy)), graphql_name='orderBy', default=('NATURAL',))),
))
    )
    query = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='query')
    setting_by_node_id = sgqlc.types.Field('Setting', graphql_name='settingByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    settings = sgqlc.types.Field(SettingsConnection, graphql_name='settings', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(SettingsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    tag = sgqlc.types.Field('Tag', graphql_name='tag', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    tag_by_node_id = sgqlc.types.Field('Tag', graphql_name='tagByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    tag_by_tag = sgqlc.types.Field('Tag', graphql_name='tagByTag', args=sgqlc.types.ArgDict((
        ('tag', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='tag', default=None)),
))
    )
    tags = sgqlc.types.Field(TagsConnection, graphql_name='tags', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(TagCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(TagFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    task = sgqlc.types.Field('Task', graphql_name='task', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='id', default=None)),
))
    )
    task_by_node_id = sgqlc.types.Field('Task', graphql_name='taskByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    tasks = sgqlc.types.Field(TasksConnection, graphql_name='tasks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(TaskCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(TaskFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    users = sgqlc.types.Field(UsersConnection, graphql_name='users', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UsersOrderBy)), graphql_name='orderBy', default=('NATURAL',))),
))
    )
    work_on_task = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTask', args=sgqlc.types.ArgDict((
        ('profile_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='profileId', default=None)),
        ('task_id', sgqlc.types.Arg(sgqlc.types.non_null(Int), graphql_name='taskId', default=None)),
))
    )
    work_on_task_by_node_id = sgqlc.types.Field('WorkOnTask', graphql_name='workOnTaskByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    work_on_tasks = sgqlc.types.Field(WorkOnTasksConnection, graphql_name='workOnTasks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(WorkOnTaskCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class Setting(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('discord_integration_enabled', 'ical_password', 'registration_allowed', 'registration_default_role', 'registration_password', 'registration_password_allowed', 'style')
    discord_integration_enabled = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='discordIntegrationEnabled')
    ical_password = sgqlc.types.Field(String, graphql_name='icalPassword')
    registration_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='registrationAllowed')
    registration_default_role = sgqlc.types.Field(sgqlc.types.non_null(Role), graphql_name='registrationDefaultRole')
    registration_password = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='registrationPassword')
    registration_password_allowed = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='registrationPasswordAllowed')
    style = sgqlc.types.Field(sgqlc.types.non_null(JSON), graphql_name='style')


class Tag(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('assigned_tags', 'id', 'tag', 'tasks_by_assigned_tag_tag_id_and_task_id')
    assigned_tags = sgqlc.types.Field(sgqlc.types.non_null(AssignedTagsConnection), graphql_name='assignedTags', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(AssignedTagCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(AssignedTagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    tag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='tag')
    tasks_by_assigned_tag_tag_id_and_task_id = sgqlc.types.Field(sgqlc.types.non_null(TagTasksByAssignedTagTagIdAndTaskIdManyToManyConnection), graphql_name='tasksByAssignedTagTagIdAndTaskId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(TaskCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(TaskFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class Task(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('assigned_tags', 'ctf', 'ctf_id', 'description', 'files', 'flag', 'id', 'pad_url', 'profiles_by_work_on_task_task_id_and_profile_id', 'solved', 'tags_by_assigned_tag_task_id_and_tag_id', 'title', 'work_on_tasks')
    assigned_tags = sgqlc.types.Field(sgqlc.types.non_null(AssignedTagsConnection), graphql_name='assignedTags', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(AssignedTagCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(AssignedTagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    ctf = sgqlc.types.Field(Ctf, graphql_name='ctf')
    ctf_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='ctfId')
    description = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='description')
    files = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='files')
    flag = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='flag')
    id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='id')
    pad_url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='padUrl')
    profiles_by_work_on_task_task_id_and_profile_id = sgqlc.types.Field(sgqlc.types.non_null(TaskProfilesByWorkOnTaskTaskIdAndProfileIdManyToManyConnection), graphql_name='profilesByWorkOnTaskTaskIdAndProfileId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(ProfileCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(ProfileFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ProfilesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    solved = sgqlc.types.Field(Boolean, graphql_name='solved')
    tags_by_assigned_tag_task_id_and_tag_id = sgqlc.types.Field(sgqlc.types.non_null(TaskTagsByAssignedTagTaskIdAndTagIdManyToManyConnection), graphql_name='tagsByAssignedTagTaskIdAndTagId', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(TagCondition, graphql_name='condition', default=None)),
        ('filter', sgqlc.types.Arg(TagFilter, graphql_name='filter', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')
    work_on_tasks = sgqlc.types.Field(sgqlc.types.non_null(WorkOnTasksConnection), graphql_name='workOnTasks', args=sgqlc.types.ArgDict((
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('condition', sgqlc.types.Arg(WorkOnTaskCondition, graphql_name='condition', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(WorkOnTasksOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class WorkOnTask(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('active', 'profile', 'profile_id', 'task', 'task_id')
    active = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='active')
    profile = sgqlc.types.Field(Profile, graphql_name='profile')
    profile_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='profileId')
    task = sgqlc.types.Field(Task, graphql_name='task')
    task_id = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='taskId')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = Subscription

