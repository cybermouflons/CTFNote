<template>
  <div class="q-gutter-sm">
    <div class="row q-gutter-md q-pl-sm">
      <div class="text-h6 col col-auto">Credentials</div>
      <div class="col">
        <q-btn
          v-if="me.isManager"
          round
          size="sm"
          color="warning"
          icon="edit"
          @click="editCredentials"
        >
          <q-tooltip>Edit the credentials</q-tooltip>
        </q-btn>
      </div>
    </div>
    <div class="row">
      <div class="col col-auto hide-last-newline">
        <q-markdown no-html :src="'CTF url: ' + ctf.ctfUrl" class="blur" />
        <q-markdown no-html :src="'username: ' + ctf.username" class="blur" />
        <q-markdown no-html :src="'password: ' + ctf.password" class="blur" />
        <q-markdown
          no-html
          :src="'scoreboard name: ' + ctf.scoreboardName"
          class="blur"
        />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Ctf } from 'src/ctfnote/models';
import ctfnote from 'src/ctfnote';
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    ctf: { type: Object as () => Ctf, required: true },
  },

  setup() {
    return {
      me: ctfnote.me.injectMe(),
      resolveAndNotify: ctfnote.ui.useNotify().resolveAndNotify,
      updateCtfCredentials: ctfnote.ctfs.useUpdateCtfCredentials(),
    };
  },
  methods: {
    editCredentials() {
      this.$q
        .dialog({
          title: 'Edit username',
          color: 'primary',
          class: 'compact-dialog',
          prompt: {
            model: this.ctf.username ?? '',
            type: 'textarea',
            label: 'Username',
            filled: true,
          },
          ok: {
            label: 'Save',
            color: 'positive',
          },
          cancel: {
            label: 'Cancel',
            flat: true,
          },
        })
        .onOk((username: string) => {
          this.$q
            .dialog({
              title: 'Edit password',
              color: 'primary',
              class: 'compact-dialog',
              prompt: {
                model: this.ctf.password ?? '',
                type: 'textarea',
                label: 'Password',
                filled: true,
              },
              ok: {
                label: 'Save',
                color: 'positive',
              },
              cancel: {
                label: 'Cancel',
                flat: true,
              },
            })
            .onOk((password: string) => {
              this.$q
                .dialog({
                  title: 'Edit scoreboard name',
                  color: 'primary',
                  class: 'compact-dialog',
                  prompt: {
                    model: this.ctf.scoreboardName ?? '',
                    type: 'textarea',
                    label: 'scoreboard Name',
                    filled: true,
                  },
                  ok: {
                    label: 'Save',
                    color: 'positive',
                  },
                  cancel: {
                    label: 'Cancel',
                    flat: true,
                  },
                })
                .onOk((scoreboardName: string) => {
                  const opts = {
                    message: 'Credentials updated!',
                    icon: 'key',
                  };
                  void this.resolveAndNotify(
                    this.updateCtfCredentials(
                      this.ctf,
                      username,
                      password,
                      scoreboardName
                    ),
                    opts
                  );
                });
            });
        });
    },
  },
});
</script>

<style>
.hide-last-newline p:last-child {
  display: inline;
}
</style>
