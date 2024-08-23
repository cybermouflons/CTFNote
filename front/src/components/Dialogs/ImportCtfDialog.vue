<template>
  <q-dialog ref="dialogRef" no-backdrop-dismiss @hide="onDialogHide">
    <q-card class="q-dialog-plugin ctfnote-dialog">
      <q-form @submit="submit">
        <q-card-section class="row items-center no-wrap">
          <div class="text-h6 ellipsis">
            {{ title }}
          </div>
          <q-space />
          <q-btn v-close-popup icon="close" flat round dense />
        </q-card-section>

        <q-card-section class="q-pb-sm">
          <div class="col q-col-gutter-sm">
            <div class="row q-col-gutter-sm q-mb-sm">
              <div class="col">
                <q-input
                  v-model.number="form.ctftimeUrl"
                  filled
                  dense
                  required
                  class="q-pb-sm"
                  label="CTFtime.org URL or ID"
                  :rules="[validate]"
                  autofocus
                >
                  <template #prepend>
                    <div class="q-icon svg-icon">
                      <img src="/ctftime-icon.svg" />
                    </div>
                  </template>
                </q-input>
              </div>
            </div>

            <div class="row q-pt-none q-col-gutter-sm">
              <div class="col">
                <q-select
                  v-model.number="form.ctfPlatform"
                  required
                  label="CTF Platform"
                  options-dense
                  :options="parserOptions"
                  filled
                  dense
                >
                  <template #prepend>
                    <q-icon name="platform" />
                  </template>
                </q-select>
              </div>
            </div>

            <div class="row q-col-gutter-md">
              <div class="col">
                <q-input
                  v-model="form.description"
                  filled
                  type="textarea"
                  label="Description (Markdown)"
                />
              </div>
            </div>
          </div>
        </q-card-section>

        <q-card-actions align="right" class="q-px-md q-pb-md">
          <q-btn color="primary" flat label="Cancel" @click="onCancelClick" />
          <q-btn color="positive" type="submit" :label="editText" />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script lang="ts">
import { useDialogPluginComponent } from 'quasar';
import { Ctf } from 'src/ctfnote/models';
import ctfnote from 'src/ctfnote';
import parsers from 'src/ctfnote/parsers';
import { defineComponent, reactive, ref } from 'vue';

interface Form {
  ctfPlatform: string;
  ctftimeUrl: string | null;
}

function parseCtftimeId(s: string): number | null {
  const url = s.trim();
  const idReg = /^\d+$/;
  const urlReg = /^(?:https?:\/\/)?ctftime\.org\/event\/(\d+)(?:\/.*)?$/i;
  if (idReg.exec(url)) {
    return parseInt(url);
  }
  const match = urlReg.exec(url);
  if (!match) return null;
  return parseInt(match[1]);
}

export default defineComponent({
  props: {
    ctf: { type: Object as () => Ctf | null, default: null },
  },
  emits: useDialogPluginComponent.emits,
  setup(props) {
    const parserOptions = parsers.map((p) => p.name);
    const form = reactive<Form>({
      ctfPlatform: 'Raw / Other',
      ctftimeUrl: null,
      ...(props.ctf as Form | null), // Ensure props.ctf matches Form interface or is null
    });

    const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } =
      useDialogPluginComponent();

    return {
      currentParser: ref(parserOptions[0]),
      resolveAndNotify: ctfnote.ui.useNotify().resolveAndNotify,
      importCtf: ctfnote.ctfs.useImportCtf(),
      dialogRef,
      form,
      parserOptions,
      onDialogHide,
      onDialogOK,
      onCancelClick: onDialogCancel,
    };
  },
  computed: {
    editText() {
      return this.ctf ? 'Save' : 'Import';
    },
    title() {
      return this.ctf ? `Edit ${this.ctf.title}` : 'Import CTF';
    },
  },
  methods: {
    async submit() {
      const id = parseCtftimeId(this.form.ctftimeUrl);
      if (id === null) return;
      const success = await this.resolveAndNotify(
        this.importCtf(id, this.form.ctfPlatform)
      );
      if (success) {
        this.onDialogOK();
      }
    },
    validate() {
      if (this.form && parseCtftimeId(this.form.ctftimeUrl) === null)
        return 'Invalid url or id';
    },
  },
});
</script>

<style lang="scss">
.datetime-input-no-error {
  height: 40px;
}

// Hide error text if not needed to make items underneath clickable
.datetime-input-no-error .q-field__bottom {
  display: none;
}
</style>
