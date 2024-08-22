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
            <div class="row q-pt-none q-col-gutter-sm">
              <div class="col">
                <q-input
                  v-model="form.title"
                  required
                  label="Title"
                  filled
                  dense
                >
                  <template #prepend>
                    <q-icon name="title" />
                  </template>
                </q-input>
              </div>
              <div class="col">
                <q-input v-model="form.ctfUrl" label="CTF link" filled dense>
                  <template #prepend>
                    <q-icon name="link" />
                  </template>
                </q-input>
              </div>
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

            <div class="row q-col-gutter-sm">
              <div class="col">
                <logo-field v-model="form.logoUrl" dense />
              </div>
            </div>

            <div class="row q-col-gutter-sm q-mb-sm">
              <div class="col">
                <datetime-input
                  v-model="form.startTime"
                  filled
                  dense
                  label="Start on"
                  class="datetime-input-no-error"
                  @update:model-value="
                    () => {
                      if (form.endTime < form.startTime) {
                        form.endTime = new Date(
                          form.startTime.getTime() +
                            1000 * 60 * 60 * 24 /* 24 hours in milliseconds */
                        );
                      }
                    }
                  "
                />
              </div>
              <div class="col">
                <datetime-input
                  v-model="form.endTime"
                  filled
                  dense
                  label="End on"
                  lazy-rules
                  :class="{ 'datetime-input-no-error': checkValidDateRange }"
                  :rules="[
                    () =>
                      checkValidDateRange ||
                      'End time must be after start time',
                  ]"
                />
              </div>
            </div>

            <div class="row q-col-gutter-sm q-mb-sm">
              <div class="col">
                <q-input
                  v-model="form.ctftimeUrl"
                  label="CTFTime Link"
                  filled
                  dense
                >
                  <template #prepend>
                    <div class="q-icon svg-icon">
                      <img src="/ctftime-icon.svg" />
                    </div>
                  </template>
                </q-input>
              </div>
              <div class="col-auto">
                <q-input
                  v-model.number="form.weight"
                  step="0.01"
                  type="number"
                  label="Weight"
                  style="width: 140px"
                  filled
                  dense
                >
                  <template #prepend>
                    <q-icon name="fitness_center" />
                  </template>
                </q-input>
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
import DatetimeInput from '../Utils/DatetimeInput.vue';
import LogoField from '../Utils/LogoField.vue';

interface Form {
  title: string;
  description: string;
  startTime: Date;
  endTime: Date;
  weight: number;
  ctfUrl: string | null;
  ctfPlatform: string;
  ctftimeUrl: string | null;
  logoUrl: string | null;
}

export default defineComponent({
  components: { DatetimeInput, LogoField },
  props: {
    ctf: { type: Object as () => Ctf | null, default: null },
  },
  emits: useDialogPluginComponent.emits,
  setup(props) {
    const parserOptions = parsers.map((p) => p.name);
    const now = new Date();
    const form = reactive<Form>({
      title: '',
      description: '',
      startTime: now,
      endTime: new Date(now.getTime() + 1000 * 60 * 60 * 24),
      weight: 0,
      ctfUrl: null,
      ctfPlatform: 'Raw / Other',
      ctftimeUrl: null,
      logoUrl: null,
      ...(props.ctf as Form | null), // Ensure props.ctf matches Form interface or is null
    });

    const { dialogRef, onDialogHide, onDialogOK, onDialogCancel } =
      useDialogPluginComponent();

    return {
      currentParser: ref(parserOptions[0]),
      resolveAndNotify: ctfnote.ui.useNotify().resolveAndNotify,
      updateCtf: ctfnote.ctfs.useUpdateCtf(),
      createCtf: ctfnote.ctfs.useCreateCtf(),
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
      return this.ctf ? 'Save' : 'Create';
    },
    title() {
      return this.ctf ? `Edit ${this.ctf.title}` : 'Create CTF';
    },
    checkValidDateRange(): boolean {
      return (
        this.form.endTime instanceof Date &&
        this.form.startTime instanceof Date &&
        this.form.endTime >= this.form.startTime
      );
    },
  },
  methods: {
    submit() {
      const ctf = this.ctf;
      if (ctf) {
        const opts = {
          message: `CTF ${ctf.title} updated!`,
          icon: 'flag',
        };
        void this.resolveAndNotify(
          this.updateCtf(ctf, {
            ...this.form,
            startTime: this.form.startTime.toISOString(),
            endTime: this.form.endTime.toISOString(),
          }),
          opts
        );
      } else {
        void this.resolveAndNotify(
          this.createCtf({
            ...this.form,
            startTime: this.form.startTime.toISOString(),
            endTime: this.form.endTime.toISOString(),
          })
        );
      }
      this.onDialogOK();
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
