<template>
  <div class="q-gutter-sm">
    <div class="row q-gutter-md q-pl-sm">
      <q-markdown no-html :src="'Placement: ' + ctf.ctfUrl" />
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
});
</script>

<style>
.hide-last-newline p:last-child {
  display: inline;
}
</style>
