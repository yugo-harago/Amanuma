<template>
  <section v-if="!loading" class="border-top border-bottom pb-4" style="background: #fff8e6">
    <div v-for="worship in worshipInfo.info" class="container mt-5">
      <div class="row">
        <div class="col">
          <div class="row">
            <div class="col">
              <h3 class="text-xl-center">{{ worship.name }}</h3>
            </div>
          </div>
          <div class="row py-4">
            <div class="col align-items-lg-center">
              <ul class="list-group list-group-root">
                <li v-for="event in worship.events" class="list-group-item text-nowrap justify-content-between">
                  <div class="row">
                    <div class="col">
                      <span class="justify-content-lg-start">{{ event.name }}</span>
                    </div>
                    <div class="col">
                      <span class="justify-content-end">{{ event.startTime }}-{{ event.endTime }}</span>
                    </div>
                    <div class="col-lg-2 mt-1">
                      <i class="la la-toggle-down" style="font-size: 21px"></i>
                    </div>
                  </div>
                  <ul class="list-group">
                    <li v-for="subEvent in event.subEvents" class="list-group-item">
                      <div class="row">
                        <div class="col-6">
                          <span>{{ subEvent.name }}</span>
                        </div>
                        <div class="col-6">
                          <span>{{ subEvent.responsible }}</span>
                        </div>
                      </div>
                    </li>
                  </ul>
                </li>
              </ul>
            </div>
            <div
              class="col-lg-5 col-xl-4 d-none d-lg-flex justify-content-center"
            >
              <img
                class="img-thumbnail img-fluid sticky-top mt-4"
                src="@/assets/img/istockphoto-1177881788-612x612.jpg"
                loading="lazy"
                width="295"
                height="1113"
                style="height: 309px"
              />
            </div>
          </div>
          <div class="row justify-content-xl-center">
            <div class="col-xl-9"></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
<script>
import { mapActions, mapState } from 'pinia'
import { useWorshipStore } from '@/stores/worship'

export default {
  name: 'WorshipView',
  data: () => {
    return {
      loading: true,
    }
  },
  async mounted() {
    this.loading = true
    await this.fecthWorshipInfo();
    this.loading = false
  },
  methods: {
    ...mapActions(useWorshipStore, ['fecthWorshipInfo', 'saveWorshipInfo']),
  },
  computed: {
    ...mapState(useWorshipStore, ['worshipInfo']),
  },
}
</script>